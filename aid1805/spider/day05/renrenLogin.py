from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get("http://renren.com")
browser.find_element_by_id('email').send_keys('123456')
browser.find_element_by_id('password').send_keys('111222')

time.sleep(10)
# browser.find_element_by_id('login_weixin').click()
