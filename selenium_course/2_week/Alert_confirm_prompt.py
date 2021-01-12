#Всплывающие окна

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    button = browser.find_element_by_class_name("btn").click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(str(y))

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла