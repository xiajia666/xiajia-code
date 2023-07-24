import pyautogui
import yaml
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
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())


@allure.feature('DXF放码')
@allure.severity(allure.severity_level.BLOCKER)
class TestDXFGrade:

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
        # self.style.click_cloth_textured_surface2d()
        # self.style.click_cloth_textured_surface3d()

    def teardown_method(self):
        """不做操作，直接新建 """
        auto.press('q')
        self.log.info('结束该用例')

    def test_send_message(self):
        self.style.send_message("Style3D DXF专项开始，本次测试版本号：", None, "15757119427")

    @allure.story('3个码')
    def test_add_three(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading','3Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],y=conf["ImportDxfSubject"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],y=conf["ImportDxfSubject"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],y=conf["ImportDxfSubject"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],y=conf["ImportDxfSubject"]["click_one_11"]['y'],clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] +'放码1', '\\DXF\\EditGrading\\3Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] +'放码2', '\\DXF\\EditGrading\\3Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] +'放码3', '\\DXF\\EditGrading\\3Size\\')
                time.sleep(2)

    @allure.story('4个码')
    def test_add_four(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '4Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\4Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\4Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\4Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\4Size\\')
                time.sleep(2)

    @allure.story('5个码')
    def test_add_five(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '5Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\5Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\5Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\5Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\5Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\5Size\\')
                time.sleep(2)

    @allure.story('6个码')
    def test_add_six(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '6Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\6Size\\')
                time.sleep(2)

    @allure.story('7个码')
    def test_add_seven(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '7Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 375, dxf_name.split('.', 1)[0] + '放码7', '\\DXF\\EditGrading\\7Size\\')
                time.sleep(2)

    @allure.story('8个码')
    def test_add_eight(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '8Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 375, dxf_name.split('.', 1)[0] + '放码7', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 405, dxf_name.split('.', 1)[0] + '放码8', '\\DXF\\EditGrading\\8Size\\')
                time.sleep(2)

    @allure.story('9个码')
    def test_add_nine(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '9Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1764, 195, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 255, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 375, dxf_name.split('.', 1)[0] + '放码7', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 405, dxf_name.split('.', 1)[0] + '放码8', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)
                self.style.test_click_grade(1764, 434, dxf_name.split('.', 1)[0] + '放码9', '\\DXF\\EditGrading\\9Size\\')
                time.sleep(2)

    @allure.story('10个码')
    def test_add_ten(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '10Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                auto.click(x=1540, y=160, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  #点击3D空白处，取消控制球
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1760, 194, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 254, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 374, dxf_name.split('.', 1)[0] + '放码7', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 404, dxf_name.split('.', 1)[0] + '放码8', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 434, dxf_name.split('.', 1)[0] + '放码9', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)
                auto.scroll(-300)
                self.style.test_click_grade(1760, 438, dxf_name.split('.', 1)[0] + '放码10', '\\DXF\\EditGrading\\10Size\\')
                time.sleep(2)

    @allure.story('11个码')
    def test_add_eleven(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '11Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                auto.click(x=1540, y=160, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 点击3D空白处，取消控制球
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1760, 194, dxf_name.split('.', 1)[0] + '放码1', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 224, dxf_name.split('.', 1)[0] + '放码2', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 254, dxf_name.split('.', 1)[0] + '放码3', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 284, dxf_name.split('.', 1)[0] + '放码4', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 314, dxf_name.split('.', 1)[0] + '放码5', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 344, dxf_name.split('.', 1)[0] + '放码6', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 374, dxf_name.split('.', 1)[0] + '放码7', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 404, dxf_name.split('.', 1)[0] + '放码8', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 434, dxf_name.split('.', 1)[0] + '放码9', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                auto.scroll(-300)
                self.style.test_click_grade(1760, 407, dxf_name.split('.', 1)[0] + '放码10', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 437, dxf_name.split('.', 1)[0] + '放码11', '\\DXF\\EditGrading\\11Size\\')
                time.sleep(2)

    @allure.story('12个码')
    def test_add_twelve(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '12Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                auto.click(x=1540, y=160, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击3D空白处，取消控制球
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1760, 194, dxf_name.split('.', 1)[0] + '放码1',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 224, dxf_name.split('.', 1)[0] + '放码2',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 254, dxf_name.split('.', 1)[0] + '放码3',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 284, dxf_name.split('.', 1)[0] + '放码4',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 314, dxf_name.split('.', 1)[0] + '放码5',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 344, dxf_name.split('.', 1)[0] + '放码6',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 374, dxf_name.split('.', 1)[0] + '放码7',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 404, dxf_name.split('.', 1)[0] + '放码8',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 434, dxf_name.split('.', 1)[0] + '放码9',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                auto.scroll(-300)
                self.style.test_click_grade(1760, 407, dxf_name.split('.', 1)[0] + '放码10',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 437, dxf_name.split('.', 1)[0] + '放码11',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 467, dxf_name.split('.', 1)[0] + '放码12',
                                            '\\DXF\\EditGrading\\12Size\\')
                time.sleep(2)

    @allure.story('13个码')
    def test_add_thirteen(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'EditGrading', '13Size')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            if os.path.splitext(dxf_name)[1] == '.dxf':
                self.style.click_new_project()
                self.style.click_import_dxf()
                dxf_path = import_path + '\\' + dxf_name
                pyperclip.copy(dxf_path)
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_1"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_3"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_4"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_10"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'],
                           y=conf["ImportDxfSubject"]["click_one_11"]['y'],
                           clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],
                           button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
                auto.click(x=1540, y=160, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击3D空白处，取消控制球
                time.sleep(6)
                self.style.click_cloth_textured_surface2d()
                auto.click(x=1675, y=101, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击场景-尺寸
                auto.click(x=1830, y=134, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击放码
                self.style.test_click_grade(1760, 194, dxf_name.split('.', 1)[0] + '放码1',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 224, dxf_name.split('.', 1)[0] + '放码2',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 254, dxf_name.split('.', 1)[0] + '放码3',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 284, dxf_name.split('.', 1)[0] + '放码4',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 314, dxf_name.split('.', 1)[0] + '放码5',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 344, dxf_name.split('.', 1)[0] + '放码6',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 374, dxf_name.split('.', 1)[0] + '放码7',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 404, dxf_name.split('.', 1)[0] + '放码8',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 434, dxf_name.split('.', 1)[0] + '放码9',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                auto.scroll(-300)
                self.style.test_click_grade(1760, 407, dxf_name.split('.', 1)[0] + '放码10',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 437, dxf_name.split('.', 1)[0] + '放码11',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 467, dxf_name.split('.', 1)[0] + '放码12',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)
                self.style.test_click_grade(1760, 497, dxf_name.split('.', 1)[0] + '放码13',
                                            '\\DXF\\EditGrading\\13Size\\')
                time.sleep(2)