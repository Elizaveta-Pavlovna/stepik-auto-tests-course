import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Вероятно, вы заметили, что мы не использовали в этом примере команду browser.quit(). Это привело к тому, что несколько окон
# браузера оставались открыты после окончания тестов, а закрылись только после завершения всех тестов. Закрытие браузеров произошло
# благодаря встроенной фикстуре — сборщику мусора. Но если бы количество тестов насчитывало больше нескольких десятков, то открытые
# окна браузеров могли привести к тому, что оперативная память закончилась бы очень быстро.