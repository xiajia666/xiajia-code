# -*- coding: utf-8 -*-
import sys
import os
import pyperclip
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('拉链')
@allure.severity(allure.severity_level.CRITICAL)
class TestZipper:

    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        # self.style.start_style3D()

    def teardown_method(self):
        self.log.info('测试结束，关闭软件')
        # self.style.close_style3D()


    @allure.story('STUDIO-78843D在内部线上添加拉链')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/c5ee42e48fa7879cd891546649',name='STUDIO-7884')
    def test_symmetrical_five(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7884.sproj')
        self.style.focus_panorama()
        auto.click(x=990, y=260, clicks=1, button='left', duration=0.2) #3D点击空白处，变焦到全景
        auto.press("9")

        auto.click(x=1603, y=252, clicks=1, button='left', duration=0.2)  # 点击当前栏拉链
        time.sleep(1)

        auto.click(x=886, y=459, clicks=1, button='left', duration=0.2)  # 点击拉链起点
        auto.doubleClick(x=912, y=659, clicks=1, button='left', duration=0.2) # 点击拉链终点
        time.sleep(1)
        auto.click(x=1164, y=468, clicks=1, button='left', duration=0.2)  # 点击拉链起点
        auto.doubleClick(x=1203, y=628, clicks=1, button='left', duration=0.2)  # 点击拉链终点

        style = "STUDIO-78843D在内部线上添加拉链"
        new = "\\RunBug\\Zipper\\" + style + "_new.png"
        old = "\\RunBug\\Zipper\\" + style + "_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)



