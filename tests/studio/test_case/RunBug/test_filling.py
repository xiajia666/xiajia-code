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

    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()


    @allure.story('STUDIO-6975生成里布层后，无法再生成充绒版片')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/6741f485868e7a2b1a5e43bc60',name='STUDIO-6975')
    def test_filling_one(self):
        self.style.add_tshirt('Female_T-Shirt')
        auto.click(x=560, y=750, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击2D空白处
        auto.keyDown('ctrl')
        auto.keyDown('a')
        auto.keyUp('a')
        auto.keyUp('ctrl')
        auto.click(x=507, y=611, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear) #右键
        time.sleep(2)
        auto.click(x=579, y=95, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击生成里布
        time.sleep(2)
        auto.click(x=740, y=95, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成里布层
        time.sleep(2)
        auto.click(x=502, y=890, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击里布层放置的位置
        time.sleep(2)
        auto.press('9')
        auto.mouseDown(x=90, y=290, button='left')  # 框选版片
        auto.mouseUp(x=720, y=540, button='left', duration=0.2)
        auto.click(x=500, y=450, clicks=1, interval=0.0, button='right', duration=0.2, tween=auto.linear)  # 右键
        time.sleep(2)
        auto.click(x=580, y=95, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成里布
        time.sleep(2)
        auto.click(x=748, y=148, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击生成充绒版片
        time.sleep(2)
        auto.click(x=502, y=1000, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击充绒版片放置的位置
        time.sleep(2)
        auto.click(x=700, y=577, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击2D空白处
        auto.press('9')

        style = 'STUDIO-6975生成里布层后，无法再生成充绒版片'
        new = '\\RunBug\\Filling\\' + style + '_new.png'
        old = '\\RunBug\\Filling\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)








