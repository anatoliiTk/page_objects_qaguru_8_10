from page_objects_qaguru_8_10.pages.registration_page import RegistrationPage
from page_objects_qaguru_8_10.data.users import User, User_form

registration_page = RegistrationPage()
def test_student_registration_page():
    student = User(first_name='Anatolii', last_name='Tkach', email='tkach.vip@gmail.com', phone_number='0550391393',
                   month='2', year='1999', day='08', image='cat.jpg', subject='Maths', address='Pushkin 22', state='NCR', city='Delhi')

    student_form = User_form(full_name='Tkach Anatolii', email='tkach.vip@gmail.com', gender='Male', phone_number='0550391393',
                             date_of_birth='08 November,1999', subject='Maths', hobby='Sports', image='cat.jpg', address='Pushkin 22',
                             city='NCR Delhi')
    #открытие браузера
    registration_page.open()
    #заполнение формы
    registration_page.register(student)
    #проверка заполненой формы
    registration_page.student_form_dy_registret(student_form)