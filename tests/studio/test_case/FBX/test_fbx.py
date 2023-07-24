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
screen_width, screen_height = auto.size()

@allure.feature('fbx导入导出')
@allure.severity(allure.severity_level.CRITICAL)
class TestFBX():

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


    @allure.story('工程导出fbx后导入')
    def test_add_one(self):
        self.operationfile.delete_file_style('export_fbx.fbx')
        self.style.add_open_sproj('sproj', 'export.sproj')
        self.style.click_export_fbx()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'export_fbx.fbx'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(5)
        style = 'fbx导出界面查看'
        new = '\\FBX\\' + style + '_new.png'
        old = '\\FBX\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        if str(screen_width) == '1920':
            auto.click(x=1100, y=818, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #导出fbx，点击重置
            time.sleep(2)
            auto.click(x=1186, y=818, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #导出fbx，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=863, y=1169, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
            auto.click(x=1607, y=1169, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(7)
        self.style.click_new_project()
        self.style.click_import_fbx()
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        if str(screen_width) == '1920':
            auto.click(x=845, y=828, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #导入fbx，点击重置
            auto.click(x=994, y=828, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #导入fbx，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=787, y=828, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
            auto.click(x=1414, y=1096, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(5)
        style = 'FBX导入查看'
        new = '\\FBX\\' + style + '_new.png'
        old = '\\FBX\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

    @allure.story('模特导出带骨骼的fbx后导入')
    def test_add_two(self):
        self.operationfile.delete_file_style('savt_fbx.fbx')
        self.style.add_avatar('Female.savt')
        style = '模特fbx导出界面查看'
        new = '\\FBX\\' + style + '_new.png'
        old = '\\FBX\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)
        self.style.click_export_fbx()
        export_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'savt_fbx.fbx'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        if str(screen_width) == '1920':
            auto.click(x=1100, y=828, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 导出fbx，点击重置
            time.sleep(2)
            auto.click(x=1087, y=535, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 导出fbx，勾选导出骨骼
            auto.click(x=1186, y=828, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 导出fbx，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=638, y=885, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
            auto.click(x=1052, y=583, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
            auto.click(x=1607, y=1168, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(7)
        self.style.click_import_fbx()
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        if str(screen_width) == '1920':
            auto.click(x=845, y=828, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 导入fbx，点击重置
            auto.click(x=994, y=828, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 导入fbx，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=787, y=828, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
            auto.click(x=1414, y=1096, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(20)
        auto.click(x=820, y=162, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #3D显示骨骼
        time.sleep(2)
        style = '模特带骨骼FBX导入查看'
        new = '\\FBX\\' + style + '_new.png'
        old = '\\FBX\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)