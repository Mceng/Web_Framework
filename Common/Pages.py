#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : pages

import time
from Common.BaseYaml import getYaml
from Common.BasePage import BasePage
from Common.ElementPath import Element


class Pages:
    def __init__(self,kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYaml(kwargs["path"]),"caseName": kwargs["caseName"]}

        self.driver = _init["driver"]

        if _init.get("launch", "0") == "0":  # 若为空， 刷新页面
            self.driver.get(self.driver.current_url)
        self.operateElement = ""
        self.isOperate = True
        self.test_msg = _init["test_msg"]
        self.testInfo = self.test_msg[1]["testinfo"]
        self.testCase = self.test_msg[1]["testcase"]
        self.test_check = self.test_msg[1]["check"]
        self.caseName = _init["caseName"]
        self.get_value = []
        self.is_get = False
        self.msg = ""


    def operate(self):
        """
        操作步骤
        :return:
        """

        if self.test_msg[0] is False:
            self.isOperate = False
            return False
        self.operateElement = BasePage(self.driver)
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo)
            print(result)
            if not result["result"]:
                self.isOperate = False
                return False
            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间
                print("==等待%s秒==" % item["is_time"])
            if item.get("operate_type", "0") == Element.GET_VALUE or item.get("operate_type", "0") == Element.GET_TEXT:
                self.get_value.append(result["text"])
                self.is_get = True  # 对比数据

        return True
    def check(self,kwargs={}):
        result = True
        if self.isOperate:
            for item in self.test_check:
                resp = self.operateElement.operate(item, self.testInfo)
                # 默认检查点，就是查找页面元素
                if item.get("check", Element.DEFAULT_CHECK) == Element.DEFAULT_CHECK and not resp["result"]:
                    result = False
                    break
                # 历史数据和实际数据对比
                if item.get("check", Element.DEFAULT_CHECK) == Element.COMPARE and self.is_get and resp["text"]\
                        not in self.get_value:  # 历史数据和实际数据对比
                    result = False
                    break
                #  相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
                if item.get("check", Element.DEFAULT_CHECK) == Element.CONTRARY and resp["result"]:
                    result = False
                    break
                # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
                if item.get("check", Element.DEFAULT_CHECK) == Element.CONTRARY_GETVAL and self.is_get and resp["result"] \
                        in self.get_value:
                    # m = get_error(
                    #     {"type": be.CONTRARY_GETVAL, "current": item["element_info"], "history": resp["text"]})
                    # print(m)
                    # self.testInfo[0]["msg"] = m
                    result = False
                    break

        else:
            result = False
        return result
