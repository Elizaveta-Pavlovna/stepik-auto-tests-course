# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option,
# как указано в примере ниже:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)