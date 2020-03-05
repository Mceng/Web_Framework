#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : basepage

"""
封装基本函数 - 定位方法、 截图、查找元素是否存在，操作页面元素
"""

import logging
import time, datetime
import re
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.ElementPath import Element
import selenium.common.exceptions
from selenium.common.exceptions import NoSuchElementException
from Common.base_web_page import Base_Web_Page
from Common.BaseAppPage import Base_App_Page


class BasePage(Base_Web_Page, Base_App_Page):

    def operate(self, operate, testInfo):
        res = self.findElement(operate)
        if res["result"]:
            return self.operate_by(operate, testInfo)
        else:
            return res

    def findElement(self, operate):
        '''
        查找元素.operate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            t = operate["check_time"] if operate.get("check_time", "0") != "0" \
                else Element.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
            if type(operate) == list:  # 多检查点
                for item in operate:
                    t = item["check_time"] if item.get("check_time", "0") != "0" else Element.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                return {"result": True}

            if type(operate) == dict:  # 单检查点
                if operate.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {"result": True}

                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operate))
                return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            self.write_step_img('查找元素超时')
            logging.error("==查找元素超时==")
            return {"result": False, "type": Element.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            self.write_step_img('查找元素不存在')
            logging.error("==查找元素不存在==")
            return {"result": False, "type": Element.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            self.write_step_img('WebDriver出现问题了')
            logging.error("==WebDriver出现问题了==")
            return {"result": False, "type": Element.WEB_DROVER_EXCEPTION}

    def operate_by(self, operate, testInfo):
        elements = {
            Element.CLICK: lambda: self.click(operate),
            Element.GET_VALUE: lambda: self.get_value(operate),
            Element.GET_TEXT: lambda: self.get_text(operate),
            Element.SEND_KEYS: lambda: self.send_keys(operate),
            Element.MOVE_TO_ELEMENT: lambda: self.move_to_element(operate)
        }
        try:
            info = "定位元素-%s_定位方法-%s_操作方法-%s_具体信息-%s" % (
                operate.get("element_info", " "), operate.get("find_type"), operate.get("operate_type", " "),
                operate.get("msg", " "))

            logging.info(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_操作步骤：%s==" + info)  # 记录日志

            if operate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
                return {"result": True}

            return elements[operate.get("operate_type")]()
        except IndexError:
            logging.error(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
            return {"result": False, "type": Element.INDEX_ERROR}

        except selenium.common.exceptions.NoSuchElementException:
            logging.error(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志

            return {"result": False, "type": Element.NO_SUCH}
        except selenium.common.exceptions.StaleElementReferenceException:
            logging.error(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            return {"result": False, "type": Element.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 点击事件
    def click(self, operate):
        if operate["find_type"] == Element.find_element_by_id or operate["find_type"] == Element.find_element_by_xpath \
                or Element.find_element_by_css_selector or operate["find_type"] == Element.find_element_by_class_name or \
                operate["find_type"] == Element.find_element_by_link_text:
            self.elements_by(operate).click()
        elif operate.get("find_type") == Element.find_elements_by_id:
            self.elements_by(operate)[operate["index"]].click()
        return {"result": True}

    def send_keys(self, operate):
        """
        :param operate:
        :return:
        """
        time.sleep(0.5)
        self.elements_by(operate).send_keys(operate["msg"])
        return {"result": True}

    def get_text(self, operate):
        '''
        :param operate:
        :return: {}
        '''

        if operate.get("find_type") == Element.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("text")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        # result = element_info.get_attribute("text")
        result = element_info.text

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    def get_value(self, operate):
        if operate.get("find_type") == Element.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("value")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("value")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    def move_to_element(self, operate):
        """
        鼠标悬停
        :param operate:
        :return:
        """

        ActionChains(self.driver).move_to_element(self.elements_by(operate)).perform()
        return {"result": True}

    def elements_by(self, case):
        """
        封装常用的标签

        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        :param case: dist={element_info,find_type,operate_type,info}
        :return:
        """

        elements = {
            Element.find_element_by_id: lambda: self.driver.find_element_by_id(case["element_info"]),
            Element.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(case["element_info"]),
            Element.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(case['element_info']),
            Element.find_elements_by_id: lambda: self.driver.find_elements_by_id(case['element_info']),
            Element.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(
                case['element_info']),
            Element.find_element_by_link_text: lambda: self.driver.find_element_by_link_text(case['element_info'])

        }
        return elements[case["find_type"]]()


    #
    # def find_element(self, *loc):
    #     try:
    #         return WebDriverWait(self.driver, Element.WAIT_TIME).until(
    #             lambda x: x.find_element(*loc)
    #         )
    #         # return self.driver.find_element(*loc)
    #     except NoSuchElementException as e:
    #         logging.error(e.args[0])
    #
    # def find_elements(self, *loc):
    #     try:
    #         return WebDriverWait(self.driver, Element.WAIT_TIME).until(
    #             lambda x: x.find_elements(*loc)
    #         )
    #     except NoSuchElementException as e:
    #         logging.error(e.args[0])

    # def send_keys(self, key, *loc):
    #     self.find_element(*loc).clear()
    #     return self.find_element(*loc).send_keys(key)
    #
    # def click(self, *loc):
    #     return self.find_element(*loc).click()

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
        screen_name = Element.IMAGES + '/' + imagetime + '_' + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info('截图成功，路径为：{}'.format(screen_name))
            return screen_name

        except NameError as e:
            logging.error("截图失败:{}".format(e))
            return False

    def write_step_img(self, name):
        image=self.get_windows_img(name)
        if image:
            with open(image, mode='rb') as f:
                file = f.read()
                allure.attach(file, name, allure.attachment_type.PNG)

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
            self.get_windows_img(doc)


if __name__ == '__main__':
    pass
