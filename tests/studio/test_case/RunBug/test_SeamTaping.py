# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('粘衬')
@allure.severity(allure.severity_level.CRITICAL)
class TestSeamTaping:

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

    @allure.story('STUDIO-6032关闭净边粘衬，2D3D版片网格异常--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/a841707b56a26a0b3e9df0a35d', name='STUDIO-6032')
    def test_SeamTaping_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6032.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()
        auto.click(x=140, y=557, button='left', duration=0.2)  # 点击净边
        auto.click(x=1881, y=772, button='left', duration=0.2)  # 属性栏关闭粘衬
        style = "STUDIO-6032，关闭净边粘衬，2D3D版片网格异常"
        new = "\\RunBug\\SeamTaping\\"+style+"_new.png"
        old = "\\RunBug\\SeamTaping\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)