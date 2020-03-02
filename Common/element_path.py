#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : element_path

"""
定义文件路径
"""

import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Element():
    # 常用操作关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"

    # 路径
    REPORT_XML = PATH("../OutPuts/reports/xml")
    REPORT_HTML = PATH("../OutPuts/reports/html")
    IMAGES=PATH("../OutPuts/images")

    CONFIG = PATH("../config/config.ini")
    PARAMS = PATH("../TestData")
    ASSERT_SQL = PATH("../params/assert_sql.yml")
    Allure_Path = PATH("../OutPuts/allure-2.12.1/bin")
    ENVIRONMENT = PATH("../reports/xml/environment.xml")
