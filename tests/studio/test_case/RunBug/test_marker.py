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

@allure.feature('排料')
@allure.severity(allure.severity_level.CRITICAL)
class TestMarker:

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

    @allure.story('其中一个版片隐藏后，在2D打开显示尺寸或显示面料，全选版片进入排料崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/2b6d55d48a2d40f81f513c5709', name='STUDIO-6689')
    def test_marker_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6689.sproj')
        time.sleep(2)
        self.style.focus_panorama()
        auto.click(x=555, y=430, button='left', duration=0.2)  # 点击2D
        auto.hotkey('ctrl', 'a')
        auto.click(x=30, y=136, button='left', duration=0.2)  #点击显示面料
        auto.click(x=30, y=303, button='left', duration=0.2)  #点击显示尺寸
        self.style.click_marker()
        time.sleep(2)
        style = "STUDIO-6689，有隐藏版片，在2D打开显示尺寸或显示面料，全选版片进入排料崩溃"
        new = "\\RunBug\\Marker\\"+style+"_new.png"
        old = "\\RunBug\\Marker\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)



