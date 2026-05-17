import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class StreamerPage(BasePage):

    POPUPS = [
        (By.CSS_SELECTOR, "button[data-a-target='ms-proceed-button']"),
        (By.CSS_SELECTOR, "button[aria-label='Proceed']"),
        (By.CSS_SELECTOR, "button[aria-label='Continue']"),
        (By.XPATH, "//button[contains(text(), 'Proceed')]"),
        (By.CSS_SELECTOR, "[data-test-selector='proceed-button']"),
        (By.CSS_SELECTOR, "[data-a-target='consent-banner-accept']"),
        (By.XPATH, "//*[text()='Proceed']"),
        (By.XPATH, "//span[contains(text(), 'Proceed')]"),
        (By.XPATH, "//div[@role='button'][contains(., 'Proceed')]"),
        (By.CSS_SELECTOR, "div.consent-banner button"),
        (By.CSS_SELECTOR, "div[role='dialog'] button:last-child"),
        (By.CSS_SELECTOR, ".overlay-container button"),
        (By.CSS_SELECTOR, "#root .video-player__overlay button")
    ]
    
    VIDEO = (By.CSS_SELECTOR, "video")

    def handle_popup(self):
        for by, selector in self.POPUPS:
            try:
                elements = self.driver.find_elements(by, selector)
                if elements and elements[0].is_displayed():
                    self.driver.execute_script("arguments[0].click();", elements[0])
                    logger.info(f"deal with popup: {selector}")
            except Exception:
                pass

    def wait_video_loaded(self):

        try:
            self.wait.until(EC.presence_of_element_located(self.VIDEO))
            logger.info("Video tag detected, please wait 5 seconds for buffering...")
            
            time.sleep(5)
        except TimeoutException:
            raise AssertionError("Video element not found.")