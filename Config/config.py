#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : config


from configparser import ConfigParser
from Common.ElementPath import Element


class Config:

    def __init__(self):
        self.config = ConfigParser()
        self.conf_path = Element.CONFIG

        self.config.read(self.conf_path, encoding='utf-8')

        # base_url
        self.base_url = self.get_conf('base_url', 'url')

        # 数据库
        self.mysql_host = self.get_conf('mysql', 'host')
        self.mysql_port = self.get_conf('mysql', 'port')
        self.mysql_user = self.get_conf('mysql', 'user')
        self.mysql_password = self.get_conf('mysql', 'password')
        self.mysql_db = self.get_conf('mysql', 'db')
        self.mysql_charset = self.get_conf('mysql', 'charset')

        # 邮箱
        self.mail_smtpserver = self.get_conf('mail', 'smtpserver')
        self.mail_sender = self.get_conf('mail', 'sender')
        self.mail_receiver = self.get_conf('mail', 'receiver')
        self.mail_name = self.get_conf('mail', 'name')
        self.mail_username = self.get_conf('mail', 'username')
        self.mail_password = self.get_conf('mail', 'password')

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)


if __name__ == '__main__':
    a = Config()
    print(a.mail_password)
