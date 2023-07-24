import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
import allure
import pytest
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud


# @pytest.mark.skip
@allure.feature('动画编辑器')
@allure.severity(allure.severity_level.CRITICAL)
class Test_AnimationRender:

    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info("测试结束")
        self.style.close_style3D()


    @allure.story('导出mp4 vary动画')
    def test_exprot_vary(self):
        self.operationfile.delete_file_style('vary_mp4.mp4')
        self.style.add_open_sproj('sproj', 'test_animation.sproj')
        self.style.click_animation_editor()
        auto.click(x=conf["AnimationRender"]["export_video"]['x'], y=conf["AnimationRender"]["export_video"]['y'],clicks=conf["AnimationRender"]["export_video"]['clicks'],button=conf["AnimationRender"]["export_video"]['button'], duration=0.2)
        auto.click(x=conf["AnimationRender"]["local_render"]['x'], y=conf["AnimationRender"]["local_render"]['y'],clicks=conf["AnimationRender"]["local_render"]['clicks'],button=conf["AnimationRender"]["local_render"]['button'], duration=0.2)
        animation_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'vary_mp4.mp4'
        pyperclip.copy(animation_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        self.cloud.assert_animation_render(animation_path)
        auto.click(x=conf["AnimationRender"]["click_enter"]['x'], y=conf["AnimationRender"]["click_enter"]['y'],clicks=conf["AnimationRender"]["click_enter"]['clicks'],button=conf["AnimationRender"]["click_enter"]['button'], duration=0.2)

    @allure.story('导出普通mp4 动画')
    def test_exprot_normal_mp4(self):
        self.operationfile.delete_file_style('normal_mp4.mp4')
        self.style.add_open_sproj('sproj', 'test_animation.sproj')
        self.style.click_animation_editor()
        auto.click(x=conf["AnimationRender"]["export_video"]['x'], y=conf["AnimationRender"]["export_video"]['y'],clicks=conf["AnimationRender"]["export_video"]['clicks'],button=conf["AnimationRender"]["export_video"]['button'], duration=0.2)
        auto.click(x=conf["AnimationRender"]["save"]['x'], y=conf["AnimationRender"]["save"]['y'],clicks=conf["AnimationRender"]["save"]['clicks'],button=conf["AnimationRender"]["save"]['button'], duration=0.2)
        animation_path = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'normal_mp4.mp4'
        pyperclip.copy(animation_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        self.cloud.assert_animation_render(animation_path)
        auto.click(x=conf["AnimationRender"]["click_enter"]['x'], y=conf["AnimationRender"]["click_enter"]['y'],clicks=conf["AnimationRender"]["click_enter"]['clicks'],button=conf["AnimationRender"]["click_enter"]['button'], duration=0.2)

