#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : conftest

import pytest
import logging
from Common.LoggingConf import loggering
from Common.Webdrivers import *
from Config.config import Config

loggering()
driver = None

@pytest.fixture(scope='module')
def Driver():
    driver = Webdriver()
    driver.maximize_window()
    driver.get(Config().base_url)
    yield driver
    driver.quit()
