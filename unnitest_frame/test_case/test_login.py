
import unittest
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from pageobjects.pagelogin import Loginpage
from data.read_write import ReadWrite
from config.config import driver_path,url,file,sheet
from log.log import logger

class TestCases(unittest.TestCase):
    def setUp(self):        #跟随类执行一次
        print('打开浏览器')
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)  # 打开浏览器
        self.driver.maximize_window()
        self.driver.get(url)
        self.page=Loginpage(self.driver)
        self.doc1=ReadWrite(file,sheet)

    def tearDown(self):
        print('关闭浏览器')
        time.sleep(5)
        self.driver.quit()

# 测试用例1
    def test_login_success(self):
        '''成功登录'''
        data_list=self.doc1.read()
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()
        time.sleep(2)
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            print('验证登录成功测试----passed')
            logger.info("验证用户登录成功的信息")
        except:
            print("验证登录成功测试----failed")

# # 测试用例2
    @unittest.skip("该版本不需要执行")              #加装饰器，跳过
    def test_login_wrongpassword(self):
        """错误密码登录失败"""
        data_list=self.doc1.read()
        self.page.type_username(data_list[1][0])
        self.page.type_password(data_list[1][1])
        self.page.click_login()
        time.sleep(2)
        try:
            alert=self.driver.switch_to.alert
            assert "登录失败" in alert.text
            alert.accept()
            print("验证错误的密码登录失败----passed")
        except:
            print("验证错误的密码登录失败----failed")

 # #测试用例3
    @unittest.skip("该版本不需要执行")          #加装饰器，跳过
    def test_login_wrongaccount(self):
        """用户不存在登录失败"""
        data_list = self.doc1.read()
        self.page.type_username(data_list[2][0])
        self.page.type_password(data_list[2][1])
        self.page.click_login()
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            assert "登录失败" in alert.text
            alert.accept()
            print("验证不存在的用户登录失败----passed")
        except:
            print("验证不存在的用户登录失败----failed")



if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    # suite.addTest(TestCases('test_adduser'))
    # suite.addTest(TestCases('test_showuser'))
    # suite.addTest(TestCases('test_updateuser'))
    # suite.addTest(TestCases('test_deleteuser'))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    test_runner=unittest.TextTestRunner()
    test_runner.run(suite)