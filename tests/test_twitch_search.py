import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from utils.config_reader import (
    load_config
)


@pytest.mark.smoke
@pytest.mark.flaky(reruns=0)
def test_twitch_streamer_flow(driver):

    config = load_config()
    base_url = config["base_url"]
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    streamer_page = StreamerPage(driver)

    home_page.open(base_url)
    streamer_page.handle_popup()
    home_page.click_search()

    search_page.search_game("StarCraft II")
    search_page.scroll_twice(3)
    search_page.select_first_streamer()

    streamer_page.handle_popup()
    streamer_page.wait_video_loaded()