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

@allure.feature('剪切-自交')
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

    @allure.story('one:jira-12376')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '12376.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，中间对称轴，右键选择剪切，查看假缝没有消失
        auto.click(x=conf["selfing-12376"]["click_one_1"]["x"], y=conf["selfing-12376"]["click_one_1"]["y"], clicks=conf["selfing-12376"]["click_one_1"]["clicks"],button=conf["selfing-12376"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(5)
        auto.click(x=conf["selfing-12376"]["click_one_8"]["x"], y=conf["selfing-12376"]["click_one_8"]["y"], clicks=conf["selfing-12376"]["click_one_8"]["clicks"],button=conf["selfing-12376"]["click_one_8"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["selfing-12376"]["click_one_11"]["x"], y=conf["selfing-12376"]["click_one_11"]["y"], clicks=conf["selfing-12376"]["click_one_11"]["clicks"],button=conf["selfing-12376"]["click_one_11"]["button"], duration=0.2)
        auto.click(x=conf["selfing-12376"]["click_one_26"]["x"], y=conf["selfing-12376"]["click_one_26"]["y"], clicks=conf["selfing-12376"]["click_one_26"]["clicks"],button=conf["selfing-12376"]["click_one_26"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["selfing-12376"]["click_one_38"]["x"], y=conf["selfing-12376"]["click_one_38"]["y"], clicks=conf["selfing-12376"]["click_one_38"]["clicks"],button=conf["selfing-12376"]["click_one_38"]["button"], duration=0.2)
        auto.click(x=conf["selfing-12376"]["click_one_40"]["x"], y=conf["selfing-12376"]["click_one_40"]["y"], clicks=conf["selfing-12376"]["click_one_40"]["clicks"],button=conf["selfing-12376"]["click_one_40"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-12376'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-9969')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '9969.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["selfing-9969"]["click_one_1"]["x"], y=conf["selfing-9969"]["click_one_1"]["y"], clicks=conf["selfing-9969"]["click_one_1"]["clicks"],button=conf["selfing-9969"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(4)
        auto.click(x=conf["selfing-9969"]["click_one_7"]["x"], y=conf["selfing-9969"]["click_one_7"]["y"], clicks=conf["selfing-9969"]["click_one_7"]["clicks"],button=conf["selfing-9969"]["click_one_7"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        auto.click(x=conf["selfing-9969"]["click_one_10"]["x"], y=conf["selfing-9969"]["click_one_10"]["y"], clicks=conf["selfing-9969"]["click_one_10"]["clicks"],button=conf["selfing-9969"]["click_one_10"]["button"], duration=0.2)
        self.style.scroll_big_number(14)
        auto.click(x=conf["selfing-9969"]["click_one_26"]["x"], y=conf["selfing-9969"]["click_one_26"]["y"], clicks=conf["selfing-9969"]["click_one_26"]["clicks"],button=conf["selfing-9969"]["click_one_26"]["button"], duration=0.2)
        self.style.scroll_big_number(9)
        auto.click(x=conf["selfing-9969"]["click_one_37"]["x"], y=conf["selfing-9969"]["click_one_37"]["y"], clicks=conf["selfing-9969"]["click_one_37"]["clicks"],button=conf["selfing-9969"]["click_one_37"]["button"], duration=0.2)
        auto.click(x=conf["selfing-9969"]["click_one_39"]["x"], y=conf["selfing-9969"]["click_one_39"]["y"], clicks=conf["selfing-9969"]["click_one_39"]["clicks"],button=conf["selfing-9969"]["click_one_39"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-9969'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-3421')
    def test_add_three(self):

        self.style.add_open_sproj('cut', '3421.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["selfing-3421"]["click_one_1"]["x"], y=conf["selfing-3421"]["click_one_1"]["y"], clicks=conf["selfing-3421"]["click_one_1"]["clicks"],button=conf["selfing-3421"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(3)
        auto.click(x=conf["selfing-3421"]["click_one_6"]["x"], y=conf["selfing-3421"]["click_one_6"]["y"], clicks=conf["selfing-3421"]["click_one_6"]["clicks"],button=conf["selfing-3421"]["click_one_6"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["selfing-3421"]["click_one_14"]["x"], y=conf["selfing-3421"]["click_one_14"]["y"], clicks=conf["selfing-3421"]["click_one_14"]["clicks"],button=conf["selfing-3421"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["selfing-3421"]["click_one_16"]["x"], y=conf["selfing-3421"]["click_one_16"]["y"], clicks=conf["selfing-3421"]["click_one_16"]["clicks"],button=conf["selfing-3421"]["click_one_16"]["button"], duration=0.2)
        auto.click(x=conf["selfing-3421"]["click_one_18"]["x"], y=conf["selfing-3421"]["click_one_18"]["y"], clicks=conf["selfing-3421"]["click_one_18"]["clicks"],button=conf["selfing-3421"]["click_one_18"]["button"], duration=0.2)
        auto.click(x=conf["selfing-3421"]["click_one_20"]["x"], y=conf["selfing-3421"]["click_one_20"]["y"], clicks=conf["selfing-3421"]["click_one_20"]["clicks"],button=conf["selfing-3421"]["click_one_20"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-3421'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')