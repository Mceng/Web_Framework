#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : conftest

import pytest
import logging
from Common.logging_conf import loggering
from Common.webdrivers import *

loggering()
driver = None

@pytest.fixture(scope='module')
def Driver():
    driver = Webdriver()
    driver.maximize_window()
    yield driver
    driver.quit()
