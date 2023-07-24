# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure


@allure.feature('右键功能')
@allure.severity(allure.severity_level.CRITICAL)
class TestRightFun:

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

    @allure.story('2D右键复制，选择等功能')
    def test_right_one(self):
        auto.click(x=conf["Graphic"]["right_one_1"]["x"], y=conf["Graphic"]["right_one_1"]["y"], clicks=conf["Graphic"]["right_one_1"]["clicks"],button=conf["Graphic"]["right_one_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["right_one_4"]["x"], y=conf["Graphic"]["right_one_4"]["y"], clicks=conf["Graphic"]["right_one_4"]["clicks"],button=conf["Graphic"]["right_one_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_6"]["x"], y=conf["Graphic"]["right_one_6"]["y"], clicks=conf["Graphic"]["right_one_6"]["clicks"],button=conf["Graphic"]["right_one_6"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_8"]["x"], y=conf["Graphic"]["right_one_8"]["y"], clicks=conf["Graphic"]["right_one_8"]["clicks"],button=conf["Graphic"]["right_one_8"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["right_one_11"]["x"], y=conf["Graphic"]["right_one_11"]["y"], clicks=conf["Graphic"]["right_one_11"]["clicks"],button=conf["Graphic"]["right_one_11"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_13"]["x"], y=conf["Graphic"]["right_one_13"]["y"], clicks=conf["Graphic"]["right_one_13"]["clicks"],button=conf["Graphic"]["right_one_13"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_15"]["x"], y=conf["Graphic"]["right_one_15"]["y"], clicks=conf["Graphic"]["right_one_15"]["clicks"],button=conf["Graphic"]["right_one_15"]["button"], duration=0.2)
        auto.press("2")
        auto.click(x=conf["Graphic"]["right_one_18"]["x"], y=conf["Graphic"]["right_one_18"]["y"], clicks=conf["Graphic"]["right_one_18"]["clicks"],button=conf["Graphic"]["right_one_18"]["button"], duration=0.2)
        auto.press("9")
        auto.click(x=conf["Graphic"]["right_one_21"]["x"], y=conf["Graphic"]["right_one_21"]["y"], clicks=conf["Graphic"]["right_one_21"]["clicks"],button=conf["Graphic"]["right_one_21"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_23"]["x"], y=conf["Graphic"]["right_one_23"]["y"], clicks=conf["Graphic"]["right_one_23"]["clicks"],button=conf["Graphic"]["right_one_23"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_25"]["x"], y=conf["Graphic"]["right_one_25"]["y"], clicks=conf["Graphic"]["right_one_25"]["clicks"],button=conf["Graphic"]["right_one_25"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["right_one_27"]["x"], y=conf["Graphic"]["right_one_27"]["y"],button=conf["Graphic"]["right_one_27"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["right_one_28taiqi"]["x"], y=conf["Graphic"]["right_one_28taiqi"]["y"],button=conf["Graphic"]["right_one_28taiqi"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_29"]["x"], y=conf["Graphic"]["right_one_29"]["y"], clicks=conf["Graphic"]["right_one_29"]["clicks"],button=conf["Graphic"]["right_one_29"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_31"]["x"], y=conf["Graphic"]["right_one_31"]["y"], clicks=conf["Graphic"]["right_one_31"]["clicks"],button=conf["Graphic"]["right_one_31"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_33"]["x"], y=conf["Graphic"]["right_one_33"]["y"], clicks=conf["Graphic"]["right_one_33"]["clicks"],button=conf["Graphic"]["right_one_33"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_35"]["x"], y=conf["Graphic"]["right_one_35"]["y"], clicks=conf["Graphic"]["right_one_35"]["clicks"],button=conf["Graphic"]["right_one_35"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_37"]["x"], y=conf["Graphic"]["right_one_37"]["y"], clicks=conf["Graphic"]["right_one_37"]["clicks"],button=conf["Graphic"]["right_one_37"]["button"], duration=0.2)
        time.sleep(2)
        style = '图案右键复制粘贴'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_one_40"]["x"], y=conf["Graphic"]["right_one_40"]["y"], clicks=conf["Graphic"]["right_one_40"]["clicks"],button=conf["Graphic"]["right_one_40"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_42"]["x"], y=conf["Graphic"]["right_one_42"]["y"], clicks=conf["Graphic"]["right_one_42"]["clicks"],button=conf["Graphic"]["right_one_42"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_44"]["x"], y=conf["Graphic"]["right_one_44"]["y"], clicks=conf["Graphic"]["right_one_44"]["clicks"],button=conf["Graphic"]["right_one_44"]["button"], duration=0.2)
        time.sleep(2)
        style = '图案镜像粘贴'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_one_47"]["x"], y=conf["Graphic"]["right_one_47"]["y"], clicks=conf["Graphic"]["right_one_47"]["clicks"],button=conf["Graphic"]["right_one_47"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_49"]["x"], y=conf["Graphic"]["right_one_49"]["y"], clicks=conf["Graphic"]["right_one_49"]["clicks"],button=conf["Graphic"]["right_one_49"]["button"], duration=0.2)
        time.sleep(2)
        style = '复制到对称版片'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_one_52"]["x"], y=conf["Graphic"]["right_one_52"]["y"], clicks=conf["Graphic"]["right_one_52"]["clicks"],button=conf["Graphic"]["right_one_52"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_54"]["x"], y=conf["Graphic"]["right_one_54"]["y"], clicks=conf["Graphic"]["right_one_54"]["clicks"],button=conf["Graphic"]["right_one_54"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_56"]["x"], y=conf["Graphic"]["right_one_56"]["y"], clicks=conf["Graphic"]["right_one_56"]["clicks"],button=conf["Graphic"]["right_one_56"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_60"]["x"], y=conf["Graphic"]["right_one_60"]["y"], clicks=conf["Graphic"]["right_one_60"]["clicks"],button=conf["Graphic"]["right_one_60"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_62"]["x"], y=conf["Graphic"]["right_one_62"]["y"], clicks=conf["Graphic"]["right_one_62"]["clicks"],button=conf["Graphic"]["right_one_62"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_one_64"]["x"], y=conf["Graphic"]["right_one_64"]["y"], clicks=conf["Graphic"]["right_one_64"]["clicks"],button=conf["Graphic"]["right_one_64"]["button"], duration=0.2)
        time.sleep(2)
        style = '重复X,Y轴'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('2D右键旋转，水平翻转，垂直翻转')
    def test_right_two(self):
        auto.click(x=conf["Graphic"]["right_two_1"]["x"], y=conf["Graphic"]["right_two_1"]["y"], clicks=conf["Graphic"]["right_two_1"]["clicks"],button=conf["Graphic"]["right_two_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["right_two_4"]["x"], y=conf["Graphic"]["right_two_4"]["y"], clicks=conf["Graphic"]["right_two_4"]["clicks"],button=conf["Graphic"]["right_two_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_6"]["x"], y=conf["Graphic"]["right_two_6"]["y"], clicks=conf["Graphic"]["right_two_6"]["clicks"],button=conf["Graphic"]["right_two_6"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["right_two_9"]["x"], y=conf["Graphic"]["right_two_9"]["y"], clicks=conf["Graphic"]["right_two_9"]["clicks"],button=conf["Graphic"]["right_two_9"]["button"], duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["right_two_13"]["x"], y=conf["Graphic"]["right_two_13"]["y"], clicks=conf["Graphic"]["right_two_13"]["clicks"],button=conf["Graphic"]["right_two_13"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_15"]["x"], y=conf["Graphic"]["right_two_15"]["y"], clicks=conf["Graphic"]["right_two_15"]["clicks"],button=conf["Graphic"]["right_two_15"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_17"]["x"], y=conf["Graphic"]["right_two_17"]["y"], clicks=conf["Graphic"]["right_two_17"]["clicks"],button=conf["Graphic"]["right_two_17"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_19"]["x"], y=conf["Graphic"]["right_two_19"]["y"], clicks=conf["Graphic"]["right_two_19"]["clicks"],button=conf["Graphic"]["right_two_19"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["right_two_21"]["x"], y=conf["Graphic"]["right_two_21"]["y"],button=conf["Graphic"]["right_two_21"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["right_two_22taiqi"]["x"], y=conf["Graphic"]["right_two_22taiqi"]["y"],button=conf["Graphic"]["right_two_22taiqi"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_23"]["x"], y=conf["Graphic"]["right_two_23"]["y"], clicks=conf["Graphic"]["right_two_23"]["clicks"],button=conf["Graphic"]["right_two_23"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_25"]["x"], y=conf["Graphic"]["right_two_25"]["y"], clicks=conf["Graphic"]["right_two_25"]["clicks"],button=conf["Graphic"]["right_two_25"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_27"]["x"], y=conf["Graphic"]["right_two_27"]["y"], clicks=conf["Graphic"]["right_two_27"]["clicks"],button=conf["Graphic"]["right_two_27"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_28taiqi"]["x"], y=conf["Graphic"]["right_two_28taiqi"]["y"], clicks=conf["Graphic"]["right_two_28taiqi"]["clicks"],button=conf["Graphic"]["right_two_28taiqi"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_29"]["x"], y=conf["Graphic"]["right_two_29"]["y"], clicks=conf["Graphic"]["right_two_29"]["clicks"],button=conf["Graphic"]["right_two_29"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D逆时针旋转90度'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_two_32"]["x"], y=conf["Graphic"]["right_two_32"]["y"], clicks=conf["Graphic"]["right_two_32"]["clicks"],button=conf["Graphic"]["right_two_32"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_34"]["x"], y=conf["Graphic"]["right_two_34"]["y"], clicks=conf["Graphic"]["right_two_34"]["clicks"],button=conf["Graphic"]["right_two_34"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D水平翻转'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_two_37"]["x"], y=conf["Graphic"]["right_two_37"]["y"], clicks=conf["Graphic"]["right_two_37"]["clicks"],button=conf["Graphic"]["right_two_37"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_two_39"]["x"], y=conf["Graphic"]["right_two_39"]["y"], clicks=conf["Graphic"]["right_two_39"]["clicks"],button=conf["Graphic"]["right_two_39"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D垂直翻转'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('2D对焦，勾勒')
    def test_right_three(self):
        auto.click(x=conf["Graphic"]["right_three_1"]["x"], y=conf["Graphic"]["right_three_1"]["y"], clicks=conf["Graphic"]["right_three_1"]["clicks"],button=conf["Graphic"]["right_three_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["right_three_4"]["x"], y=conf["Graphic"]["right_three_4"]["y"], clicks=conf["Graphic"]["right_three_4"]["clicks"],button=conf["Graphic"]["right_three_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_6"]["x"], y=conf["Graphic"]["right_three_6"]["y"], clicks=conf["Graphic"]["right_three_6"]["clicks"],button=conf["Graphic"]["right_three_6"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_8"]["x"], y=conf["Graphic"]["right_three_8"]["y"], clicks=conf["Graphic"]["right_three_8"]["clicks"],button=conf["Graphic"]["right_three_8"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_10"]["x"], y=conf["Graphic"]["right_three_10"]["y"], clicks=conf["Graphic"]["right_three_10"]["clicks"],button=conf["Graphic"]["right_three_10"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_12"]["x"], y=conf["Graphic"]["right_three_12"]["y"], clicks=conf["Graphic"]["right_three_12"]["clicks"],button=conf["Graphic"]["right_three_12"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_14"]["x"], y=conf["Graphic"]["right_three_14"]["y"], clicks=conf["Graphic"]["right_three_14"]["clicks"],button=conf["Graphic"]["right_three_14"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_16"]["x"], y=conf["Graphic"]["right_three_16"]["y"], clicks=conf["Graphic"]["right_three_16"]["clicks"],button=conf["Graphic"]["right_three_16"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_18"]["x"], y=conf["Graphic"]["right_three_18"]["y"], clicks=conf["Graphic"]["right_three_18"]["clicks"],button=conf["Graphic"]["right_three_18"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D对焦至选定的'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_three_20"]["x"], y=conf["Graphic"]["right_three_20"]["y"], clicks=conf["Graphic"]["right_three_20"]["clicks"],button=conf["Graphic"]["right_three_20"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_three_22"]["x"], y=conf["Graphic"]["right_three_22"]["y"], clicks=conf["Graphic"]["right_three_22"]["clicks"],button=conf["Graphic"]["right_three_22"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["right_three_24"]["x"], y=conf["Graphic"]["right_three_24"]["y"],button=conf["Graphic"]["right_three_24"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["right_three_25up"]["x"], y=conf["Graphic"]["right_three_25up"]["y"],button=conf["Graphic"]["right_three_25up"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D勾勒内部图形'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('2D图案顺序，添加组，解除组')
    def test_right_four(self):
        auto.click(x=conf["Graphic"]["right_four_1"]["x"], y=conf["Graphic"]["right_four_1"]["y"], clicks=conf["Graphic"]["right_four_1"]["clicks"],button=conf["Graphic"]["right_four_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["right_four_4"]["x"], y=conf["Graphic"]["right_four_4"]["y"], clicks=conf["Graphic"]["right_four_4"]["clicks"],button=conf["Graphic"]["right_four_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_6"]["x"], y=conf["Graphic"]["right_four_6"]["y"], clicks=conf["Graphic"]["right_four_6"]["clicks"],button=conf["Graphic"]["right_four_6"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_8"]["x"], y=conf["Graphic"]["right_four_8"]["y"], clicks=conf["Graphic"]["right_four_8"]["clicks"],button=conf["Graphic"]["right_four_8"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["right_four_11"]["x"], y=conf["Graphic"]["right_four_11"]["y"], clicks=conf["Graphic"]["right_four_11"]["clicks"],button=conf["Graphic"]["right_four_11"]["button"], duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["right_four_15"]["x"], y=conf["Graphic"]["right_four_15"]["y"], clicks=conf["Graphic"]["right_four_15"]["clicks"],button=conf["Graphic"]["right_four_15"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_17"]["x"], y=conf["Graphic"]["right_four_17"]["y"], clicks=conf["Graphic"]["right_four_17"]["clicks"],button=conf["Graphic"]["right_four_17"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["right_four_19"]["x"], y=conf["Graphic"]["right_four_19"]["y"],button=conf["Graphic"]["right_four_19"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["right_four_20taiqi"]["x"], y=conf["Graphic"]["right_four_20taiqi"]["y"],button=conf["Graphic"]["right_four_20taiqi"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_21"]["x"], y=conf["Graphic"]["right_four_21"]["y"], clicks=conf["Graphic"]["right_four_21"]["clicks"],button=conf["Graphic"]["right_four_21"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_23"]["x"], y=conf["Graphic"]["right_four_23"]["y"], clicks=conf["Graphic"]["right_four_23"]["clicks"],button=conf["Graphic"]["right_four_23"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_25"]["x"], y=conf["Graphic"]["right_four_25"]["y"], clicks=conf["Graphic"]["right_four_25"]["clicks"],button=conf["Graphic"]["right_four_25"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_27"]["x"], y=conf["Graphic"]["right_four_27"]["y"], clicks=conf["Graphic"]["right_four_27"]["clicks"],button=conf["Graphic"]["right_four_27"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_29"]["x"], y=conf["Graphic"]["right_four_29"]["y"], clicks=conf["Graphic"]["right_four_29"]["clicks"],button=conf["Graphic"]["right_four_29"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_31"]["x"], y=conf["Graphic"]["right_four_31"]["y"], clicks=conf["Graphic"]["right_four_31"]["clicks"],button=conf["Graphic"]["right_four_31"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_33"]["x"], y=conf["Graphic"]["right_four_33"]["y"], clicks=conf["Graphic"]["right_four_33"]["clicks"],button=conf["Graphic"]["right_four_33"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_35"]["x"], y=conf["Graphic"]["right_four_35"]["y"], clicks=conf["Graphic"]["right_four_35"]["clicks"],button=conf["Graphic"]["right_four_35"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_36taiqi"]["x"], y=conf["Graphic"]["right_four_36taiqi"]["y"], clicks=conf["Graphic"]["right_four_36taiqi"]["clicks"],button=conf["Graphic"]["right_four_36taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D顺序，图案移动到最后'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.mouseDown(x=conf["Graphic"]["right_four_38"]["x"], y=conf["Graphic"]["right_four_38"]["y"],button=conf["Graphic"]["right_four_38"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["right_four_39taiqi"]["x"], y=conf["Graphic"]["right_four_39taiqi"]["y"],button=conf["Graphic"]["right_four_39taiqi"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_40"]["x"], y=conf["Graphic"]["right_four_40"]["y"], clicks=conf["Graphic"]["right_four_40"]["clicks"],button=conf["Graphic"]["right_four_40"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["right_four_42"]["x"], y=conf["Graphic"]["right_four_42"]["y"], clicks=conf["Graphic"]["right_four_42"]["clicks"],button=conf["Graphic"]["right_four_42"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Graphic"]["right_four_44"]["x"], y=conf["Graphic"]["right_four_44"]["y"], clicks=conf["Graphic"]["right_four_44"]["clicks"],button=conf["Graphic"]["right_four_44"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D图案添加组'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["Graphic"]["right_four_45"]["x"], y=conf["Graphic"]["right_four_45"]["y"], clicks=conf["Graphic"]["right_four_45"]["clicks"],button=conf["Graphic"]["right_four_45"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Graphic"]["right_four_46"]["x"], y=conf["Graphic"]["right_four_46"]["y"], clicks=conf["Graphic"]["right_four_46"]["clicks"],button=conf["Graphic"]["right_four_46"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Graphic"]["right_four_47"]["x"], y=conf["Graphic"]["right_four_47"]["y"], clicks=conf["Graphic"]["right_four_47"]["clicks"],button=conf["Graphic"]["right_four_47"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D图案解除组'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

