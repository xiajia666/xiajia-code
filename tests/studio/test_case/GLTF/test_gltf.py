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


@allure.feature('gltf导入导出')
@allure.severity(allure.severity_level.CRITICAL)
class TestGLTF:

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

    @allure.story('gltf导出后导入')
    def test_add_one(self):
        self.operationfile.delete_file_style('export_gltf.gltf')
        self.style.add_open_sproj('sproj', 'export_savt.sproj')
        self.style.click_export_gltf()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_gltf.gltf'
        self.log.info(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(5)
        style = 'GLTF导出界面查看'
        new = '\\GLTF\\' + style + '_new.png'
        old = '\\GLTF\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["GLTF"]["add_one_1"]['x'], y=conf["GLTF"]["add_one_1"]['y'],clicks=conf["GLTF"]["add_one_1"]['clicks'],button=conf["GLTF"]["add_one_1"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["GLTF"]["add_one_2"]['x'], y=conf["GLTF"]["add_one_2"]['y'],clicks=conf["GLTF"]["add_one_2"]['clicks'], button=conf["GLTF"]["add_one_2"]['button'], duration=0.2)
        time.sleep(10)
        self.style.click_new_project()
        self.style.click_import_gltf()
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["GLTF"]["add_one_3"]['x'], y=conf["GLTF"]["add_one_3"]['y'],clicks=conf["GLTF"]["add_one_3"]['clicks'],button=conf["GLTF"]["add_one_3"]['button'], duration=0.2)
        auto.click(x=conf["GLTF"]["add_one_4"]['x'], y=conf["GLTF"]["add_one_4"]['y'],clicks=conf["GLTF"]["add_one_4"]['clicks'], button=conf["GLTF"]["add_one_4"]['button'], duration=0.2)
        time.sleep(10)
        style = 'GLTF导入查看'
        new = '\\GLTF\\' + style + '_new.png'
        old = '\\GLTF\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["GLB"]["add_one_5"]['x'], y=conf["GLB"]["add_one_5"]['y'],clicks=conf["GLB"]["add_one_5"]['clicks'],button=conf["GLB"]["add_one_5"]['button'], duration=0.2)
        time.sleep(3)
        auto.press('del')
        time.sleep(2)

    @allure.story('gltf后导入后作为附件')
    def test_add_two(self):
        self.style.click_import_gltf()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_gltf.gltf'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["GLTF"]["add_two_1"]['x'], y=conf["GLTF"]["add_two_1"]['y'],clicks=conf["GLTF"]["add_two_1"]['clicks'], button=conf["GLTF"]["add_two_1"]['button'], duration=0.2)
        auto.click(x=conf["GLTF"]["add_two_2"]['x'], y=conf["GLTF"]["add_two_2"]['y'],clicks=conf["GLTF"]["add_two_2"]['clicks'], button=conf["GLTF"]["add_two_2"]['button'], duration=0.2)
        auto.click(x=conf["GLTF"]["add_two_3"]['x'], y=conf["GLTF"]["add_two_3"]['y'],clicks=conf["GLTF"]["add_two_3"]['clicks'], button=conf["GLTF"]["add_two_3"]['button'], duration=0.2)
        time.sleep(10)
        style = 'GLTF导入为附件查看'
        new = '\\GLTF\\' + style + '_new.png'
        old = '\\GLTF\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
        time.sleep(2)

    @allure.story('gltf导入后作为附件')
    def test_add_three(self):
        self.style.click_import_gltf()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_gltf.gltf'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["GLTF"]["add_three_1"]['x'], y=conf["GLTF"]["add_three_1"]['y'],clicks=conf["GLTF"]["add_three_1"]['clicks'], button=conf["GLTF"]["add_three_1"]['button'], duration=0.2)
        auto.click(x=conf["GLTF"]["add_three_2"]['x'], y=conf["GLTF"]["add_three_2"]['y'],clicks=conf["GLTF"]["add_three_2"]['clicks'], button=conf["GLTF"]["add_three_2"]['button'], duration=0.2)
        auto.click(x=conf["GLTF"]["add_three_3"]['x'], y=conf["GLTF"]["add_three_3"]['y'],clicks=conf["GLTF"]["add_three_3"]['clicks'], button=conf["GLTF"]["add_three_3"]['button'], duration=0.2)
        time.sleep(10)
        style = 'GLTF导入为道具查看'
        new = '\\GLTF\\' + style + '_new.png'
        old = '\\GLTF\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
        time.sleep(2)

