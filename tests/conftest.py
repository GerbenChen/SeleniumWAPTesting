import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.artifact_manager import artifact_manager
from utils.config_reader import load_config
from utils.logger import get_logger


logger = get_logger()


@pytest.fixture(scope="function")
def driver(request):
    """
    Selenium Chrome Driver Fixture
    """

    config = load_config()

    chrome_options = Options()

    mobile_emulation = {
        "deviceName": config["browser"]["mobile_emulator"]
    }
    chrome_options.add_experimental_option(
        "mobileEmulation",
        mobile_emulation
    )
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )
    chrome_options.add_argument("--touch-events")

    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )
    chrome_options.add_experimental_option(
        "useAutomationExtension",
        False
    )
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=390,844")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")

    if config["browser"]["headless"]:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })

        Object.defineProperty(navigator, 'platform', {
            get: () => 'iPhone'
        })

        Object.defineProperty(navigator, 'maxTouchPoints', {
            get: () => 5
        })

        Object.defineProperty(navigator, 'hardwareConcurrency', {
            get: () => 8
        })
    """)
    timeout = int(config["timeout"])
    driver.implicitly_wait(timeout)
    driver.set_page_load_timeout(timeout)
    logger.info("Chrome Driver Started")

    time.sleep(random.uniform(1.5, 3.0))

    yield driver

    try:
        report = getattr(request.node, "rep_call", None)

        if report:
            outcome = report.outcome.upper()
        else:
            outcome = "INTERRUPTED"

        file_name = f"{outcome}_{request.node.name}"

        screenshot_path = artifact_manager.screenshot_path(
            file_name
        )

        driver.save_screenshot(screenshot_path)

        log_msg = (
            f"Test {outcome}: "
            f"{request.node.name} | "
            f"Screenshot: {screenshot_path}"
        )

        if outcome == "FAILED":
            logger.error(log_msg)

        elif outcome == "INTERRUPTED":
            logger.warning(log_msg)

        else:
            logger.info(log_msg)

    except Exception as error:
        logger.exception(
            f"Teardown screenshot failed: {error}"
        )

    finally:
        driver.quit()
        logger.info("Driver Closed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)