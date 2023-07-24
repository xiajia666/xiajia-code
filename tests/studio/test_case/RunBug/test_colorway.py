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

@allure.feature('齐色')
@allure.severity(allure.severity_level.CRITICAL)
class TestColorway:

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

    @allure.story('附件齐色材质为空，到出SCO崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d85d985660a49465eb9a1c0622', name='STUDIO-6639')
    def test_colorway_one(self):
        self.operationfile.delete_file_style('export_STUDIO-6639.sco')
        self.style.add_open_sproj('sproj', 'STUDIO-6639.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        self.style.click_export_sco()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'),'export') + '\\' + 'export_STUDIO-6639.sco'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=585, y=888, button='left', duration=0.2) #点击重置
        auto.click(x=1132, y=309, button='left', duration=0.2) #勾选多有齐色
        time.sleep(3)
        auto.click(x=1264, y=890, button='left', duration=0.2)  #点击确定
        time.sleep(15)
        style = "STUDIO-6639，附件齐色材质为空，导出SCO崩溃"
        new = "\\RunBug\\Colorway\\"+style+"_new.png"
        old = "\\RunBug\\Colorway\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)



