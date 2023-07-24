# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('图案选择')
@allure.severity(allure.severity_level.CRITICAL)
class TestChoose:

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

    @allure.story('2D, 3D拖拽，旋转图案')
    def test_choose_one(self):
        auto.click(x=conf["Graphic"]["choose_one_1"]["x"], y=conf["Graphic"]["choose_one_1"]["y"], clicks=conf["Graphic"]["choose_one_1"]["clicks"],button=conf["Graphic"]["choose_one_1"]["button"], duration=0.2)

        auto.press("s")
        auto.click(x=conf["Graphic"]["choose_one_5"]["x"], y=conf["Graphic"]["choose_one_5"]["y"], clicks=conf["Graphic"]["choose_one_5"]["clicks"],button=conf["Graphic"]["choose_one_5"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_7"]["x"], y=conf["Graphic"]["choose_one_7"]["y"], clicks=conf["Graphic"]["choose_one_7"]["clicks"],button=conf["Graphic"]["choose_one_7"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["choose_one_10"]["x"], y=conf["Graphic"]["choose_one_10"]["y"], clicks=conf["Graphic"]["choose_one_10"]["clicks"],button=conf["Graphic"]["choose_one_10"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_12"]["x"], y=conf["Graphic"]["choose_one_12"]["y"], clicks=conf["Graphic"]["choose_one_12"]["clicks"],button=conf["Graphic"]["choose_one_12"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_14"]["x"], y=conf["Graphic"]["choose_one_14"]["y"], clicks=conf["Graphic"]["choose_one_14"]["clicks"],button=conf["Graphic"]["choose_one_14"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_16"]["x"], y=conf["Graphic"]["choose_one_16"]["y"], clicks=conf["Graphic"]["choose_one_16"]["clicks"],button=conf["Graphic"]["choose_one_16"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_18"]["x"], y=conf["Graphic"]["choose_one_18"]["y"], clicks=conf["Graphic"]["choose_one_18"]["clicks"],button=conf["Graphic"]["choose_one_18"]["button"], duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["choose_one_22"]["x"], y=conf["Graphic"]["choose_one_22"]["y"], clicks=conf["Graphic"]["choose_one_22"]["clicks"],button=conf["Graphic"]["choose_one_22"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_24"]["x"], y=conf["Graphic"]["choose_one_24"]["y"], clicks=conf["Graphic"]["choose_one_24"]["clicks"],button=conf["Graphic"]["choose_one_24"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_26"]["x"], y=conf["Graphic"]["choose_one_26"]["y"], clicks=conf["Graphic"]["choose_one_26"]["clicks"],button=conf["Graphic"]["choose_one_26"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_28"]["x"], y=conf["Graphic"]["choose_one_28"]["y"], clicks=conf["Graphic"]["choose_one_28"]["clicks"],button=conf["Graphic"]["choose_one_28"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_30"]["x"], y=conf["Graphic"]["choose_one_30"]["y"], clicks=conf["Graphic"]["choose_one_30"]["clicks"],button=conf["Graphic"]["choose_one_30"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_32"]["x"], y=conf["Graphic"]["choose_one_32"]["y"], clicks=conf["Graphic"]["choose_one_32"]["clicks"],button=conf["Graphic"]["choose_one_32"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_34"]["x"], y=conf["Graphic"]["choose_one_34"]["y"], clicks=conf["Graphic"]["choose_one_34"]["clicks"],button=conf["Graphic"]["choose_one_34"]["button"], duration=0.2)
        time.sleep(0.5)
        auto.click(x=conf["Graphic"]["choose_one_36"]["x"], y=conf["Graphic"]["choose_one_36"]["y"], clicks=conf["Graphic"]["choose_one_36"]["clicks"],button=conf["Graphic"]["choose_one_36"]["button"], duration=0.2)
        time.sleep(0.5)
        auto.click(x=conf["Graphic"]["choose_one_38"]["x"], y=conf["Graphic"]["choose_one_38"]["y"], clicks=conf["Graphic"]["choose_one_38"]["clicks"],button=conf["Graphic"]["choose_one_38"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_40"]["x"], y=conf["Graphic"]["choose_one_40"]["y"], clicks=conf["Graphic"]["choose_one_40"]["clicks"],button=conf["Graphic"]["choose_one_40"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_66"]["x"], y=conf["Graphic"]["choose_one_66"]["y"], clicks=conf["Graphic"]["choose_one_66"]["clicks"],button=conf["Graphic"]["choose_one_66"]["button"], duration=0.2)
        time.sleep(0.5)
        auto.click(x=conf["Graphic"]["choose_one_67"]["x"], y=conf["Graphic"]["choose_one_67"]["y"], clicks=conf["Graphic"]["choose_one_67"]["clicks"],button=conf["Graphic"]["choose_one_67"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_one_68"]["x"], y=conf["Graphic"]["choose_one_68"]["y"], clicks=conf["Graphic"]["choose_one_68"]["clicks"],button=conf["Graphic"]["choose_one_68"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_44"]["x"], y=conf["Graphic"]["choose_one_44"]["y"],button=conf["Graphic"]["choose_one_44"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_45taiqi"]["x"], y=conf["Graphic"]["choose_one_45taiqi"]["y"],button=conf["Graphic"]["choose_one_45taiqi"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_46"]["x"], y=conf["Graphic"]["choose_one_46"]["y"],button=conf["Graphic"]["choose_one_46"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_47taiqi"]["x"], y=conf["Graphic"]["choose_one_47taiqi"]["y"],button=conf["Graphic"]["choose_one_47taiqi"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_48"]["x"], y=conf["Graphic"]["choose_one_48"]["y"],button=conf["Graphic"]["choose_one_48"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_49taiqi"]["x"], y=conf["Graphic"]["choose_one_49taiqi"]["y"],button=conf["Graphic"]["choose_one_49taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '2D拖拽，旋转图案'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)
        auto.click(x=conf["Graphic"]["choose_one_66"]["x"], y=conf["Graphic"]["choose_one_66"]["y"], clicks=conf["Graphic"]["choose_one_66"]["clicks"],button=conf["Graphic"]["choose_one_66"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_50"]["x"], y=conf["Graphic"]["choose_one_50"]["y"],button=conf["Graphic"]["choose_one_50"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_51taiqi"]["x"], y=conf["Graphic"]["choose_one_51taiqi"]["y"],button=conf["Graphic"]["choose_one_51taiqi"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_52"]["x"], y=conf["Graphic"]["choose_one_52"]["y"],button=conf["Graphic"]["choose_one_52"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_53taiqi"]["x"], y=conf["Graphic"]["choose_one_53taiqi"]["y"],button=conf["Graphic"]["choose_one_53taiqi"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_one_54"]["x"], y=conf["Graphic"]["choose_one_54"]["y"],button=conf["Graphic"]["choose_one_54"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_one_55taiqi"]["x"], y=conf["Graphic"]["choose_one_55taiqi"]["y"],button=conf["Graphic"]["choose_one_55taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '3D拖拽，旋转图案'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('2D, 3D拖拽，图案到版片外')
    def test_choose_two(self):
        auto.click(x=conf["Graphic"]["choose_two_1"]["x"], y=conf["Graphic"]["choose_two_1"]["y"], clicks=conf["Graphic"]["choose_two_1"]["clicks"],button=conf["Graphic"]["choose_two_1"]["button"], duration=0.2)
        auto.press("q")
        auto.press("s")
        auto.click(x=conf["Graphic"]["choose_two_5"]["x"], y=conf["Graphic"]["choose_two_5"]["y"], clicks=conf["Graphic"]["choose_two_5"]["clicks"],button=conf["Graphic"]["choose_two_5"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_two_7"]["x"], y=conf["Graphic"]["choose_two_7"]["y"], clicks=conf["Graphic"]["choose_two_7"]["clicks"],button=conf["Graphic"]["choose_two_7"]["button"], duration=0.2)
        auto.press("2")
        auto.press("q")
        auto.click(x=conf["Graphic"]["choose_two_11"]["x"], y=conf["Graphic"]["choose_two_11"]["y"], clicks=conf["Graphic"]["choose_two_11"]["clicks"],button=conf["Graphic"]["choose_two_11"]["button"], duration=0.2)
        auto.press("9")
        auto.click(x=conf["Graphic"]["choose_two_14"]["x"], y=conf["Graphic"]["choose_two_14"]["y"], clicks=conf["Graphic"]["choose_two_14"]["clicks"],button=conf["Graphic"]["choose_two_14"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_two_16"]["x"], y=conf["Graphic"]["choose_two_16"]["y"], clicks=conf["Graphic"]["choose_two_16"]["clicks"],button=conf["Graphic"]["choose_two_16"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_two_18"]["x"], y=conf["Graphic"]["choose_two_18"]["y"], clicks=conf["Graphic"]["choose_two_18"]["clicks"],button=conf["Graphic"]["choose_two_18"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_two_20"]["x"], y=conf["Graphic"]["choose_two_20"]["y"], clicks=conf["Graphic"]["choose_two_20"]["clicks"],button=conf["Graphic"]["choose_two_20"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["choose_two_22"]["x"], y=conf["Graphic"]["choose_two_22"]["y"], clicks=conf["Graphic"]["choose_two_22"]["clicks"],button=conf["Graphic"]["choose_two_22"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["choose_two_24"]["x"], y=conf["Graphic"]["choose_two_24"]["y"],button=conf["Graphic"]["choose_two_24"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_two_25taiqi"]["x"], y=conf["Graphic"]["choose_two_25taiqi"]["y"],button=conf["Graphic"]["choose_two_25taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '拖拽2D图案出版片'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.mouseDown(x=conf["Graphic"]["choose_two_26"]["x"], y=conf["Graphic"]["choose_two_26"]["y"],button=conf["Graphic"]["choose_two_26"]["button"], duration=0.2)
        auto.moveTo(x=conf["Graphic"]["choose_two_27taiqi"]["x"], y=conf["Graphic"]["choose_two_27taiqi"]["y"], tween=auto.linear, duration=1)
        auto.mouseUp(x=conf["Graphic"]["choose_two_27taiqi"]["x"], y=conf["Graphic"]["choose_two_27taiqi"]["y"],button=conf["Graphic"]["choose_two_27taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '拖拽3D图案无法出版片'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.mouseDown(x=conf["Graphic"]["choose_two_28"]["x"], y=conf["Graphic"]["choose_two_28"]["y"],button=conf["Graphic"]["choose_two_28"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["choose_two_29taiqi"]["x"], y=conf["Graphic"]["choose_two_29taiqi"]["y"],button=conf["Graphic"]["choose_two_29taiqi"]["button"], duration=0.2)
        time.sleep(2)
        style = '拖拽2D回版片'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)



