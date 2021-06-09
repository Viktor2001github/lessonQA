from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link) 
    FirstName = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group first_class"]/input[@type="text"]').send_keys("Viktor")
    LastName = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group second_class"]/input[@type="text"]').send_keys("Samoylenko")
    Email= browser.find_element(By.XPATH, '//div[@class="form-group third_class"]/input[@type="text"]').send_keys("vvs2001.viktor@gmail.com")
    phone = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group first_class"]/input[@type="text"]').send_keys("2020939494003")
    Adress = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group second_class"]/input[@type="text"]').send_keys("Kyiv")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
   



finally:
    time.sleep(10)
    browser.quit()
