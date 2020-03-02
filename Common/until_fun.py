#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/2
# @Author  : Mcen (mmocheng@163.com)
# @Name    : until_fun
import os
import yaml
import shutil
from Common.element_path import Element


def read_yaml(yaml_path):
    """
    读取yaml文件
    :param name: yml文件路径
    :return:
    """
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.load(file)

def read_params(file_name):
    """
    读取测试数据文件
    :param file_name:
    :return:
    """
    yaml_path = os.path.join(Element.PARAMS, file_name + '.yml')
    return read_yaml(yaml_path)

def remore_filedir(path):
    """
    删除文件夹下的所有文件
    :param path:
    :return:
    """
    if os.path.isdir(path):
        filelist = []
        filelist = os.listdir(path)  # 列出该目录下的所有文件名
        for f in filelist:
            filepath = os.path.join(path, f)
            if os.path.isfile(filepath):
                os.remove(filepath)  # 若为文件，则直接删除
                print(str(filepath) + " removed!")
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
                print("dir " + str(filepath) + " removed!")
        shutil.rmtree(path, True)  # 最后删除path总文件夹
