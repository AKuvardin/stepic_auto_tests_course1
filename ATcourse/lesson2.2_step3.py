from selenium import webdriver
import time
import math

from selenium.webdriver.support.select import Select


def sum(x, y):
    return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # выдергивание чисел со страницы и их суммирование
    num1 = browser.find_element_by_id('num1')
    x = num1.text
    num2 = browser.find_element_by_id('num2')
    y = num2.text
    z = str(int(x) + int(y))
    print(z)
    # выбор в селекторе подходящего значения
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(z)
    # нажатие кнопки сабмит
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
