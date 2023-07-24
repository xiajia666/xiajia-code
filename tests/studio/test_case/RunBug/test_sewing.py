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

@allure.feature('缝纫线')
@allure.severity(allure.severity_level.CRITICAL)
class TestSewing(Log):

    def setup_method(self):
        global conf9
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


    @allure.story('STUDIO-7069编辑缝纫，移动距离较小时触发端点吸附，导致移动距离无法生效')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/c07748bd44f6324115e62deaf6',name='STUDIO-7069')
    def test_sewing_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7069.sproj')
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击2D空白处
        auto.press('9')
        auto.click(x=1111, y=300, clicks=1, button='left', duration=0.2) #点击3D空白处
        auto.press('9')
        time.sleep(1)
        self.style.click_edit_sewing()
        time.sleep(1)
        auto.mouseDown(x=449, y=655, button='left')  # 移动缝纫线
        auto.click(x=449, y=627, clicks=1, button='right', duration=0.2)  # 右键
        auto.mouseUp(x=449, y=627, button='left', duration=0.2)
        time.sleep(1)
        auto.press('delete')
        auto.typewrite('10')
        auto.click(x=923, y=622, clicks=1, button='left', duration=0.2)  # 点击确认

        style = 'STUDIO-7069编辑缝纫，移动距离较小时触发端点吸附，导致移动距离无法生效'
        new = '\\RunBug\\Sewing\\' + style + '_new.png'
        old = '\\RunBug\\Sewing\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)








