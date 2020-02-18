from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


try: 
    
    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_id('num1')
    num1 = int(num1.text)

    num2 = browser.find_element_by_id('num2')
    num2 = int(num2.text)

    y = num1 + num2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
