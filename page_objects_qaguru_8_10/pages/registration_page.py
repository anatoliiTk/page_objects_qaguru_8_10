import os
from selene import browser, be, have, command

from page_objects_qaguru_8_10 import resources


class RegistrationPage:
    def open (self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register (self, user):
        browser.element('#firstName').type(user.last_name)
        browser.element('#lastName').type(user.first_name)
        browser.element('#userEmail').type(user.email)
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(user.month)
        browser.element('.react-datepicker__year-select').send_keys(user.year)
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').should(be.visible).type(resources.path(user.image))
        browser.element('[id="currentAddress"]').type(user.address).perform(command.js.scroll_into_view)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('[id="submit"]').press_enter()


    def student_form_dy_registret(self, user):
        browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
            user.full_name,
            user.email,
            user.gender,
            user.phone_number,
            user.date_of_birth,
            user.subject,
            user.hobby,
            user.image,
            user.address,
            user.city
        ))