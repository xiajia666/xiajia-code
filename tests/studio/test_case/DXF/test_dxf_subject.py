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
screen_width, screen_height = auto.size()


@allure.feature('导入dxf的bug集合')
@allure.severity(allure.severity_level.BLOCKER)
class TestDXFSubject:

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

    @allure.story('重置默认勾选项+自动排序导入dxf')
    def test_add_one(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'DefaultTick')
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
                time.sleep(4)
                self.style.click_cloth_textured_surface2d()
                # self.style.click_cloth_textured_surface3d()
                time.sleep(1)
                new = '\\DXF\\DefaultTick\\' + dxf_name.split('.', 1)[0] + '_new.png'
                old = '\\DXF\\DefaultTick\\' + dxf_name.split('.', 1)[0] + '_old.png'
                style = dxf_name.split('.', 1)[0] + '导入dxf'
                self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('勾选修正轮廓至内侧净边导入dxf')
    def test_add_two(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'ModifiedProfile')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            self.style.click_new_project()
            self.style.click_import_dxf()
            dxf_path = import_path + '\\' + dxf_name
            pyperclip.copy(dxf_path)
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'], y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'], y=conf["ImportDxfSubject"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'], y=conf["ImportDxfSubject"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_8"]['x'], y=conf["ImportDxfSubject"]["click_one_8"]['y'],clicks=conf["ImportDxfSubject"]["click_one_8"]['clicks'],button=conf["ImportDxfSubject"]["click_one_8"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'], y=conf["ImportDxfSubject"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
            time.sleep(3)
            self.style.click_cloth_textured_surface2d()
            # self.style.click_cloth_textured_surface3d()
            time.sleep(1)
            new = '\\DXF\\ModifiedProfile\\' + dxf_name.split('.', 1)[0] + '_new.png'
            old = '\\DXF\\ModifiedProfile\\' + dxf_name.split('.', 1)[0] + '_old.png'
            style = dxf_name.split('.', 1)[0] + '导入dxf'
            self.operationfile.comparison_picture_allure(new, old, style, 50)

    # @allure.story('勾选将基础线勾勒为内部线导入dxf，bug未解决')
    # def test_add_three(self):
    #     path = self.operationfile.get_garder_path('studio')
    #     import_path = os.path.join(path, 'dxf', 'TurnInternalLine')
    #     file_list = []
    #     for root, dirs, files in os.walk(import_path):
    #         file_list = files
    #     for dxf_name in file_list:
    #         self.style.click_new_project()
    #         self.style.click_import_dxf()
    #         dxf_path = import_path + '\\' + dxf_name
    #         pyperclip.copy(dxf_path)
    #         time.sleep(2)
    #         auto.hotkey('ctrl', 'v')
    #         time.sleep(2)
    #         auto.press('enter')
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'], y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'], y=conf["ImportDxfSubject"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'], y=conf["ImportDxfSubject"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_5"]['x'], y=conf["ImportDxfSubject"]["click_one_5"]['y'],clicks=conf["ImportDxfSubject"]["click_one_5"]['clicks'],button=conf["ImportDxfSubject"]["click_one_5"]['button'], duration=0.2)
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'], y=conf["ImportDxfSubject"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
    #         auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'], y=conf["ImportDxfSubject"]["click_one_11"]['y'], clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
    #         time.sleep(7)
    #         auto.click(x=33, y=136, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 2D打开面料纹理
    #         auto.click(x=822, y=249, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 3D打开面料纹理
    #         time.sleep(1)
    #         new = '\\DXF\\' + dxf_name.split('.', 1)[0] + '_new.png'
    #         old = '\\DXF\\' + dxf_name.split('.', 1)[0] + '_old.png'
    #         style = dxf_name.split('.', 1)[0] + '导入dxf'
    #         self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('重置默认勾选项，导入dxf点数过多')
    def test_add_four(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'AutomaticCutPoint')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            self.style.click_new_project()
            self.style.click_import_dxf()
            dxf_path = import_path + '\\' + dxf_name
            pyperclip.copy(dxf_path)
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'], y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'], y=conf["ImportDxfSubject"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'], y=conf["ImportDxfSubject"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'], y=conf["ImportDxfSubject"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
            auto.click(x=conf["ImportDxfSubject"]["click_one_11"]['x'], y=conf["ImportDxfSubject"]["click_one_11"]['y'],clicks=conf["ImportDxfSubject"]["click_one_11"]['clicks'],button=conf["ImportDxfSubject"]["click_one_11"]['button'], duration=0.2)
            time.sleep(7)
            self.style.click_cloth_textured_surface2d()
            # self.style.click_cloth_textured_surface3d()
            time.sleep(1)
            new = '\\DXF\\AutomaticCutPoint\\' + dxf_name.split('.', 1)[0] + '_new.png'
            old = '\\DXF\\AutomaticCutPoint\\' + dxf_name.split('.', 1)[0] + '_old.png'
            style = dxf_name.split('.', 1)[0] + '导入dxf'
            self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('重置默认勾选项，导入dxf查看注释')
    def test_add_five(self):
        path = self.operationfile.get_garder_path('studio')
        import_path = os.path.join(path, 'dxf', 'Annotation')
        file_list = []
        for root, dirs, files in os.walk(import_path):
            file_list = files
        for dxf_name in file_list:
            self.style.click_new_project()
            self.style.click_import_dxf()
            dxf_path = import_path + '\\' + dxf_name
            pyperclip.copy(dxf_path)
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            if str(screen_width) == '1920':
                auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'], y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_3"]['x'], y=conf["ImportDxfSubject"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_4"]['x'], y=conf["ImportDxfSubject"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject"]["click_one_10"]['x'], y=conf["ImportDxfSubject"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject"]["click_one_10"]['button'], duration=0.2)
            elif str(screen_width) == '2560':
                auto.click(x=conf["ImportDxfSubject2K"]["click_one_1"]['x'],y=conf["ImportDxfSubject2K"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject2K"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject2K"]["click_one_1"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject2K"]["click_one_3"]['x'],y=conf["ImportDxfSubject2K"]["click_one_3"]['y'],clicks=conf["ImportDxfSubject2K"]["click_one_3"]['clicks'],button=conf["ImportDxfSubject2K"]["click_one_3"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject2K"]["click_one_4"]['x'],y=conf["ImportDxfSubject2K"]["click_one_4"]['y'],clicks=conf["ImportDxfSubject2K"]["click_one_4"]['clicks'],button=conf["ImportDxfSubject2K"]["click_one_4"]['button'], duration=0.2)
                auto.click(x=conf["ImportDxfSubject2K"]["click_one_10"]['x'],y=conf["ImportDxfSubject2K"]["click_one_10"]['y'],clicks=conf["ImportDxfSubject2K"]["click_one_10"]['clicks'],button=conf["ImportDxfSubject2K"]["click_one_10"]['button'], duration=0.2)
            time.sleep(2)
            self.style.click_cloth_textured_surface2d()
            # self.style.click_cloth_textured_surface3d()
            time.sleep(1)
            self.style.click_addannotation()
            time.sleep(1)
            new = '\\DXF\\Annotation\\' + dxf_name.split('.', 1)[0] + '_new.png'
            old = '\\DXF\\Annotation\\' + dxf_name.split('.', 1)[0] + '_old.png'
            style = dxf_name.split('.', 1)[0] + '导入dxf'
            self.operationfile.comparison_picture_allure(new, old, style, 50)