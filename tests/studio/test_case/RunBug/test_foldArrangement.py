# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('折叠安排')
@allure.severity(allure.severity_level.CRITICAL)
class TestfoldArrangement:

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

    @allure.story('两条内部线无法折叠安排，会将整个版片旋转--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d2fdab93dc2f26e2acf870d7fc', name='STUDIO-4366')
    def test_foldArrangement_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-4366.sproj')
        self.style.focus_panorama()
        self.style.click_oldArrangement()
        auto.click(x=1225, y=527, button='left', duration=0.2)  #
        time.sleep(0.5)
        auto.mouseDown(x=1218, y=479, button='left', duration=0.2)  #
        auto.mouseUp(x=1253, y=500, button='left', duration=0.2)  #
        time.sleep(1)
        style = "STUDIO-4366，两条内部线无法折叠安排，会将整个版片旋转"
        new = "\\RunBug\\foldArrangement\\"+style+"_new.png"
        old = "\\RunBug\\foldArrangement\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)