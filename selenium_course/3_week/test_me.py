from selenium import webdriver
import time
import pytest


def registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
    input1.send_keys("Liza")
    input2 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
    input2.send_keys("Antonenko")
    input3 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
    input3.send_keys("liza99.liza@mail.ru")
    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(3)
    browser.quit()


def registration2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
    input1.send_keys("Liza")
    input2 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
    input2.send_keys("Antonenko")
    input3 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
    input3.send_keys("liza99.liza@mail.ru")
    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(3)
    browser.quit()

class TestReg():
    def test_registration1(self):
        registration1()
    def test_registration2(self):
        registration2()

