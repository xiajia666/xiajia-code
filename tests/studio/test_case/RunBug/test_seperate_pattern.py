# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('分割版片')
@allure.severity(allure.severity_level.CRITICAL)
class TestSeperatePattern:

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

    @allure.story('分割版片')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/a4489370e0f5bf12a256a86c46', name='STUDIO-6982')
    def test_seperate_pattern_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6982.sproj', '2')
        self.style.focus_panorama()
        auto.press('z')
        auto.click(x=411, y=431, button='left', duration=0.2)  # 点击内部线
        time.sleep(2)
        auto.press('del')
        time.sleep(1)
        style = "STUDIO-6982，在2D选择分割线内部线，删除后，还保留分割版片的2个织物信息"
        new = "\\RunBug\\SeperatePattern\\"+style+"_new.png"
        old = "\\RunBug\\SeperatePattern\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

