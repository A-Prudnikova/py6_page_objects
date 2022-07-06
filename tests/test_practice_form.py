from selene.support.shared import browser
from selene import have
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.resourse import resourse
from demoqa_tests.controls import TagsInput, Dropdown, Datepicker, Table

firstname = 'Anna'
lastname = 'Hanna'
email = '1@test.ru'
gender = 'Other'
phonenumber = '1111111111'
year = '2000'
years = Datepicker(s('.react-datepicker__year-select'))
month_str = 'April'
# переменная month_int должна иметь значение (число месяца из переменной month_str минус 1)
month_int = 3
months = Datepicker(s('.react-datepicker__month-select'))
# переменная day всегда должна быть обозначена двумя знаками: 01, 02, 15, 31
day = '20'
days = Datepicker(s(f'.react-datepicker__day--0{day}'))
subject = 'English'
subjects = TagsInput(s('#subjectsInput'))
hobby = 'Sports'
picture = '1.jpg'
address = 'my room'
state = 'NCR'
states = Dropdown(s('#state'))
city = 'Delhi'
cities = Dropdown(s('#city'))
results = Table(s('.modal-content .table'))


# тест заполнения формы через установку значений вручную
def test_setting_data_manual(browser_config):
    browser.open('/automation-practice-form').driver.maximize_window()

    s('#firstName').type(firstname)
    s('#lastName').type(lastname)
    s('#userEmail').type(email)
    s('[for="gender-radio-3"]').click()
    s('#userNumber').type(phonenumber)
    s('#dateOfBirthInput').click()
    years.set_year(option=year)
    months.set_month(option=month_str)
    days.set_day(option=day)
    subjects.input_subject_by_tab(to_type=subject)
    s('[for="hobbies-checkbox-1"]').click()
    s('#uploadPicture').send_keys(resourse(picture))
    s('#currentAddress').type(address)
    states.set(option=state)
    cities.set(option=city)
    s('#submit').click()

    # Проверка с использованием Page Object
    results.row(0).should(have.exact_texts('Student Name', f'{firstname} {lastname}'))
    results.row(1).should(have.exact_texts('Student Email', f'{email}'))
    results.row(2).should(have.exact_texts('Gender', f'{gender}'))
    results.row(3).should(have.exact_texts('Mobile', f'{phonenumber}'))
    results.row(4).should(have.exact_texts('Date of Birth', f'{day} {month_str},{year}'))
    results.row(5).should(have.exact_texts('Subjects', f'{subject}'))
    results.row(6).should(have.exact_texts('Hobbies', f'{hobby}'))
    results.row(7).should(have.exact_texts('Picture', f'{picture}'))
    results.row(8).should(have.exact_texts('Address', f'{address}'))
    results.row(9).should(have.exact_texts('State and City', f'{state} {city}'))


# тест заполнения формы через выбор значений из предложенных
def test_select_data_from_given(browser_config):
    browser.open('/automation-practice-form').driver.maximize_window()

    s('#firstName').type(firstname)
    s('#lastName').type(lastname)
    s('#userEmail').type(email)
    s('[for="gender-radio-3"]').click()
    s('#userNumber').type(phonenumber)
    s('#dateOfBirthInput').click()
    years.select_year(option=year)
    months.select_month(option=month_int)
    days.select_day(option=day)
    subjects.select_subject_from_list(to_type=subject)
    s('[for="hobbies-checkbox-1"]').click()
    s('#uploadPicture').send_keys(resourse(picture))
    s('#currentAddress').type(address)
    states.select(option=state)
    cities.select(option=city)
    s('#submit').click()

    # Проверка без Page Object
    ss('table tbody tr').should(have.texts(
        f'{firstname} {lastname}',
        f'{email}',
        f'{gender}',
        f'{phonenumber}',
        f'{day} {month_str},{year}',
        f'Subjects {subject}',
        f'Hobbies {hobby}',
        f'Picture {picture}',
        f'Address {address}',
        f'State and City {state} {city}'))
