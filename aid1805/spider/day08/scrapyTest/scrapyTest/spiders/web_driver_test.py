# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:37:47 2021

@author: 13775
"""
#from selenium import webdriver
#import random
#
#driver = webdriver.Firefox()
#driver.get("https://www.baidu.com")
#driver.implicitly_wait(10)
#driver.find_element_by_id("kw").send_keys(u"测试部落")
#driver.find_element_by_id("kw").submit()
#s = driver.find_elements_by_css_selector("h3.t>a")
#print(s)
#
## 设置随机值
#t = random.randint(0, 9)
## 随机取一个结果点击鼠标
#s[t].click()

#from selenium import webdriver
#import time
#
#
#driver = webdriver.Firefox()
#driver.get("https://kyfw.12306.cn/otn/index/init")
## 去掉元素的readonly属性
#js = 'document.getElementById("train_date").removeAttribute("readonly");'
#driver.execute_script(js)
#time.sleep(3)
## 用js方法输入日期
#js_value = 'document.getElementById("train_date").value="2016-12-25"'
#driver.execute_script(js_value)
# # 清空文本后输入值
#driver.find_element_by_id("train_date").clear()
#driver.find_element_by_id("train_date").send_keys("2016-12-25")
 

#import unittest
#    
#class IntegerArithmeticTestCase(unittest.TestCase):
#    def testAdd(self):  ## test method names begin 'test*'
#        self.assertEqual((1 + 2), 3)
#        self.assertEqual(0 + 1, 1)
#    def testMultiply(self):
#        self.assertEqual((0 * 10), 0)
#        self.assertEqual((5 * 8), 40)
#    
#if __name__ == '__main__':
#       unittest.main()


#from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
#import time
#import unittest
#
#
#class Blog(unittest.TestCase):
#    def setUp(self):
#        self.driver = webdriver.Firefox()
#        self.driver.get("http://www.cnblogs.com/yoyoketang")
#    def test_blog(self):
#        time.sleep(3)
#        result = EC.title_is(u'上海-悠悠 - 博客园')(self.driver)
#        print(result)
#        self.assertTrue(result)
#    def tearDown(self):
#        self.driver.quit()
#if __name__ == "__main__":
#    unittest.main()


from selenium import webdriver
import unittest
import time
class Bolg(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)
    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False
    def test_01(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"上海-悠悠", u"xxxx")  # 调用登录方法
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
