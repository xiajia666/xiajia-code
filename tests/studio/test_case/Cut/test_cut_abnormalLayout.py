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

@allure.feature('剪切-版片异常')
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

    @allure.story('one:jira-17595')

    def test_send_message(self):
        self.style.send_message("Style3D 剪切专项开始，本次测试版本号：", None, None, "18066268343")

    def test_add_one(self):
        self.style.add_open_sproj('cut', '17595.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，中间对称轴，右键选择剪切，查看假缝没有消失
        auto.click(x=conf["abnormalLayout-17595"]["click_one_1"]["x"], y=conf["abnormalLayout-17595"]["click_one_1"]["y"], clicks=conf["abnormalLayout-17595"]["click_one_1"]["clicks"],button=conf["abnormalLayout-17595"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(5)
        auto.click(x=conf["abnormalLayout-17595"]["click_one_8"]["x"], y=conf["abnormalLayout-17595"]["click_one_8"]["y"], clicks=conf["abnormalLayout-17595"]["click_one_8"]["clicks"],button=conf["abnormalLayout-17595"]["click_one_8"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-17595"]["click_one_10"]["x"], y=conf["abnormalLayout-17595"]["click_one_10"]["y"], clicks=conf["abnormalLayout-17595"]["click_one_10"]["clicks"],button=conf["abnormalLayout-17595"]["click_one_10"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17595'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-17555')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '17555.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-17555"]["click_one_1"]["x"], y=conf["abnormalLayout-17555"]["click_one_1"]["y"], clicks=conf["abnormalLayout-17555"]["click_one_1"]["clicks"],button=conf["abnormalLayout-17555"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(3)
        auto.click(x=conf["abnormalLayout-17555"]["click_one_6"]["x"], y=conf["abnormalLayout-17555"]["click_one_6"]["y"], clicks=conf["abnormalLayout-17555"]["click_one_6"]["clicks"],button=conf["abnormalLayout-17555"]["click_one_6"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["abnormalLayout-17555"]["click_one_14"]["x"], y=conf["abnormalLayout-17555"]["click_one_14"]["y"], clicks=conf["abnormalLayout-17555"]["click_one_14"]["clicks"],button=conf["abnormalLayout-17555"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-17555"]["click_one_16"]["x"], y=conf["abnormalLayout-17555"]["click_one_16"]["y"], clicks=conf["abnormalLayout-17555"]["click_one_16"]["clicks"],button=conf["abnormalLayout-17555"]["click_one_16"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17555'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-17295')
    def test_add_three(self):

        self.style.add_open_sproj('cut', '17295.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-17295"]["click_one_1"]["x"], y=conf["abnormalLayout-17295"]["click_one_1"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_1"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(2)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_5"]["x"], y=conf["abnormalLayout-17295"]["click_one_5"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_5"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_5"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_13"]["x"], y=conf["abnormalLayout-17295"]["click_one_13"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_13"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_13"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_21"]["x"], y=conf["abnormalLayout-17295"]["click_one_21"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_21"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_21"]["button"], duration=0.2)
        self.style.scroll_big_number(2)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_27"]["x"], y=conf["abnormalLayout-17295"]["click_one_27"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_27"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_27"]["button"], duration=0.2)
        # auto.click(x=conf["abnormalLayout-17295"]["click_one_29"]["x"], y=conf["abnormalLayout-17295"]["click_one_29"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_29"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_29"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["abnormalLayout-17295"]["click_one_35"]["x"], y=conf["abnormalLayout-17295"]["click_one_35"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_35"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_35"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_3"]["x"], y=conf["abnormalLayout-17295"]["click_one_3"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_3"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_3"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_4"]["x"], y=conf["abnormalLayout-17295"]["click_one_4"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_4"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_4"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_6"]["x"], y=conf["abnormalLayout-17295"]["click_one_6"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_6"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_6"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_7"]["x"], y=conf["abnormalLayout-17295"]["click_one_7"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_7"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_7"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-17295"]["click_one_8"]["x"], y=conf["abnormalLayout-17295"]["click_one_8"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_8"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_8"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["abnormalLayout-17295"]["click_one_9"]["x"], y=conf["abnormalLayout-17295"]["click_one_9"]["y"], clicks=conf["abnormalLayout-17295"]["click_one_9"]["clicks"],button=conf["abnormalLayout-17295"]["click_one_9"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17295'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-17182')
    def test_add_four(self):

        self.style.add_open_sproj('cut', '17182.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-17182"]["click_one_1"]["x"], y=conf["abnormalLayout-17182"]["click_one_1"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_1"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_small_number(2)
        auto.click(x=conf["abnormalLayout-17182"]["click_one_5"]["x"], y=conf["abnormalLayout-17182"]["click_one_5"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_5"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_5"]["button"], duration=0.2)
        self.style.scroll_big_number(11)
        # auto.click(x=conf["abnormalLayout-17182"]["click_one_18"]["x"], y=conf["abnormalLayout-17182"]["click_one_18"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_18"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_18"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["abnormalLayout-17182"]["click_one_26"]["x"], y=conf["abnormalLayout-17182"]["click_one_26"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_26"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_26"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["abnormalLayout-17182"]["click_one_121"]["x"], y=conf["abnormalLayout-17182"]["click_one_121"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_121"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_121"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["abnormalLayout-17182"]["click_one_200"]["x"], y=conf["abnormalLayout-17182"]["click_one_200"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_200"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_200"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        time.sleep(3)
        auto.click(x=conf["abnormalLayout-17182"]["click_one_217"]["x"], y=conf["abnormalLayout-17182"]["click_one_217"]["y"], clicks=conf["abnormalLayout-17182"]["click_one_217"]["clicks"],button=conf["abnormalLayout-17182"]["click_one_217"]["button"], duration=0.5)
        time.sleep(3)
        style = 'jira-17182'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-17014')
    def test_add_five(self):

        self.style.add_open_sproj('cut', '17014.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-17014"]["click_one_1"]["x"], y=conf["abnormalLayout-17014"]["click_one_1"]["y"], clicks=conf["abnormalLayout-17014"]["click_one_1"]["clicks"],button=conf["abnormalLayout-17014"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(8)
        auto.click(x=conf["abnormalLayout-17014"]["click_one_11"]["x"], y=conf["abnormalLayout-17014"]["click_one_11"]["y"], clicks=conf["abnormalLayout-17014"]["click_one_11"]["clicks"],button=conf["abnormalLayout-17014"]["click_one_11"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-17014"]["click_one_13"]["x"], y=conf["abnormalLayout-17014"]["click_one_13"]["y"], clicks=conf["abnormalLayout-17014"]["click_one_13"]["clicks"],button=conf["abnormalLayout-17014"]["click_one_13"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17014'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-7366')
    def test_add_six(self):

        self.style.add_open_sproj('cut', '7366.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-7366"]["click_one_1"]["x"], y=conf["abnormalLayout-7366"]["click_one_1"]["y"], clicks=conf["abnormalLayout-7366"]["click_one_1"]["clicks"],button=conf["abnormalLayout-7366"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(9)
        # auto.click(x=conf["abnormalLayout-7366"]["click_one_12"]["x"], y=conf["abnormalLayout-7366"]["click_one_12"]["y"], clicks=conf["abnormalLayout-7366"]["click_one_12"]["clicks"],button=conf["abnormalLayout-7366"]["click_one_12"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-7366"]["click_one_14"]["x"], y=conf["abnormalLayout-7366"]["click_one_14"]["y"], clicks=conf["abnormalLayout-7366"]["click_one_14"]["clicks"],button=conf["abnormalLayout-7366"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-7366"]["click_one_16"]["x"], y=conf["abnormalLayout-7366"]["click_one_16"]["y"], clicks=conf["abnormalLayout-7366"]["click_one_16"]["clicks"],button=conf["abnormalLayout-7366"]["click_one_16"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-7366"]["click_one_18"]["x"], y=conf["abnormalLayout-7366"]["click_one_18"]["y"], clicks=conf["abnormalLayout-7366"]["click_one_18"]["clicks"],button=conf["abnormalLayout-7366"]["click_one_18"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-7366'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')


    @allure.story('one:jira-6392')
    def test_add_seven(self):

        self.style.add_open_sproj('cut', '6392.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        auto.click(x=conf["abnormalLayout-6392"]["click_one_1"]["x"], y=conf["abnormalLayout-6392"]["click_one_1"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_1"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(8)
        auto.click(x=conf["abnormalLayout-6392"]["click_one_11"]["x"], y=conf["abnormalLayout-6392"]["click_one_11"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_11"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_11"]["button"], duration=0.2)
        # auto.click(x=conf["abnormalLayout-6392"]["click_one_13"]["x"], y=conf["abnormalLayout-6392"]["click_one_13"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_13"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_13"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["abnormalLayout-6392"]["click_one_20"]["x"], y=conf["abnormalLayout-6392"]["click_one_20"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_20"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_20"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-6392"]["click_one_80"]["x"], y=conf["abnormalLayout-6392"]["click_one_80"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_80"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_80"]["button"], duration=0.2)
        auto.click(x=conf["abnormalLayout-6392"]["click_one_116"]["x"], y=conf["abnormalLayout-6392"]["click_one_116"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_116"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_116"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["abnormalLayout-6392"]["click_one_126"]["x"], y=conf["abnormalLayout-6392"]["click_one_126"]["y"], clicks=conf["abnormalLayout-6392"]["click_one_126"]["clicks"],button=conf["abnormalLayout-6392"]["click_one_126"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-6392'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')