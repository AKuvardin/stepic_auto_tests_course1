from selenium import webdriver
import time
import math
import os

def calc(x) -> object:
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element_by_xpath("//input[@name='firstname']")
    fname.send_keys('Ivan')
    lname = browser.find_element_by_xpath("//input[@name='lastname']")
    lname.send_keys('Ivanov')
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys('ivanov-ivan@mail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'bio.txt')  # добавляем к этому пути имя файла
    dwn = browser.find_element_by_xpath("//input[@type='file']")
    dwn.send_keys(file_path)
    print(current_dir)
    print(file_path)
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
