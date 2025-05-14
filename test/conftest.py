import pytest,os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from selene.api import *
from selenium.common.exceptions import InvalidSessionIdException
import pytest

from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)


    browser.quit()



@pytest.fixture(scope='function', autouse=True)
def browser_management(options=None):
    browser.config.base_url = 'https://demoqa.com'


    # browser.config.type_by_js = True
    '''
    ↑ if we would want to type text via JavaScript to speed up tests a bit
    '''

    # driver_options = webdriver.FirefoxOptions()
    '''
    ↑ if we would want to use Firefox with custom browser options instead of Chrome
    '''
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--timeout=60')
    #driver_options.add_argument('')

    # browser.config.driver = webdriver.Chrome(
    #     service=ChromeService(executable_path=ChromeDriverManager().install()),
    #     options=driver_options,
    # )
    '''
    ↑ one day we need something like this for some complicated browser setup
    or support of some specific browser or driver
    ↓ but for now it's enough just to pass driver options to Selene's config
    '''
    browser.config.driver_options = driver_options

    yield browser

    try:
        browser.quit()
    except InvalidSessionIdException:
        print('ОШибка')

    '''
    ↑ Selene would automatically close browser for us in the very end of all tests
    but by we call browser.quit() explicitely after yield inside fixture of scope='function'
    so forcing browser to close after each test function for better tests independence ;)
    '''