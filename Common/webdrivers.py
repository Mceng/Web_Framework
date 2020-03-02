#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-3-2 16:34:23
# @Author  : Mcen (mmocheng@163.com)


import os
import logging
import logging.config
from selenium import webdriver
import multiprocessing


def Webdriver(name='chrome'):
    try:
        if name == 'firefox' or name == 'Firefox':
            logging.info('启动浏览器为：firefox')
            driver = webdriver.firefox()
        elif name == 'chrome':
            logging.info('启动浏览器为：Chrome')
            driver = webdriver.Chrome()
        elif name == 'ie':
            logging.info('启动浏览器为：ie')
            driver = webdriver.ie()
        elif name == 'ChromeOptions':
            logging.info('启动浏览器为：ChromeOptions')
            options=webdriver.ChromeOptions()
            options.set_headless()
            options.add_argument('--headless')
            driver=webdriver.Chrome(options=options)
        else:
            logging.error('Not found this browser')

        driver.maximize_window()
        driver.implicitly_wait(30)

        return driver

    except Exception as e:
        logging.error('启动浏览器出现异常：{}'.format(e))



def Webdriver123():

    #使用渲染式浏览器
    logging.info('=====Start Chrome=======')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    verificationErrors = []
    accept_next_alert = True
    return driver

def Webdriver11():
    threads=[]
    #drive=['chromedriver.exe','geckodriver.exe']
    Browser=['chrome','ChromeOptions']

    for i in range(len(Browser)):
        #DrivePath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_drivers', drive[i])
        desired = multiprocessing.Process(target=stratBrowser,args=(Browser[i],))
        threads.append(desired)

    for desired in threads:
        desired.start()
    for desired in threads:
        desired.join()


if __name__ == '__main__':
    Webdriver()
