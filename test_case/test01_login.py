# coding:utf-8
import unittest
import time
from selenium import webdriver
from pages.login_page import ZenTaoLogin


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()
        cls.loginfun = ZenTaoLogin(cls.driver)

    def setUp(self):
        self.loginfun.exit_refresh()

    def test_01(self):
        '''正常登录系统'''
        self.loginfun.login("spman_admin", "111111")
        text = self.loginfun.get_login_success()
        print(text)
        self.assertTrue(text == "首页")

    def test_02(self):
        '''正常登录系统'''
        self.loginfun.login("spman_admin", "111112")
        text = self.loginfun.get_login_fail()
        print(text)
        self.assertTrue(text == "密码错误")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



