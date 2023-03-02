import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
time.sleep(2)
# print('123')
# print('321')
#driver.find_element(By.CSS_SELECTOR,'.s_ipt_wr input').send_keys('123')
#driver.find_element(By.CSS_SELECTOR,'.s-hotsearch-wrapper ul li:nth-child(1)').click()
el1=driver.find_element(By.CSS_SELECTOR,'#kw')
# ActionChains(driver).key_down(Keys.SHIFT,el1).send_keys('qwe').send_keys(Keys.ARROW_LEFT)\
#             .key_down(Keys.CONTROL)\
#             .send_keys("xvvvvv")\
#             .key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.SHIFT,el1).send_keys('qwe').key_down(Keys.ENTER).perform()
time.sleep(2)
el2=driver.find_element(By.CSS_SELECTOR,'.page-item_M4MDr')
ActionChains(driver).scroll_to_element(el2).perform()
ActionChains(driver).scroll_by_amount(0, 10000).perform()
time.sleep(5)
time.sleep(2)
driver.switch_to.alert.accept()
driver.switch_to.default_content()
# js='document.documentElement.scrollTop=10000'
# driver.execute_script(js)
# time.sleep(2)
# el1.send_keys('123')
# el1.send_keys(Keys.CONTROL,'a')
# time.sleep(2)
# el1.send_keys(Keys.CONTROL,'c')
# time.sleep(2)
# el1.send_keys(Keys.CONTROL,'v')
# time.sleep(2)
# el1.send_keys(Keys.CONTROL,'v')
#ActionChains(driver).key_down(Keys.ENTER).perform()
#el1.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
#driver.find_element(By.ID,'123')
# a='ASDWQ'
# b=a.lower()
# c=b.upper()
# print(b)
# print(c)

# def waiceng(a,b):
#     def nei(driver):
#         driver.find_element(By.ID,'a').click()
#         return driver.find_element(By.ID,'b').click()
#     return nei
# WebDriverWait(driver, 10, 0.5).until(EC.waiceng('xj_kh.custman','qweqe'))
