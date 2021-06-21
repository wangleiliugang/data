from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('http://www.bing.com')
time.sleep(2)
browser.find_element_by_id('sb_form_q').send_keys('区块链')
time.sleep(2)
browser.find_element_by_id('sb_form_go').click()

with open("bingSearch.html", 'wb') as f:
    f.write(browser.page_source.encode("utf-8"))

time.sleep(5)
browser.quit()
browser.close()
