# -*- coding: utf-8 -*-
import os
import sys

import pyperclip

sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('动画')
@allure.severity(allure.severity_level.CRITICAL)
class TestAnimationRender:

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

    def test_check_window(self): #避免Jenkins调起第一次启动可能有bug
        self.style.rectangle_creat()

    def test_check_window_again(self): #避免Jenkins调起第一次启动可能有bug
        self.style.rectangle_creat()

    def test_get_version(self):
        self.style.send_message("Style3D bug专项测试开始，本次测试版本号：", "18069806966", "15757119427", "18066268343")

    @allure.story('动画可以多段录制')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/a145aaa11ddc0a56dc021c197e', name='STUDIO-6393')
    def test_animationrender_one(self):
        self.style.rectangle_creat()
        self.style.click_animation_editor()
        auto.click(x=594, y=744, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击录制
        time.sleep(3)
        auto.click(x=594, y=744, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #停止录制
        auto.click(x=594, y=744, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 再次录制
        time.sleep(2)
        auto.click(x=594, y=744, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #停止录制
        time.sleep(1)
        style = "STUDIO-6393，动画可以多段录制"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


    @allure.story('男模特增加T动作和T动作的关键帧，动画帧率切换到24后，再次切换到30，播放动画，关键帧效果抖动严重')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/1c7bebaf35228ee29f7c8a0663', name='STUDIO-7574')
    def test_animationrender_two(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7574，动画抖动.sproj')
        self.style.click_animation_editor()
        auto.click(x=1684, y=742, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击动画属性
        time.sleep(1)
        auto.click(x=1762, y=624, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击动画帧率
        auto.click(x=1763, y=649, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击切换动画帧率24
        auto.click(x=1762, y=624, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击动画帧率
        auto.click(x=1763, y=688, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击切换动画帧率30
        time.sleep(2)
        auto.click(x=787, y=740, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击跳到最后
        time.sleep(2)
        style = "STUDIO-7574，动画抖动"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('素材库男模特，添加T动作或者I动作，初始位置不正确')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/09a5b2f38b90a15196af0fbe49', name='STUDIO-6538')
    def test_animationrender_three(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6538，素材库男模特，添加T动作或者I动作，初始位置不正确.sproj')
        self.style.click_animation_editor()
        auto.click(x=118, y=798, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击动作
        time.sleep(1)
        auto.click(x=142, y=826, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击添加T动作
        time.sleep(1)
        auto.click(x=990, y=591, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
        time.sleep(2)
        style = "STUDIO-6538，素材库男模特，添加T动作或者I动作，初始位置不正确"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('多齐色工程，动画添加齐色关键帧，明线纽扣等素材，在3D的预览效果跟齐色匹配不上，录制动画后导出是正常的')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/844fff496f89d47b0a23f162d0', name='STUDIO-5276')
    def test_animationrender_four(self):
        self.style.add_open_sproj('sproj', 'STUDIO-5276，动画.sproj')
        self.style.click_animation_editor()
        auto.click(x=1039, y=771, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击齐色1的位置
        time.sleep(1)
        style = "STUDIO-5276，齐色1的图片"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)
        auto.click(x=1151, y=844, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击齐色2的位置
        time.sleep(1)
        style = "STUDIO-5276，齐色2的图片"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    # @allure.story('abc导入作为模特，固定针固定到模特后，录制动画，固定针还是再原来位置，应固定到模特')
    # @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/844fff496f89d47b0a23f162d0', name='STUDIO-4286')
    # def test_animationrender_five(self):
    #     self.style.add_open_sproj('sproj', 'STUDIO-4286，固定针固定到模特调试.sproj')
    #     self.style.click_animation_editor()
    #     auto.click(x=1039, y=771, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击齐色1的位置
    #     time.sleep(1)
    #     style = "STUDIO-5276，齐色1的图片"
    #     new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
    #     old = "\\RunBug\\AnimationRender\\"+style+"_new.png"
    #     self.operationfile.comparison_picture_allure(new, old, style, 50)
    #     auto.click(x=1151, y=844, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击齐色2的位置
    #     time.sleep(1)
    #     style = "STUDIO-5276，齐色2的图片"
    #     new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
    #     old = "\\RunBug\\AnimationRender\\"+style+"_new.png"
    #     self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('项目abc，导入软件后，最后一帧没有动画')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/11cced7cf4c0e43beb9d0ee25b', name='STUDIO-301')
    def test_animationrender_six(self):
        self.style.click_import_alembic()
        abc_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj') + '\\' + 'CJJ140_anim_v005.abc'
        pyperclip.copy(abc_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(1)
        auto.click(x=809, y=618, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击abc栏重置
        auto.click(x=798, y=566, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击自动调整比例
        auto.click(x=1036, y=614, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击确定
        time.sleep(15)
        self.style.click_animation_editor()
        auto.click(x=128, y=795, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击添加动画
        auto.click(x=128, y=795, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击添加动画
        auto.click(x=788, y=742, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击最后一帧
        time.sleep(2)
        style = "STUDIO-301，项目abc，导入软件后，最后一帧没有动画"
        new = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        old = "\\RunBug\\AnimationRender\\"+style+"_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)