#Кликаем по пунктикам

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(str(y))

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

# не забываем оставить пустую строку в конце файла