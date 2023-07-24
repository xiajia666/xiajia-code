import json
import os,sys
import requests
import yaml
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
import logging
import glob
import autoit


@allure.feature('工程打开保存')
@allure.severity(allure.severity_level.BLOCKER)
class TestOpenAndSave:

    def setup_class(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
    def teardown_class(self):

        self.log.info("测试结束")
        self.style.close_style3D()

    def test_check_window(self): #避免Jenkins调起第一次启动可能有bug
        self.style.start_style3D()
        self.style.rectangle_creat()
        self.style.close_style3D()

    def test_send_message(self):
        self.style.start_style3D()
        self.style.send_message("Style3D 性能专项开始，本次测试版本号：", "18069806966")
        self.style.close_style3D()

    @allure.story('工程打开')
    def test_open(self):
        pass
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'OpenProject')
        sproj_len = self.operationfile.get_file_name(file_path)[0]
        self.log.info(sproj_len)
        length = len(sproj_len)
        for i in range(1, length+1):
            sproj_name = sproj_len[i - 1]
            self.log.info(sproj_name)
            if sproj_name.endswith('.sproj'):
                self.log.info('执行打开')
                self.style.start_style3D()
                sproj_path  = file_path + "\\" + sproj_name
                print(sproj_path)
                pyperclip.copy(sproj_path)
                auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 打开保存机制修改，适配脚本
                auto.click(x=60, y=9, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
                auto.click(x=89, y=66, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
                auto.click(x=229, y=68, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
                auto.click(x=1012, y=596, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                time.sleep(2)
                auto.click(x=987, y=671, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) # 点击确定
                for j in range(100):
                    style = "工程打开确定"
                    new = "\\OpenAndSave\\"+style+"_new.png"
                    old = "\\OpenAndSave\\"+style+"_old.png"
                    # difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
                    difference_data = self.operationfile.comparison_picture_difference(new, old, style, 4, 1017, 77, 1035)
                    difference = difference_data[1][0]
                    self.log.info("%s打开图片有差别" % difference)
                    if difference < 1:
                        self.log.info('工程打开成功')
                        style = "Studio_Test" + str(i)
                        new = "\\Open\\" + style + "_new.png"
                        old = "\\Open\\" + style + "_new.png"
                        self.operationfile.comparison_picture_allure(new, old, style, 50)
                        self.style.close_style3D()
                        break
                    else:
                        self.log.info('等待工程打开')
                        time.sleep(3)
            else:
                self.log.info('非sproj工程不做处理')