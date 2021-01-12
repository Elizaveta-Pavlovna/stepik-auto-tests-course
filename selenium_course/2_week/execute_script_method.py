'''from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Halo';alert('Robots at work');")'''

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    not_rob = browser.find_element_by_id("robotCheckbox")
    not_rob.click()
    
#Находим элемент, до которого нужно проскроллить
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Проскроллить на 100 пикселей вниз browser.execute_script("window.scrollBy(0, 100);")

    click1 = browser.find_element_by_id("peopleRule")
    click1.click()

    click2 = browser.find_element_by_id("robotsRule")
    click2.click()

    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
