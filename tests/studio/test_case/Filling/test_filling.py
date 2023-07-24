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

@allure.feature('充绒')
@allure.severity(allure.severity_level.CRITICAL)
class TestFilling(Log):

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


    @allure.story('STUDIO-5801默认T_shirt，生成充绒版片，查看边缘对称版片的参数')
    def test_add_one(self):
        self.style.add_tshirt('Female_T-Shirt')
        auto.click(x=560, y=750, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击2D空白处
        auto.keyDown('ctrl')
        auto.keyDown('a')
        auto.keyUp('a')
        auto.keyUp('ctrl')
        auto.click(x=507, y=611, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear) #右键
        time.sleep(2)
        auto.click(x=579, y=95, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击生成里布层
        time.sleep(2)
        auto.click(x=767, y=148, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成充绒版片
        time.sleep(2)
        auto.click(x=502, y=890, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击充绒版片放置的位置
        time.sleep(2)
        auto.click(x=1892, y=773, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击属性栏充绒量
        auto.typewrite('500')
        auto.click(x=1892, y=800, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击属性栏绗缝间距
        auto.typewrite('5')
        auto.press('enter')
        auto.click(x=487, y=860, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击前片

        time.sleep(2)
        style = '查看充绒参数'
        new = '\\Filling\\' + style + '_new.png'
        old = '\\Filling\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 2, 92, 1907, 1014)
        time.sleep(2)

    @allure.story('STUDIO-5807取消边缘对称、剪切后充绒关系解除')
    def test_add_two(self):
        self.style.add_tshirt('Female_T-Shirt')
        self.style.click_edit_pattern()
        auto.click(x=205, y=572, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 点击后片对称轴
        auto.click(x=253, y=581, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 点击取消对称
        self.style.click_select()
        auto.click(x=560, y=750, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击2D空白处
        auto.keyDown('ctrl')
        auto.keyDown('a')
        auto.keyUp('a')
        auto.keyUp('ctrl')
        auto.click(x=507, y=611, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 右键
        time.sleep(2)
        auto.click(x=579, y=95, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成里布层
        time.sleep(2)
        auto.click(x=767, y=148, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成充绒版片
        time.sleep(2)
        auto.click(x=502, y=890, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击充绒版片放置的位置
        time.sleep(2)

        self.style.click_edit_pattern()
        auto.click(x=474, y=584, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 点击前片对称轴
        auto.click(x=520, y=600, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击取消对称
        time.sleep(2)
        self.style.click_trace()
        auto.click(x=205, y=577, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 点击后片基础线
        auto.click(x=245, y=678, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击剪切

        time.sleep(2)
        style = '查看版片关系'
        new = '\\Filling\\' + style + '_new.png'
        old = '\\Filling\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200,)
        time.sleep(2)






