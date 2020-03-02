# Web_Framework
这是一个WebUI自动化测试的项目

Python+Pytest+Selenium+Allure+PageObject

实现页面元素、页面对象及业务、测试数据分离

项目结构：说明

            .
            |-- AppDrivers                  ---------------------存放驱动
            |-- TestCases                   --------------------- 测试用例模块
            |   |-- conftest.py
            |   |-- __init__.py
            |   |-- logincases              --------------------- 测试模块
            |   |   |-- conftest.py
            |   |   |-- __init__.py
            |   |   `-- test_login.py
            |-- Common                      --------------------- 功能函数
            |   |   |-- basepage.py         --------------------- 基础界面
            |   |   |-- element_path.py     --------------------- 封装的常用路径
            |   |   |-- get_config.py       --------------------- 获取配置文件方法
            |   |   |-- logging_conf.py     --------------------- 日志的配置方法
            |   |   |-- until_fun.py        --------------------- 工具方法
            |   |   |-- webdrivers.py        --------------------- 封装的 webdriver
            |   |   |-- __init__.py
            |-- OutPuts                     --------------------- 输出
            |   |-- images                  --------------------- 截图
            |   |-- logs                    --------------------- 日志
            |   -- reports                  --------------------- 报告
            |-- PageObjects                 ---------------------- 业务流程
            |   |-- LoginPage               ---------------------- 登录模块的页面对象
            |   |   |-- __init__.py
            |   |   |-- login_page.py
            |-- TestDatas                   ---------------------- 测试数据
            |-- README.md
            |-- pytest.ini
            |-- run.py                      ---------------------- 城市执行入口
            


