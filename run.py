#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : run



"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import sys

import pytest
from Common.Shell import Shell
from Common.ElementPath import Element
from Common.UntilFun import remore_filedir
# from utils.send_email import SendMail
from Common.LoggingConf import loggering
import logging


loggering()

def run():

    xml_report_path = Element.REPORT_XML
    html_report_path = Element.REPORT_HTML


    remore_filedir(html_report_path)





    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    # pytest.main()



    run_allure_html(xml_report_path, html_report_path)

    # 发送邮件
    # SendMail().send_mail()


def run_allure_html(xml_report_path, html_report_path):
    """
    通过XML文件生成HTML报告
    :param xml_report_path:
    :param html_report_path:
    :return:
    """
    try:
        cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
        Shell.run_shell(cmd)
    except Exception:
        logging.error('执行用例失败，请检查环境配置')
        raise


if __name__ == '__main__':
    run()
