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

@allure.feature('剪切-三角化异常')
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

    @allure.story('one:jira-17366')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '17366.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，点击左边内部线，按住ctrl同时点击右边内部线，松开ctrl，右键选择剪切
        auto.click(x=conf["CutTriangulation-17366"]["click_one_3"]["x"], y=conf["CutTriangulation-17366"]["click_one_3"]["y"], clicks=conf["CutTriangulation-17366"]["click_one_3"]["clicks"],button=conf["CutTriangulation-17366"]["click_one_3"]["button"], duration=0.2)
        self.style.scroll_big_number(14)
        auto.click(x=conf["CutTriangulation-17366"]["click_one_19"]["x"], y=conf["CutTriangulation-17366"]["click_one_19"]["y"], clicks=conf["CutTriangulation-17366"]["click_one_19"]["clicks"],button=conf["CutTriangulation-17366"]["click_one_19"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["CutTriangulation-17366"]["click_one_22"]["x"], y=conf["CutTriangulation-17366"]["click_one_22"]["y"], clicks=conf["CutTriangulation-17366"]["click_one_22"]["clicks"],button=conf["CutTriangulation-17366"]["click_one_22"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["CutTriangulation-17366"]["click_one_30"]["x"], y=conf["CutTriangulation-17366"]["click_one_30"]["y"], clicks=conf["CutTriangulation-17366"]["click_one_30"]["clicks"],button=conf["CutTriangulation-17366"]["click_one_30"]["button"], duration=0.2)
        auto.click(x=conf["CutTriangulation-17366"]["click_one_32"]["x"], y=conf["CutTriangulation-17366"]["click_one_32"]["y"], clicks=conf["CutTriangulation-17366"]["click_one_32"]["clicks"],button=conf["CutTriangulation-17366"]["click_one_32"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-17366'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('jira-15181')
    def test_add_two(self):

        self.style.add_open_sproj('cut', '15181.sproj')
        self.style.click_edit_pattern()  # 编辑版片模式

        #打开2D视窗网格，放大视角，剪切，再缩小视角
        auto.click(x=conf["CutTriangulation-15181"]["click_one_3"]["x"], y=conf["CutTriangulation-15181"]["click_one_3"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_3"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_3"]["button"], duration=0.2)
        auto.click(x=conf["CutTriangulation-15181"]["click_one_5"]["x"], y=conf["CutTriangulation-15181"]["click_one_5"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_5"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_5"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["CutTriangulation-15181"]["click_one_13"]["x"], y=conf["CutTriangulation-15181"]["click_one_13"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_13"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_13"]["button"], duration=0.2)
        self.style.scroll_big_number(5)
        auto.click(x=conf["CutTriangulation-15181"]["click_one_20"]["x"], y=conf["CutTriangulation-15181"]["click_one_20"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_20"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_20"]["button"], duration=0.2)
        auto.click(x=conf["CutTriangulation-15181"]["click_one_22"]["x"], y=conf["CutTriangulation-15181"]["click_one_22"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_22"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_22"]["button"], duration=0.2)
        auto.click(x=conf["CutTriangulation-15181"]["click_one_24"]["x"], y=conf["CutTriangulation-15181"]["click_one_24"]["y"], clicks=conf["CutTriangulation-15181"]["click_one_24"]["clicks"],button=conf["CutTriangulation-15181"]["click_one_24"]["button"], duration=0.2)
        self.style.scroll_small_number(6)
        time.sleep(3)
        style = 'jira-15181'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
