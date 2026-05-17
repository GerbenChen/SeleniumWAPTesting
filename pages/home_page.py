from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_TEXTS = [
        "Search",
        "搜尋",
        "瀏覽",
        "Browse"
    ]

    def open(self, url: str) -> None:

        self.driver.get(url)

        # Wait DOM complete
        WebDriverWait(
            self.driver,
            5
        ).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Twitch React rendering delay
        self.sleep(3)

    def remove_popup(self) -> None:

        popup_selectors = [
            "button[aria-label='Close']",
            "[data-a-target='consent-banner-accept']"
        ]

        for selector in popup_selectors:

            try:
                popup = WebDriverWait(
                    self.driver,
                    0,5
                ).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            selector
                        )
                    )
                )

                if popup.is_displayed():

                    self.driver.execute_script(
                        "arguments[0].click();",
                        popup
                    )

            except Exception:
                pass

    def click_search(self) -> None:

        for text in self.SEARCH_TEXTS:

            xpath_selectors = [
                (
                    By.XPATH,
                    f"//a[normalize-space()='{text}']"
                ),
                (
                    By.XPATH,
                    f"//button[normalize-space()='{text}']"
                ),
                (
                    By.XPATH,
                    f"//*[normalize-space()='{text}']"
                )
            ]

            for by, locator in xpath_selectors:

                try:

                    element = WebDriverWait(
                        self.driver,
                        1
                    ).until(
                        EC.presence_of_element_located(
                            (by, locator)
                        )
                    )

                    if element.is_displayed():
                        self.driver.execute_script(
                            """
                            arguments[0].scrollIntoView({
                                block: 'center'
                            });
                            """,
                            element
                        )

                        self.sleep(1)

                        # JS click more stable on Twitch
                        self.driver.execute_script(
                            "arguments[0].click();",
                            element
                        )

                        return

                except (
                    TimeoutException,
                    NoSuchElementException
                ):
                    pass

        raise AssertionError(
            "Search/Browse button not found."
        )