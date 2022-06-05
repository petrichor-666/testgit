

import unittest
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        s = Service(r"D:\Python\loguru\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)  # 打开浏览器
        cls.driver.maximize_window()
        cls.driver.get('http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        time.sleep(5)
        cls.driver.quit()

    def setUp(self):        #跟随类执行一次
        print('登录')
        self.driver.find_element(By.CSS_SELECTOR, '#account').send_keys('shelly')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('p@ssw0rd')
        self.driver.find_element(By.CSS_SELECTOR, '.form-actions :nth-child(1)').click()
        time.sleep(2)

    def tearDown(self):
        print('登出禅道')
        self.driver.find_element(By.XPATH, '//a[@class="dropdown-toggle"]/span[1]').click()
        self.driver.find_element(By.LINK_TEXT, '退出').click()

# 测试用例1
    def test_addbug_success(self):
        """成功添加bug"""
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, '测试').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//nav[@id="subNavbar"]/ul/li[1]/a').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, '提Bug').click()
        self.driver.find_element(By.CLASS_NAME, 'search-field').click()
        self.driver.find_element(By.CLASS_NAME, 'active-result').click()
        self.driver.find_element(By.ID, 'title').send_keys('代码错误')
        time.sleep(1)
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)  # 鼠标滚动1000
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(1)

        dialog = win32gui.FindWindow('#32770', '打开')  # 一级窗口
        combox_32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)  # 二级
        combox = win32gui.FindWindowEx(combox_32, 0, 'ComboBox', None)  # 三级
        edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'button', '打开&O')  # 二级
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None,r'C:\Users\Wangtao\Desktop\mmexport1646572895679.jpg')  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        self.driver.find_element(By.ID,'submit').click()
        time.sleep(2)

        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT, '提Bug').text,"提Bug")
            print("创建Bug成功")
        except:
            print("创建Bug失败")
