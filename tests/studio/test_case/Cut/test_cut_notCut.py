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

@allure.feature('剪切-没有剪开')
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

    @allure.story('one:jira-18209')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '18209.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["notCut-18209"]["click_one_1"]["x"], y=conf["notCut-18209"]["click_one_1"]["y"], clicks=conf["notCut-18209"]["click_one_1"]["clicks"],button=conf["notCut-18209"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["notCut-18209"]["click_one_3"]["x"], y=conf["notCut-18209"]["click_one_3"]["y"], clicks=conf["notCut-18209"]["click_one_3"]["clicks"],button=conf["notCut-18209"]["click_one_3"]["button"], duration=0.2)
        auto.click(x=conf["notCut-18209"]["click_one_5"]["x"], y=conf["notCut-18209"]["click_one_5"]["y"], clicks=conf["notCut-18209"]["click_one_5"]["clicks"],button=conf["notCut-18209"]["click_one_5"]["button"], duration=0.2)
        auto.click(x=conf["notCut-18209"]["click_one_7"]["x"], y=conf["notCut-18209"]["click_one_7"]["y"], clicks=conf["notCut-18209"]["click_one_7"]["clicks"],button=conf["notCut-18209"]["click_one_7"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-18209'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-5927')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '5927.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["notCut-5927"]["click_one_1"]["x"], y=conf["notCut-5927"]["click_one_1"]["y"], clicks=conf["notCut-5927"]["click_one_1"]["clicks"],button=conf["notCut-5927"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["notCut-5927"]["click_one_3"]["x"], y=conf["notCut-5927"]["click_one_3"]["y"], clicks=conf["notCut-5927"]["click_one_3"]["clicks"],button=conf["notCut-5927"]["click_one_3"]["button"], duration=0.2)
        auto.click(x=conf["notCut-5927"]["click_one_5"]["x"], y=conf["notCut-5927"]["click_one_5"]["y"], clicks=conf["notCut-5927"]["click_one_5"]["clicks"],button=conf["notCut-5927"]["click_one_5"]["button"], duration=0.2)
        auto.click(x=conf["notCut-5927"]["click_one_7"]["x"], y=conf["notCut-5927"]["click_one_7"]["y"], clicks=conf["notCut-5927"]["click_one_7"]["clicks"],button=conf["notCut-5927"]["click_one_7"]["button"], duration=0.2)
        auto.click(x=conf["notCut-5927"]["click_one_9"]["x"], y=conf["notCut-5927"]["click_one_9"]["y"], clicks=conf["notCut-5927"]["click_one_9"]["clicks"],button=conf["notCut-5927"]["click_one_9"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-5927'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')