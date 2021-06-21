from selenium import webdriver
import time


# 打开浏览器，进入百度指数首页
url = "http://index.baidu.com/v2/index.html#/"
browser = webdriver.Firefox()
browser.get(url)

# 完成登录的过程
browser.find_element_by_class_name("username-text").click()
time.sleep(1)
browser.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("15862491019")
browser.find_element_by_id("TANGRAM__PSP_4__password").send_keys("WL890208li")
browser.find_element_by_id("TANGRAM__PSP_4__submit").click()

# 找到百度指数的搜索框，输入关键词语，点击搜索按钮
time.sleep(10)  # 此处等待目的是手动完成验证码操作
browser.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(5)
browser.find_element_by_class_name("search-input").send_keys("python爬虫")
browser.find_element_by_class_name("search-input-cancle").click()

# 对图标数据不好抓，可以截图
time.sleep(1)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
browser.save_screenshot("baiduIndex.png")
