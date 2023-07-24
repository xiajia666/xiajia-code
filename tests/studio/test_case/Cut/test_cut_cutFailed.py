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

@allure.feature('剪切-剪切失败')
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

    @allure.story('one:jira-9699')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '9699.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["cutFailed-9699"]["click_one_1"]["x"], y=conf["cutFailed-9699"]["click_one_1"]["y"], clicks=conf["cutFailed-9699"]["click_one_1"]["clicks"],button=conf["cutFailed-9699"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9699"]["click_one_3"]["x"], y=conf["cutFailed-9699"]["click_one_3"]["y"], clicks=conf["cutFailed-9699"]["click_one_3"]["clicks"],button=conf["cutFailed-9699"]["click_one_3"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9699"]["click_one_5"]["x"], y=conf["cutFailed-9699"]["click_one_5"]["y"], clicks=conf["cutFailed-9699"]["click_one_5"]["clicks"],button=conf["cutFailed-9699"]["click_one_5"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-9699'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-9017')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '9017.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["cutFailed-9017"]["click_one_1"]["x"], y=conf["cutFailed-9017"]["click_one_1"]["y"], clicks=conf["cutFailed-9017"]["click_one_1"]["clicks"],button=conf["cutFailed-9017"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9017"]["click_one_3"]["x"], y=conf["cutFailed-9017"]["click_one_3"]["y"], clicks=conf["cutFailed-9017"]["click_one_3"]["clicks"],button=conf["cutFailed-9017"]["click_one_3"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9017"]["click_one_5"]["x"], y=conf["cutFailed-9017"]["click_one_5"]["y"], clicks=conf["cutFailed-9017"]["click_one_5"]["clicks"],button=conf["cutFailed-9017"]["click_one_5"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9017"]["click_one_7"]["x"], y=conf["cutFailed-9017"]["click_one_7"]["y"], clicks=conf["cutFailed-9017"]["click_one_7"]["clicks"],button=conf["cutFailed-9017"]["click_one_7"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-9017"]["click_one_9"]["x"], y=conf["cutFailed-9017"]["click_one_9"]["y"], clicks=conf["cutFailed-9017"]["click_one_9"]["clicks"],button=conf["cutFailed-9017"]["click_one_9"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-9017'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-16540')
    def test_add_three(self):

        self.style.add_open_sproj('cut', '16540.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["cutFailed-16540"]["click_one_1"]["x"], y=conf["cutFailed-16540"]["click_one_1"]["y"], clicks=conf["cutFailed-16540"]["click_one_1"]["clicks"],button=conf["cutFailed-16540"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-16540"]["click_one_3"]["x"], y=conf["cutFailed-16540"]["click_one_3"]["y"], clicks=conf["cutFailed-16540"]["click_one_3"]["clicks"],button=conf["cutFailed-16540"]["click_one_3"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-16540'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-6647')
    def test_add_four(self):

        self.style.add_open_sproj('cut', '6647.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["cutFailed-6647"]["click_one_1"]["x"], y=conf["cutFailed-6647"]["click_one_1"]["y"], clicks=conf["cutFailed-6647"]["click_one_1"]["clicks"],button=conf["cutFailed-6647"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(12)
        auto.click(x=conf["cutFailed-6647"]["click_one_15"]["x"], y=conf["cutFailed-6647"]["click_one_15"]["y"], clicks=conf["cutFailed-6647"]["click_one_15"]["clicks"],button=conf["cutFailed-6647"]["click_one_15"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-6647"]["click_one_17"]["x"], y=conf["cutFailed-6647"]["click_one_17"]["y"], clicks=conf["cutFailed-6647"]["click_one_17"]["clicks"],button=conf["cutFailed-6647"]["click_one_17"]["button"], duration=0.2)
        auto.click(x=conf["cutFailed-6647"]["click_one_19"]["x"], y=conf["cutFailed-6647"]["click_one_19"]["y"], clicks=conf["cutFailed-6647"]["click_one_19"]["clicks"],button=conf["cutFailed-6647"]["click_one_19"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-6647'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-6037')
    def test_add_five(self):

        self.style.add_open_sproj('cut', '6037.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["cutFailed-6037"]["click_one_1"]["x"], y=conf["cutFailed-6037"]["click_one_1"]["y"], clicks=conf["cutFailed-6037"]["click_one_1"]["clicks"],button=conf["cutFailed-6037"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["cutFailed-6037"]["click_one_9"]["x"], y=conf["cutFailed-6037"]["click_one_9"]["y"], clicks=conf["cutFailed-6037"]["click_one_9"]["clicks"],button=conf["cutFailed-6037"]["click_one_9"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["cutFailed-6037"]["click_one_36"]["x"], y=conf["cutFailed-6037"]["click_one_36"]["y"], clicks=conf["cutFailed-6037"]["click_one_36"]["clicks"],button=conf["cutFailed-6037"]["click_one_36"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["cutFailed-6037"]["click_one_52"]["x"], y=conf["cutFailed-6037"]["click_one_52"]["y"], clicks=conf["cutFailed-6037"]["click_one_52"]["clicks"],button=conf["cutFailed-6037"]["click_one_52"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-6037'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')