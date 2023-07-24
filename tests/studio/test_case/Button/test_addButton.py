import yaml
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
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())
screen_width, screen_height = auto.size()


@allure.feature('添加纽扣')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddButton:

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
        self.style.click_cloth_textured_surface3d()

    def teardown_method(self):
        """不做操作，直接新建 """
        auto.press('q')
        self.log.info('结束该用例')

    @allure.story('1.添加沿线纽扣;2.单击添加单个纽扣;3.顶点添加纽扣;4.右键弹框添加纽扣;5.净边双击添加纽扣;6.3D添加纽扣')
    def test_add_one(self):
        self.style.rectangle_creat()
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2) #点击空白处，使长方形失焦
        self.style.click_edit_pattern()
        auto.click(x=486, y=435, clicks=1, button='right', duration=0.2)  # 点击长方形右侧净边
        auto.click(x=530, y=498, clicks=1, button='right', duration=0.2)  # 点击边缘对称
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦

        '''添加沿线纽扣'''
        self.style.click_button()
        auto.click(x=354, y=404, clicks=1, button='right', duration=0.2) #点击左侧净边
        auto.click(x=1042, y=502, clicks=1, button='left', duration=0.2) #点击起始位置
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1042, y=530, clicks=1, button='left', duration=0.2) #点击终止位置
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1042, y=600, clicks=1, button='left', duration=0.2) #点击数量
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1000, y=639, clicks=1, button='left', duration=0.2) #点击确认
        time.sleep(2)

        '''单击添加单个纽扣'''
        auto.click(x=417, y=445, clicks=1, button='left', duration=0.2)
        time.sleep(1)

        '''顶点添加纽扣'''
        auto.click(x=617, y=508, clicks=1, button='left', duration=0.2) #点击右下角顶点
        time.sleep(1)

        '''右键弹框添加纽扣'''
        auto.click(x=547, y=434, clicks=1, button='right', duration=0.2)
        auto.click(x=1045, y=590, clicks=1, button='left', duration=0.2)
        time.sleep(1)
        auto.typewrite('5')
        auto.click(x=1045, y=640, clicks=1, button='left', duration=0.2)
        time.sleep(1)
        auto.typewrite('5')
        auto.click(x=992, y=691, clicks=1, button='left', duration=0.2)  # 点击确认
        time.sleep(1)

        '''净边双击添加纽扣'''
        auto.doubleClick(x=618, y=440, interval=0.0, button='left', duration=0.2)

        '''3D添加纽扣'''
        auto.click(x=1253, y=630, clicks=1, button='left', duration=0.2)

        self.style.focus_panorama()
        auto.press('2')
        style = '添加纽扣'
        new = '\\Button\\' + style + '_new.png'
        old = '\\Button\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)