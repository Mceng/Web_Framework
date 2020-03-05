#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : login_page

from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from Common.Pages import Pages

class LoginPage():
    def __init__(self,app):
        self.page = Pages(app)

    def operate(self):
        self.page.operate()

    def checkPoint(self):  # 检查点
        return self.page.check()

    # login_username = (By.ID, 'inp')
    # password = (By.XPATH,'//*[@id ="password"]/div/div[1]/input')
    # login_Btn = (By.XPATH,'//*[@id="app"]/div/div[1]/form/div[4]/div/button')


    # def login(self):
    #     base_url = 'https://iparking.ibotech.com.cn/'
    #
    #     self.driver.get(base_url)
    #     time.sleep(10)
    #     username = 13800138001
    #     password = 138001
    #     # self.find_element(*self.login_username).send_keys(username)
    #     self.send_keys(username, *self.login_username)
    #     self.send_keys(password, *self.password)
    #
    #     self.get_windows_img('登录')
    #
    #
    #     self.find_element(*self.login_Btn).click()
    #     time.sleep(10)
    #     return 2