from selenium import webdriver


myinput = input("请输入您要查询的单词：")

browser = webdriver.Firefox()
browser.get('http://fanyi.youdao.com/')
browser.find_element_by_id('inputOriginal').send_keys(myinput)
