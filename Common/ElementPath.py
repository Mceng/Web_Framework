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
    find_element_by_link_text = "link_text"

    CLICK = "click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUE = "get_value"
    WAIT_TIME = 20  # 查找元素等待时间
    MOVE_TO_ELEMENT = "move_to_element" # 鼠标悬停
    DEFAULT_OPERATE= "default_operate" # 默认值

    # 检查点
    CONTRARY = "contrary" # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval" # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check" # 默认检查点，就是查找页面元素
    COMPARE = "compare" # 历史数据和实际数据对比

    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"


    # 路径
    REPORT_XML = PATH("../OutPuts/reports/xml")
    REPORT_HTML = PATH("../OutPuts/reports/html")
    IMAGES = PATH("../OutPuts/images")
    CONFIG = PATH("../Config/config.ini")
    PARAMS = PATH("../TestData")
    ASSERT_SQL = PATH("../params/assert_sql.yml")
    Allure_Path = PATH("../OutPuts/allure-2.12.1/bin")
    ENVIRONMENT = PATH("../reports/xml/environment.xml")

    # 用例数据路径
    test_login_data = PATH("../TestData/Login/test_login_data.yml")
