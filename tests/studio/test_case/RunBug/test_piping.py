# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('嵌条')
@allure.severity(allure.severity_level.CRITICAL)
class Testpiping:

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

    @allure.story('项目文件，嵌条衔接出异常--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/ff020bbe41bf9023a944a74961', name='STUDIO-6096')
    def test_piping_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6096.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        time.sleep(1)
        style = "STUDIO-6096，项目文件，嵌条衔接出异常"
        new = "\\RunBug\\piping\\"+style+"_new.png"
        old = "\\RunBug\\piping\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('项目文件，嵌条衔接出异常--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/099d9d7dbb8c64df66e0ce09d1',name='STUDIO-5263')
    def test_piping_two(self):
        self.style.add_open_sproj('sproj', 'STUDIO-5263.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        time.sleep(1)
        style = "STUDIO-5263，项目文件，嵌条衔接出异常"
        new = "\\RunBug\\piping\\" + style + "_new.png"
        old = "\\RunBug\\piping\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)