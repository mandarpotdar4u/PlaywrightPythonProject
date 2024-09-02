from idlelib import browser

import pytest
from playwright.sync_api import Playwright
from utilities.logger import logGen
logger = logGen()


@pytest.fixture(scope="function")
def initialize_driver(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Open new Page
    page = context.new_page()

    # Navigate to URL
    page.set_viewport_size({"width": 1920, "height": 1080})
    url = "https://www.saucedemo.com/"
    page.goto('https://www.saucedemo.com/')
    logger.info(f"Launching website {url}")
    yield page
    print("Close Driver")
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, video_path):
    return {
        **browser_context_args,
        "record_video_dir": video_path,
        "viewport": {
            "width": 1920,
            "height": 1080
        }
    }
@pytest.fixture(scope="session")
def video_path():
    return "./videos"
