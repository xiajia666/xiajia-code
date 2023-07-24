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

@allure.feature('剪切-边界值')
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
        # self.operationfile.keep_window()
        # self.style.start_style3D()

    def teardown_class(self):
        self.log.info('测试结束，关闭软件')
        # self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        self.log.info('结束该用例')

    @allure.story('one:min')
    def test_add_one(self):

        self.style.add_open_sproj('cut', 'min.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # auto.click(x=conf["minimum-min"]["click_one_1"]["x"], y=conf["minimum-min"]["click_one_1"]["y"], clicks=conf["minimum-min"]["click_one_1"]["clicks"],button=conf["minimum-min"]["click_one_1"]["button"], duration=0.2)
        # self.style.scroll_big_number(7)
        # auto.click(x=conf["minimum-min"]["click_one_10"]["x"], y=conf["minimum-min"]["click_one_10"]["y"], clicks=conf["minimum-min"]["click_one_10"]["clicks"],button=conf["minimum-min"]["click_one_10"]["button"], duration=0.2)
        # self.style.scroll_big_number(3)
        # auto.click(x=conf["minimum-min"]["click_one_15"]["x"], y=conf["minimum-min"]["click_one_15"]["y"], clicks=conf["minimum-min"]["click_one_15"]["clicks"],button=conf["minimum-min"]["click_one_15"]["button"], duration=0.2)
        # self.style.scroll_big_number(3)
        # auto.click(x=conf["minimum-min"]["click_one_20"]["x"], y=conf["minimum-min"]["click_one_20"]["y"], clicks=conf["minimum-min"]["click_one_20"]["clicks"],button=conf["minimum-min"]["click_one_20"]["button"], duration=0.2)
        # self.style.scroll_big_number(3)
        # auto.click(x=conf["minimum-min"]["click_one_25"]["x"], y=conf["minimum-min"]["click_one_25"]["y"], clicks=conf["minimum-min"]["click_one_25"]["clicks"],button=conf["minimum-min"]["click_one_25"]["button"], duration=0.2)
        # self.style.scroll_big_number(5)
        auto.click(x=conf["minimum-min"]["click_one_32"]["x"], y=conf["minimum-min"]["click_one_32"]["y"], clicks=conf["minimum-min"]["click_one_32"]["clicks"],button=conf["minimum-min"]["click_one_32"]["button"], duration=0.2)
        auto.click(x=conf["minimum-min"]["click_one_34"]["x"], y=conf["minimum-min"]["click_one_34"]["y"], clicks=conf["minimum-min"]["click_one_34"]["clicks"],button=conf["minimum-min"]["click_one_34"]["button"], duration=0.2)
        time.sleep(3)
        style = 'min'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')