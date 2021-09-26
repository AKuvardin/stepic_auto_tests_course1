from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x) -> object:
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #step 1
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    #step 2
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    #step 3
    book = browser.find_element_by_xpath("//button[@id='book']")
    book.click()
    #step 4
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()

finally:
    #time.sleep(15)
    browser.quit()
