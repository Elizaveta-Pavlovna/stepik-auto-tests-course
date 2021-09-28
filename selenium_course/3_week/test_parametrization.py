import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1"
    answer = math.log(int(time.time()))
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_class_name("textarea").send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(2)
    correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert correct == "Correct!", f"Текст {correct} не совпадает с 'Correct!'"
    time.sleep(1)

