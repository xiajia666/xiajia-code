import requests
import json
import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
auto.FAILSAFE = False
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud
import allure
import pytest

@allure.feature('获取版本号')
@allure.severity(allure.severity_level.CRITICAL)
class TestGetVersion:
    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()

    def test_check_window(self): #避免Jenkins调起第一次启动可能有bug
        self.style.rectangle_creat()

    def test_check_window_again(self): #避免Jenkins调起第一次启动可能有bug
        self.style.rectangle_creat()

    def test_get_version(self):
        self.style.send_message("Style3D 自动化测试开始，本次测试版本号：", "18069806966", "15757119427", "18066268343")