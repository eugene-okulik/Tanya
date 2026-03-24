from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_input_text(driver):
    input_data = 'Qa_practice'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_string = driver.find_element(By.ID, 'id_text_string')
    input_string.send_keys(input_data)
    input_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data
    print(result_text.text)


def test_fill_out_student_form(driver):
    data = ['Tanya', 'Chishevich', 'tanyaChishevich@gmail.com', '1234567896', '11', '1992', 'Arts',
            'test adress']
    driver.get('https://demoqa.com/automation-practice-form')
    input_firstname = driver.find_element(By.ID, 'firstName')
    input_firstname.send_keys(data[0])
    input_lastname = driver.find_element(By.ID, 'lastName')
    input_lastname.send_keys(data[1])
    input_email = driver.find_element(By.ID, 'userEmail')
    input_email.send_keys(data[2])
    driver.find_element(By.CSS_SELECTOR, "input[id='gender-radio-2']").click()
    input_phone = driver.find_element(By.ID, 'userNumber')
    input_phone.send_keys(data[3])
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    dropdown_month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    select_month = Select(dropdown_month)
    select_month.select_by_value(data[4])
    dropdown_year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    select_year = Select(dropdown_year)
    select_year.select_by_value(data[5])
    driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--019').click()
    subject = driver.find_element(By.ID, 'subjectsInput')
    subject.send_keys(data[6])
    subject.send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, "input[id='hobbies-checkbox-1']").click()
    input_current_address = driver.find_element(By.ID, 'currentAddress')
    input_current_address.send_keys(data[7])
    wait = WebDriverWait(driver, 1)
    select_state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
    select_state.click()
    choose_state = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, '-option') and text()='Haryana']")))
    choose_state.click()
    select_city = wait.until(
        EC.element_to_be_clickable((By.ID, "react-select-4-input")))
    select_city.click()
    choose_city = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, '-option') and text()='Karnal']")))
    choose_city.click()
    button = driver.find_element(By.ID, 'submit')
    button.click()
    table = driver.find_element(By.CLASS_NAME, "table-dark")
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        print(row_data)


def test_choose_language(driver):
    language = 'Java'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown_choose_language = driver.find_element(By.CSS_SELECTOR, '.form-select')
    select_language = Select(dropdown_choose_language)
    select_language.select_by_visible_text(language)
    button = driver.find_element(By.ID, 'submit-id-submit')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == language


def test_check_text(driver):
    text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.XPATH, "//div[@id='start']//button")
    button.click()
    wait = WebDriverWait(driver, 5)
    result_text = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert (result_text.text == text)
