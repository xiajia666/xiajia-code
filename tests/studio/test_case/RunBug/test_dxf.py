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

@allure.feature('DXF')
@allure.severity(allure.severity_level.CRITICAL)
class TestDxf:

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


    @allure.story('STUDIO-7409导入DXF，勾选将基础线勾勒为内部线，软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/56f268c77525f0a66cc8dfdf12',name='STUDIO-7409')
    def test_dxf_one(self):
        self.style.click_import_dxf()
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'sproj\\STUDIO-7409.dxf')
        pyperclip.copy(import_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')

        time.sleep(1)
        auto.click(x=857, y=635, clicks=1, button='left', duration=0.2)  # 点击重置
        auto.click(x=829, y=577, clicks=1, button='left', duration=0.2)  # 点击选项
        auto.click(x=848, y=744, clicks=1, button='left', duration=0.2)  # 点击将基础线勾勒为内部线
        auto.click(x=992, y=909, clicks=1, button='left', duration=0.2)  # 点击确定

        time.sleep(3)

        style = "STUDIO-7409导入DXF，勾选将基础线勾勒为内部线，软件崩溃"
        new = "\\RunBug\\DXF\\" + style + "_new.png"
        old = "\\RunBug\\DXF\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=1060, y=600, clicks=1, button='left', duration=0.2)  # 点击自交确定

