import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('剪切-崩溃')
@allure.severity(allure.severity_level.BLOCKER)
class TestCUT():

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

    @allure.story('one:jira-17472')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '17472.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，边缘对称的内部线，右键选择剪切，软件没有崩溃
        auto.click(x=conf["CutCollapse-17472"]["click_one_1"]["x"], y=conf["CutCollapse-17472"]["click_one_1"]["y"], clicks=conf["CutCollapse-17472"]["click_one_1"]["clicks"],button=conf["CutCollapse-17472"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(3)
        auto.click(x=conf["CutCollapse-17472"]["click_one_6"]["x"], y=conf["CutCollapse-17472"]["click_one_6"]["y"], clicks=conf["CutCollapse-17472"]["click_one_6"]["clicks"],button=conf["CutCollapse-17472"]["click_one_6"]["button"], duration=0.2)
        auto.click(x=conf["CutCollapse-17472"]["click_one_8"]["x"], y=conf["CutCollapse-17472"]["click_one_8"]["y"], clicks=conf["CutCollapse-17472"]["click_one_8"]["clicks"],button=conf["CutCollapse-17472"]["click_one_8"]["button"], duration=0.2)

        time.sleep(3)
        style = 'jira-17472'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-17270')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '17270.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，选择内部线，右键选择剪切，软件没有崩溃
        auto.click(x=conf["CutCollapse-17270"]["click_one_1"]["x"], y=conf["CutCollapse-17270"]["click_one_1"]["y"], clicks=conf["CutCollapse-17270"]["click_one_1"]["clicks"],button=conf["CutCollapse-17270"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(2)
        auto.click(x=conf["CutCollapse-17270"]["click_one_9"]["x"], y=conf["CutCollapse-17270"]["click_one_9"]["y"], clicks=conf["CutCollapse-17270"]["click_one_9"]["clicks"],button=conf["CutCollapse-17270"]["click_one_9"]["button"], duration=0.2)
        auto.click(x=conf["CutCollapse-17270"]["click_one_11"]["x"], y=conf["CutCollapse-17270"]["click_one_11"]["y"], clicks=conf["CutCollapse-17270"]["click_one_11"]["clicks"],button=conf["CutCollapse-17270"]["click_one_11"]["button"], duration=0.2)
        time.sleep(3)

        style = 'jira-17270'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-17204')
    def test_add_three(self):

        self.style.add_open_sproj('cut', '17204.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，选择内部线，右键选择剪切，软件没有崩溃
        auto.click(x=conf["CutCollapse-17204"]["click_one_1"]["x"], y=conf["CutCollapse-17204"]["click_one_1"]["y"], clicks=conf["CutCollapse-17204"]["click_one_1"]["clicks"],button=conf["CutCollapse-17204"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(4)
        auto.click(x=conf["CutCollapse-17204"]["click_one_7"]["x"], y=conf["CutCollapse-17204"]["click_one_7"]["y"], clicks=conf["CutCollapse-17204"]["click_one_7"]["clicks"],button=conf["CutCollapse-17204"]["click_one_7"]["button"], duration=0.2)
        auto.click(x=conf["CutCollapse-17204"]["click_one_9"]["x"], y=conf["CutCollapse-17204"]["click_one_9"]["y"], clicks=conf["CutCollapse-17204"]["click_one_9"]["clicks"],button=conf["CutCollapse-17204"]["click_one_9"]["button"], duration=0.2)
        time.sleep(3)

        style = 'jira-17204'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-17181')
    def test_add_four(self):

        self.style.add_open_sproj('cut', '17181.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，选择内部线，右键选择剪切，软件没有崩溃
        auto.typewrite("9")
        auto.click(x=conf["CutCollapse-17181"]["click_one_4"]["x"], y=conf["CutCollapse-17181"]["click_one_4"]["y"],clicks=conf["CutCollapse-17181"]["click_one_4"]["clicks"],button=conf["CutCollapse-17181"]["click_one_4"]["button"], duration=0.2)
        self.style.scroll_big_number(9)
        auto.typewrite("i")
        auto.click(x=conf["CutCollapse-17181"]["click_one_16"]["x"], y=conf["CutCollapse-17181"]["click_one_16"]["y"],clicks=conf["CutCollapse-17181"]["click_one_16"]["clicks"],button=conf["CutCollapse-17181"]["click_one_16"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["CutCollapse-17181"]["click_one_38"]["x"], y=conf["CutCollapse-17181"]["click_one_38"]["y"],clicks=conf["CutCollapse-17181"]["click_one_38"]["clicks"],button=conf["CutCollapse-17181"]["click_one_38"]["button"], duration=0.2)
        auto.click(x=conf["CutCollapse-17181"]["click_one_83"]["x"], y=conf["CutCollapse-17181"]["click_one_83"]["y"],clicks=conf["CutCollapse-17181"]["click_one_83"]["clicks"],button=conf["CutCollapse-17181"]["click_one_83"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["CutCollapse-17181"]["click_one_96"]["x"], y=conf["CutCollapse-17181"]["click_one_96"]["y"],clicks=conf["CutCollapse-17181"]["click_one_96"]["clicks"],button=conf["CutCollapse-17181"]["click_one_96"]["button"], duration=0.2)
        auto.click(x=conf["CutCollapse-17181"]["click_one_98"]["x"], y=conf["CutCollapse-17181"]["click_one_98"]["y"],clicks=conf["CutCollapse-17181"]["click_one_98"]["clicks"],button=conf["CutCollapse-17181"]["click_one_98"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17181'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')