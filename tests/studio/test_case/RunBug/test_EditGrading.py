# -*- coding: utf-8 -*-
import sys
import os
import pyperclip
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('放码')
@allure.severity(allure.severity_level.CRITICAL)
class TestEditGrading:

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

    @allure.story('STUDIO-6658切换放码信息为s的时候，在3D上袖子上的内部线渲染有问题---sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/830c660febe2187c1b1e082f6e', name='STUDIO-6658')
    def test_EditGrading_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6658.sproj')
        time.sleep(2)
        auto.click(x=107, y=51, button='left', duration=0.2)  # 编辑版片
        auto.click(x=1680, y=103, button='left', duration=0.2)  # 当前栏尺寸
        auto.click(x=1784, y=136, button='left', duration=0.2)  # 放码
        auto.click(x=1764, y=195, button='left', duration=0.2)  # s
        time.sleep(2)
        style = "STUDIO-6658，切换放码信息为s的时候，在3D上袖子上的内部线渲染有问题"
        new = "\\RunBug\\EditGrading\\"+style+"_new.png"
        old = "\\RunBug\\EditGrading\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)