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


@allure.feature('OBJ添加方式：打开')
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

    @allure.story('obj导出后导入')
    def test_open_one(self):
        self.operationfile.delete_file_style('export_obj.zip')
        self.style.add_open_sproj('sproj', 'export.sproj')
        self.style.click_export_obj()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj.zip'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(5)
        style = 'OBJ导出界面查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["OBJ"]["open_one_1"]['x'], y=conf["OBJ"]["open_one_1"]['y'], clicks=conf["OBJ"]["open_one_1"]['clicks'], button=conf["OBJ"]["open_one_1"]['button'], duration=0.2)
        time.sleep(5)
        auto.click(x=conf["OBJ"]["open_choose_zip"]['x'], y=conf["OBJ"]["open_choose_zip"]['y'],clicks=conf["OBJ"]["open_choose_zip"]['clicks'], button=conf["OBJ"]["open_choose_zip"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_one_2"]['x'], y=conf["OBJ"]["open_one_2"]['y'],clicks=conf["OBJ"]["open_one_2"]['clicks'], button=conf["OBJ"]["open_one_2"]['button'], duration=0.2)
        time.sleep(5)
        self.style.click_new_project()
        self.style.click_import_obj()
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_one_3"]['x'], y=conf["OBJ"]["open_one_3"]['y'],clicks=conf["OBJ"]["open_one_3"]['clicks'],button=conf["OBJ"]["open_one_3"]['button'], duration=0.2)
        time.sleep(5)
        style = 'OBJ导入查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["OBJ"]["open_one_4"]['x'], y=conf["OBJ"]["open_one_4"]['y'],clicks=conf["OBJ"]["open_one_4"]['clicks'], button=conf["OBJ"]["open_one_4"]['button'], duration=0.2)
        auto.press('delete')

    @allure.story('obj导入后作为附件')
    def test_open_two(self):
        self.style.click_import_obj()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj.zip'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_two_1"]['x'], y=conf["OBJ"]["open_two_1"]['y'],clicks=conf["OBJ"]["open_two_1"]['clicks'], button=conf["OBJ"]["open_two_1"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_two_2"]['x'], y=conf["OBJ"]["open_two_2"]['y'],clicks=conf["OBJ"]["open_two_2"]['clicks'], button=conf["OBJ"]["open_two_2"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_two_3"]['x'], y=conf["OBJ"]["open_two_3"]['y'],clicks=conf["OBJ"]["open_two_3"]['clicks'], button=conf["OBJ"]["open_two_3"]['button'], duration=0.2)
        time.sleep(5)
        style = 'OBJ导入为附件查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
        time.sleep(2)

    @allure.story('obj导入后作为道具')
    def test_open_three(self):
        self.style.click_import_obj()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj.zip'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_three_1"]['x'], y=conf["OBJ"]["open_three_1"]['y'],clicks=conf["OBJ"]["open_three_1"]['clicks'], button=conf["OBJ"]["open_three_1"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_three_2"]['x'], y=conf["OBJ"]["open_three_2"]['y'],clicks=conf["OBJ"]["open_three_2"]['clicks'], button=conf["OBJ"]["open_three_2"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_three_3"]['x'], y=conf["OBJ"]["open_three_3"]['y'],clicks=conf["OBJ"]["open_three_3"]['clicks'], button=conf["OBJ"]["open_three_3"]['button'], duration=0.2)
        time.sleep(5)
        style = 'OBJ导入为道具查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')
        time.sleep(2)

    @allure.story('obj导入后作为服装')
    def test_open_four(self):
        self.style.click_import_obj()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj.zip'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_four_1"]['x'], y=conf["OBJ"]["open_four_1"]['y'],clicks=conf["OBJ"]["open_four_1"]['clicks'], button=conf["OBJ"]["open_four_1"]['button'],duration=0.2)
        auto.click(x=conf["OBJ"]["open_four_2"]['x'], y=conf["OBJ"]["open_four_2"]['y'],clicks=conf["OBJ"]["open_four_2"]['clicks'], button=conf["OBJ"]["open_four_2"]['button'],duration=0.2)
        # auto.click(x=conf["OBJ"]["open_four_3"]['x'], y=conf["OBJ"]["open_four_3"]['y'],clicks=conf["OBJ"]["open_four_3"]['clicks'], button=conf["OBJ"]["open_four_3"]['button'],duration=0.2)
        auto.click(x=conf["OBJ"]["open_four_4"]['x'], y=conf["OBJ"]["open_four_4"]['y'],clicks=conf["OBJ"]["open_four_4"]['clicks'], button=conf["OBJ"]["open_four_4"]['button'],duration=0.2)
        time.sleep(15)
        auto.click(x=conf["OBJ"]["open_four_5"]['x'], y=conf["OBJ"]["open_four_5"]['y'],clicks=conf["OBJ"]["open_four_5"]['clicks'], button=conf["OBJ"]["open_four_5"]['button'], duration=0.2)
        time.sleep(2)
        style = 'OBJ导入为服装查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)


    @allure.story('obj导入后,"在uv图中勾勒2D版片",作为服装')
    def test_open_five(self):
        self.style.click_import_obj()
        time.sleep(2)
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj.zip'
        print(export_path)
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_four_1"]['x'], y=conf["OBJ"]["open_four_1"]['y'],clicks=conf["OBJ"]["open_four_1"]['clicks'], button=conf["OBJ"]["open_four_1"]['button'],duration=0.2)
        auto.click(x=conf["OBJ"]["open_four_2"]['x'], y=conf["OBJ"]["open_four_2"]['y'],clicks=conf["OBJ"]["open_four_2"]['clicks'], button=conf["OBJ"]["open_four_2"]['button'],duration=0.2)
        auto.click(x=conf["OBJ"]["open_four_3"]['x'], y=conf["OBJ"]["open_four_3"]['y'],clicks=conf["OBJ"]["open_four_3"]['clicks'], button=conf["OBJ"]["open_four_3"]['button'],duration=0.2)
        auto.click(x=conf["OBJ"]["open_four_4"]['x'], y=conf["OBJ"]["open_four_4"]['y'],clicks=conf["OBJ"]["open_four_4"]['clicks'], button=conf["OBJ"]["open_four_4"]['button'],duration=0.2)
        time.sleep(15)
        auto.click(x=conf["OBJ"]["open_four_5"]['x'], y=conf["OBJ"]["open_four_5"]['y'],clicks=conf["OBJ"]["open_four_5"]['clicks'], button=conf["OBJ"]["open_four_5"]['button'], duration=0.2)
        time.sleep(2)
        style = '在uv图中勾勒2D版片'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)


    @allure.story('导出obj时，勾统一uv，烘焙纹理')
    def test_open_six(self):
        self.operationfile.delete_file_style('export_obj_uv.zip')
        self.style.add_open_sproj('sproj', 'export_backing.sproj')
        self.style.click_export_obj()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_obj_uv.zip'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(5)
        auto.click(x=conf["OBJ"]["open_six_1"]['x'], y=conf["OBJ"]["open_six_1"]['y'], clicks=conf["OBJ"]["open_six_1"]['clicks'], button=conf["OBJ"]["open_six_1"]['button'], duration=0.2)
        time.sleep(5)
        auto.click(x=conf["OBJ"]["open_choose_zip"]['x'], y=conf["OBJ"]["open_choose_zip"]['y'],clicks=conf["OBJ"]["open_choose_zip"]['clicks'], button=conf["OBJ"]["open_choose_zip"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_2"]['x'], y=conf["OBJ"]["open_six_2"]['y'],clicks=conf["OBJ"]["open_six_2"]['clicks'], button=conf["OBJ"]["open_six_2"]['button'], duration=0.2)
        time.sleep(2)
        auto.mouseDown(x=conf["OBJ"]["open_drag_1"]['x'], y=conf["OBJ"]["open_drag_1"]['y'], button=conf["OBJ"]["open_drag_1"]['button'], duration=0.2)
        auto.moveTo(x=conf["OBJ"]["open_move_1"]['x'], y=conf["OBJ"]["open_move_1"]['y'], duration=0.0, tween=auto.linear)
        auto.mouseUp(x=conf["OBJ"]["open_drag_2"]['x'], y=conf["OBJ"]["open_drag_2"]['y'], button=conf["OBJ"]["open_drag_2"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_3"]['x'], y=conf["OBJ"]["open_six_3"]['y'],clicks=conf["OBJ"]["open_six_3"]['clicks'], button=conf["OBJ"]["open_six_3"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_4"]['x'], y=conf["OBJ"]["open_six_4"]['y'],clicks=conf["OBJ"]["open_six_4"]['clicks'], button=conf["OBJ"]["open_six_4"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_5"]['x'], y=conf["OBJ"]["open_six_5"]['y'],clicks=conf["OBJ"]["open_six_5"]['clicks'], button=conf["OBJ"]["open_six_5"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_6"]['x'], y=conf["OBJ"]["open_six_6"]['y'],clicks=conf["OBJ"]["open_six_6"]['clicks'], button=conf["OBJ"]["open_six_6"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_7"]['x'], y=conf["OBJ"]["open_six_7"]['y'],clicks=conf["OBJ"]["open_six_7"]['clicks'], button=conf["OBJ"]["open_six_7"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_8"]['x'], y=conf["OBJ"]["open_six_8"]['y'],clicks=conf["OBJ"]["open_six_8"]['clicks'], button=conf["OBJ"]["open_six_8"]['button'], duration=0.2)
        auto.click(x=conf["OBJ"]["open_six_9"]['x'], y=conf["OBJ"]["open_six_9"]['y'],clicks=conf["OBJ"]["open_six_9"]['clicks'], button=conf["OBJ"]["open_six_9"]['button'], duration=0.2)
        time.sleep(35)
        self.style.click_new_project()
        self.style.click_import_obj()
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        auto.click(x=conf["OBJ"]["open_six_10"]['x'], y=conf["OBJ"]["open_six_10"]['y'],clicks=conf["OBJ"]["open_six_10"]['clicks'],button=conf["OBJ"]["open_six_10"]['button'], duration=0.2)
        time.sleep(45)
        # self.style.click_depth_peeling()
        style = 'OBJ勾统一uv，烘焙纹理导入查看'
        new = '\\OBJ\\' + style + '_new.png'
        old = '\\OBJ\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
