from selene import browser, command, have
import os

class RegistrationPage:
    def open (self):
        browser.open('https://demoqa.com/automation-practice-form')
    def fill_full_name(self, last_name, first_name):
        browser.element('#firstName').type(last_name)
        browser.element('#lastName').type(first_name)

    def fill_mail(self, email):
        browser.element('#userEmail').type(email)
    def click_male(self):
        browser.element('[for="gender-radio-1"]').click()
    def fill_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
    def choose_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
    def choose_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
    def command_scroll(self):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    def choose_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
    def add_image(self, image):
        browser.element('[id="uploadPicture"]').send_keys(os.path.abspath(image))
    def fill_current_address(self, address):
        browser.element('[id="currentAddress"]').type(address).perform(command.js.scroll_into_view)
    def chosse_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()
    def chosse_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
    def press_enter(self):
        browser.element('[id="submit"]').press_enter()
    def student_form_should_have_text(self, text):
        browser.element('.modal-title').should(have.text(text))
    def student_form_dy_registret(self, full_name, email, gender, phonr_number, date_of_birth, subject, hobby, image, address, sity):
        browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
            full_name,
            email,
            gender,
            phonr_number,
            date_of_birth,
            subject,
            hobby,
            image,
            address,
            sity
        ))