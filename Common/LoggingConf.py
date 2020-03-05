#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/25
# @Author  : Mcen (mmocheng@163.com)
# @Name    : log_conf
# coding=utf-8
"""
定义执行日志
"""



import logging,time



def loggering():
    log_date = time.strftime("%Y-%m-%d")
    log_file = log_date + '_run_logging.log'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M',
                        filename='./OutPuts/logs/' + log_file,
                        # filename='../../OutPuts/logs/' + log_file,
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    loggering()
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical error message')
