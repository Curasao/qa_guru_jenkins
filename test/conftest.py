import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080


    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()