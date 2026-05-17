import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            timeout
        )

    @staticmethod
    def sleep(seconds: float) -> None:

        time.sleep(seconds)

    def click(self, by: By, locator: str) -> None:

        element = self.wait.until(
            EC.element_to_be_clickable(
                (by, locator)
            )
        )

        element.click()

    def type(self, by: By, locator: str, text: str) -> None:

        element = self.wait.until(
            EC.visibility_of_element_located(
                (by, locator)
            )
        )
        element.clear()
        element.send_keys(text)

    def wait_visible(self, by: By, locator: str):

        return self.wait.until(
            EC.visibility_of_element_located(
                (by, locator)
            )
        )

    def wait_url_contains(self, keyword: str):

        return self.wait.until(
            EC.url_contains(keyword)
        )