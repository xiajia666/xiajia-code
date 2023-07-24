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

@allure.feature('剪切-素材改变')
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

    @allure.story('one:jira-17778')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '17778.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，点击左边内部线，按住ctrl同时点击右边内部线，松开ctrl，右键选择剪切
        auto.click(x=conf["MaterialChange-17778"]["click_one_1"]["x"], y=conf["MaterialChange-17778"]["click_one_1"]["y"], clicks=conf["MaterialChange-17778"]["click_one_1"]["clicks"],button=conf["MaterialChange-17778"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(5)
        auto.click(x=conf["MaterialChange-17778"]["click_one_10"]["x"], y=conf["MaterialChange-17778"]["click_one_10"]["y"], clicks=conf["MaterialChange-17778"]["click_one_10"]["clicks"],button=conf["MaterialChange-17778"]["click_one_10"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17778"]["click_one_12"]["x"], y=conf["MaterialChange-17778"]["click_one_12"]["y"], clicks=conf["MaterialChange-17778"]["click_one_12"]["clicks"],button=conf["MaterialChange-17778"]["click_one_12"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17778'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-17627')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '17627.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["MaterialChange-17627"]["click_one_1"]["x"], y=conf["MaterialChange-17627"]["click_one_1"]["y"], clicks=conf["MaterialChange-17627"]["click_one_1"]["clicks"],button=conf["MaterialChange-17627"]["click_one_1"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17627"]["click_one_3"]["x"], y=conf["MaterialChange-17627"]["click_one_3"]["y"], clicks=conf["MaterialChange-17627"]["click_one_3"]["clicks"],button=conf["MaterialChange-17627"]["click_one_3"]["button"], duration=0.2)
        self.style.scroll_big_number(3)
        auto.click(x=conf["MaterialChange-17627"]["click_one_10"]["x"], y=conf["MaterialChange-17627"]["click_one_10"]["y"], clicks=conf["MaterialChange-17627"]["click_one_10"]["clicks"],button=conf["MaterialChange-17627"]["click_one_10"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17627"]["click_one_12"]["x"], y=conf["MaterialChange-17627"]["click_one_12"]["y"], clicks=conf["MaterialChange-17627"]["click_one_12"]["clicks"],button=conf["MaterialChange-17627"]["click_one_12"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17627'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-17105')
    def test_add_three(self):

        self.style.add_open_sproj('cut', '17105.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["MaterialChange-17105"]["click_one_3"]["x"], y=conf["MaterialChange-17105"]["click_one_3"]["y"], clicks=conf["MaterialChange-17105"]["click_one_3"]["clicks"],button=conf["MaterialChange-17105"]["click_one_3"]["button"], duration=0.2)
        self.style.scroll_big_number(7)
        auto.click(x=conf["MaterialChange-17105"]["click_one_14"]["x"], y=conf["MaterialChange-17105"]["click_one_14"]["y"], clicks=conf["MaterialChange-17105"]["click_one_14"]["clicks"],button=conf["MaterialChange-17105"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17105"]["click_one_16"]["x"], y=conf["MaterialChange-17105"]["click_one_16"]["y"], clicks=conf["MaterialChange-17105"]["click_one_16"]["clicks"],button=conf["MaterialChange-17105"]["click_one_16"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17105"]["click_one_18"]["x"], y=conf["MaterialChange-17105"]["click_one_18"]["y"], clicks=conf["MaterialChange-17105"]["click_one_18"]["clicks"],button=conf["MaterialChange-17105"]["click_one_18"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-17105"]["click_one_20"]["x"], y=conf["MaterialChange-17105"]["click_one_20"]["y"], clicks=conf["MaterialChange-17105"]["click_one_20"]["clicks"],button=conf["MaterialChange-17105"]["click_one_20"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17105'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-16962')
    def test_add_four(self):

        self.style.add_open_sproj('cut', '16962.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["MaterialChange-16962"]["click_one_1"]["x"], y=conf["MaterialChange-16962"]["click_one_1"]["y"], clicks=conf["MaterialChange-16962"]["click_one_1"]["clicks"],button=conf["MaterialChange-16962"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(3)
        auto.click(x=conf["MaterialChange-16962"]["click_one_6"]["x"], y=conf["MaterialChange-16962"]["click_one_6"]["y"], clicks=conf["MaterialChange-16962"]["click_one_6"]["clicks"],button=conf["MaterialChange-16962"]["click_one_6"]["button"], duration=0.2)
        self.style.scroll_big_number(4)
        auto.click(x=conf["MaterialChange-16962"]["click_one_14"]["x"], y=conf["MaterialChange-16962"]["click_one_14"]["y"], clicks=conf["MaterialChange-16962"]["click_one_14"]["clicks"],button=conf["MaterialChange-16962"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["MaterialChange-16962"]["click_one_16"]["x"], y=conf["MaterialChange-16962"]["click_one_16"]["y"], clicks=conf["MaterialChange-16962"]["click_one_16"]["clicks"],button=conf["MaterialChange-16962"]["click_one_16"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-16962'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
