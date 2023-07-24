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

@allure.feature('延展')
@allure.severity(allure.severity_level.CRITICAL)
class TestFullness:

    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()

    @allure.story('延展起终点在同一边上，其中一个在版片端点，延展鼠标移动到端点处，点击崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/9081cbe8e26518905fabf4e42b', name='STUDIO-6644')
    def test_fullness_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=144, y=302, button='left', duration=0.2) #点击起点
        auto.click(x=285, y=302, button='left', duration=0.2) #点击终点
        time.sleep(3)
        auto.click(x=144, y=302, button='left', duration=0.2)  #点击起点
        auto.click(x=245, y=210, button='left', duration=0.2)   #旋转
        time.sleep(1)
        style = "STUDIO-6644，延展起终点在同一边上，点击崩溃"
        new = "\\RunBug\\Fullness\\"+style+"_new.png"
        old = "\\RunBug\\Fullness\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)



