#C Selenium_waits WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной.
#На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки,
#но неактивная кнопка в момент загрузки — обычное дело для реального сайта.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
#button = WebDriverWait(browser, 5).until_not(
#       EC.element_to_be_clickable((By.ID, "verify"))
#    )

assert "successful" in message.text


# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions