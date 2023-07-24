# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('曲线点')
@allure.severity(allure.severity_level.CRITICAL)
class TestCurvePoint:

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

    @allure.story('未更新曲线控制点')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/ebdfd409a00d1aae3c0f971857', name='STUDIO-6429')
    def test_curvePoint_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6429.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        auto.click(x=conf["RunBug"]["curvePoint_one_1"]["x"], y=conf["RunBug"]["curvePoint_one_1"]["y"], clicks=conf["RunBug"]["curvePoint_one_1"]["clicks"],button=conf["RunBug"]["curvePoint_one_1"]["button"], duration=0.2)
        auto.hotkey('ctrl', 'c')
        auto.hotkey('ctrl', 'v')
        auto.click(x=conf["RunBug"]["curvePoint_one_2"]["x"], y=conf["RunBug"]["curvePoint_one_2"]["y"], clicks=conf["RunBug"]["curvePoint_one_2"]["clicks"],button=conf["RunBug"]["curvePoint_one_2"]["button"], duration=0.2)
        self.style.click_select()
        time.sleep(0.5)
        auto.mouseDown(x=277, y=500, button='left', duration=0.2) #移动版片
        auto.mouseUp(x=540, y=170, button='left', duration=0.2)
        time.sleep(0.5)
        self.style.click_edit_curvePoint()
        style = "STUDIO-6429，复制粘贴曲线后移动版片，曲线点脱离线段"
        new = "\\RunBug\\CurvePoint\\"+style+"_new.png"
        old = "\\RunBug\\CurvePoint\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)



