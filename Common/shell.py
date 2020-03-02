#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : shell
"""
封装执行shell语句方法

"""

import subprocess
import logging


class Shell:
    @staticmethod
    def run_shell(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        if errors :
            logging.error(errors.decode("GBK"))
        return o