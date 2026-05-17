import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages.base_page import BasePage

class SearchPage(BasePage):

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    
    STREAMER_SELECTORS = [
        "a[data-a-target='preview-card-image-link']",
        "a[data-a-id='preview-card-image-link']",
        "article a",
        "main a[href^='/']"
    ]

    def search_game(self, keyword: str):

        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.click()
        search_input.clear()

        for char in keyword:
            search_input.send_keys(char)
            time.sleep(0.15)
        time.sleep(3)
        self.select_first_suggestion(keyword)

    def select_first_suggestion(self, keyword: str):

        suggestion_xpath = (By.XPATH, f"//a[contains(., '{keyword}')]")
        try:
            suggestion = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(suggestion_xpath)
            )
            suggestion.click()

        except TimeoutException:
            self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        
        self.wait_for_page_load()
        time.sleep(2)

    def scroll_twice(self, times):

        for _ in range(times):
            last_height = self.driver.execute_script("return window.pageYOffset;")
            self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.8);")
            time.sleep(2)
            current_height = self.driver.execute_script("return window.pageYOffset;")
            if current_height == last_height:
                self.driver.execute_script("window.scrollBy(0, 200);")

    def wait_for_page_load(self):

        try:
            self.wait.until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            time.sleep(1) 
        except Exception as e:
            raise AssertionError("Page loading timeout")

    def select_first_streamer(self):
            invalid_keywords = ["directory", "search", "login", "signup", "downloads", "videos"]

            for selector in self.STREAMER_SELECTORS:
                try:
                    streamers = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    
                    for streamer in streamers:
                        try:
                            href = streamer.get_attribute("href")
                            if not href or any(k in href for k in invalid_keywords):
                                continue

                            if streamer.is_displayed():
                                self.driver.execute_script("arguments[0].click();", streamer)
                                streamer_id = href.split('/')[-1].split('?')[0]
                                self.wait.until(EC.url_contains(f"/{streamer_id}"))
                                self.wait.until(EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, "video, .video-player, [data-a-target='video-player']")
                                ))
                                return
                        except (StaleElementReferenceException, Exception):
                            continue
                except Exception:
                    continue

            raise AssertionError("Streamer not found.")