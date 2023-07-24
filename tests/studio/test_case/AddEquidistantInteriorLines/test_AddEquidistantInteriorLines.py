# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('生成等距内部线')
@allure.severity(allure.severity_level.CRITICAL)
class Test_AddEquidistantInteriorLines:

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

    @allure.story('STUDIO-532生成等距内部线，前后片内部线对不上')
    def test_add_one(self):
        self.style.add_open_sproj('addEquidistantInteriorLines', 'STUDIO-532.sproj')
        self.style.focus_panorama()
        auto.sleep(2)
        # 框选底部净边，右键生成内部线
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_1"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_1"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_1"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_1"]["button"], duration=0.2)
        auto.mouseDown(x=conf["AddEquidistantInteriorLines"]["click_one_3"]["x"],
                       y=conf["AddEquidistantInteriorLines"]["click_one_3"]["y"],
                       button=conf["AddEquidistantInteriorLines"]["click_one_3"]["button"], duration=0.2)
        auto.mouseUp(x=conf["AddEquidistantInteriorLines"]["click_one_4up"]["x"],
                     y=conf["AddEquidistantInteriorLines"]["click_one_4up"]["y"],
                     button=conf["AddEquidistantInteriorLines"]["click_one_4up"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_5"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_5"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_5"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_5"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_7"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_7"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_7"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_7"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_9"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_9"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_9"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_9"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("40")
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_13"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_13"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_13"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_13"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("2")
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_17"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_17"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_17"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_17"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_19"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_19"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_19"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_19"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_one_21"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_one_21"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_one_21"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_one_21"]["button"], duration=0.2)
        time.sleep(1)
        style = "STUDIO-532生成等距内部线，前后片内部线对不上"
        new = "\\AddEquidistantInteriorLines\\" + style + "_new.png"
        old = "\\AddEquidistantInteriorLines\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-479生成等距内部线，设置特定参数后崩溃')
    def test_add_two(self):
        self.style.add_open_sproj('addEquidistantInteriorLines', 'STUDIO-479.sproj')
        self.style.focus_panorama()
        auto.sleep(2)

        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_1"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_1"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_1"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_1"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_3"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_3"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_3"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_3"]["button"], duration=0.2)
        auto.sleep(1)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_5"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_5"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_5"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_5"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_7"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_7"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_7"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_7"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_9"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_9"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_9"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_9"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("1")
        auto.sleep(1)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_17"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_17"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_17"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_17"]["button"], duration=0.2)
        auto.press("del")
        auto.typewrite("2")
        auto.sleep(1)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_21"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_21"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_21"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_21"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_23"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_23"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_23"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_23"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_25"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_25"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_25"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_25"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_27"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_27"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_27"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_27"]["button"], duration=0.2)
        auto.click(x=conf["AddEquidistantInteriorLines"]["click_two_29"]["x"],
                   y=conf["AddEquidistantInteriorLines"]["click_two_29"]["y"],
                   clicks=conf["AddEquidistantInteriorLines"]["click_two_29"]["clicks"],
                   button=conf["AddEquidistantInteriorLines"]["click_two_29"]["button"], duration=0.2)

        time.sleep(1)
        style = "STUDIO-479生成等距内部线，设置特定参数后崩溃"
        new = "\\AddEquidistantInteriorLines\\" + style + "_new.png"
        old = "\\AddEquidistantInteriorLines\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)
