import json
import os,sys
import requests
import yaml
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
auto.FAILSAFE = False
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud
import allure
import pytest
import logging
import glob
import autoit


@allure.feature('工程打开保存')
@allure.severity(allure.severity_level.BLOCKER)
class TestOpenAndSave:

    def setup_method(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()
    def teardown_method(self):

        self.log.info("测试结束")
        self.style.close_style3D()

    # @allure.story('工程打开保存')
    # def test_open_and_save(self):
    #     file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
    #     sproj_len = self.operationfile.get_file_name(file_path)[0]
    #     self.log.info(sproj_len)
    #     length = len(sproj_len)
    #     for i in range(1, length+1):
    #         sproj_name = sproj_len[i - 1]
    #         self.log.info(sproj_name)
    #         if sproj_name.endswith('.sproj'):
    #             self.log.info('执行打开')
    #             self.style.start_style3D()
    #             sproj_path  = file_path + "\\" + sproj_name
    #             print(sproj_path)
    #             pyperclip.copy(sproj_path)
    #             auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 打开保存机制修改，适配脚本
    #             auto.click(x=60, y=9, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
    #             auto.click(x=89, y=66, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
    #             auto.click(x=229, y=68, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
    #             auto.click(x=1012, y=596, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
    #             time.sleep(2)
    #             auto.hotkey('ctrl', 'v')
    #             time.sleep(2)
    #             auto.press('enter')
    #             time.sleep(2)
    #             auto.click(x=987, y=671, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) # 点击确定
    #             for i in range(60):
    #                 style = "工程打开确定"
    #                 new = "\\OpenAndSave\\"+style+"_new.png"
    #                 old = "\\OpenAndSave\\"+style+"_old.png"
    #                 difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
    #                 self.log.info("%s打开图片有差别" % difference)
    #                 if difference < 1:
    #                     self.log.info('工程打开成功')
    #                     break
    #                 else:
    #                     self.log.info('等待工程打开')
    #                     time.sleep(3)
    #             time.sleep(2)
    #             auto.click(x=808, y=574, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击3D界面触发保存
    #             time.sleep(1)
    #             auto.hotkey('ctrl', 's') # 保存工程
    #             for i in range(60):
    #                 style = "保存成功对比"
    #                 new = "\\OpenAndSave\\"+style+"_new.png"
    #                 old = "\\OpenAndSave\\"+style+"_old.png"
    #                 difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
    #                 self.log.info("%s保存图片有差别" % difference)
    #                 if difference < 1:
    #                     self.log.info('工程保存成功')
    #                     self.style.close_style3D()
    #                     break
    #                 else:
    #                     self.log.info('等待工程保存')
    #                     time.sleep(3)
    #         else:
    #             self.log.info('非sproj工程不做处理')
    #

    def run_common(self):
        auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 打开保存机制修改，适配脚本
        auto.click(x=60, y=9, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
        auto.click(x=89, y=66, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
        auto.click(x=229, y=68, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
        auto.click(x=1012, y=596, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=987, y=671, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
        for i in range(100):
            style = "工程打开确定"
            new = "\\OpenAndSave\\" + style + "_new.png"
            old = "\\OpenAndSave\\" + style + "_old.png"
            difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
            self.log.info("%s打开图片有差别" % difference)
            if difference < 1:
                self.log.info('工程打开成功')
                break
            else:
                self.log.info('等待工程打开')
                time.sleep(3)
        time.sleep(2)
        auto.click(x=808, y=574, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击3D界面触发保存
        time.sleep(1)
        auto.hotkey('ctrl', 's')  # 保存工程
        for i in range(100):
            style = "保存成功对比"
            new = "\\OpenAndSave\\" + style + "_new.png"
            old = "\\OpenAndSave\\" + style + "_old.png"
            difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
            self.log.info("%s保存图片有差别" % difference)
            if difference < 1:
                self.log.info('工程保存成功')
                break
            else:
                self.log.info('等待工程保存')
                time.sleep(3)
    @allure.story('工程1打开保存')
    def test_open_and_save_1(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test1.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程2打开保存')
    def test_open_and_save_2(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test2.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程3打开保存')
    def test_open_and_save_3(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test3.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程4打开保存')
    def test_open_and_save_4(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test4.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程5打开保存')
    def test_open_and_save_5(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test5.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程6打开保存')
    def test_open_and_save_6(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test6.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程7打开保存')
    def test_open_and_save_7(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test7.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程8打开保存')
    def test_open_and_save_8(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test8.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程9打开保存')
    def test_open_and_save_9(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test9.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程10打开保存')
    def test_open_and_save_10(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test10.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程11打开保存')
    def test_open_and_save_11(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test11.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程12打开保存')
    def test_open_and_save_12(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test12.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程13打开保存')
    def test_open_and_save_13(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test13.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程14打开保存')
    def test_open_and_save_14(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test14.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程15打开保存')
    def test_open_and_save_15(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test15.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程16打开保存')
    def test_open_and_save_16(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test16.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程17打开保存')
    def test_open_and_save_17(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test17.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程18打开保存')
    def test_open_and_save_18(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test18.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程19打开保存')
    def test_open_and_save_19(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test19.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程20打开保存')
    def test_open_and_save_20(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test20.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程21打开保存')
    def test_open_and_save_21(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test21.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程22打开保存')
    def test_open_and_save_22(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test22.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程23打开保存')
    def test_open_and_save_23(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test23.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程24打开保存')
    def test_open_and_save_24(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test24.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程25打开保存')
    def test_open_and_save_25(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test25.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程26打开保存')
    def test_open_and_save_26(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test26.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程27打开保存')
    def test_open_and_save_27(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test27.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程28打开保存')
    def test_open_and_save_28(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test28.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程29打开保存')
    def test_open_and_save_29(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test29.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()

    @allure.story('工程30打开保存')
    def test_open_and_save_30(self):
        file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'SaveProject')
        sproj_path= file_path + "\\" + "Studio_Test30.sproj"
        self.log.info(sproj_path)
        pyperclip.copy(sproj_path)
        self.run_common()