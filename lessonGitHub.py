from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link) 
    FirstName = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group first_class"]/input[@type="text"]').send_keys("")
    LastName = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group second_class"]/input[@type="text"]').send_keys("")
    Email= browser.find_element(By.XPATH, '//div[@class="form-group third_class"]/input[@type="text"]').send_keys("")
    phone = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group first_class"]/input[@type="text"]').send_keys("")
    Adress = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group second_class"]/input[@type="text"]').send_keys("")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
   



finally:
    time.sleep(10)
    browser.quit()
