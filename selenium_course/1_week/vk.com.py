from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://vk.com")

#Заходим в аккаунт
    login = browser.find_element_by_id("index_email")
    login.send_keys("89889529649")

    password = browser.find_element_by_id("index_pass")
    password.send_keys("Santa1999")

#Пишем сообщение Антоненко Лизе
    button = browser.find_element_by_class_name("index_login_button")
    button.click()
    time.sleep(2)

    messenger = browser.find_element_by_id("l_msg")
    messenger.click()
    time.sleep(2)

    liza = browser.find_element_by_xpath("//span[contains(text(),'Лиза Антоненко')]")
    liza.click()
    time.sleep(2)

    chat = browser.find_element_by_id("im_editable0")
    chat.click()
    time.sleep(2)

    write = browser.find_element_by_id("im_editable0")
    write.send_keys("Привееет, это я, робот!")

    send = browser.find_element_by_class_name("im-chat-input--send")
    send.click()

#Лайкаем фото
    akk = browser.find_element_by_class_name("_im_header_link")
    akk.click()

    like = 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла