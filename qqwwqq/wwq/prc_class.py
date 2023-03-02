import time

from selenium.webdriver.common.by import By


class preee():
    def __init__(self,driver):
        self.driver=driver
    def t11(self):
        self.driver.find_element(By.NAME, 'wd').send_keys('111')
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3)
    def t12(self):
        self.driver.find_element(By.NAME, 'wd').send_keys('333')
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3)