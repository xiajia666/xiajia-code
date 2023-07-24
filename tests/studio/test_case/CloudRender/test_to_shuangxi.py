import json
import os,sys
import requests
import yaml
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
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

with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())
with open('../../../config/studio_config.yaml', encoding='utf-8') as yaml_file:
    conf_config = yaml.safe_load(yaml_file.read())

@pytest.mark.skip
@allure.feature('平台云渲染对比')
@allure.severity(allure.severity_level.BLOCKER)
class TestToShuangXi:

    def setup_class(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        self.operationfile.keep_window()
        self.style.start_style3D()
    def teardown_class(self):

        self.log.info("测试结束")
        self.style.close_style3D()

    @allure.story('所有图片查看')
    def test_add_one(self):
        # self.operationfile.del_file('C:\\Users\\12540\\Desktop\\test') #一开始删除文件夹中图片，注意是否要删除
        sproj_path = 'C:\\Users\\12540\\Desktop\\双喜-批量模拟\\Fabric_prefer.sproj' #工程的位置
        pyperclip.copy(sproj_path)
        auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,
                   tween=auto.linear)  # 打开保存机制修改，适配脚本
        auto.click(x=122, y=16, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击开始
        auto.click(x=60, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
        auto.click(x=68, y=115, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
        auto.click(x=220, y=115, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
        auto.click(x=1012, y=596, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=987, y=680, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(9)
        file_path = "C:\\Users\\12540\\Desktop\\双喜-批量模拟\\面料文件" #面料的位置
        sfab_len = self.operationfile.get_file_name(file_path)[0]
        print(sfab_len)
        length = len(sfab_len)
        print(length)
        self.style.click_photo_rendering()
        auto.click(x=560, y=163, clicks=1, button='left', duration=0.2)  # 点击离线渲染的图片属性
        auto.click(x=1897, y=605, clicks=1, button='left', duration=0.2)  # 点击修改文件夹保存路径
        time.sleep(2)
        photo_file_save = 'C:\\Users\\12540\\Desktop\\test' #面料保存的位置
        pyperclip.copy(photo_file_save)
        auto.hotkey('ctrl', 'v')
        auto.press('enter')
        time.sleep(4)
        autoit.control_click("选择", "Button1")
        time.sleep(2)
        for i in range(1, length+1):
            fabric_name = sfab_len[i-1]
            print(fabric_name)
            auto.click(x=28, y=252, clicks=1, button='left', duration=0.2)#点击场景管理织物
            time.sleep(5)
            auto.click(x=1830, y=163, clicks=1, button='left', duration=0.2)#点击打开织物
            time.sleep(4)
            fabric_path  = file_path +"\\" +fabric_name
            print(fabric_path)
            pyperclip.copy(fabric_path)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            time.sleep(3)
            self.style.click_normal_similate()
            time.sleep(8)
            self.style.click_normal_similate()
            auto.click(x=560, y=163, clicks=1, button='left', duration=0.2)  # 点击离线渲染的图片属性
            auto.click(x=1880, y=574, clicks=1, button='left', duration=0.2)  # 点击修改名字
            fabric_name_photo = fabric_name[:-5]
            print(fabric_name_photo)
            pyperclip.copy(fabric_name_photo)
            auto.hotkey('ctrl', 'v')
            auto.press('enter')
            auto.click(x=430, y=162, clicks=1, button='left', duration=0.2)  # 点击最终渲染
            fabric_photo_path = photo_file_save +  '\\' + fabric_name_photo + '.png'
            print(fabric_photo_path)
            self.cloud.assert_render_picture_minute(fabric_photo_path, 30)
            self.log.info('渲染成功过')
            time.sleep(2)
            auto.click(x=1080, y=570, clicks=1, button='left', duration=0.2)  # 点击关闭完成弹框

    @allure.story('快照保存循环出图')
    def test_two_one(self):
        sproj_path = 'C:\\Users\\12540\\Desktop\\双喜-批量模拟\\Fabric_prefer.sproj' #工程的位置
        pyperclip.copy(sproj_path)
        auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,
                   tween=auto.linear)  # 打开保存机制修改，适配脚本
        auto.click(x=60, y=12, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
        auto.click(x=89, y=70, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
        auto.click(x=224, y=69, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
        auto.click(x=992, y=681, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=987, y=680, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击确定
        time.sleep(9)
        auto.click(x=1658, y=274, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击织物
        time.sleep(2)
        file_path = "C:\\Users\\12540\\Desktop\\双喜-批量模拟\\面料文件" #面料的位置
        sfab_len = self.operationfile.get_file_name(file_path)[0]
        print(sfab_len)
        length = len(sfab_len)
        print(length)
        for i in range(1, length+1):
            fabric_name = sfab_len[i-1]
            print(fabric_name)
            fabric_path  = file_path + "\\" + fabric_name
            print(fabric_path)
            pyperclip.copy(fabric_path)
            auto.click(x=16, y=480, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开织物
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            time.sleep(3)
            auto.press('space')
            time.sleep(60)
            auto.press('space')
            time.sleep(2)
            self.style.click_snapshot_3d()
            time.sleep(3)
            fabric_name_photo = fabric_name[:-5]
            snapshot_file_save_path = 'C:\\Users\\12540\\Desktop\\CLO预设-sfab保存' + "\\" + fabric_name_photo + '.png'  # 3D快照保存位置
            print(snapshot_file_save_path)
            pyperclip.copy(snapshot_file_save_path)
            auto.click(x=1100, y=1016, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击直接保存
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            time.sleep(3)
            self.cloud.assert_render_picture_minute(snapshot_file_save_path, 30)
            time.sleep(6)
            auto.click(x=1060, y=583, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击关闭弹框
            auto.click(x=1362, y=294, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击关闭3D快照

    def test_three_one(self):
        sproj_path = 'C:\\Users\\12540\\Desktop\\桌面\\双喜-批量模拟\\Fabric_prefer.sproj'  # 工程的位置
        pyperclip.copy(sproj_path)
        auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,
                   tween=auto.linear)  # 打开保存机制修改，适配脚本
        auto.click(x=60, y=12, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
        auto.click(x=89, y=70, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
        auto.click(x=224, y=69, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
        auto.click(x=992, y=605, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=987, y=680, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
        time.sleep(9)
        auto.click(x=820, y=473, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击隐藏样式
        # self.style.click_snapshot_3d()
        # time.sleep(3)
        # auto.click(x=1161, y=362, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击视图名称，准备滚动
        # self.style.scroll_big_number(4)
        # auto.click(x=1144, y=937, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击命名
        # self.style.scroll_big_number(4)
        # auto.click(x=1287, y=863, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击类型
        # time.sleep(2)
        # auto.click(x=1287, y=903, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 选择自定义编号
        # time.sleep(3)
        # auto.click(x=1337, y=971, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件夹
        # save_path = 'C:\\Users\\12540\\Desktop\\双喜-批量模拟\\面料保存'
        # pyperclip.copy(save_path)
        # time.sleep(2)
        # auto.hotkey('ctrl', 'v')
        # time.sleep(2)
        # auto.press('enter')
        # time.sleep(2)
        # auto.press('enter')
        # auto.click(x=1361, y=296, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 关闭3D快照
        auto.click(x=1682, y=192, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击织物
        time.sleep(3)
        auto.click(x=1588, y=714, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击材质属性缩起


        file_path = "C:\\Users\\12540\\Desktop\\桌面\\双喜-批量模拟\\面料文件"  # 面料的位置
        sfab_len = self.operationfile.get_file_name(file_path)[0]
        print(sfab_len)
        length = len(sfab_len)
        print(length)
        for i in range(1, length + 1):
            fabric_name = sfab_len[i - 1]
            print(fabric_name)
            fabric_path = file_path + "\\" + fabric_name
            print(fabric_path)
            pyperclip.copy(fabric_path)
            # auto.click(x=1830, y=480, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开织物
            auto.click(x=1874, y=743, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开物理属性
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            time.sleep(3)


            auto.click(x=682, y=721, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击2D视窗
            auto.hotkey('ctrl', 'a')
            time.sleep(2)
            auto.hotkey('ctrl', 'h') #硬化
            time.sleep(2)
            auto.press('space')
            time.sleep(30)
            auto.press('space')
            time.sleep(2)
            auto.hotkey('ctrl', 'h')  # 取消硬化
            time.sleep(2)
            auto.press('space')
            time.sleep(60)
            auto.press('space')
            time.sleep(2)
            # self.style.click_snapshot_3d()
            # self.style.click_snapshot_3d()
            auto.click(x=280, y=13, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击工具
            auto.click(x=50, y=50, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击快照
            time.sleep(3)
            auto.click(x=1161, y=362, clicks=1, interval=0.0, button='left', duration=0.2,
                       tween=auto.linear)  # 点击视图名称，准备滚动
            self.style.scroll_big_number(4)
            auto.click(x=1144, y=937, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击命名
            self.style.scroll_big_number(4)
            time.sleep(2)
            fabric_name_photo = fabric_name[:-5]
            print(fabric_name_photo)
            pyperclip.copy(fabric_name_photo)
            auto.click(x=1344, y=864, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击自定义
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            auto.click(x=1108, y=1016, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击直接保存
            # snapshot_file_save_path = 'C:\\Users\\12540\\Desktop' + "\\" + fabric_name_photo + '.png'  # 3D快照保存位置
            # self.cloud.assert_render_picture_minute(snapshot_file_save_path, 30)
            time.sleep(6)
            auto.click(x=1060, y=600, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击关闭弹框
            auto.click(x=1360, y=293, clicks=1, interval=0.0, button='left', duration=0.2,
                       tween=auto.linear)  # 点击关闭3D快照

            sproj_path = 'C:\\Users\\12540\\Desktop\\桌面\\双喜-批量模拟\\Fabric_prefer.sproj'  # 工程的位置
            pyperclip.copy(sproj_path)
            auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,
                       tween=auto.linear)  # 打开保存机制修改，适配脚本
            auto.click(x=60, y=12, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
            auto.click(x=89, y=70, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
            auto.click(x=224, y=69, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击打开项目
            auto.click(x=992, y=605, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
            time.sleep(2)
            auto.hotkey('ctrl', 'v')
            time.sleep(2)
            auto.press('enter')
            time.sleep(2)
            auto.click(x=987, y=680, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
            time.sleep(9)
            auto.click(x=820, y=473, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击隐藏样式
            auto.click(x=1682, y=192, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击织物
            time.sleep(2)


    def test_smd_one(self):
        # file_path = os.path.join(OperationFile().get_garder_path('studio'), 'sproj', 'OpenProject')
        file_path = "C:\\Users\\12540\\Desktop\\smd2-100"
        sproj_len = self.operationfile.get_file_name(file_path)[0]
        self.log.info(sproj_len)
        length = len(sproj_len)
        for i in range(1, length + 1):
            sproj_name = sproj_len[i - 1]
            self.log.info(sproj_name)
            if sproj_name.endswith('.sproj'):
                self.log.info('执行打开')
                self.style.start_style3D()
                sproj_path = file_path + "\\" + sproj_name
                print(sproj_path)
                pyperclip.copy(sproj_path)
                auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 打开保存机制修改，适配脚本
                auto.click(x=60, y=9, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
                auto.click(x=89, y=66, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击打开
                auto.click(x=229, y=68, clicks=1, interval=0.0, button='left', duration=0.2,
                           tween=auto.linear)  # 点击打开项目
                auto.click(x=1012, y=596, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
                time.sleep(2)
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                time.sleep(2)
                auto.click(x=987, y=671, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定

                time.sleep(5)
                #
                # style = "工程打开确定"
                # new = "\\smd\\" + style + "_new.png"
                # old = "\\smd\\" + style + "_new.png"
                # # difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
                # difference_data = self.operationfile.comparison_picture_difference(new, old, style, 4, 1017, 77, 1035)


                for j in range(45):
                    style = "工程打开确定"
                    new = "\\smd\\"+style+"_new.png"
                    old = "\\smd\\"+style+"_old.png"
                    # difference = self.operationfile.comparison_picture_allure(new, old, style, 50, 4, 1017, 77, 1035)
                    difference_data = self.operationfile.comparison_picture_difference(new, old, style, 4, 1017, 77, 1035)
                    difference = difference_data[1][0]
                    self.log.info("%s打开图片有差别" % difference)
                    if difference < 1:
                        self.log.info('工程打开成功')
                        break
                    else:
                        self.log.info('等待工程打开')
                        time.sleep(2)
                smd_path ="C:\\Users\\12540\\Desktop\\smd2" + "\\" + sproj_name[:-6] + ".smd"
                print(smd_path)
                pyperclip.copy(smd_path)
                auto.click(x=60, y=9, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击文件
                auto.click(x=93, y=209, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击导出
                auto.moveTo(x=231, y=210, duration=0.2, tween=auto.linear)  # 点击导出
                auto.click(x=222, y=561, clicks=1, interval=0.0, button='left', duration=0.5, tween=auto.linear)  # 点击导出smd
                auto.hotkey('ctrl', 'v')
                time.sleep(2)
                auto.press('enter')
                # auto.mouseDown(x=1003, y=434, button='left', duration=0.3,tween=auto.linear)
                # auto.mouseUp(x=932, y=434, button='left',duration=0.3, tween=auto.linear)
                # time.sleep(2)
                # auto.press('del')
                # time.sleep(1)
                # auto.typewrite('2048')
                time.sleep(2)
                auto.click(x=976, y=681, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
                self.cloud.assert_render_picture_minute(smd_path, 30)
                auto.click(x=1061, y=602, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击确定
                self.style.close_style3D()
            else:
                self.log.info('非sproj工程不做处理')




