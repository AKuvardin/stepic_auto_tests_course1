from selenium import webdriver
import time
import math

def calc(x) -> object:
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath("//input[@class='form-control']")
    input1.send_keys(y)
    checkb = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    checkb.click()
    radiob = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radiob.click()
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
