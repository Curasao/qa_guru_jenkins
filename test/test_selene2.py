import allure
import os, time
from selene import browser, have, be
from selene.support.shared import config
from test import conftest
config.timeout = 100

def test_complete_todo2():
    with allure.step('Открыть страницу DemoQA'):
        browser.open('https://2ip.ru/')
        time.sleep(10)

