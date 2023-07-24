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
import pytest
screen_width, screen_height = auto.size()

@allure.feature('排料')
@allure.severity(allure.severity_level.CRITICAL)
class Test2DSnapshot(Log):

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
        self.log.info("测试结束")
        self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        auto.press('q')
        self.log.info('结束该用例')


    @allure.story('多码排料')
    def test_add_one(self):
        self.style.add_open_sproj('sproj', 'many_Marker.sproj')
        self.style.click_marker()
        auto.click(x=conf["ClickMarker"]["add_one_3"]['x'], y=conf["ClickMarker"]["add_one_3"]['y'],
                   clicks=conf["ClickMarker"]["add_one_3"]['clicks'], interval=0.0,
                   button=conf["ClickMarker"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(13)
        style = '多码排料'
        new = '\\Marker\\' + style + '_new.png'
        old = '\\Marker\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)


    @allure.story('空工程/隐藏/辅料排料')
    def test_add_two(self):
        #空工程排料
        self.style.click_marker()
        style = '空工程排料'
        new = '\\Marker\\' + style + '_new.png'
        old = '\\Marker\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)

        #隐藏/辅料排料
        self.style.add_open_sproj('sproj', '2D_Snapshot_null.sproj')
        self.style.click_marker()
        style = '辅料及隐藏版片排料'
        new = '\\Marker\\' + style + '_new.png'
        old = '\\Marker\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(3)

    @allure.story('统一贴图方式排料')
    def test_add_three(self):
        self.style.add_open_sproj('sproj', 'sfab_Unified.sproj')
        self.style.click_marker()
        style = '统一贴图方式排料'
        new = '\\Marker\\' + style + '_new.png'
        old = '\\Marker\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(3)
        #关闭提示弹窗
        auto.click(x=925, y=505, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.press('esc')



