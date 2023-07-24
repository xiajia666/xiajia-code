# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('两线之间生成内部线')
@allure.severity(allure.severity_level.CRITICAL)
class TestDistributeInternalLineBetweenSegments:

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

    @allure.story('两线之间生成等距内部线崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/69009ee19f19430fdbd34ce436', name='STUDIO-6394')
    def test_seperate_pattern_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6394，两线之间生成等距内部线崩溃.sproj', '2')
        self.style.focus_panorama()
        auto.press('z')
        auto.mouseDown(x=61, y=225,button='left', duration=0.2)  #框选版片
        auto.mouseUp(x=680, y=893,button='left', duration=0.2)
        # time.sleep(1)
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=384, y=805, button='left', duration=0.2)  # 反选去除上下净边
        auto.click(x=384, y=300, button='left', duration=0.2)  # 反选去除上下净边
        auto.keyUp('shift')  # 松开shift键
        auto.click(x=648, y=466, button='right', duration=0.5)  # 右键线段之间生成内部线
        auto.click(x=708, y=612, button='left', duration=0.2)
        auto.click(x=989, y=656, button='left', duration=0.2)  #点击确定
        time.sleep(1)
        style = "STUDIO-6394，两线之间生成等距内部线崩溃"
        new = "\\RunBug\\DistributeInternalLineBetweenSegments\\"+style+"_new.png"
        old = "\\RunBug\\DistributeInternalLineBetweenSegments\\"+style+"_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

