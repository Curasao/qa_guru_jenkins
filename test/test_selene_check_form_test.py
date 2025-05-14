import allure
import os
from selene import browser, have, be
from selene.support.shared import config
from test import conftest
from selene.api import *

config.timeout = 10

def test_complete_todo(browser_management):
    with allure.step('Открыть страницу DemoQA'):
        browser.open('/automation-practice-form')

    with allure.step('Проверить имя пользователя'):
    #проверка имени
        browser.element('#userName-wrapper').element('#firstName').should(be.blank).type('Dasha')

    with allure.step("Проверка фамилии пользователя"):
    #проверка фамилии
        browser.element('#userName-wrapper').element('#lastName').should(be.blank).type('Lenina')

    with allure.step("Проверка емейл"):
    #проверка емейл
        browser.element('#userEmail-wrapper').element('#userEmail').should(be.blank).type('lenina5@email.com')

    with allure.step("Проверка чекбокса гендера"):
    #проверка чекбокса гендера
        browser.element('#genterWrapper').element('[for=gender-radio-2]').click()

    with allure.step("Проверка номера"):
    #проверка юзернейм
        browser.element('#userNumber-wrapper').element('#userNumber').should(be.blank).type('1712345678')

    with allure.step("Проверка календаря"):
    #проверка календаря (датапикер)
        browser.element("#dateOfBirthInput").click()

        browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()

        browser.element('.react-datepicker__year-select').click().element('option[value="2008"]').click()

        browser.element('.react-datepicker__day--005').click()

    with allure.step("Проверка поля хобби"):
    #проверка поля хобби
        browser.element("#hobbiesWrapper").click()

        browser.element('#hobbiesWrapper').element('[for=hobbies-checkbox-3]').click()

    with allure.step("Проверка выбора предметов"):
    #проверка поля subjects
        browser.element('#subjectsWrapper').element('#subjectsInput').should(be.blank).type('E')
        browser.element('#react-select-2-option-0').click()

    with allure.step("Проверка поля текущий адрес"):
    #проверка поля текущий адрес
        browser.element('#currentAddress-wrapper').element('#currentAddress').should(be.blank).type('Lenina')

    with allure.step("Проверка загрузки фото"):
    #проверка кнопки "Загрузить фото"
        browser.element('#uploadPicture').type(os.path.abspath('water.jpg'))

    with allure.step("Проверка дропдаун списка город и штат"):
    #проверка дропдаун списков город и штат

        browser.element('#state').execute_script("document.querySelector('#state').scrollIntoView()")
        browser.element('#state').click()

        browser.element('#react-select-3-option-0').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-0').click()

    with allure.step("Отправка формы"):
    #отправка формы
        browser.element('#submit').click()

    with allure.step("Проверка что форма видима"):
        browser.element(".table").should(be.visible)

    # Проверка содержимого таблицы

    with allure.step("Проверка что указаны валидные данные"):
        browser.element(".table").element('tr:nth-child(1) td:last-child').should(have.text('Dasha'))

        browser.element(".table").element('tr:nth-child(3) td:last-child').should(have.text('Female'))
        browser.element(".table").element('tr:nth-child(2) td:last-child').should(have.text('lenina5@email.com'))
        browser.element(".table").element('tr:nth-child(4) td:last-child').should(have.text('1712345678'))
        browser.element(".table").element('tr:nth-child(5) td:last-child').should(have.text('05 April,2008'))
        browser.element(".table").element('tr:nth-child(1) td:last-child').should(have.text('Lenina'))
        browser.element(".table").element('tr:nth-child(6) td:last-child').should(have.text('English'))
        browser.element(".table").element('tr:nth-child(7) td:last-child').should(have.text('Reading, Music'))
        browser.element(".table").element('tr:nth-child(8) td:last-child').should(have.text('water.jpg'))
        browser.element(".table").element('tr:nth-child(9) td:last-child').should(have.text('Lenina'))
        browser.element(".table").element('tr:nth-child(10) td:last-child').should(have.text('NCR Delhi'))


