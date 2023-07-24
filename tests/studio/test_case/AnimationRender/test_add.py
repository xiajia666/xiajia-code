import os
import sys
sys.path.append('../../../../all')
import pyperclip
import allure
import pytest
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud


# @pytest.mark.skip
@allure.feature('动画编辑器增加')
@allure.severity(allure.severity_level.CRITICAL)
class Test_AnimationRender:

    def setup_class(self):
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

    def teardown_class(self):
        self.log.info("测试结束")
        self.style.close_style3D()

    @allure.story('添加动作')
    def test_add_one(self):
        self.style.add_library_female_avatar()
        # self.style.add_library_female_garment()
        self.style.add_tshirt('Female_T-Shirt')
        self.style.click_animation_editor()
        auto.click(x=conf["AnimationRender"]["add_one_1"]['x'], y=conf["AnimationRender"]["add_one_1"]['y'],clicks=conf["AnimationRender"]["add_one_1"]['clicks'],button=conf["AnimationRender"]["add_one_1"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["AnimationRender"]["add_one_2"]['x'], y=conf["AnimationRender"]["add_one_2"]['y'],clicks=conf["AnimationRender"]["add_one_2"]['clicks'],button=conf["AnimationRender"]["add_one_2"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["AnimationRender"]["add_one_3"]['x'], y=conf["AnimationRender"]["add_one_3"]['y'],clicks=conf["AnimationRender"]["add_one_3"]['clicks'],button=conf["AnimationRender"]["add_one_3"]['button'], duration=0.2)
        time.sleep(1)
        style = '添加平底鞋走秀I'
        new = '\\AnimationRender\\'+style+'_new.png'
        old = '\\AnimationRender\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["AnimationRender"]["add_one_4"]['x'], y=conf["AnimationRender"]["add_one_4"]['y'],clicks=conf["AnimationRender"]["add_one_4"]['clicks'],button=conf["AnimationRender"]["add_one_4"]['button'], duration=0.2)
        time.sleep(2)
        style = '点击动画栏查看动作'
        new = '\\AnimationRender\\'+style+'_new.png'
        old = '\\AnimationRender\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["AnimationRender"]["go_to_start"]['x'], y=conf["AnimationRender"]["go_to_start"]['y'],clicks=conf["AnimationRender"]["go_to_start"]['clicks'],button=conf["AnimationRender"]["go_to_start"]['button'], duration=0.2)


    @allure.story('点击录制')
    def test_add_two(self):
        auto.click(x=conf["AnimationRender"]["animation_property"]['x'], y=conf["AnimationRender"]["animation_property"]['y'],clicks=conf["AnimationRender"]["animation_property"]['clicks'],button=conf["AnimationRender"]["animation_property"]['button'], duration=0.2)
        auto.click(x=conf["AnimationRender"]["add_two_1"]['x'], y=conf["AnimationRender"]["add_two_1"]['y'],clicks=conf["AnimationRender"]["add_two_1"]['clicks'],button=conf["AnimationRender"]["add_two_1"]['button'], duration=0.2)
        self.style.scroll_big_number(2)
        auto.click(x=conf["AnimationRender"]["add_two_2"]['x'], y=conf["AnimationRender"]["add_two_2"]['y'],clicks=conf["AnimationRender"]["add_two_2"]['clicks'],button=conf["AnimationRender"]["add_two_2"]['button'], duration=0.2)
        auto.press('2')
        auto.click(x=conf["AnimationRender"]["record"]['x'], y=conf["AnimationRender"]["record"]['y'],clicks=conf["AnimationRender"]["record"]['clicks'],button=conf["AnimationRender"]["record"]['button'], duration=0.2)
        time.sleep(60)
        style = '录制2s动画查看'
        new = '\\AnimationRender\\'+style+'_new.png'
        old = '\\AnimationRender\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)


