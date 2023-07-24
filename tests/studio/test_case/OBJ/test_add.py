import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
import allure
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


@allure.feature('OBJ添加方式：添加')
@allure.severity(allure.severity_level.CRITICAL)
class TestOBJ:

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
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        self.log.info('结束该用例')

    @allure.story('有模特时，特殊obj添加')
    def test_add_one(self):
        self.style.add_avatar('Male.savt')
        self.style.click_import_obj()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'sproj') + '\\' + 'obj_add_test.zip'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(5)

        auto.click(x=conf["OBJ"]["add_one_1"]['x'], y=conf["OBJ"]["add_one_1"]['y'], clicks=conf["OBJ"]["add_one_1"]['clicks'], button=conf["OBJ"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["add_one_2"]['x'], y=conf["OBJ"]["add_one_2"]['y'], clicks=conf["OBJ"]["add_one_2"]['clicks'], button=conf["OBJ"]["add_one_2"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["add_one_3"]['x'], y=conf["OBJ"]["add_one_3"]['y'], clicks=conf["OBJ"]["add_one_3"]['clicks'], button=conf["OBJ"]["add_one_3"]['button'], duration=0.2)

        time.sleep(23)
        style = '有模特时，特殊obj添加'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

