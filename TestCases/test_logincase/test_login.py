#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_login


import allure
from PageObjects.LoginPage.login_page import LoginPage
from Common.element_path import Element


class Test_Login():
    @allure.story('测试测试')
    def test_login_usernameFormat_error(self, Driver):
        with open(Element.IMAGES + "/images20200302141947_登录.png", mode='rb') as f:
            file = f.read()
            allure.attach(file, '登录界面', allure.attachment_type.PNG)

        assert LoginPage(Driver).login() == 2
