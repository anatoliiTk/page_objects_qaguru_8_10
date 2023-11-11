import os.path
from selene import browser, command, have
from page_objects_qaguru_8_10.resources import RegistrationPage


def test_tools_qa():
    #открытие браузера
    registration_page = RegistrationPage()
    registration_page.open()

    #заполнение формы
    registration_page.fill_full_name("Anatolii", 'Tkach')
    registration_page.fill_mail('tkach.vip@gmail.com')
    registration_page.click_male()
    registration_page.fill_number('0550391393')
    registration_page.choose_date_of_birth(month='2', year='1999', day='08')
    registration_page.choose_subjects('Maths')
    registration_page.command_scroll()
    registration_page.choose_hobbies()
    registration_page.add_image('../page_objects_qaguru_8_10/image/cat.jpg')
    registration_page.fill_current_address('Pushkin 22')
    registration_page.chosse_state('NCR')
    registration_page.chosse_city('Delhi')
    registration_page.press_enter()

    #проверка резльтата
    registration_page.student_form_should_have_text('Thanks for submitting the form')
    browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
        'Anatolii Tkach',
        'tkach.vip@gmail.com',
        'Male',
        '0550391393',
        '08 November,1999',
        'Maths',
        'Sports',
        'cat.jpg',
        'Pushkin 22',
        'NCR Delhi'
    ))