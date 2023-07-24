# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('图案属性栏编辑')
@allure.severity(allure.severity_level.CRITICAL)
class TestChange:

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

    @allure.story('属性栏角度，网格面修改')
    def test_change_one(self):
        auto.click(x=conf["Graphic"]["change_one_1"]["x"], y=conf["Graphic"]["change_one_1"]["y"], clicks=conf["Graphic"]["change_one_1"]["clicks"],button=conf["Graphic"]["change_one_1"]["button"], duration=0.3)
        auto.press("s")
        auto.click(x=conf["Graphic"]["change_one_4"]["x"], y=conf["Graphic"]["change_one_4"]["y"], clicks=conf["Graphic"]["change_one_4"]["clicks"],button=conf["Graphic"]["change_one_4"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one_6"]["x"], y=conf["Graphic"]["change_one_6"]["y"], clicks=conf["Graphic"]["change_one_6"]["clicks"],button=conf["Graphic"]["change_one_6"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one_8"]["x"], y=conf["Graphic"]["change_one_8"]["y"], clicks=conf["Graphic"]["change_one_8"]["clicks"],button=conf["Graphic"]["change_one_8"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one_10"]["x"], y=conf["Graphic"]["change_one_10"]["y"], clicks=conf["Graphic"]["change_one_10"]["clicks"],button=conf["Graphic"]["change_one_10"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one_12"]["x"], y=conf["Graphic"]["change_one_12"]["y"], clicks=conf["Graphic"]["change_one_12"]["clicks"],button=conf["Graphic"]["change_one_12"]["button"], duration=0.3)
        auto.press("2")
        auto.click(x=conf["Graphic"]["change_one_15"]["x"], y=conf["Graphic"]["change_one_15"]["y"], clicks=conf["Graphic"]["change_one_15"]["clicks"],button=conf["Graphic"]["change_one_15"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one_17"]["x"], y=conf["Graphic"]["change_one_17"]["y"], clicks=conf["Graphic"]["change_one_17"]["clicks"],button=conf["Graphic"]["change_one_17"]["button"], duration=0.3)
        auto.typewrite("50")
        auto.press('enter')
        auto.click(x=conf["Graphic"]["change_one1_1"]["x"], y=conf["Graphic"]["change_one1_1"]["y"], clicks=conf["Graphic"]["change_one1_1"]["clicks"],button=conf["Graphic"]["change_one1_1"]["button"], duration=0.3)
        auto.press("8")
        auto.click(x=conf["Graphic"]["change_one1_4"]["x"], y=conf["Graphic"]["change_one1_4"]["y"], clicks=conf["Graphic"]["change_one1_4"]["clicks"],button=conf["Graphic"]["change_one1_4"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_6"]["x"], y=conf["Graphic"]["change_one1_6"]["y"], clicks=conf["Graphic"]["change_one1_6"]["clicks"],button=conf["Graphic"]["change_one1_6"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_8"]["x"], y=conf["Graphic"]["change_one1_8"]["y"], clicks=conf["Graphic"]["change_one1_8"]["clicks"],button=conf["Graphic"]["change_one1_8"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_10"]["x"], y=conf["Graphic"]["change_one1_10"]["y"], clicks=conf["Graphic"]["change_one1_10"]["clicks"],button=conf["Graphic"]["change_one1_10"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_12"]["x"], y=conf["Graphic"]["change_one1_12"]["y"], clicks=conf["Graphic"]["change_one1_12"]["clicks"],button=conf["Graphic"]["change_one1_12"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_14"]["x"], y=conf["Graphic"]["change_one1_14"]["y"], clicks=conf["Graphic"]["change_one1_14"]["clicks"],button=conf["Graphic"]["change_one1_14"]["button"], duration=0.3)
        auto.typewrite("30")
        auto.press("enter")
        auto.click(x=conf["Graphic"]["change_one1_19"]["x"], y=conf["Graphic"]["change_one1_19"]["y"], clicks=conf["Graphic"]["change_one1_19"]["clicks"],button=conf["Graphic"]["change_one1_19"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_one1_21"]["x"], y=conf["Graphic"]["change_one1_21"]["y"], clicks=conf["Graphic"]["change_one1_21"]["clicks"],button=conf["Graphic"]["change_one1_21"]["button"], duration=0.3)
        time.sleep(1)
        style = '属性栏角度，网格面修改'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

    @allure.story('图案大小修改，图案工艺效果修改')
    def test_change_two(self):
        auto.click(x=conf["Graphic"]["change_two_1"]["x"], y=conf["Graphic"]["change_two_1"]["y"], clicks=conf["Graphic"]["change_two_1"]["clicks"],button=conf["Graphic"]["change_two_1"]["button"], duration=0.3)
        auto.press("s")
        auto.click(x=conf["Graphic"]["change_two_4"]["x"], y=conf["Graphic"]["change_two_4"]["y"], clicks=conf["Graphic"]["change_two_4"]["clicks"],button=conf["Graphic"]["change_two_4"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_6"]["x"], y=conf["Graphic"]["change_two_6"]["y"], clicks=conf["Graphic"]["change_two_6"]["clicks"],button=conf["Graphic"]["change_two_6"]["button"], duration=0.3)
        auto.press("2")
        auto.press("q")
        auto.click(x=conf["Graphic"]["change_two_10"]["x"], y=conf["Graphic"]["change_two_10"]["y"], clicks=conf["Graphic"]["change_two_10"]["clicks"],button=conf["Graphic"]["change_two_10"]["button"], duration=0.3)
        auto.press("9")
        auto.click(x=conf["Graphic"]["change_two_13"]["x"], y=conf["Graphic"]["change_two_13"]["y"], clicks=conf["Graphic"]["change_two_13"]["clicks"],button=conf["Graphic"]["change_two_13"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_15"]["x"], y=conf["Graphic"]["change_two_15"]["y"], clicks=conf["Graphic"]["change_two_15"]["clicks"],button=conf["Graphic"]["change_two_15"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_17"]["x"], y=conf["Graphic"]["change_two_17"]["y"], clicks=conf["Graphic"]["change_two_17"]["clicks"],button=conf["Graphic"]["change_two_17"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_19"]["x"], y=conf["Graphic"]["change_two_19"]["y"], clicks=conf["Graphic"]["change_two_19"]["clicks"],button=conf["Graphic"]["change_two_19"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_21"]["x"], y=conf["Graphic"]["change_two_21"]["y"], clicks=conf["Graphic"]["change_two_21"]["clicks"],button=conf["Graphic"]["change_two_21"]["button"], duration=0.3)
        time.sleep(2)
        auto.click(x=conf["Graphic"]["change_two_24"]["x"], y=conf["Graphic"]["change_two_24"]["y"], clicks=conf["Graphic"]["change_two_24"]["clicks"],button=conf["Graphic"]["change_two_24"]["button"], duration=0.3)
        auto.press("del")
        auto.typewrite("250")
        auto.press("enter")
        time.sleep(2)
        style = '图案宽度修改'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["Graphic"]["change_two_32"]["x"], y=conf["Graphic"]["change_two_32"]["y"], clicks=conf["Graphic"]["change_two_32"]["clicks"],button=conf["Graphic"]["change_two_32"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_34"]["x"], y=conf["Graphic"]["change_two_34"]["y"], clicks=conf["Graphic"]["change_two_34"]["clicks"],button=conf["Graphic"]["change_two_34"]["button"], duration=0.3)
        time.sleep(3)
        style = '图案刺绣效果'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        #
        auto.click(x=conf["Graphic"]["change_two_32"]["x"], y=conf["Graphic"]["change_two_32"]["y"], clicks=conf["Graphic"]["change_two_32"]["clicks"],button=conf["Graphic"]["change_two_32"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_39"]["x"], y=conf["Graphic"]["change_two_39"]["y"], clicks=conf["Graphic"]["change_two_39"]["clicks"],button=conf["Graphic"]["change_two_39"]["button"], duration=0.3)
        time.sleep(3)
        style = '图案裂纹效果'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["Graphic"]["change_two_32"]["x"], y=conf["Graphic"]["change_two_32"]["y"], clicks=conf["Graphic"]["change_two_32"]["clicks"],button=conf["Graphic"]["change_two_32"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_two_44"]["x"], y=conf["Graphic"]["change_two_44"]["y"], clicks=conf["Graphic"]["change_two_44"]["clicks"],button=conf["Graphic"]["change_two_44"]["button"], duration=0.3)
        time.sleep(3)
        style = '图案金粉印效果'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

    @allure.story('图案使用织物镂空')
    def test_change_three(self):
        self.style.add_open_sproj('sproj', 'graphic_test.sproj')
        auto.click(x=conf["Graphic"]["change_three_1"]["x"], y=conf["Graphic"]["change_three_1"]["y"], clicks=conf["Graphic"]["change_three_1"]["clicks"],button=conf["Graphic"]["change_three_1"]["button"], duration=0.3)
        time.sleep(4)
        auto.click(x=conf["Graphic"]["change_three_25"]["x"], y=conf["Graphic"]["change_three_25"]["y"], clicks=conf["Graphic"]["change_three_25"]["clicks"],button=conf["Graphic"]["change_three_25"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_three_27"]["x"], y=conf["Graphic"]["change_three_27"]["y"], clicks=conf["Graphic"]["change_three_27"]["clicks"],button=conf["Graphic"]["change_three_27"]["button"], duration=0.3)
        time.sleep(2)
        style = '图案多实例织物镂空'
        new = '\\Graphic\\'+style+'_new.png'
        old = '\\Graphic\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)


        auto.click(x=conf["Graphic"]["change_three_15"]["x"], y=conf["Graphic"]["change_three_15"]["y"], clicks=conf["Graphic"]["change_three_15"]["clicks"],button=conf["Graphic"]["change_three_15"]["button"], duration=0.3)
        auto.press("esc")
        auto.click(x=conf["Graphic"]["change_three_16up"]["x"], y=conf["Graphic"]["change_three_16up"]["y"], clicks=conf["Graphic"]["change_three_16up"]["clicks"],button=conf["Graphic"]["change_three_16up"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_three_17"]["x"], y=conf["Graphic"]["change_three_17"]["y"], clicks=conf["Graphic"]["change_three_17"]["clicks"],button=conf["Graphic"]["change_three_17"]["button"], duration=0.3)
        auto.press("del")
        auto.click(x=conf["Graphic"]["change_three_20"]["x"], y=conf["Graphic"]["change_three_20"]["y"], clicks=conf["Graphic"]["change_three_20"]["clicks"],button=conf["Graphic"]["change_three_20"]["button"], duration=0.3)
        time.sleep(2)
        auto.click(x=conf["Graphic"]["change_three_25"]["x"], y=conf["Graphic"]["change_three_25"]["y"], clicks=conf["Graphic"]["change_three_25"]["clicks"],button=conf["Graphic"]["change_three_25"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_three_27"]["x"], y=conf["Graphic"]["change_three_27"]["y"], clicks=conf["Graphic"]["change_three_27"]["clicks"],button=conf["Graphic"]["change_three_27"]["button"], duration=0.3)
        time.sleep(2)
        style = '图案不镂空生成图案工艺'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["Graphic"]["change_three_25"]["x"], y=conf["Graphic"]["change_three_25"]["y"], clicks=conf["Graphic"]["change_three_25"]["clicks"],button=conf["Graphic"]["change_three_25"]["button"], duration=0.3)
        auto.click(x=conf["Graphic"]["change_three_27"]["x"], y=conf["Graphic"]["change_three_27"]["y"], clicks=conf["Graphic"]["change_three_27"]["clicks"],button=conf["Graphic"]["change_three_27"]["button"], duration=0.3)
        time.sleep(2)
        style = '图案镂空生成图案工艺'
        new = '\\Graphic\\' + style + '_new.png'
        old = '\\Graphic\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
