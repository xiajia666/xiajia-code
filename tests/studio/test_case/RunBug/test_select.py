# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('选择')
@allure.severity(allure.severity_level.CRITICAL)
class TestSelect:

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

    @allure.story('边缘对称按ctrl和其他版片拖拽')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/69009ee19f19430fdbd34ce436', name='STUDIO-6677')
    def test_select_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6677，边缘对称按ctrl和其他版片拖拽.sproj', '2')
        self.style.focus_panorama()
        auto.press('q')
        auto.click(x=345, y=592, button='left', duration=0.2)  # 选择边缘对称版片
        auto.keyDown('ctrl')  # 按下ctrl键
        auto.click(x=615, y=601, button='left', duration=0.2)  # 选择另一个版片
        auto.keyUp('ctrl')  # 松开ctrl键
        auto.mouseDown(x=592, y=611,button='left', duration=0.2) # 一起拖拽版片
        auto.mouseUp(x=592, y=947,button='left', duration=0.2)
        time.sleep(1)
        style = "STUDIO-6677，边缘对称按ctrl和其他版片拖拽"
        new = "\\RunBug\\Select\\"+style+"_new.png"
        old = "\\RunBug\\Select\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-8177从右下往左上框选内部线和省道，删除崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d667fad6be605b8e6cd501c677',name='STUDIO-8177')
    def test_select_two(self):
        self.style.add_open_sproj('sproj', 'STUDIO-8177.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()

        auto.mouseDown(x=440, y=536, button='left', duration=0.2)  # 从右下往左上框选内部线和省道
        auto.mouseUp(x=180, y=410, button='left', duration=0.2)
        time.sleep(1)
        auto.press("Delete")

        style = "STUDIO-8177从右下往左上框选内部线和省道，删除崩溃"
        new = "\\RunBug\\Select\\" + style + "_new.png"
        old = "\\RunBug\\Select\\" + style + "_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)
