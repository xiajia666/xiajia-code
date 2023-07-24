import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure
import pytest
screen_width, screen_height = auto.size()

@allure.feature('排料初始化位置')
@allure.severity(allure.severity_level.CRITICAL)
class Test2DSnapshot(Log):

    def setup_class(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_class(self):
        self.log.info("测试结束")
        self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        auto.press('q')
        self.log.info('结束该用例')


    @allure.story('导入DXF,查看排料初始化位置')
    def test_add_one(self):
        self.style.click_import_dxf()
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf\\ImportAndExport')
        dxf_path = import_path + '\\' + 'PUFFB边缘对称.dxf'
        pyperclip.copy(dxf_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["DXF"]["add_one_1"]['x'], y=conf["DXF"]["add_one_1"]['y'],
                   clicks=conf["DXF"]["add_one_1"]['clicks'], button=conf["DXF"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["DXF"]["add_one_2"]['x'], y=conf["DXF"]["add_one_2"]['y'],
                   clicks=conf["DXF"]["add_one_2"]['clicks'], button=conf["DXF"]["add_one_2"]['button'], duration=0.2)
        time.sleep(2)
        self.style.click_cloth_textured_surface2d()
        self.style.click_marker()
        time.sleep(3)
        style = '导入DXF,查看排料初始化位置'
        new = '\\Marker\\' + style + '_new.png'
        old = '\\Marker\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)



