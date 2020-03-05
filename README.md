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
            


用例说明
```
testinfo:
    - id: test001-------用例名称
      title: 登录成功
      info: 打开ibotech
testcase:
    - element_info: inp（定位元素信息）
      find_type: id（定位元素方法）
      operate_type: send_keys（定位元素动作方法）
      info: 输入用户名（信息说明）
      msg: 13800138001（输入信息）
      is_time: 10（等待时间）
      check_time: 10 (等待元素超时时间，默认20)
      index: 1(当定位find_type为复数时，index为定位索引)
    - element_info: //*[@id ="password"]/div/div[1]/input
      find_type: xpath
      operate_type: send_keys
      msg: 138001
      info: 输入密码138001
    - element_info: //*[@id="app"]/div/div[1]/form/div[4]/div/button
      find_type: xpath
      operate_type: click
      info: 点击登录
      is_time: 10

check:
    - element_info: div.alert-warning
      find_type: css
      info: 出现错误的密码登录不成功提示框
```

