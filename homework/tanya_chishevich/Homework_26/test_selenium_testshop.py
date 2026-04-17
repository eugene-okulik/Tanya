from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_customizable_desk_press_on_link(driver):
    driver.get('http://testshop.qa-practice.com/')
    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Customizable Desk')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.ID, 'add_to_cart').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-secondary')]")
    button.click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'o_notification_fade-enter-active')]")))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, '.fa-shopping-cart').click()
    assert driver.find_element(By.TAG_NAME, 'h6').text == 'Customizable Desk (Steel, White)'


def test_customizable_desk_press_on_picture(driver):
    driver.get('http://testshop.qa-practice.com/')
    immage_element = driver.find_element(By.CSS_SELECTOR, 'img[alt*="Customizable Desk"]')
    shop_cart = driver.find_element(By.CSS_SELECTOR, ".a-submit")
    actions = ActionChains(driver)
    actions.move_to_element(immage_element)
    actions.move_to_element(shop_cart)
    actions.click(shop_cart)
    actions.perform()
    driver.implicitly_wait(3)
    result = driver.find_element(By.TAG_NAME, 'strong')
    assert result.text == '[FURN_0096] Customizable Desk (Steel, White)'
