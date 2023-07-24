# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('图案')
@allure.severity(allure.severity_level.CRITICAL)
class Testgraphic:

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

    @allure.story('3D视窗中图案定位线没有了--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/196cb1c8b6160fd6c13568a156', name='STUDIO-5417')
    def test_graphic_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-5417.sproj')
        self.style.focus_panorama()
        time.sleep(1)
        style = "STUDIO-5417，3D视窗中图案定位线没有了"
        new = "\\RunBug\\graphic\\"+style+"_new.png"
        old = "\\RunBug\\graphic\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('对称版片多选图案，3D中旋转图案，图案旋转方向不一致--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d7950d60bc155603a4e4531412', name='STUDIO-6504')
    def test_graphic_two(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6504.sproj')
        self.style.focus_panorama()
        self.style.click_transform_graphic()
        time.sleep(1)
        auto.mouseDown(x=1218, y=652, button='left', duration=0.2)
        auto.mouseUp(x=930, y=524, button='left', duration=0.2)
        auto.mouseDown(x=973, y=553, button='left', duration=0.2)
        auto.mouseUp(x=930, y=577, button='left', duration=0.2)
        style = "STUDIO-6504，对称版片多选图案，3D中旋转图案，图案旋转方向不一致"
        new = "\\RunBug\\graphic\\"+style+"_new.png"
        old = "\\RunBug\\graphic\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)