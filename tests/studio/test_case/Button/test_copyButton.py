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


@allure.feature('复制纽扣')
@allure.severity(allure.severity_level.CRITICAL)
class TestCopyButton:

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

    @allure.story('边缘对称：1.沿线纽扣右键复制到对称版片;2.框选多纽扣,右键将扣眼复制到对称版片;3.3D单个纽扣ctrl+c复制')
    def test_add_one(self):
        self.style.rectangle_creat()
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2) #点击空白处，使长方形失焦
        self.style.click_edit_pattern()
        auto.click(x=486, y=435, clicks=1, button='right', duration=0.2)  # 点击长方形右侧净边
        auto.click(x=530, y=498, clicks=1, button='right', duration=0.2)  # 点击边缘对称
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦

        '''沿线纽扣右键复制到对称版片'''
        self.style.click_button()
        auto.click(x=354, y=404, clicks=1, button='right', duration=0.2) #点击左侧净边
        auto.click(x=1031, y=500, clicks=1, button='left', duration=0.2) #点击起始位置
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1031, y=528, clicks=1, button='left', duration=0.2) #点击终止位置
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1042, y=600, clicks=1, button='left', duration=0.2) #点击数量
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1000, y=637, clicks=1, button='left', duration=0.2) #点击确认
        time.sleep(1)
        auto.click(x=356, y=416, clicks=1, button='right', duration=0.2)  #选中沿线纽扣右键
        auto.click(x=411, y=591, clicks=1, button='left', duration=0.2)  #复制到对称版片

        # '''框选多纽扣,右键将扣眼复制到对称版片'''
        auto.click(x=547, y=434, clicks=1, button='right', duration=0.2)
        auto.click(x=1031, y=588, clicks=1, button='left', duration=0.2)
        auto.press('delete')
        auto.typewrite('50')
        auto.click(x=1031, y=642, clicks=1, button='left', duration=0.2)
        auto.press('delete')
        auto.typewrite('5')
        auto.click(x=993, y=690, clicks=1, button='left', duration=0.2)  # 点击确认
        time.sleep(1)
        auto.mouseDown(x=524, y=419, button='left') #框选纽扣
        auto.mouseUp(x=580, y=502, button='left', duration=0.2)
        time.sleep(1)
        auto.click(x=547, y=447, clicks=1, button='right', duration=0.2) #右键将扣眼复制到对称版片
        time.sleep(1)
        auto.click(x=620, y=625, clicks=1, button='left', duration=0.2) #将扣眼复制到对称版片

        '''3D单个纽扣ctrl+c复制'''
        auto.click(x=1253, y=630, clicks=1, button='left', duration=0.2) #3D添加纽扣
        auto.click(x=1253, y=630, clicks=1, button='left', duration=0.2) #3D选中纽扣
        auto.hotkey('ctrl', 'c')
        auto.hotkey('ctrl', 'v')
        auto.click(x=1305, y=700, clicks=1, button='left', duration=0.2)
        time.sleep(1)

        self.style.focus_panorama()
        auto.press('2')
        style = '边缘对称复制纽扣'
        new = '\\Button\\' + style + '_new.png'
        old = '\\Button\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)



    @allure.story('对称版片：1.沿线纽扣右键复制到对称版片;2.框选多纽扣,右键将扣眼复制到对称版片')
    def test_add_two(self):
        self.style.rectangle_creat()
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2) #点击空白处，使长方形失焦
        self.style.click_select()
        auto.click(x=420, y=444, clicks=1, button='right', duration=0.2)  # 点击长方形右键
        auto.click(x=468, y=68, clicks=1, button='left', duration=0.2)  # 右键克隆对称版片
        auto.click(x=570, y=440, clicks=1, button='left', duration=0.2)
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦

        '''沿线纽扣右键复制到对称版片'''
        self.style.click_button()
        auto.click(x=354, y=404, clicks=1, button='right', duration=0.2) #点击左侧净边
        auto.click(x=1042, y=502, clicks=1, button='left', duration=0.2) #点击起始位置
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1042, y=530, clicks=1, button='left', duration=0.2) #点击终止位置
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1042, y=600, clicks=1, button='left', duration=0.2) #点击数量
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=1000, y=639, clicks=1, button='left', duration=0.2) #点击确认
        time.sleep(1)
        auto.click(x=356, y=416, clicks=1, button='right', duration=0.2)  #选中沿线纽扣右键
        time.sleep(1)
        auto.click(x=416, y=592, clicks=1, button='left', duration=0.2)  #复制到对称版片

        '''框选多纽扣,右键将扣眼复制到对称版片'''
        auto.click(x=547, y=434, clicks=1, button='right', duration=0.2)
        auto.click(x=1031, y=588, clicks=1, button='left', duration=0.2)
        auto.press('delete')
        auto.typewrite('50')
        time.sleep(1)
        auto.click(x=1031, y=642, clicks=1, button='left', duration=0.2)
        auto.press('delete')
        auto.typewrite('5')
        time.sleep(1)
        auto.click(x=993, y=690, clicks=1, button='left', duration=0.2)  # 点击确认
        time.sleep(1)
        auto.mouseDown(x=524, y=419, button='left') #框选纽扣
        auto.mouseUp(x=580, y=502, button='left', duration=0.2)
        time.sleep(1)
        auto.click(x=547, y=447, clicks=1, button='right', duration=0.2) #右键将扣眼复制到对称版片
        time.sleep(1)
        auto.click(x=620, y=625, clicks=1, button='left', duration=0.2) #将扣眼复制到对称版片


        self.style.focus_panorama()
        auto.press('2')
        style = '对称版片复制纽扣'
        new = '\\Button\\' + style + '_new.png'
        old = '\\Button\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)