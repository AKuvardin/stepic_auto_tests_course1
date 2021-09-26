from selenium import webdriver
import time
import math
import os

def calc(x) -> object:
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #step 1
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #step 2
    iwtg_button = browser.find_element_by_xpath("//button[@type='submit']")
    iwtg_button.click()
    #step 3
    comfirm = browser.switch_to.alert
    comfirm.accept()
    #step 4
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()


finally:
    time.sleep(5)
    browser.quit()
