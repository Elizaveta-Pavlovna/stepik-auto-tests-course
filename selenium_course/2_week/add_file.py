#Добавляем файл

from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Liza")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Antonenko")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("liza99.liza@mail.ru")

    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Hello,World!.txt')
    file.send_keys(file_path)

    submit = browser.find_element_by_class_name("btn")
    submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла