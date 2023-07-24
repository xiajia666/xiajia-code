# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('图形显示')
@allure.severity(allure.severity_level.CRITICAL)
class TestShow:

    def setup_class(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_class(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        self.log.info('结束该用例')

    @allure.story('添加时2D测量，外框预览')
    def test_show_one(self):
        auto.click(x=conf["Graphic"]["show_one_1"]["x"], y=conf["Graphic"]["show_one_1"]["y"], clicks=conf["Graphic"]["show_one_1"]["clicks"],button=conf["Graphic"]["show_one_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["show_one_4"]["x"], y=conf["Graphic"]["show_one_4"]["y"], clicks=conf["Graphic"]["show_one_4"]["clicks"],button=conf["Graphic"]["show_one_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_one_6"]["x"], y=conf["Graphic"]["show_one_6"]["y"], clicks=conf["Graphic"]["show_one_6"]["clicks"],button=conf["Graphic"]["show_one_6"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["show_one_9"]["x"], y=conf["Graphic"]["show_one_9"]["y"], clicks=conf["Graphic"]["show_one_9"]["clicks"],button=conf["Graphic"]["show_one_9"]["button"], duration=0.2)
        auto.press("9")
        auto.click(x=conf["Graphic"]["show_one_12"]["x"], y=conf["Graphic"]["show_one_12"]["y"], clicks=conf["Graphic"]["show_one_12"]["clicks"],button=conf["Graphic"]["show_one_12"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_one_14"]["x"], y=conf["Graphic"]["show_one_14"]["y"], clicks=conf["Graphic"]["show_one_14"]["clicks"],button=conf["Graphic"]["show_one_14"]["button"], duration=0.2)
        auto.press("2")
        auto.click(x=conf["Graphic"]["show_one_21"]["x"], y=conf["Graphic"]["show_one_21"]["y"], clicks=conf["Graphic"]["show_one_21"]["clicks"],button=conf["Graphic"]["show_one_21"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_one_23"]["x"], y=conf["Graphic"]["show_one_23"]["y"], clicks=conf["Graphic"]["show_one_23"]["clicks"],button=conf["Graphic"]["show_one_23"]["button"], duration=0.2)
        auto.moveTo(x=conf["Graphic"]["show_one_27"]["x"], y=conf["Graphic"]["show_one_27"]["y"], tween=auto.linear, duration=0.2)
        time.sleep(2)
        style = '添加时2D测量，外框预览'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)


    @allure.story('图案显示2D测量')
    def test_show_two(self):
        auto.click(x=conf["Graphic"]["show_two_1"]["x"], y=conf["Graphic"]["show_two_1"]["y"], clicks=conf["Graphic"]["show_two_1"]["clicks"],button=conf["Graphic"]["show_two_1"]["button"], duration=0.2)
        auto.typewrite("s")
        auto.click(x=conf["Graphic"]["show_two_4"]["x"], y=conf["Graphic"]["show_two_4"]["y"], clicks=conf["Graphic"]["show_two_4"]["clicks"],button=conf["Graphic"]["show_two_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_6"]["x"], y=conf["Graphic"]["show_two_6"]["y"], clicks=conf["Graphic"]["show_two_6"]["clicks"],button=conf["Graphic"]["show_two_6"]["button"], duration=0.2)
        auto.typewrite("q")
        auto.click(x=conf["Graphic"]["show_two_9"]["x"], y=conf["Graphic"]["show_two_9"]["y"], clicks=conf["Graphic"]["show_two_9"]["clicks"],button=conf["Graphic"]["show_two_9"]["button"], duration=0.2)
        auto.typewrite("9")
        auto.click(x=conf["Graphic"]["show_two_12"]["x"], y=conf["Graphic"]["show_two_12"]["y"], clicks=conf["Graphic"]["show_two_12"]["clicks"],button=conf["Graphic"]["show_two_12"]["button"], duration=0.2)
        auto.typewrite("2")
        auto.click(x=conf["Graphic"]["show_two_15"]["x"], y=conf["Graphic"]["show_two_15"]["y"], clicks=conf["Graphic"]["show_two_15"]["clicks"],button=conf["Graphic"]["show_two_15"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_17"]["x"], y=conf["Graphic"]["show_two_17"]["y"], clicks=conf["Graphic"]["show_two_17"]["clicks"],button=conf["Graphic"]["show_two_17"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_19"]["x"], y=conf["Graphic"]["show_two_19"]["y"], clicks=conf["Graphic"]["show_two_19"]["clicks"],button=conf["Graphic"]["show_two_19"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_21"]["x"], y=conf["Graphic"]["show_two_21"]["y"], clicks=conf["Graphic"]["show_two_21"]["clicks"],button=conf["Graphic"]["show_two_21"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_23"]["x"], y=conf["Graphic"]["show_two_23"]["y"], clicks=conf["Graphic"]["show_two_23"]["clicks"],button=conf["Graphic"]["show_two_23"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_25"]["x"], y=conf["Graphic"]["show_two_25"]["y"], clicks=conf["Graphic"]["show_two_25"]["clicks"],button=conf["Graphic"]["show_two_25"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_27"]["x"], y=conf["Graphic"]["show_two_27"]["y"], clicks=conf["Graphic"]["show_two_27"]["clicks"],button=conf["Graphic"]["show_two_27"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_29"]["x"], y=conf["Graphic"]["show_two_29"]["y"], clicks=conf["Graphic"]["show_two_29"]["clicks"],button=conf["Graphic"]["show_two_29"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_31"]["x"], y=conf["Graphic"]["show_two_31"]["y"], clicks=conf["Graphic"]["show_two_31"]["clicks"],button=conf["Graphic"]["show_two_31"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_33"]["x"], y=conf["Graphic"]["show_two_33"]["y"], clicks=conf["Graphic"]["show_two_33"]["clicks"],button=conf["Graphic"]["show_two_33"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_35"]["x"], y=conf["Graphic"]["show_two_35"]["y"], clicks=conf["Graphic"]["show_two_35"]["clicks"],button=conf["Graphic"]["show_two_35"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["show_two_37"]["x"], y=conf["Graphic"]["show_two_37"]["y"], clicks=conf["Graphic"]["show_two_37"]["clicks"],button=conf["Graphic"]["show_two_37"]["button"], duration=0.2)
        time.sleep(1)
        style = '图案显示2D测量'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)