# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('合并')
@allure.severity(allure.severity_level.CRITICAL)
class Testmerge:

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

    @allure.story('如图所示合并两条线，提示自交--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/a888f6c6e97134da0bfe45f862', name='STUDIO-3657')
    def test_merge_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-3657.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=213, y=621, button='left', duration=0.2)  #
        auto.click(x=220, y=639, button='right', duration=0.2)  #
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=253, y=704, button='left', duration=0.2)  #点合并
        time.sleep(1)
        style = "STUDIO-3657，如图所示合并两条线，提示自交"
        new = "\\RunBug\\merge\\"+style+"_new.png"
        old = "\\RunBug\\merge\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('对称版片合并，会提示自交，可用附件工程调试--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/54d1495be17ec77910a712f67e', name='STUDIO-841')
    def test_merge_two(self):
        self.style.add_open_sproj('sproj', 'STUDIO-841.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=425, y=444, button='left', duration=0.2)  #
        auto.click(x=437, y=665, button='right', duration=0.2)  #
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=486, y=730, button='left', duration=0.2)  #点合并
        time.sleep(1)
        style = "STUDIO-841，对称版片合并，会提示自交"
        new = "\\RunBug\\merge\\"+style+"_new.png"
        old = "\\RunBug\\merge\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('合并后2/3D中版片位置不对--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/e61409d32efeac61e4708c6c30', name='STUDIO-1004')
    def test_merge_three(self):
        self.style.add_open_sproj('sproj', 'STUDIO-1004.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()

        auto.mouseDown(x=296, y=673, button='left', duration=0.2)  #
        auto.mouseUp(x=243, y=624, button='left', duration=0.2)  #
        time.sleep(0.5)
        auto.click(x=254, y=612, button='right', duration=0.2)
        auto.click(x=309, y=682, button='left', duration=0.2)  #点合并
        time.sleep(1)
        style = "STUDIO-1004，合并后23D中版片位置不对"
        new = "\\RunBug\\merge\\"+style+"_new.png"
        old = "\\RunBug\\merge\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('选择两条边后，右键合并，程序崩溃--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/e61409d32efeac61e4708c6c30', name='STUDIO-7410')
    def test_merge_four(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7410.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        auto.keyDown('shift')
        auto.click(x=657, y=604, button='left', duration=0.2)  #
        auto.click(x=133, y=612, button='right', duration=0.2)  #
        auto.keyUp('shift')
        time.sleep(0.5)
        auto.click(x=189, y=707, button='left', duration=0.2)  #点合并
        time.sleep(2)
        style = "STUDIO-7410，选择两条边后，右键合并，程序崩溃"
        new = "\\RunBug\\merge\\"+style+"_new.png"
        old = "\\RunBug\\merge\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('合并版片，合并结果是自交的情况下，程序崩溃--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/3b26d253863255a7c63d1982e6', name='STUDIO-7415')
    def test_merge_five(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7415.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        auto.keyDown('shift')
        auto.click(x=479, y=575, button='left', duration=0.2)  #
        auto.click(x=333, y=588, button='right', duration=0.2)  #
        auto.keyUp('shift')
        time.sleep(0.5)
        auto.click(x=386, y=656, button='left', duration=0.2)  #点合并
        time.sleep(2)
        style = "STUDIO-7415，合并版片，合并结果是自交的情况下，程序崩溃"
        new = "\\RunBug\\merge\\"+style+"_new.png"
        old = "\\RunBug\\merge\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)