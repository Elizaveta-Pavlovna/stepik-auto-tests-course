#Получаем значение атрибута

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    x = chest.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    not_rob = browser.find_element_by_id("robotCheckbox")
    not_rob.click()

    click1 = browser.find_element_by_id("peopleRule")
    click1.click()

    click2 = browser.find_element_by_id("robotsRule")
    click2.click()

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

