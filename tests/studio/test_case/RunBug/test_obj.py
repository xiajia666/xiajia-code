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

@allure.feature('OBJ')
@allure.severity(allure.severity_level.CRITICAL)
class TestObj:

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


    @allure.story('STUDIO-7655编辑版片模式，导入OBJ作为服装，软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/f18bdb394a843247cb0086fb93',name='STUDIO-7655')
    def test_obj_one(self):
        self.style.click_edit_pattern()
        self.style.click_import_obj()
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'sproj\\STUDIO-7655.obj')
        pyperclip.copy(import_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')

        time.sleep(1)
        auto.click(x=846, y=762, clicks=1, button='left', duration=0.2)  # 点击重置
        auto.click(x=965, y=322, clicks=1, button='left', duration=0.2)  # 点击物体类型下拉框
        auto.click(x=965, y=383, clicks=1, button='left', duration=0.2)  # 点击添加服装
        auto.click(x=922, y=346, clicks=1, button='left', duration=0.2)  # 点击在UV图中勾勒2D版片
        auto.click(x=995, y=697, clicks=1, button='left', duration=0.2)  # 点击确定

        time.sleep(3)

        style = "STUDIO-7655编辑版片模式，导入OBJ作为服装，软件崩溃"
        new = "\\RunBug\\OBJ\\" + style + "_new.png"
        old = "\\RunBug\\OBJ\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

