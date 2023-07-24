# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('图案增加')
@allure.severity(allure.severity_level.CRITICAL)
class TestAdd:

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

    @allure.story('版片上2D新增的图案，拖拽图案')
    def test_add_one(self):
        auto.click(x=conf["Graphic"]["add_one_1"]["x"], y=conf["Graphic"]["add_one_1"]["y"], clicks=conf["Graphic"]["add_one_1"]["clicks"],button=conf["Graphic"]["add_one_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_one_4"]["x"], y=conf["Graphic"]["add_one_4"]["y"], clicks=conf["Graphic"]["add_one_4"]["clicks"],button=conf["Graphic"]["add_one_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_6"]["x"], y=conf["Graphic"]["add_one_6"]["y"], clicks=conf["Graphic"]["add_one_6"]["clicks"],button=conf["Graphic"]["add_one_6"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_8"]["x"], y=conf["Graphic"]["add_one_8"]["y"], clicks=conf["Graphic"]["add_one_8"]["clicks"],button=conf["Graphic"]["add_one_8"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_10"]["x"], y=conf["Graphic"]["add_one_10"]["y"], clicks=conf["Graphic"]["add_one_10"]["clicks"],button=conf["Graphic"]["add_one_10"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_12"]["x"], y=conf["Graphic"]["add_one_12"]["y"], clicks=conf["Graphic"]["add_one_12"]["clicks"],button=conf["Graphic"]["add_one_12"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_14"]["x"], y=conf["Graphic"]["add_one_14"]["y"], clicks=conf["Graphic"]["add_one_14"]["clicks"],button=conf["Graphic"]["add_one_14"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_one_16"]["x"], y=conf["Graphic"]["add_one_16"]["y"], clicks=conf["Graphic"]["add_one_16"]["clicks"],button=conf["Graphic"]["add_one_16"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.click(x=conf["Graphic"]["add_one_26"]["x"], y=conf["Graphic"]["add_one_26"]["y"], clicks=conf["Graphic"]["add_one_26"]["clicks"],button=conf["Graphic"]["add_one_26"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["add_one_28"]["x"], y=conf["Graphic"]["add_one_28"]["y"],button=conf["Graphic"]["add_one_28"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_one_29taiqi"]["x"], y=conf["Graphic"]["add_one_29taiqi"]["y"],button=conf["Graphic"]["add_one_29taiqi"]["button"], duration=0.2)
        time.sleep(1)
        style = '版片上2D新增的图案，拖拽图案'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('在版片外新增图案，无法增加')
    def test_add_two(self):
        auto.click(x=conf["Graphic"]["add_two_1"]["x"], y=conf["Graphic"]["add_two_1"]["y"],clicks=conf["Graphic"]["add_two_1"]["clicks"], button=conf["Graphic"]["add_two_1"]["button"],duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_two_4"]["x"], y=conf["Graphic"]["add_two_4"]["y"],clicks=conf["Graphic"]["add_two_4"]["clicks"], button=conf["Graphic"]["add_two_4"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_two_6"]["x"], y=conf["Graphic"]["add_two_6"]["y"],clicks=conf["Graphic"]["add_two_6"]["clicks"], button=conf["Graphic"]["add_two_6"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_two_8"]["x"], y=conf["Graphic"]["add_two_8"]["y"],clicks=conf["Graphic"]["add_two_8"]["clicks"], button=conf["Graphic"]["add_two_8"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_two_10"]["x"], y=conf["Graphic"]["add_two_10"]["y"],clicks=conf["Graphic"]["add_two_10"]["clicks"], button=conf["Graphic"]["add_two_10"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_two_12"]["x"], y=conf["Graphic"]["add_two_12"]["y"],clicks=conf["Graphic"]["add_two_12"]["clicks"], button=conf["Graphic"]["add_two_12"]["button"],duration=0.2)
        time.sleep(1)
        style = '在版片外新增图案，无法增加'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('版片上3D新增的图案，拖拽图案')
    def test_add_three(self):
        auto.click(x=conf["Graphic"]["add_three_1"]["x"], y=conf["Graphic"]["add_three_1"]["y"],clicks=conf["Graphic"]["add_three_1"]["clicks"], button=conf["Graphic"]["add_three_1"]["button"],duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_three_4"]["x"], y=conf["Graphic"]["add_three_4"]["y"],clicks=conf["Graphic"]["add_three_4"]["clicks"], button=conf["Graphic"]["add_three_4"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_three_6"]["x"], y=conf["Graphic"]["add_three_6"]["y"],clicks=conf["Graphic"]["add_three_6"]["clicks"], button=conf["Graphic"]["add_three_6"]["button"],duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["add_three_9"]["x"], y=conf["Graphic"]["add_three_9"]["y"],clicks=conf["Graphic"]["add_three_9"]["clicks"], button=conf["Graphic"]["add_three_9"]["button"],duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["add_three_13"]["x"], y=conf["Graphic"]["add_three_13"]["y"],clicks=conf["Graphic"]["add_three_13"]["clicks"], button=conf["Graphic"]["add_three_13"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_three_15"]["x"], y=conf["Graphic"]["add_three_15"]["y"],clicks=conf["Graphic"]["add_three_15"]["clicks"], button=conf["Graphic"]["add_three_15"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_three_17"]["x"], y=conf["Graphic"]["add_three_17"]["y"],clicks=conf["Graphic"]["add_three_17"]["clicks"], button=conf["Graphic"]["add_three_17"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_three_19"]["x"], y=conf["Graphic"]["add_three_19"]["y"],clicks=conf["Graphic"]["add_three_19"]["clicks"], button=conf["Graphic"]["add_three_19"]["button"],duration=0.2)
        auto.click(x=conf["Graphic"]["add_three_21"]["x"], y=conf["Graphic"]["add_three_21"]["y"],clicks=conf["Graphic"]["add_three_21"]["clicks"], button=conf["Graphic"]["add_three_21"]["button"],duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["add_three_23"]["x"], y=conf["Graphic"]["add_three_23"]["y"],button=conf["Graphic"]["add_three_23"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_three_24taiqi"]["x"], y=conf["Graphic"]["add_three_24taiqi"]["y"],button=conf["Graphic"]["add_three_24taiqi"]["button"], duration=0.2)
        time.sleep(1)
        style = '版片上3D新增的图案，拖拽图案'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('在2D视窗右键弹框添加图案，修改图案个数')
    def test_add_four(self):
        auto.click(x=conf["Graphic"]["add_four_1"]["x"], y=conf["Graphic"]["add_four_1"]["y"], clicks=conf["Graphic"]["add_four_1"]["clicks"],button=conf["Graphic"]["add_four_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_four_4"]["x"], y=conf["Graphic"]["add_four_4"]["y"], clicks=conf["Graphic"]["add_four_4"]["clicks"],button=conf["Graphic"]["add_four_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_four_6"]["x"], y=conf["Graphic"]["add_four_6"]["y"], clicks=conf["Graphic"]["add_four_6"]["clicks"],button=conf["Graphic"]["add_four_6"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["add_four_9"]["x"], y=conf["Graphic"]["add_four_9"]["y"], clicks=conf["Graphic"]["add_four_9"]["clicks"],button=conf["Graphic"]["add_four_9"]["button"], duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["add_four_13"]["x"], y=conf["Graphic"]["add_four_13"]["y"], clicks=conf["Graphic"]["add_four_13"]["clicks"],button=conf["Graphic"]["add_four_13"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_four_15"]["x"], y=conf["Graphic"]["add_four_15"]["y"], clicks=conf["Graphic"]["add_four_15"]["clicks"],button=conf["Graphic"]["add_four_15"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_four_17"]["x"], y=conf["Graphic"]["add_four_17"]["y"], clicks=conf["Graphic"]["add_four_17"]["clicks"],button=conf["Graphic"]["add_four_17"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["add_four_19"]["x"], y=conf["Graphic"]["add_four_19"]["y"],button=conf["Graphic"]["add_four_19"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_four_20taiqi"]["x"], y=conf["Graphic"]["add_four_20taiqi"]["y"],button=conf["Graphic"]["add_four_20taiqi"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("80")
        auto.mouseDown(x=conf["Graphic"]["add_four_24"]["x"], y=conf["Graphic"]["add_four_24"]["y"],button=conf["Graphic"]["add_four_24"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_four_25taiqi"]["x"], y=conf["Graphic"]["add_four_25taiqi"]["y"],button=conf["Graphic"]["add_four_25taiqi"]["button"], duration=0.2)
        auto.typewrite("45")
        auto.mouseDown(x=conf["Graphic"]["add_four_28"]["x"], y=conf["Graphic"]["add_four_28"]["y"],button=conf["Graphic"]["add_four_28"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_four_29taiqi"]["x"], y=conf["Graphic"]["add_four_29taiqi"]["y"],button=conf["Graphic"]["add_four_29taiqi"]["button"], duration=0.2)
        auto.typewrite("15")
        auto.click(x=conf["Graphic"]["add_four_32"]["x"], y=conf["Graphic"]["add_four_32"]["y"], clicks=conf["Graphic"]["add_four_32"]["clicks"],button=conf["Graphic"]["add_four_32"]["button"], duration=0.2)
        time.sleep(1)
        style = '在2D视窗右键弹框添加图案，修改图案个数'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('在2D视窗右键弹框添加图案， 边距修改')
    def test_add_five(self):
        auto.click(x=conf["Graphic"]["add_five_1"]["x"], y=conf["Graphic"]["add_five_1"]["y"], clicks=conf["Graphic"]["add_five_1"]["clicks"],button=conf["Graphic"]["add_five_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_five_4"]["x"], y=conf["Graphic"]["add_five_4"]["y"], clicks=conf["Graphic"]["add_five_4"]["clicks"],button=conf["Graphic"]["add_five_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_five_6"]["x"], y=conf["Graphic"]["add_five_6"]["y"], clicks=conf["Graphic"]["add_five_6"]["clicks"],button=conf["Graphic"]["add_five_6"]["button"], duration=0.2)
        auto.press("q")
        auto.click(x=conf["Graphic"]["add_five_9"]["x"], y=conf["Graphic"]["add_five_9"]["y"], clicks=conf["Graphic"]["add_five_9"]["clicks"],button=conf["Graphic"]["add_five_9"]["button"], duration=0.2)
        auto.press("9")
        auto.press("2")
        auto.click(x=conf["Graphic"]["add_five_13"]["x"], y=conf["Graphic"]["add_five_13"]["y"], clicks=conf["Graphic"]["add_five_13"]["clicks"],button=conf["Graphic"]["add_five_13"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_five_15"]["x"], y=conf["Graphic"]["add_five_15"]["y"], clicks=conf["Graphic"]["add_five_15"]["clicks"],button=conf["Graphic"]["add_five_15"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_five_17"]["x"], y=conf["Graphic"]["add_five_17"]["y"], clicks=conf["Graphic"]["add_five_17"]["clicks"],button=conf["Graphic"]["add_five_17"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Graphic"]["add_five_19"]["x"], y=conf["Graphic"]["add_five_19"]["y"],button=conf["Graphic"]["add_five_19"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_five_20up"]["x"], y=conf["Graphic"]["add_five_20up"]["y"],button=conf["Graphic"]["add_five_20up"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("350")
        auto.mouseDown(x=conf["Graphic"]["add_five_28"]["x"], y=conf["Graphic"]["add_five_28"]["y"],button=conf["Graphic"]["add_five_28"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Graphic"]["add_five_29up"]["x"], y=conf["Graphic"]["add_five_29up"]["y"],button=conf["Graphic"]["add_five_29up"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("130")
        auto.click(x=conf["Graphic"]["add_five_34"]["x"], y=conf["Graphic"]["add_five_34"]["y"], clicks=conf["Graphic"]["add_five_34"]["clicks"],button=conf["Graphic"]["add_five_34"]["button"], duration=0.2)
        time.sleep(1)
        style = '在2D视窗右键弹框添加图案， 边距修改'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('场景管理双击切换到图案模式，可以添加成功')
    def test_add_six(self):
        auto.click(x=conf["Graphic"]["add_six_1"]["x"], y=conf["Graphic"]["add_six_1"]["y"], clicks=conf["Graphic"]["add_six_1"]["clicks"],button=conf["Graphic"]["add_six_1"]["button"], duration=0.2)
        auto.press("s")
        auto.click(x=conf["Graphic"]["add_six_4"]["x"], y=conf["Graphic"]["add_six_4"]["y"], clicks=conf["Graphic"]["add_six_4"]["clicks"],button=conf["Graphic"]["add_six_4"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_six_6"]["x"], y=conf["Graphic"]["add_six_6"]["y"], clicks=conf["Graphic"]["add_six_6"]["clicks"],button=conf["Graphic"]["add_six_6"]["button"], duration=0.2)
        auto.press("2")
        auto.click(x=conf["Graphic"]["add_six_8"]["x"], y=conf["Graphic"]["add_six_8"]["y"], clicks=conf["Graphic"]["add_six_8"]["clicks"],button=conf["Graphic"]["add_six_8"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_six_10"]["x"], y=conf["Graphic"]["add_six_10"]["y"], clicks=conf["Graphic"]["add_six_10"]["clicks"],button=conf["Graphic"]["add_six_10"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_six_12"]["x"], y=conf["Graphic"]["add_six_12"]["y"], clicks=conf["Graphic"]["add_six_12"]["clicks"],button=conf["Graphic"]["add_six_12"]["button"], duration=0.2)
        auto.click(x=conf["Graphic"]["add_six_14"]["x"], y=conf["Graphic"]["add_six_14"]["y"], clicks=conf["Graphic"]["add_six_14"]["clicks"],button=conf["Graphic"]["add_six_14"]["button"], duration=0.2)
        time.sleep(3)
        style = '场景管理双击切换到图案模式，可以添加成功'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)