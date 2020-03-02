#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : basepage

import logging
import time, datetime, os, sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.element_path import Element


# 封装基本函数 - 定位方法、 截图
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, type, *loc):
        elements = {
            Element.find_element_by_id: lambda: self.driver.find_element(*loc),

        }
        return elements[type]()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def send_keys(self, key, *loc):
        self.find_element(*loc).clear()
        return self.find_element(*loc).send_keys(key)

    def get_time(self):
        self.now = time.strftime("%Y%m%d%H%M%S")
        return self.now

    def get_window_size(self):
        """
        获取窗口大小
        :return:
        """
        return self.driver.get_window_size()

    def get_windows_img(self, name):
        """截图函数"""

        imagetime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logging.error(Element.IMAGES)
        screen_name = Element.IMAGES + '/' + imagetime + '_' + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info('截图成功，路径为：{}'.format(screen_name))
        except NameError as e:
            logging.error("截图失败:{}".format(e))

    # 等待页面元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logging.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except:
            logging.info('{0},等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)


if __name__ == '__main__':
    pass
