# coding:utf-8

import time
from selenium import webdriver
from common.base import Base

url = "https://spman.shb02.net/admin/login"


class ZenTaoLogin(Base):
    # 定位登录
    loc1 = ("xpath", ".//*[@id='login_name']")
    loc2 = ("xpath", ".//*[@id='password']")
    loc3 = ("xpath", "//*[text()='登录']")
    loc4 = ("xpath", "//*[text()='首页']")
    loc5 = ("xpath", "//*[text()='密码错误']")

    def login(self, user, paw):
        '''登录'''
        self.driver.get(url)
        self.sendKeys(self.loc1, user)
        self.sendKeys(self.loc2, paw)
        self.click(self.loc3)

    def get_login_success(self):
        '''登陆成功判断'''
        result = self.get_text(self.loc4)
        return result

    def get_login_fail(self):
        '''登陆失败判断'''
        result = self.get_text(self.loc5)
        return result

    def exit_refresh(self):
        '''清空cookie并刷新'''
        self.driver.delete_all_cookies()
        self.driver.refresh()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login = ZenTaoLogin(driver)
    login.login("spman_admin", "111111")
    a = login.get_login_success()
    print(a)





