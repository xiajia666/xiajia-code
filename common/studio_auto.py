# -*- coding: utf-8 -*-
import json
import time
import win32gui
import pyautogui as auto
import autoit
import pyperclip
import yaml
import os
import psutil
from common.logs import Log
from common.operation_file import OperationFile

with open('../../../config/studio_config.yaml', encoding='utf-8') as yaml_file:
    conf_config = yaml.safe_load(yaml_file.read())
with open('../config/studio_mouse.yaml') as yaml_file:
    conf_mouse = yaml.safe_load(yaml_file.read())   #读取文件内容
screen_width, screen_height = auto.size()   #当前电脑的分辨率

class Style3DAuto(Log):
    """鼠标点击的公共位置"""

    def get_conf_mouse(self): #获取具体坐标
        global conf_mouse
        conf_mouse = OperationFile().open_yaml() #根据分辨率读取配置文件
        return conf_mouse
    def start_style3D(self):  #软件启动
        from common.studio_cloud import Style3DCloud
        Style3DCloud().un_bundling()
        # style_path = conf["Style3D"]["style3d_pro_path"]
        style_path = conf_config["Style3D"]["style3d_path"]
        style_title = "[CLASS:Qt5152QWindowIcon]"
        autoit.run(style_path)
        auto.hotkey('win','d')
        # autoit.win_wait_active(style_title)
        time.sleep(17)
        cla = 'Qt5152QWindowIcon'
        # 利用方法，通过类名找到窗体句柄
        ctjb = win32gui.FindWindow(cla, None)
        # 利用方法，通过窗体句柄前置窗体
        self.info(ctjb)
        try:
            win32gui.SetForegroundWindow(ctjb)
        except:
            print("没有消息可用")
        self.info('执行窗口最前面')
        time.sleep(2)
        if str(screen_width) == '1920':
            auto.click(x=1877, y=42, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear) # 点击新手指引  点击次数clicks=1, 两次点击之间的间隔时间 interval=0.0  鼠标逐渐移动到对应坐标 duration=0.2
            time.sleep(1)
            auto.click(x=731, y=19, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击抬头
            time.sleep(1)
            auto.click(x=1057, y=600, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 是否打开最近工程，点击取消
            time.sleep(1)
            auto.click(x=1877, y=42, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) # 点击新手指引
            auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.4,tween=auto.linear)  # 打开保存机制修改，适配脚本
        elif str(screen_width) == '2560':
            auto.click(x=1443, y=774, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 是否打开最近工程，点击取消
            auto.click(x=500, y=500, clicks=1, interval=0.0, button='left', duration=0.4,tween=auto.linear)  # 打开保存机制修改，适配脚本

    def close_style3D(self):  #软件关闭
        auto.click(x=conf_mouse["CloseStyle3D"]["add_one_1"]['x'], y=conf_mouse["CloseStyle3D"]["add_one_1"]['y'],clicks=conf_mouse["CloseStyle3D"]["add_one_1"]['clicks'],button=conf_mouse["CloseStyle3D"]["add_one_1"]['button'], duration=0.5)
        auto.click(x=conf_mouse["CloseStyle3D"]["add_one_2"]['x'], y=conf_mouse["CloseStyle3D"]["add_one_2"]['y'],clicks=conf_mouse["CloseStyle3D"]["add_one_2"]['clicks'],button=conf_mouse["CloseStyle3D"]["add_one_2"]['button'], duration=0.5)
        pids = psutil.pids()  #返回当前正在运行的PID（进程ID）的排序列表
        try:
            for pid in pids:
                p = psutil.Process(pid)
                if p.name() == 'Style3D.exe':
                    cmd = 'taskkill /F /IM Style3D.exe'
                    os.system(cmd)
                elif p.name() == 'Style3DTest.exe':
                    cmd = 'taskkill /F /IM Style3DTest.exe'
                    os.system(cmd)
        except ProcessLookupError as e:
            print("结束进程有点问题情况1")
        except psutil.NoSuchProcess as e:
            print("结束进程有点问题情况2")
        finally:
            print('结束style3D进程')

    def scroll_big_number(self,number):#滚轮放大控制视角
        for i in range(number):
            auto.scroll(-120)

    def scroll_small_number(self,number):#滚轮缩小控制视角
        for i in range(number):
            auto.scroll(120)

    def tab_big_number(self,number):#tab按键使用次数
        for i in range(number):
            auto.scroll(-100)

    def click_backspace_number(self,number):#Backspace删除次数
        for i in range(number):
            auto.press('backspace')

    def garment_click(self):#当前服装点击
        auto.click(x=conf_mouse["ClickGarment"]["add_one_1"]['x'], y=conf_mouse["ClickGarment"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarment"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarment"]["add_one_1"]['button'], duration=0.5, tween=auto.linear)
        auto.click(x=conf_mouse["ClickGarment"]["add_one_2"]['x'], y=conf_mouse["ClickGarment"]["add_one_2"]['y'],clicks=conf_mouse["ClickGarment"]["add_one_2"]['clicks'],button=conf_mouse["ClickGarment"]["add_one_2"]['button'], duration=0.5, tween=auto.linear)

    def garment_graphic_click(self):#当前图案双击
        auto.click(x=conf_mouse["ClickGarmentGraphic"]["add_one_1"]['x'], y=conf_mouse["ClickGarmentGraphic"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentGraphic"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentGraphic"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)

    def garment_button_click(self):  # 当前纽扣双击
        auto.click(x=conf_mouse["ClickGarmentButton"]["add_one_1"]['x'],y=conf_mouse["ClickGarmentButton"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentButton"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentButton"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)

    def garment_buttonhole_click(self):  # 当前扣眼双击
        auto.click(x=conf_mouse["ClickGarmentButtonhole"]["add_one_1"]['x'],y=conf_mouse["ClickGarmentButtonhole"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentButtonhole"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentButtonhole"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)

    def garment_zipper_click(self):  # 当前拉链双击
        auto.click(x=conf_mouse["ClickGarmentZipper"]["add_one_1"]['x'],y=conf_mouse["ClickGarmentZipper"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentZipper"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentZipper"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(3)

    def garment_topstitch_click(self):  # 当前明线双击
        auto.click(x=conf_mouse["ClickGarmentTopstitch"]["add_one_1"]['x'],y=conf_mouse["ClickGarmentTopstitch"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentTopstitch"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentTopstitch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)

    def garment_puckering_click(self):  # 当前褶皱双击
        auto.click(x=conf_mouse["ClickGarmentPuckering"]["add_one_1"]['x'],y=conf_mouse["ClickGarmentPuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickGarmentPuckering"]["add_one_1"]['clicks'],button=conf_mouse["ClickGarmentPuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)

    def library_click(self):#素材库点击
        auto.click(x=conf_mouse["Clicklibrary"]["add_one_1"]['x'],y=conf_mouse["Clicklibrary"]["add_one_1"]['y'],clicks=conf_mouse["Clicklibrary"]["add_one_1"]['clicks'],button=conf_mouse["Clicklibrary"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["Clicklibrary"]["add_one_2"]['x'],y=conf_mouse["Clicklibrary"]["add_one_2"]['y'],clicks=conf_mouse["Clicklibrary"]["add_one_2"]['clicks'],button=conf_mouse["Clicklibrary"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def add_tshirt(self, tshirt_name):  # 添加默认t-shirt
        path = OperationFile().get_garder_path('studio')
        sproj_path = os.path.join(path, 'garment')
        if tshirt_name == 'T-Shirt':
            sproj_path = sproj_path + '\\' + 'T-Shirt.sgar'
        elif tshirt_name == 'Female_T-Shirt':
            sproj_path = sproj_path + '\\' + 'Female_T-Shirt.sgar'
        elif tshirt_name == 'Male_T-Shirt':
            sproj_path = sproj_path + '\\' + 'Shirt-Shirt.sgar'
        pyperclip.copy(sproj_path)
        auto.click(x=conf_mouse["AddTshirt"]["add_one_1"]['x'], y=conf_mouse["AddTshirt"]["add_one_1"]['y'],clicks=conf_mouse["AddTshirt"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["AddTshirt"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddTshirt"]["add_one_2"]['x'], y=conf_mouse["AddTshirt"]["add_one_2"]['y'],clicks=conf_mouse["AddTshirt"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["AddTshirt"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddTshirt"]["add_one_3"]['x'], y=conf_mouse["AddTshirt"]["add_one_3"]['y'],clicks=conf_mouse["AddTshirt"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["AddTshirt"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(1)
        auto.hotkey('ctrl', 'v')
        time.sleep(1)
        auto.press('enter')
        if str(screen_width) == '1920':
            auto.click(x=985, y=625, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  #点击确认
        elif str(screen_width) == '2560':
            auto.click(x=1317, y=840, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(2.5)

    def add_open_sproj(self, file_path, sprojname, press=None):#添加不同工程
        path = OperationFile().get_garder_path('studio')
        sproj_path = os.path.join(path, file_path)
        sproj_path = sproj_path + '\\' + sprojname
        pyperclip.copy(sproj_path)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_1"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_1"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_1"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_2"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_2"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_2"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_3"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_3"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_3"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_4"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_4"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_4"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)
        if str(screen_width) == '1920':
            auto.click(x=998, y=600, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 弹窗点击否
        elif str(screen_width) == '2560':
            auto.click(x=1005, y=603, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        print(sproj_path)
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=994, y=672, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(9)
        if press == None:
            print("视角不做切换")
        else:
            auto.press('2')

    def add_add_sproj(self, file_path, sprojname, press=None):#添加不同工程(加载类型为添加)
        path = OperationFile().get_garder_path('studio')
        sproj_path = os.path.join(path, file_path)
        sproj_path = sproj_path + '\\' + sprojname
        pyperclip.copy(sproj_path)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_1"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_1"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_1"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_2"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_2"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_2"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_3"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_3"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_3"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddOpenSproj"]["add_one_4"]['x'], y=conf_mouse["AddOpenSproj"]["add_one_4"]['y'],clicks=conf_mouse["AddOpenSproj"]["add_one_4"]['clicks'],button=conf_mouse["AddOpenSproj"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)
        if str(screen_width) == '1920':
            auto.click(x=998, y=600, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 弹窗点击否
        elif str(screen_width) == '2560':
            auto.click(x=1005, y=603, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        print(sproj_path)
        time.sleep(2)
        auto.press('enter')
        auto.click(x=954, y=389, button='left', duration=0.2)
        auto.click(x=935, y=424, button='left', duration=0.2)
        time.sleep(2)
        auto.click(x=994, y=672, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(9)
        if press == None:
            print("视角不做切换")
        else:
            auto.press('2')


    def add_avatar(self, avatarname):#添加默认男175
        path = OperationFile().get_garder_path('studio')
        avatar_path = os.path.join(path, 'avatar')
        avatar_path = avatar_path + '\\' + avatarname
        pyperclip.copy(avatar_path)
        auto.click(x=conf_mouse["AddAvatar"]["add_one_1"]['x'], y=conf_mouse["AddAvatar"]["add_one_1"]['y'],clicks=conf_mouse["AddAvatar"]["add_one_1"]['clicks'],button=conf_mouse["AddAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddAvatar"]["add_one_2"]['x'], y=conf_mouse["AddAvatar"]["add_one_2"]['y'],clicks=conf_mouse["AddAvatar"]["add_one_2"]['clicks'],button=conf_mouse["AddAvatar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["AddAvatar"]["add_one_3"]['x'], y=conf_mouse["AddAvatar"]["add_one_3"]['y'],clicks=conf_mouse["AddAvatar"]["add_one_3"]['clicks'],button=conf_mouse["AddAvatar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(1.5)
        auto.hotkey('ctrl','v')
        time.sleep(2)
        auto.press('enter')
        auto.press('enter')  # 避免因为输入法无法按确定键
        time.sleep(2)
        auto.click(x=conf_mouse["AddAvatar"]["add_one_4"]['x'], y=conf_mouse["AddAvatar"]["add_one_4"]['y'],clicks=conf_mouse["AddAvatar"]["add_one_4"]['clicks'],button=conf_mouse["AddAvatar"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(5)

    def add_library_female_avatar(self): #添加素材库女模特
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_1"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_1"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_1"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_2"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_2"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_2"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_2"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_3"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_3"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_3"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_3"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_4"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_4"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_4"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_4"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_5"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_5"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_5"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_5"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(5)
        auto.click(x=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_6"]['x'], y=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_6"]['y'],clicks=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_6"]['clicks'],button=conf_mouse["ADDLibraryFemaleAvatar"]["add_one_6"]['button'], duration=0.5, tween=auto.linear)

    def add_library_female_garment(self): #添加素材库女服装
        auto.click(x=conf_mouse["ADDLibraryFemaleGarment"]["add_one_1"]['x'], y=conf_mouse["ADDLibraryFemaleGarment"]["add_one_1"]['y'],clicks=conf_mouse["ADDLibraryFemaleGarment"]["add_one_1"]['clicks'],button=conf_mouse["ADDLibraryFemaleGarment"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleGarment"]["add_one_2"]['x'], y=conf_mouse["ADDLibraryFemaleGarment"]["add_one_2"]['y'],clicks=conf_mouse["ADDLibraryFemaleGarment"]["add_one_2"]['clicks'],button=conf_mouse["ADDLibraryFemaleGarment"]["add_one_2"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleGarment"]["add_one_3"]['x'], y=conf_mouse["ADDLibraryFemaleGarment"]["add_one_3"]['y'],clicks=conf_mouse["ADDLibraryFemaleGarment"]["add_one_3"]['clicks'],button=conf_mouse["ADDLibraryFemaleGarment"]["add_one_3"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(2)
        auto.click(x=conf_mouse["ADDLibraryFemaleGarment"]["add_one_4"]['x'], y=conf_mouse["ADDLibraryFemaleGarment"]["add_one_4"]['y'],clicks=conf_mouse["ADDLibraryFemaleGarment"]["add_one_4"]['clicks'],button=conf_mouse["ADDLibraryFemaleGarment"]["add_one_4"]['button'], duration=0.5, tween=auto.linear)
        time.sleep(3)
        auto.click(x=conf_mouse["ADDLibraryFemaleGarment"]["add_one_5"]['x'], y=conf_mouse["ADDLibraryFemaleGarment"]["add_one_5"]['y'],clicks=conf_mouse["ADDLibraryFemaleGarment"]["add_one_5"]['clicks'],button=conf_mouse["ADDLibraryFemaleGarment"]["add_one_5"]['button'], duration=0.5, tween=auto.linear)

    def add_fabric(self, fabricname):#添加织物
        path = OperationFile().get_garder_path('studio')
        fabric_path = os.path.join(path, 'sproj')
        fabric_path = fabric_path + '\\' + fabricname
        auto.click(x=conf_mouse["AddFabric"]["add_one_1"]['x'], y=conf_mouse["AddFabric"]["add_one_1"]['y'],clicks=conf_mouse["AddFabric"]["add_one_1"]['clicks'],button=conf_mouse["AddFabric"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        time.sleep(1.5)
        auto.typewrite(fabric_path)
        time.sleep(2)
        auto.press('enter')
        auto.press('enter')  # 避免因为输入法无法按确定键

    def cancel_tshirt_axis(self):
        auto.press('z')
        auto.click(x=conf_mouse["CancelTshirtAxis"]["add_one_1"]['x'], y=conf_mouse["CancelTshirtAxis"]["add_one_1"]['y'],clicks=conf_mouse["CancelTshirtAxis"]["add_one_1"]['clicks'],button=conf_mouse["CancelTshirtAxis"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["CancelTshirtAxis"]["add_one_2"]['x'], y=conf_mouse["CancelTshirtAxis"]["add_one_2"]['y'],clicks=conf_mouse["CancelTshirtAxis"]["add_one_2"]['clicks'],button=conf_mouse["CancelTshirtAxis"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def cancel_frontpanel_axis(self):
        auto.press('z')
        auto.click(x=conf_mouse["CancelFrontpanelAxis"]["add_one_1"]['x'],y=conf_mouse["CancelFrontpanelAxis"]["add_one_1"]['y'],clicks=conf_mouse["CancelFrontpanelAxis"]["add_one_1"]['clicks'],button=conf_mouse["CancelFrontpanelAxis"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["CancelFrontpanelAxis"]["add_one_2"]['x'],y=conf_mouse["CancelFrontpanelAxis"]["add_one_2"]['y'],clicks=conf_mouse["CancelFrontpanelAxis"]["add_one_2"]['clicks'],button=conf_mouse["CancelFrontpanelAxis"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def symmeetry_with_seam(self):#克隆对称版片
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_1"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_1"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_1"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)#新增克隆对称版片
        time.sleep(0.5)
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_2"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_2"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_2"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_3"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_3"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_3"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.keyUp('shift')  # 松开shift键
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_4"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_4"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_4"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)#点击场景
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_5"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_5"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_5"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_5"]['button'], duration=0.2, tween=auto.linear)#重置2D版片
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_6"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_6"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_6"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_6"]['button'], duration=0.2, tween=auto.linear)
        auto.keyUp('shift')  # 松开shift键
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_7"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_7"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_7"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_7"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["SymmeetryWithSeam"]["add_one_8"]['x'],y=conf_mouse["SymmeetryWithSeam"]["add_one_8"]['y'],clicks=conf_mouse["SymmeetryWithSeam"]["add_one_8"]['clicks'],button=conf_mouse["SymmeetryWithSeam"]["add_one_8"]['button'], duration=0.2, tween=auto.linear)

    def color_modify(self): # 颜色修改
        auto.click(x=conf_mouse["ModifyColor"]["add_one_1"]['x'],y=conf_mouse["ModifyColor"]["add_one_1"]['y'],clicks=conf_mouse["ModifyColor"]["add_one_1"]['clicks'],button=conf_mouse["ModifyColor"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.press('del')
        auto.typewrite('556677')
        auto.click(x=conf_mouse["ModifyColor"]["add_one_2"]['x'],y=conf_mouse["ModifyColor"]["add_one_2"]['y'],clicks=conf_mouse["ModifyColor"]["add_one_2"]['clicks'],button=conf_mouse["ModifyColor"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def rectangle_creat(self):  # 创建正方形
        auto.click(x=conf_mouse["CreatRectangle"]["add_one_1"]['x'], y=conf_mouse["CreatRectangle"]["add_one_1"]['y'],clicks=conf_mouse["CreatRectangle"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["CreatRectangle"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.press('s')  # 快捷键操作画正方形
        time.sleep(1)
        auto.click(x=conf_mouse["CreatRectangle"]["add_one_2"]['x'], y=conf_mouse["CreatRectangle"]["add_one_2"]['y'],clicks=conf_mouse["CreatRectangle"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["CreatRectangle"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=989, y=585, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 创建正方形，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(1)
        auto.press('q')

    def elipse_creat(self):  # 创建圆形
        auto.click(x=conf_mouse["CreatElipse"]["add_one_1"]['x'], y=conf_mouse["CreatElipse"]["add_one_1"]['y'],clicks=conf_mouse["CreatElipse"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["CreatElipse"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.press('e')  # 快捷键操作画圆形
        time.sleep(0.5)
        auto.click(x=conf_mouse["CreatElipse"]["add_one_2"]['x'], y=conf_mouse["CreatElipse"]["add_one_2"]['y'],clicks=conf_mouse["CreatElipse"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["CreatElipse"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["CreatElipse"]["add_one_3"]['x'], y=conf_mouse["CreatElipse"]["add_one_3"]['y'],clicks=conf_mouse["CreatElipse"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["CreatElipse"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        if str(screen_width) == '1920':
            auto.click(x=965, y=580, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  # 创建圆形，点击确定
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.press('q')

    def focus_panorama(self):  # 变焦到全景
        auto.click(x=conf_mouse["FocusPanorama"]["add_one_1"]['x'], y=conf_mouse["FocusPanorama"]["add_one_1"]['y'],clicks=conf_mouse["FocusPanorama"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["FocusPanorama"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.press('9')

    def click_enter(self): #点击确定
        enter_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\enter.png'
        try:
            enter_location = auto.locateOnScreen(enter_location)
            auto.click(enter_location)
        except TypeError as e:
            self.info(e)

    def click_close(self): #点击确定

        enter_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\close.png'  # 定位确定
        try:
            enter_location = auto.locateOnScreen(enter_location)
            auto.click(enter_location)
        except TypeError as e:
            self.info(e)

    def material(self): #材质修改
        color_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920')  + '\\color.png'  # 定位颜色位置，相对移动
        try:
            color = auto.locateOnScreen(color_location)
            x, y = auto.center(color)
            auto.click(color)
            Style3DAuto().color_modify()
        except TypeError as e:
            print(e)
        isdesaturation_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\isdesaturation.png'
        try:
            isdesaturation_location = auto.locateOnScreen(isdesaturation_location)  # 定位褪色位置，相对移动
            x, y = auto.center(isdesaturation_location)
            auto.click(isdesaturation_location)
            auto.moveRel(xOffset=185, yOffset=0, duration=0.0, tween=auto.linear)
            auto.click()
            time.sleep(1)
            auto.moveRel(xOffset=-10, yOffset=25, duration=0.0, tween=auto.linear)  # 修改阴影强度
            auto.dragRel(xOffset=40, yOffset=0, duration=0.0, button='left', mouseDownUp=True)
            auto.typewrite('0.23')
            auto.press('enter')
            time.sleep(1)
            auto.moveRel(xOffset=-40, yOffset=0, duration=0.0, tween=auto.linear)  # 修改总体亮度
            auto.moveRel(xOffset=0, yOffset=40, duration=0.0, tween=auto.linear)
            auto.dragRel(xOffset=40, yOffset=0, duration=0.0, button='left', mouseDownUp=True)
            auto.typewrite('0.54')
            auto.press('enter')
        except TypeError as e:
            print(e)
        normalMap_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\normalMap.png'
        try:
            normalMap = auto.locateOnScreen(normalMap_location)  # 定位法线贴图位置，相对移动
            x, y = auto.center(normalMap)
            auto.click(normalMap)
            auto.moveRel(xOffset=180, yOffset=32, duration=0.0, tween=auto.linear) # 打开自动法线
            auto.click()
            auto.moveRel(xOffset=0, yOffset=30, duration=0.0, tween=auto.linear)  # 修改法线贴图强度
            auto.dragRel(xOffset=30, yOffset=0, duration=0.0, button='left', mouseDownUp=True)
            auto.typewrite('0.6')
            auto.press('enter')
        except TypeError as e:
            print(e)
        glossMap_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\glossMap.png'
        time.sleep(0.5)
        try:
            glossMap = auto.locateOnScreen(glossMap_location)  # 定位光滑度贴图位置，相对移动
            x, y = auto.center(glossMap)
            auto.click(glossMap)
            auto.moveRel(xOffset=170, yOffset=25, duration=0.0, tween=auto.linear)  # 移动到光滑度位置
            time.sleep(1)
            auto.dragRel(xOffset=30, yOffset=0, duration=0.0, button='left', mouseDownUp=True)# 修改光滑度强度
            auto.typewrite('0.6')
            auto.press('enter')
        except TypeError as e:
            print(e)
        metalMap_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\metalMap.png'
        try:
            metalMap = auto.locateOnScreen(metalMap_location)  # 定位金属度贴图位置，相对移动
            x, y = auto.center(metalMap)
            auto.click(metalMap)
            auto.moveRel(xOffset=170, yOffset=25, duration=0.0, tween=auto.linear)  # 移动到金属度位置
            auto.dragRel(xOffset=30, yOffset=0, duration=0.0, button='left', mouseDownUp=True)# 修改金属度强度
            auto.typewrite('0.6')
            auto.press('enter')
        except TypeError as e:
            print(e)
        transparentMap_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\transparentMap.png'
        try:
            transparentMap = auto.locateOnScreen(transparentMap_location)  # 定位透明度贴图位置，相对移动
            x, y = auto.center(transparentMap)
            auto.click(transparentMap)
            auto.moveRel(xOffset=170, yOffset=25, duration=0.0, tween=auto.linear)  # 移动到透明度位置
            auto.dragRel(xOffset=30, yOffset=0, duration=0.0, button='left', mouseDownUp=True)# 修改透明度强度
            auto.typewrite('0.6')
            auto.press('enter')
        except TypeError as e:
            print(e)

    def click_polygon(self): #点击多边形
        auto.click(x=conf_mouse["ClickPolygon"]["add_one_1"]['x'], y=conf_mouse["ClickPolygon"]["add_one_1"]['y'],clicks=conf_mouse["ClickPolygon"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickPolygon"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickPolygon"]["add_one_2"]['x'], y=conf_mouse["ClickPolygon"]["add_one_2"]['y'],clicks=conf_mouse["ClickPolygon"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickPolygon"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_zipper(self): #点击拉链
        auto.click(x=conf_mouse["ClickZipper"]["add_one_1"]['x'], y=conf_mouse["ClickZipper"]["add_one_1"]['y'],clicks=conf_mouse["ClickZipper"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickZipper"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickZipper"]["add_one_2"]['x'], y=conf_mouse["ClickZipper"]["add_one_2"]['y'],clicks=conf_mouse["ClickZipper"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickZipper"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_sewing(self):#编辑缝纫
        auto.click(x=conf_mouse["ClickEditSewing"]["add_one_1"]['x'], y=conf_mouse["ClickEditSewing"]["add_one_1"]['y'],clicks=conf_mouse["ClickEditSewing"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickEditSewing"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditSewing"]["add_one_2"]['x'], y=conf_mouse["ClickEditSewing"]["add_one_2"]['y'],clicks=conf_mouse["ClickEditSewing"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickEditSewing"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_segment_sewing(self):  # 线缝纫
        auto.click(x=conf_mouse["ClickSegmentSewing"]["click_one_1"]['x'],y=conf_mouse["ClickSegmentSewing"]["click_one_1"]['y'],clicks=conf_mouse["ClickSegmentSewing"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentSewing"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentSewing"]["click_one_2"]['x'],y=conf_mouse["ClickSegmentSewing"]["click_one_2"]['y'],clicks=conf_mouse["ClickSegmentSewing"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentSewing"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentSewing"]["click_one_3"]['x'],y=conf_mouse["ClickSegmentSewing"]["click_one_3"]['y'],clicks=conf_mouse["ClickSegmentSewing"]["click_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentSewing"]["click_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_segment_mn_sewing(self):  # MN线缝纫
        auto.click(x=conf_mouse["ClickSegmentMnSewing"]["add_one_1"]['x'],y=conf_mouse["ClickSegmentMnSewing"]["add_one_1"]['y'],clicks=conf_mouse["ClickSegmentMnSewing"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentMnSewing"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentMnSewing"]["add_one_2"]['x'],y=conf_mouse["ClickSegmentMnSewing"]["add_one_2"]['y'],clicks=conf_mouse["ClickSegmentMnSewing"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentMnSewing"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentMnSewing"]["add_one_3"]['x'],y=conf_mouse["ClickSegmentMnSewing"]["add_one_3"]['y'],clicks=conf_mouse["ClickSegmentMnSewing"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentMnSewing"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_free_sewing(self):  # 自由缝纫
        auto.click(x=conf_mouse["ClickFreeSewing"]["add_one_1"]['x'],y=conf_mouse["ClickFreeSewing"]["add_one_1"]['y'],clicks=conf_mouse["ClickFreeSewing"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeSewing"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFreeSewing"]["add_one_2"]['x'],y=conf_mouse["ClickFreeSewing"]["add_one_2"]['y'],clicks=conf_mouse["ClickFreeSewing"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeSewing"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_free_mn_sewing(self):  # MN自由缝纫
        auto.click(x=conf_mouse["ClickFreeMnSewing"]["add_one_1"]['x'],y=conf_mouse["ClickFreeMnSewing"]["add_one_1"]['y'],clicks=conf_mouse["ClickFreeMnSewing"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeMnSewing"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFreeMnSewing"]["add_one_2"]['x'],y=conf_mouse["ClickFreeMnSewing"]["add_one_2"]['y'],clicks=conf_mouse["ClickFreeMnSewing"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeMnSewing"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFreeMnSewing"]["add_one_3"]['x'],y=conf_mouse["ClickFreeMnSewing"]["add_one_3"]['y'],clicks=conf_mouse["ClickFreeMnSewing"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeMnSewing"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_segment_puckering(self):#点击线褶皱
        auto.click(x=conf_mouse["ClickSegmentPuckering"]["add_one_1"]['x'], y=conf_mouse["ClickSegmentPuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickSegmentPuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentPuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentPuckering"]["add_one_2"]['x'], y=conf_mouse["ClickSegmentPuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickSegmentPuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentPuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_free_puckering(self):#点击自由褶皱
        auto.click(x=conf_mouse["ClickFreePuckering"]["add_one_1"]['x'],y=conf_mouse["ClickFreePuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickFreePuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFreePuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFreePuckering"]["add_one_2"]['x'],y=conf_mouse["ClickFreePuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickFreePuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFreePuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_seamline_puckering(self):#点击缝纫线褶皱
        auto.click(x=conf_mouse["ClickSeamlinePuckering"]["add_one_1"]['x'],y=conf_mouse["ClickSeamlinePuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickSeamlinePuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlinePuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSeamlinePuckering"]["add_one_2"]['x'],y=conf_mouse["ClickSeamlinePuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickSeamlinePuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlinePuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSeamlinePuckering"]["add_one_3"]['x'],y=conf_mouse["ClickSeamlinePuckering"]["add_one_3"]['y'],clicks=conf_mouse["ClickSeamlinePuckering"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlinePuckering"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_puckering(self):#点击编辑褶皱
        auto.click(x=conf_mouse["ClickEditPuckering"]["add_one_1"]['x'],y=conf_mouse["ClickEditPuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickEditPuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickEditPuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditPuckering"]["add_one_2"]['x'],y=conf_mouse["ClickEditPuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickEditPuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickEditPuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_test_segment_puckering(self):#点击测试版线褶皱
        auto.click(x=conf_mouse["ClickTestSegmentPuckering"]["add_one_1"]['x'], y=conf_mouse["ClickTestSegmentPuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickTestSegmentPuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTestSegmentPuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTestSegmentPuckering"]["add_one_2"]['x'], y=conf_mouse["ClickTestSegmentPuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickTestSegmentPuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTestSegmentPuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_test_free_puckering(self):#点击测试版自由褶皱
        auto.click(x=conf_mouse["ClickTestFreePuckering"]["add_one_1"]['x'],y=conf_mouse["ClickTestFreePuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickTestFreePuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTestFreePuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTestFreePuckering"]["add_one_2"]['x'],y=conf_mouse["ClickTestFreePuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickTestFreePuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTestFreePuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_test_seamline_puckering(self):#点击测试版缝纫线褶皱
        auto.click(x=conf_mouse["ClickTestSeamlinePuckering"]["add_one_1"]['x'],y=conf_mouse["ClickTestSeamlinePuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickTestSeamlinePuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTestSeamlinePuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTestSeamlinePuckering"]["add_one_2"]['x'],y=conf_mouse["ClickTestSeamlinePuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickTestSeamlinePuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTestSeamlinePuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTestSeamlinePuckering"]["add_one_3"]['x'],y=conf_mouse["ClickTestSeamlinePuckering"]["add_one_3"]['y'],clicks=conf_mouse["ClickTestSeamlinePuckering"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickTestSeamlinePuckering"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_test_edit_puckering(self):#点击测试版编辑褶皱
        auto.click(x=conf_mouse["ClickTestEditPuckering"]["add_one_1"]['x'],y=conf_mouse["ClickTestEditPuckering"]["add_one_1"]['y'],clicks=conf_mouse["ClickTestEditPuckering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTestEditPuckering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTestEditPuckering"]["add_one_2"]['x'],y=conf_mouse["ClickTestEditPuckering"]["add_one_2"]['y'],clicks=conf_mouse["ClickTestEditPuckering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTestEditPuckering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)


    def click_segment_topstitch(self):#点击线明线
        auto.click(x=conf_mouse["ClickSegmentTopstitch"]["add_one_1"]['x'], y=conf_mouse["ClickSegmentTopstitch"]["add_one_1"]['y'],clicks=conf_mouse["ClickSegmentTopstitch"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentTopstitch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSegmentTopstitch"]["add_one_2"]['x'], y=conf_mouse["ClickSegmentTopstitch"]["add_one_2"]['y'],clicks=conf_mouse["ClickSegmentTopstitch"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSegmentTopstitch"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_free_topstitch(self):#点击自由明线
        auto.click(x=conf_mouse["ClickFreeTopstitch"]["add_one_1"]['x'],y=conf_mouse["ClickFreeTopstitch"]["add_one_1"]['y'],clicks=conf_mouse["ClickFreeTopstitch"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeTopstitch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFreeTopstitch"]["add_one_2"]['x'],y=conf_mouse["ClickFreeTopstitch"]["add_one_2"]['y'],clicks=conf_mouse["ClickFreeTopstitch"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFreeTopstitch"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_seamline_topstitch(self):#点击缝纫线明线
        auto.click(x=conf_mouse["ClickSeamlineTopstitch"]["add_one_1"]['x'],y=conf_mouse["ClickSeamlineTopstitch"]["add_one_1"]['y'],clicks=conf_mouse["ClickSeamlineTopstitch"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlineTopstitch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSeamlineTopstitch"]["add_one_2"]['x'],y=conf_mouse["ClickSeamlineTopstitch"]["add_one_2"]['y'],clicks=conf_mouse["ClickSeamlineTopstitch"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlineTopstitch"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSeamlineTopstitch"]["add_one_3"]['x'],y=conf_mouse["ClickSeamlineTopstitch"]["add_one_3"]['y'],clicks=conf_mouse["ClickSeamlineTopstitch"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamlineTopstitch"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_topstitch(self):#点击编辑明线
        auto.click(x=conf_mouse["ClickEditTopstitch"]["add_one_1"]['x'],y=conf_mouse["ClickEditTopstitch"]["add_one_1"]['y'],clicks=conf_mouse["ClickEditTopstitch"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickEditTopstitch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditTopstitch"]["add_one_2"]['x'],y=conf_mouse["ClickEditTopstitch"]["add_one_2"]['y'],clicks=conf_mouse["ClickEditTopstitch"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickEditTopstitch"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)


    def click_addpen(self):  # 点击笔模式
        auto.click(x=conf_mouse["ClickAddpen"]["click_one_1"]['x'],y=conf_mouse["ClickAddpen"]["click_one_1"]['y'],clicks=conf_mouse["ClickAddpen"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAddpen"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)


    def click_addnornamldart(self):  # 点击省道
        auto.click(x=conf_mouse["ClickAddnornamldart"]["click_one_1"]['x'],y=conf_mouse["ClickAddnornamldart"]["click_one_1"]['y'],clicks=conf_mouse["ClickAddnornamldart"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAddnornamldart"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickAddnornamldart"]["click_one_2"]['x'],y=conf_mouse["ClickAddnornamldart"]["click_one_2"]['y'],clicks=conf_mouse["ClickAddnornamldart"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickAddnornamldart"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickAddnornamldart"]["click_one_3"]['x'],y=conf_mouse["ClickAddnornamldart"]["click_one_3"]['y'],clicks=conf_mouse["ClickAddnornamldart"]["click_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickAddnornamldart"]["click_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_addnornamldartenter(self):  # 创建省弹窗点击确定
        auto.click(x=conf_mouse["ClickAddnornamldart"]["click_one_4"]['x'],y=conf_mouse["ClickAddnornamldart"]["click_one_4"]['y'],clicks=conf_mouse["ClickAddnornamldart"]["click_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickAddnornamldart"]["click_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_slashandspread(self):  # 点击延展
        auto.click(x=conf_mouse["ClickSlashandspread"]["add_one_1"]['x'],y=conf_mouse["ClickSlashandspread"]["add_one_1"]['y'],clicks=conf_mouse["ClickSlashandspread"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSlashandspread"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSlashandspread"]["add_one_2"]['x'],y=conf_mouse["ClickSlashandspread"]["add_one_2"]['y'],clicks=conf_mouse["ClickSlashandspread"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSlashandspread"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSlashandspread"]["add_one_3"]['x'],y=conf_mouse["ClickSlashandspread"]["add_one_3"]['y'],clicks=conf_mouse["ClickSlashandspread"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSlashandspread"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_Notch(self):  # 点击刀口
        auto.click(x=conf_mouse["ClickNotch"]["add_one_1"]['x'],y=conf_mouse["ClickNotch"]["add_one_1"]['y'],clicks=conf_mouse["ClickNotch"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickNotch"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNotch"]["add_one_2"]['x'],y=conf_mouse["ClickNotch"]["add_one_2"]['y'],clicks=conf_mouse["ClickNotch"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickNotch"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNotch"]["add_one_3"]['x'],y=conf_mouse["ClickNotch"]["add_one_3"]['y'],clicks=conf_mouse["ClickNotch"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickNotch"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_addannotation(self):  # 点击注释
        auto.click(x=conf_mouse["ClickAddannotation"]["click_one_1"]['x'],y=conf_mouse["ClickAddannotation"]["click_one_1"]['y'],clicks=conf_mouse["ClickAddannotation"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAddannotation"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickAddannotation"]["click_one_2"]['x'],y=conf_mouse["ClickAddannotation"]["click_one_2"]['y'],clicks=conf_mouse["ClickAddannotation"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickAddannotation"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_Dart(self):  # 点击菱形省
        auto.click(x=conf_mouse["ClickDart"]["add_one_1"]['x'], y=conf_mouse["ClickDart"]["add_one_1"]['y'],clicks=conf_mouse["ClickDart"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickDart"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickDart"]["add_one_2"]['x'], y=conf_mouse["ClickDart"]["add_one_2"]['y'],clicks=conf_mouse["ClickDart"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickDart"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickDart"]["add_one_3"]['x'], y=conf_mouse["ClickDart"]["add_one_3"]['y'],clicks=conf_mouse["ClickDart"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickDart"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_Seamallowance(self):  # 点击缝边
        auto.click(x=conf_mouse["ClickSeamallowance"]["add_one_1"]['x'],y=conf_mouse["ClickSeamallowance"]["add_one_1"]['y'],clicks=conf_mouse["ClickSeamallowance"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamallowance"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSeamallowance"]["add_one_2"]['x'],y=conf_mouse["ClickSeamallowance"]["add_one_2"]['y'],clicks=conf_mouse["ClickSeamallowance"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSeamallowance"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_fastenbutton(self):  #点击系纽扣
        auto.click(x=conf_mouse["ClickFastenButton"]["add_one_1"]['x'],y=conf_mouse["ClickFastenButton"]["add_one_1"]['y'],clicks=conf_mouse["ClickFastenButton"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFastenButton"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFastenButton"]["add_one_2"]['x'],y=conf_mouse["ClickFastenButton"]["add_one_2"]['y'],clicks=conf_mouse["ClickFastenButton"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFastenButton"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_button(self): #点击纽扣
        auto.click(x=conf_mouse["ClickButton"]["add_one_1"]['x'],y=conf_mouse["ClickButton"]["add_one_1"]['y'],clicks=conf_mouse["ClickButton"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickButton"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickButton"]["add_one_2"]['x'],y=conf_mouse["ClickButton"]["add_one_2"]['y'],clicks=conf_mouse["ClickButton"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickButton"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_transform_graphic(self): #点击调整图案
        auto.click(x=235, y=11, button='left', duration=0.2)
        auto.click(x=175, y=61, button='left', duration=0.2)

    def click_graphic(self): #点击图案
        auto.click(x=conf_mouse["ClickGraphic"]["add_one_1"]['x'],y=conf_mouse["ClickGraphic"]["add_one_1"]['y'],clicks=conf_mouse["ClickGraphic"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickGraphic"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickGraphic"]["add_one_2"]['x'],y=conf_mouse["ClickGraphic"]["add_one_2"]['y'],clicks=conf_mouse["ClickGraphic"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickGraphic"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_piping(self): #点击嵌条
        auto.click(x=conf_mouse["ClickPiping"]["add_one_1"]['x'],y=conf_mouse["ClickPiping"]["add_one_1"]['y'],clicks=conf_mouse["ClickPiping"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickPiping"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickPiping"]["add_one_2"]['x'],y=conf_mouse["ClickPiping"]["add_one_2"]['y'],clicks=conf_mouse["ClickPiping"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickPiping"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)


    def click_share_upload(self):#点击一键上传
        auto.click(x=conf_mouse["ClickShareUpload"]["add_one_1"]['x'], y=conf_mouse["ClickShareUpload"]["add_one_1"]['y'],clicks=conf_mouse["ClickShareUpload"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShareUpload"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShareUpload"]["add_one_2"]['x'], y=conf_mouse["ClickShareUpload"]["add_one_2"]['y'],clicks=conf_mouse["ClickShareUpload"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShareUpload"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_share_update(self):#点击一键更新
        auto.click(x=conf_mouse["ClickShareUpdate"]["add_one_1"]['x'],y=conf_mouse["ClickShareUpdate"]["add_one_1"]['y'],clicks=conf_mouse["ClickShareUpdate"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShareUpdate"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShareUpdate"]["add_one_2"]['x'],y=conf_mouse["ClickShareUpdate"]["add_one_2"]['y'],clicks=conf_mouse["ClickShareUpdate"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShareUpdate"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_export_dxf(self):#导出dxf
        auto.click(x=conf_mouse["ClickExportDxf"]["add_one_1"]['x'], y=conf_mouse["ClickExportDxf"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportDxf"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportDxf"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportDxf"]["add_one_2"]['x'], y=conf_mouse["ClickExportDxf"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportDxf"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportDxf"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportDxf"]["add_one_3"]['x'], y=conf_mouse["ClickExportDxf"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportDxf"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportDxf"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_dxf(self):#导入dxf
        auto.click(x=conf_mouse["ClickImportDxf"]["add_one_1"]['x'], y=conf_mouse["ClickImportDxf"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportDxf"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportDxf"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportDxf"]["add_one_2"]['x'], y=conf_mouse["ClickImportDxf"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportDxf"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportDxf"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportDxf"]["add_one_3"]['x'], y=conf_mouse["ClickImportDxf"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportDxf"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportDxf"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_obj(self):#导出obj
        auto.click(x=conf_mouse["ClickExportObj"]["add_one_1"]['x'], y=conf_mouse["ClickExportObj"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportObj"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportObj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportObj"]["add_one_2"]['x'], y=conf_mouse["ClickExportObj"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportObj"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportObj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportObj"]["add_one_3"]['x'], y=conf_mouse["ClickExportObj"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportObj"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportObj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_obj(self):#导入obj
        auto.click(x=conf_mouse["ClickImportObj"]["add_one_1"]['x'], y=conf_mouse["ClickImportObj"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportObj"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportObj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportObj"]["add_one_2"]['x'], y=conf_mouse["ClickImportObj"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportObj"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportObj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportObj"]["add_one_3"]['x'], y=conf_mouse["ClickImportObj"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportObj"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportObj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_sco(self):  # 导出sco
        auto.click(x=conf_mouse["ClickExportSco"]["add_one_1"]['x'], y=conf_mouse["ClickExportSco"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportSco"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportSco"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportSco"]["add_one_2"]['x'], y=conf_mouse["ClickExportSco"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportSco"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportSco"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportSco"]["add_one_3"]['x'], y=conf_mouse["ClickExportSco"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportSco"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportSco"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_sco(self):  # 导入sco
        auto.click(x=conf_mouse["ClickImportSco"]["add_one_1"]['x'], y=conf_mouse["ClickImportSco"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportSco"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportSco"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportSco"]["add_one_2"]['x'], y=conf_mouse["ClickImportSco"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportSco"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportSco"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportSco"]["add_one_3"]['x'], y=conf_mouse["ClickImportSco"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportSco"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportSco"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_fbx(self):  # 导出fbx
        auto.click(x=conf_mouse["ClickExportFbx"]["add_one_1"]['x'], y=conf_mouse["ClickExportFbx"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportFbx"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportFbx"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportFbx"]["add_one_2"]['x'], y=conf_mouse["ClickExportFbx"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportFbx"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportFbx"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportFbx"]["add_one_3"]['x'], y=conf_mouse["ClickExportFbx"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportFbx"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportFbx"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_fbx(self):  # 导入fbx
        auto.click(x=conf_mouse["ClickImportFbx"]["add_one_1"]['x'], y=conf_mouse["ClickImportFbx"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportFbx"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportFbx"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportFbx"]["add_one_2"]['x'], y=conf_mouse["ClickImportFbx"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportFbx"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportFbx"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportFbx"]["add_one_3"]['x'], y=conf_mouse["ClickImportFbx"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportFbx"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportFbx"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_glb(self):  # 导出glb
        auto.click(x=conf_mouse["ClickExportGlb"]["add_one_1"]['x'], y=conf_mouse["ClickExportGlb"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportGlb"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGlb"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportGlb"]["add_one_2"]['x'], y=conf_mouse["ClickExportGlb"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportGlb"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGlb"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportGlb"]["add_one_3"]['x'], y=conf_mouse["ClickExportGlb"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportGlb"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGlb"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_glb(self):  # 导入glb
        auto.click(x=conf_mouse["ClickImportGlb"]["add_one_1"]['x'], y=conf_mouse["ClickImportGlb"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportGlb"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGlb"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportGlb"]["add_one_2"]['x'], y=conf_mouse["ClickImportGlb"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportGlb"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGlb"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportGlb"]["add_one_3"]['x'], y=conf_mouse["ClickImportGlb"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportGlb"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGlb"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_gltf(self):  # 导出gltf
        auto.click(x=conf_mouse["ClickExportGltf"]["add_one_1"]['x'], y=conf_mouse["ClickExportGltf"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportGltf"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGltf"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportGltf"]["add_one_2"]['x'], y=conf_mouse["ClickExportGltf"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportGltf"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGltf"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportGltf"]["add_one_3"]['x'], y=conf_mouse["ClickExportGltf"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportGltf"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportGltf"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_gltf(self):  # 导入gltf
        auto.click(x=conf_mouse["ClickImportGltf"]["add_one_1"]['x'], y=conf_mouse["ClickImportGltf"]["add_one_1"]['y'],clicks=conf_mouse["ClickImportGltf"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGltf"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportGltf"]["add_one_2"]['x'], y=conf_mouse["ClickImportGltf"]["add_one_2"]['y'],clicks=conf_mouse["ClickImportGltf"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGltf"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickImportGltf"]["add_one_3"]['x'], y=conf_mouse["ClickImportGltf"]["add_one_3"]['y'],clicks=conf_mouse["ClickImportGltf"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickImportGltf"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_export_alembic(self):  # 导出Alembic
        auto.click(x=conf_mouse["ClickExportAlembic"]["add_one_1"]['x'], y=conf_mouse["ClickExportAlembic"]["add_one_1"]['y'],clicks=conf_mouse["ClickExportAlembic"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickExportAlembic"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportAlembic"]["add_one_2"]['x'], y=conf_mouse["ClickExportAlembic"]["add_one_2"]['y'],clicks=conf_mouse["ClickExportAlembic"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickExportAlembic"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickExportAlembic"]["add_one_3"]['x'], y=conf_mouse["ClickExportAlembic"]["add_one_3"]['y'],clicks=conf_mouse["ClickExportAlembic"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickExportAlembic"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_import_alembic(self):  # 导入Alembic
        auto.click(x=conf_mouse["ClicImportAlembic"]["add_one_1"]['x'], y=conf_mouse["ClicImportAlembic"]["add_one_1"]['y'],clicks=conf_mouse["ClicImportAlembic"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClicImportAlembic"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClicImportAlembic"]["add_one_2"]['x'], y=conf_mouse["ClicImportAlembic"]["add_one_2"]['y'],clicks=conf_mouse["ClicImportAlembic"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClicImportAlembic"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClicImportAlembic"]["add_one_3"]['x'], y=conf_mouse["ClicImportAlembic"]["add_one_3"]['y'],clicks=conf_mouse["ClicImportAlembic"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClicImportAlembic"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_save_as_sproj(self):  # 另存为项目文件
        auto.click(x=conf_mouse["ClickSaveAsSproj"]["add_one_1"]['x'],y=conf_mouse["ClickSaveAsSproj"]["add_one_1"]['y'],clicks=conf_mouse["ClickSaveAsSproj"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSproj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsSproj"]["add_one_2"]['x'],y=conf_mouse["ClickSaveAsSproj"]["add_one_2"]['y'],clicks=conf_mouse["ClickSaveAsSproj"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSproj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsSproj"]["add_one_3"]['x'],y=conf_mouse["ClickSaveAsSproj"]["add_one_3"]['y'],clicks=conf_mouse["ClickSaveAsSproj"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSproj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_save_project(self):  # 保存项目
        auto.click(x=conf_mouse["ClickSaveProject"]["add_one_1"]['x'],y=conf_mouse["ClickSaveProject"]["add_one_1"]['y'],clicks=conf_mouse["ClickSaveProject"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveProject"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveProject"]["add_one_2"]['x'],y=conf_mouse["ClickSaveProject"]["add_one_2"]['y'],clicks=conf_mouse["ClickSaveProject"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveProject"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_save_as_sgar(self):  # 另存为服装文件
        auto.click(x=conf_mouse["ClickSaveAsSgar"]["add_one_1"]['x'],y=conf_mouse["ClickSaveAsSgar"]["add_one_1"]['y'],clicks=conf_mouse["ClickSaveAsSgar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSgar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsSgar"]["add_one_2"]['x'],y=conf_mouse["ClickSaveAsSgar"]["add_one_2"]['y'],clicks=conf_mouse["ClickSaveAsSgar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSgar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsSgar"]["add_one_3"]['x'],y=conf_mouse["ClickSaveAsSgar"]["add_one_3"]['y'],clicks=conf_mouse["ClickSaveAsSgar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsSgar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_save_as_avatar(self):  # 另存为虚拟模特
        auto.click(x=conf_mouse["ClickSaveAsAvatar"]["add_one_1"]['x'], y=conf_mouse["ClickSaveAsAvatar"]["add_one_1"]['y'],clicks=conf_mouse["ClickSaveAsAvatar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsAvatar"]["add_one_2"]['x'], y=conf_mouse["ClickSaveAsAvatar"]["add_one_2"]['y'],clicks=conf_mouse["ClickSaveAsAvatar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsAvatar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSaveAsAvatar"]["add_one_3"]['x'], y=conf_mouse["ClickSaveAsAvatar"]["add_one_3"]['y'],clicks=conf_mouse["ClickSaveAsAvatar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickSaveAsAvatar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_open_sproj(self):  # 打开工程文件
        auto.click(x=conf_mouse["ClickOpenSproj"]["add_one_1"]['x'],y=conf_mouse["ClickOpenSproj"]["add_one_1"]['y'],clicks=conf_mouse["ClickOpenSproj"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSproj"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenSproj"]["add_one_2"]['x'],y=conf_mouse["ClickOpenSproj"]["add_one_2"]['y'],clicks=conf_mouse["ClickOpenSproj"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSproj"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenSproj"]["add_one_3"]['x'],y=conf_mouse["ClickOpenSproj"]["add_one_3"]['y'],clicks=conf_mouse["ClickOpenSproj"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSproj"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        # auto.click(x=1011, y=570, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)#机制修改后适配

    def click_open_scene(self):  # 打开场景文件
        auto.click(x=conf_mouse["ClickOpenScene"]["add_one_1"]['x'], y=conf_mouse["ClickOpenScene"]["add_one_1"]['y'],clicks=conf_mouse["ClickOpenScene"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenScene"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenScene"]["add_one_2"]['x'], y=conf_mouse["ClickOpenScene"]["add_one_2"]['y'],clicks=conf_mouse["ClickOpenScene"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenScene"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenScene"]["add_one_3"]['x'], y=conf_mouse["ClickOpenScene"]["add_one_3"]['y'],clicks=conf_mouse["ClickOpenScene"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenScene"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_recent_files(self):  # 打开最近使用
        auto.click(x=conf_mouse["ClickRecentFiles"]["add_one_1"]['x'], y=conf_mouse["ClickRecentFiles"]["add_one_1"]['y'],clicks=conf_mouse["ClickRecentFiles"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickRecentFiles"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickRecentFiles"]["add_one_2"]['x'], y=conf_mouse["ClickRecentFiles"]["add_one_2"]['y'],clicks=conf_mouse["ClickRecentFiles"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickRecentFiles"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_open_sgar(self):  # 打开服装文件
        auto.click(x=conf_mouse["ClickOpenSgar"]["add_one_1"]['x'], y=conf_mouse["ClickOpenSgar"]["add_one_1"]['y'],clicks=conf_mouse["ClickOpenSgar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSgar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenSgar"]["add_one_2"]['x'], y=conf_mouse["ClickOpenSgar"]["add_one_2"]['y'],clicks=conf_mouse["ClickOpenSgar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSgar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenSgar"]["add_one_3"]['x'], y=conf_mouse["ClickOpenSgar"]["add_one_3"]['y'],clicks=conf_mouse["ClickOpenSgar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenSgar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_open_avatar(self):  # 打开虚拟模特
        auto.click(x=conf_mouse["ClickOpenAvatar"]["add_one_1"]['x'], y=conf_mouse["ClickOpenAvatar"]["add_one_1"]['y'],clicks=conf_mouse["ClickOpenAvatar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenAvatar"]["add_one_2"]['x'], y=conf_mouse["ClickOpenAvatar"]["add_one_2"]['y'],clicks=conf_mouse["ClickOpenAvatar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenAvatar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickOpenAvatar"]["add_one_3"]['x'], y=conf_mouse["ClickOpenAvatar"]["add_one_3"]['y'],clicks=conf_mouse["ClickOpenAvatar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickOpenAvatar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_new_project(self):  # 新建工程
        auto.click(x=conf_mouse["ClickNewProject"]["add_one_1"]['x'], y=conf_mouse["ClickNewProject"]["add_one_1"]['y'],clicks=conf_mouse["ClickNewProject"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickNewProject"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNewProject"]["add_one_2"]['x'], y=conf_mouse["ClickNewProject"]["add_one_2"]['y'],clicks=conf_mouse["ClickNewProject"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickNewProject"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        if str(screen_width) == '1920':
            auto.click(x=993, y=594, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 是否保存工程，点击否
        elif str(screen_width) == '2560':
            auto.click(x=1326, y=786, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  # 点击否
        self.focus_panorama()

    def crash_open(self):  # 程序崩溃重开软件
        auto.click(x=83, y=16, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击文件
        auto.click(x=92, y=47, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击新建
        auto.click(x=1004, y=605, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear) #点击否

    def click_new_project_only(self):
        auto.click(x=conf_mouse["ClickNewProjectOnly"]["add_one_1"]['x'], y=conf_mouse["ClickNewProjectOnly"]["add_one_1"]['y'],clicks=conf_mouse["ClickNewProjectOnly"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickNewProjectOnly"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNewProjectOnly"]["add_one_2"]['x'], y=conf_mouse["ClickNewProjectOnly"]["add_one_2"]['y'],clicks=conf_mouse["ClickNewProjectOnly"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickNewProjectOnly"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_2(self):#点击前视角
        auto.click(x=conf_mouse["ClickViewport2"]["add_one_1"]['x'], y=conf_mouse["ClickViewport2"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport2"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport2"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport2"]["add_one_2"]['x'], y=conf_mouse["ClickViewport2"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport2"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport2"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport2"]["add_one_3"]['x'], y=conf_mouse["ClickViewport2"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport2"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport2"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport2"]["add_one_4"]['x'], y=conf_mouse["ClickViewport2"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport2"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport2"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_4(self):#点击左视角
        auto.click(x=conf_mouse["ClickViewport4"]["add_one_1"]['x'], y=conf_mouse["ClickViewport4"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport4"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport4"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport4"]["add_one_2"]['x'], y=conf_mouse["ClickViewport4"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport4"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport4"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport4"]["add_one_3"]['x'], y=conf_mouse["ClickViewport4"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport4"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport4"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport4"]["add_one_4"]['x'], y=conf_mouse["ClickViewport4"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport4"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport4"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_6(self):  # 点击右视角
        auto.click(x=conf_mouse["ClickViewport6"]["add_one_1"]['x'], y=conf_mouse["ClickViewport6"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport6"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport6"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport6"]["add_one_2"]['x'], y=conf_mouse["ClickViewport6"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport6"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport6"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport6"]["add_one_3"]['x'], y=conf_mouse["ClickViewport6"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport6"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport6"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport6"]["add_one_4"]['x'], y=conf_mouse["ClickViewport6"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport6"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport6"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_8(self):#点击后视角
        auto.click(x=conf_mouse["ClickViewport8"]["add_one_1"]['x'], y=conf_mouse["ClickViewport8"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport8"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport8"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport8"]["add_one_2"]['x'], y=conf_mouse["ClickViewport8"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport8"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport8"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport8"]["add_one_3"]['x'], y=conf_mouse["ClickViewport8"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport8"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport8"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport8"]["add_one_4"]['x'], y=conf_mouse["ClickViewport8"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport8"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport8"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_5(self):#点击上视角
        auto.click(x=conf_mouse["ClickViewport5"]["add_one_1"]['x'], y=conf_mouse["ClickViewport5"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport5"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport5"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport5"]["add_one_2"]['x'], y=conf_mouse["ClickViewport5"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport5"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport5"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport5"]["add_one_3"]['x'], y=conf_mouse["ClickViewport5"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport5"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport5"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport5"]["add_one_4"]['x'], y=conf_mouse["ClickViewport5"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport5"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport5"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_0(self):#点击下视角
        auto.click(x=conf_mouse["ClickViewport0"]["add_one_1"]['x'], y=conf_mouse["ClickViewport0"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewport0"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport0"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport0"]["add_one_2"]['x'], y=conf_mouse["ClickViewport0"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewport0"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport0"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport0"]["add_one_3"]['x'], y=conf_mouse["ClickViewport0"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewport0"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport0"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewport0"]["add_one_4"]['x'], y=conf_mouse["ClickViewport0"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewport0"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewport0"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_viewport_F(self):#对焦F
        auto.click(x=conf_mouse["ClickViewportF"]["add_one_1"]['x'], y=conf_mouse["ClickViewportF"]["add_one_1"]['y'],clicks=conf_mouse["ClickViewportF"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickViewportF"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewportF"]["add_one_2"]['x'], y=conf_mouse["ClickViewportF"]["add_one_2"]['y'],clicks=conf_mouse["ClickViewportF"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickViewportF"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewportF"]["add_one_3"]['x'], y=conf_mouse["ClickViewportF"]["add_one_3"]['y'],clicks=conf_mouse["ClickViewportF"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickViewportF"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickViewportF"]["add_one_4"]['x'], y=conf_mouse["ClickViewportF"]["add_one_4"]['y'],clicks=conf_mouse["ClickViewportF"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickViewportF"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_show_avatar(self):#显示虚拟模特
        auto.click(x=conf_mouse["ClickShowAvatar"]["add_one_1"]['x'], y=conf_mouse["ClickShowAvatar"]["add_one_1"]['y'],clicks=conf_mouse["ClickShowAvatar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatar"]["add_one_2"]['x'], y=conf_mouse["ClickShowAvatar"]["add_one_2"]['y'],clicks=conf_mouse["ClickShowAvatar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatar"]["add_one_3"]['x'], y=conf_mouse["ClickShowAvatar"]["add_one_3"]['y'],clicks=conf_mouse["ClickShowAvatar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatar"]["add_one_4"]['x'], y=conf_mouse["ClickShowAvatar"]["add_one_4"]['y'],clicks=conf_mouse["ClickShowAvatar"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatar"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_show_avatar_measure(self):#显示虚拟模特尺寸
        auto.click(x=conf_mouse["ClickShowAvatarMeasure"]["add_one_1"]['x'], y=conf_mouse["ClickShowAvatarMeasure"]["add_one_1"]['y'],clicks=conf_mouse["ClickShowAvatarMeasure"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatarMeasure"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatarMeasure"]["add_one_2"]['x'], y=conf_mouse["ClickShowAvatarMeasure"]["add_one_2"]['y'],clicks=conf_mouse["ClickShowAvatarMeasure"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatarMeasure"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatarMeasure"]["add_one_3"]['x'], y=conf_mouse["ClickShowAvatarMeasure"]["add_one_3"]['y'],clicks=conf_mouse["ClickShowAvatarMeasure"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatarMeasure"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowAvatarMeasure"]["add_one_4"]['x'], y=conf_mouse["ClickShowAvatarMeasure"]["add_one_4"]['y'],clicks=conf_mouse["ClickShowAvatarMeasure"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickShowAvatarMeasure"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_show_arrangement_points_a(self):#显示安排点A
        auto.click(x=conf_mouse["ClickShowArrangementPointsA"]["add_one_1"]['x'], y=conf_mouse["ClickShowArrangementPointsA"]["add_one_1"]['y'],clicks=conf_mouse["ClickShowArrangementPointsA"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShowArrangementPointsA"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowArrangementPointsA"]["add_one_2"]['x'], y=conf_mouse["ClickShowArrangementPointsA"]["add_one_2"]['y'],clicks=conf_mouse["ClickShowArrangementPointsA"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShowArrangementPointsA"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowArrangementPointsA"]["add_one_3"]['x'], y=conf_mouse["ClickShowArrangementPointsA"]["add_one_3"]['y'],clicks=conf_mouse["ClickShowArrangementPointsA"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickShowArrangementPointsA"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowArrangementPointsA"]["add_one_4"]['x'], y=conf_mouse["ClickShowArrangementPointsA"]["add_one_4"]['y'],clicks=conf_mouse["ClickShowArrangementPointsA"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickShowArrangementPointsA"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_bounding_volumes(self):#显示安排板
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=255, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=277, y=169, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_garment(self):#显示服装
        auto.click(x=conf_mouse["ClickShowGarment"]["add_one_1"]['x'],y=conf_mouse["ClickShowGarment"]["add_one_1"]['y'],clicks=conf_mouse["ClickShowGarment"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickShowGarment"]["add_one_1"]['button'], duration=0.2,tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowGarment"]["add_one_2"]['x'],y=conf_mouse["ClickShowGarment"]["add_one_2"]['y'],clicks=conf_mouse["ClickShowGarment"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickShowGarment"]["add_one_2"]['button'], duration=0.2,tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowGarment"]["add_one_3"]['x'],y=conf_mouse["ClickShowGarment"]["add_one_3"]['y'],clicks=conf_mouse["ClickShowGarment"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickShowGarment"]["add_one_3"]['button'], duration=0.2,tween=auto.linear)
        auto.click(x=conf_mouse["ClickShowGarment"]["add_one_4"]['x'],y=conf_mouse["ClickShowGarment"]["add_one_4"]['y'],clicks=conf_mouse["ClickShowGarment"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickShowGarment"]["add_one_4"]['button'], duration=0.2,tween=auto.linear)

    def click_show_button(self):#显示纽扣扣眼
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=119, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_pins(self):#显示固定针
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=146, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_2D_sewing(self):#显示2D缝纫
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=173, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_topsitch(self):#显示明线
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=201, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_garment_measure(self):#显示服装尺寸
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=155, y=222, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_windows_garment3D(self):#点击窗口3D服装窗口
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=89, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_windows_pattern2D(self):#点击窗口3D服装窗口
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=121, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_windows_photo_rendering(self):  # 点击窗口离线渲染
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=278, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_windows_animation_editor(self):  # 点击窗口动画编辑器
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=308, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_windows_colorway(self):  # 点击窗口齐色
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=348, y=335, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_reset_layout(self):#重置窗口
        auto.click(x=430, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=444, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_smooth_curve(self):#点击圆顺曲线
        auto.click(x=247, y=19, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=631, y=64, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_edit_curvePoint(self):#点击编辑曲线点
        auto.click(x=193, y=13, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=463, y=51, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=459, y=108, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_animation_editor(self):#点击动画编辑器
        auto.click(x=conf_mouse["ClickAnimationEditor"]["add_one_1"]['x'],y=conf_mouse["ClickAnimationEditor"]["add_one_1"]['y'],clicks=conf_mouse["ClickAnimationEditor"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAnimationEditor"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickAnimationEditor"]["add_one_2"]['x'],y=conf_mouse["ClickAnimationEditor"]["add_one_2"]['y'],clicks=conf_mouse["ClickAnimationEditor"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickAnimationEditor"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_avatar_tape(self):#编辑模特胶带
        auto.click(x=180, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=91, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_avatar_circumference_tape(self):  # 模特圆周胶带
        auto.click(x=180, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=117, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_avatar_linear_tape(self):#模特线段胶带
        auto.click(x=180, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=141, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_attach_to_avatar_tape(self):#服装贴敷到胶带
        auto.click(x=180, y=24, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=668, y=169, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_rectangle(self):  #点击正方形
        auto.click(x=245, y=21, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=296, y=62, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_seamtaping(self):  #点击粘衬条
        auto.click(x=304, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=411, y=61, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_steam(self):  # 新增归拔
        auto.click(x=192, y=13, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1145, y=50, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_clear_sporj(self): #清空工程
        auto.click(x=119, y=19, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=60, y=63, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1021, y=568, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        time.sleep(1.5)

    def click_addpoint(self):  # 加点
        auto.click(x=160, y=12, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=377, y=50, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=375, y=80, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_PleatSewing(self): #缝纫褶皱
        auto.click(x=181, y=21, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=937, y=62, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=938, y=144, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_addtack(self): #添加假缝
        auto.click(x=conf_mouse["ClickAddtack"]["click_one_1"]['x'],y=conf_mouse["ClickAddtack"]["click_one_1"]['y'],clicks=conf_mouse["ClickAddtack"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAddtack"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickAddtack"]["click_one_2"]['x'],y=conf_mouse["ClickAddtack"]["click_one_2"]['y'],clicks=conf_mouse["ClickAddtack"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickAddtack"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_tack(self): #编辑假缝
        auto.click(x=conf_mouse["ClickEditTack"]["click_one_1"]['x'], y=conf_mouse["ClickEditTack"]["click_one_1"]['y'],clicks=conf_mouse["ClickEditTack"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickEditTack"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditTack"]["click_one_2"]['x'], y=conf_mouse["ClickEditTack"]["click_one_2"]['y'],clicks=conf_mouse["ClickEditTack"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickEditTack"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditTack"]["click_one_3"]['x'], y=conf_mouse["ClickEditTack"]["click_one_3"]['y'],clicks=conf_mouse["ClickEditTack"]["click_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickEditTack"]["click_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_tack_to_avatar(self): #添加假缝到模特
        auto.click(x=conf_mouse["ClickTackToAvatar"]["add_one_1"]['x'], y=conf_mouse["ClickTackToAvatar"]["add_one_1"]['y'],clicks=conf_mouse["ClickTackToAvatar"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTackToAvatar"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTackToAvatar"]["add_one_2"]['x'], y=conf_mouse["ClickTackToAvatar"]["add_one_2"]['y'],clicks=conf_mouse["ClickTackToAvatar"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTackToAvatar"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTackToAvatar"]["add_one_3"]['x'], y=conf_mouse["ClickTackToAvatar"]["add_one_3"]['y'],clicks=conf_mouse["ClickTackToAvatar"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickTackToAvatar"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_restas2D_all(self): #重置2D安排位置全部
        auto.click(x=184, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=61, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=88, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_restas2D_select(self): #重置2D安排位置选择
        auto.click(x=184, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=142, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_restas3D_all(self): #重置3D安排位置全部
        auto.click(x=184, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=61, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=118, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_restas3D_select(self): #重置3D安排位置选择
        auto.click(x=184, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=859, y=175, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_pleatfold(self): #点击翻折褶裥
        auto.click(x=184, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=939, y=61, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=930, y=120, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
    def click_simplifymeshes(self): #点击简化网格
        auto.click(x=119, y=17, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1100, y=66, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_popbutton_thick(self):  #点击厚度
        auto.click(x=1132, y=162, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_show_internal_line(self):  #点击内部线
        auto.click(x=1132, y=162, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_cloth_textured_surface2d(self):  # 点击2D面料纹理
        auto.click(x=conf_mouse["ClickClothTexturedSurface"]["click_one_1"]['x'],y=conf_mouse["ClickClothTexturedSurface"]["click_one_1"]['y'],clicks=conf_mouse["ClickClothTexturedSurface"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickClothTexturedSurface"]["click_one_1"]['button'], duration=0.2,tween=auto.linear)

    def click_cloth_textured_surface3d(self):  # 点击3D面料纹理
        auto.click(x=conf_mouse["ClickClothTexturedSurface"]["click_one_2"]['x'],y=conf_mouse["ClickClothTexturedSurface"]["click_one_2"]['y'],clicks=conf_mouse["ClickClothTexturedSurface"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickClothTexturedSurface"]["click_one_2"]['button'], duration=0.2,tween=auto.linear)

    def click_popbutton_seamallowance(self):  #点击缝边
        auto.click(x=581, y=166, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_popbutton_show_addannotation(self): #点击注释
        auto.click(x=conf_mouse["ClickPopbuttonShowAddannotation"]["add_one_1"]['x'],y=conf_mouse["ClickPopbuttonShowAddannotation"]["add_one_1"]['y'],clicks=conf_mouse["ClickPopbuttonShowAddannotation"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickPopbuttonShowAddannotation"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)

    def click_addannotation_warning_close(self): #点击版片外注释弹框，点击确定
        auto.click(x=conf_mouse["ClickAddannotationWarningClose"]["click_one_1"]['x'],y=conf_mouse["ClickAddannotationWarningClose"]["click_one_1"]['y'],clicks=conf_mouse["ClickAddannotationWarningClose"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickAddannotationWarningClose"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)

    def click_colorway(self):  #点击齐色
        auto.click(x=120, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=720, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_snapshot_3d(self):  #点击3d快照
        auto.click(x=conf_mouse["ClickSnapshot3D"]["add_one_1"]['x'],y=conf_mouse["ClickSnapshot3D"]["add_one_1"]['y'],clicks=conf_mouse["ClickSnapshot3D"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSnapshot3D"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSnapshot3D"]["add_one_2"]['x'],y=conf_mouse["ClickSnapshot3D"]["add_one_2"]['y'],clicks=conf_mouse["ClickSnapshot3D"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSnapshot3D"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_snapshot_2d(self):  # 点击2d快照
        auto.click(x=conf_mouse["ClickSnapshot2D"]["add_one_1"]['x'], y=conf_mouse["ClickSnapshot2D"]["add_one_1"]['y'],clicks=conf_mouse["ClickSnapshot2D"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSnapshot2D"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSnapshot2D"]["add_one_2"]['x'], y=conf_mouse["ClickSnapshot2D"]["add_one_2"]['y'],clicks=conf_mouse["ClickSnapshot2D"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSnapshot2D"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_marker(self):  # 点击排料
        auto.click(x=conf_mouse["ClickMarker"]["add_one_1"]['x'], y=conf_mouse["ClickMarker"]["add_one_1"]['y'],clicks=conf_mouse["ClickMarker"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickMarker"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickMarker"]["add_one_2"]['x'], y=conf_mouse["ClickMarker"]["add_one_2"]['y'],clicks=conf_mouse["ClickMarker"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickMarker"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_select(self): #点击选择
        auto.click(x=conf_mouse["ClickSelect"]["add_one_1"]['x'], y=conf_mouse["ClickSelect"]["add_one_1"]['y'],clicks=conf_mouse["ClickSelect"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickSelect"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickSelect"]["add_one_2"]['x'], y=conf_mouse["ClickSelect"]["add_one_2"]['y'],clicks=conf_mouse["ClickSelect"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickSelect"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_edit_pattern(self):  # 点击编辑版片
        auto.click(x=conf_mouse["ClickEditPattern"]["add_one_1"]['x'],y=conf_mouse["ClickEditPattern"]["add_one_1"]['y'],clicks=conf_mouse["ClickEditPattern"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickEditPattern"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickEditPattern"]["add_one_2"]['x'],y=conf_mouse["ClickEditPattern"]["add_one_2"]['y'],clicks=conf_mouse["ClickEditPattern"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickEditPattern"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_trace(self):  # 点击勾勒轮廓
        auto.click(x=conf_mouse["ClickTrace"]["add_one_1"]['x'], y=conf_mouse["ClickTrace"]["add_one_1"]['y'],clicks=conf_mouse["ClickTrace"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickTrace"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickTrace"]["add_one_2"]['x'], y=conf_mouse["ClickTrace"]["add_one_2"]['y'],clicks=conf_mouse["ClickTrace"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickTrace"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_oldArrangement(self):  # 点击折叠安排
        auto.click(x=194, y=10, button='left', duration=0.2)
        auto.click(x=1038, y=51, button='left', duration=0.2)
        auto.click(x=1035, y=82, button='left', duration=0.2)

    def click_similate_xgpu(self):  #精确普通
        auto.click(x=120, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1251, y=61, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1251, y=140, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)


    def click_normal_similate(self):  #普通模拟
        auto.click(x=conf_mouse["ClickNormalSimilate"]["add_one_1"]['x'], y=conf_mouse["ClickNormalSimilate"]["add_one_1"]['y'],clicks=conf_mouse["ClickNormalSimilate"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickNormalSimilate"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNormalSimilate"]["add_one_2"]['x'], y=conf_mouse["ClickNormalSimilate"]["add_one_2"]['y'],clicks=conf_mouse["ClickNormalSimilate"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickNormalSimilate"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNormalSimilate"]["add_one_3"]['x'], y=conf_mouse["ClickNormalSimilate"]["add_one_3"]['y'],clicks=conf_mouse["ClickNormalSimilate"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickNormalSimilate"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickNormalSimilate"]["add_one_4"]['x'], y=conf_mouse["ClickNormalSimilate"]["add_one_4"]['y'],clicks=conf_mouse["ClickNormalSimilate"]["add_one_4"]['clicks'], interval=0.0,button=conf_mouse["ClickNormalSimilate"]["add_one_4"]['button'], duration=0.2, tween=auto.linear)

    def click_similate_cpu(self):  #模拟cpu
        auto.click(x=183, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1113, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1113, y=117, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_fixpin_box(self):  #固定针箱体
        auto.click(x=conf_mouse["ClickFixpinBox"]["add_one_1"]['x'], y=conf_mouse["ClickFixpinBox"]["add_one_1"]['y'],clicks=conf_mouse["ClickFixpinBox"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFixpinBox"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFixpinBox"]["add_one_2"]['x'], y=conf_mouse["ClickFixpinBox"]["add_one_2"]['y'],clicks=conf_mouse["ClickFixpinBox"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickFixpinBox"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickFixpinBox"]["add_one_3"]['x'], y=conf_mouse["ClickFixpinBox"]["add_one_3"]['y'],clicks=conf_mouse["ClickFixpinBox"]["add_one_3"]['clicks'], interval=0.0,button=conf_mouse["ClickFixpinBox"]["add_one_3"]['button'], duration=0.2, tween=auto.linear)

    def click_fixpin_lasso(self):  #固定针套绳
        auto.click(x=120, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=119, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_selectmesh_box(self):  #选择网格箱体
        auto.click(x=120, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=145, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_electmesh_lasso(self):  #选择网格套绳
        auto.click(x=120, y=20, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=60, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        auto.click(x=1153, y=171, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_photo_rendering(self):  #点击离线渲染
        auto.click(x=conf_mouse["ClickPhotoRendering"]["add_one_1"]['x'], y=conf_mouse["ClickPhotoRendering"]["add_one_1"]['y'],clicks=conf_mouse["ClickPhotoRendering"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickPhotoRendering"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickPhotoRendering"]["add_one_2"]['x'], y=conf_mouse["ClickPhotoRendering"]["add_one_2"]['y'],clicks=conf_mouse["ClickPhotoRendering"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickPhotoRendering"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_hide_style_2d(self):  #点击2D隐藏样式
        auto.click(x=610, y=165, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_hide_style_3d(self):  #点击3D隐藏样式
        auto.click(x=1340, y=163, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)

    def click_version(self): #点击关于版本信息
        auto.click(x=conf_mouse["ClickVersion"]["add_one_1"]['x'],y=conf_mouse["ClickVersion"]["add_one_1"]['y'],clicks=conf_mouse["ClickVersion"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickVersion"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickVersion"]["add_one_2"]['x'],y=conf_mouse["ClickVersion"]["add_one_2"]['y'],clicks=conf_mouse["ClickVersion"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickVersion"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_matte(self):#点击消光材质
        auto.moveRel(xOffset=100, yOffset=0, duration=0.2, tween=auto.linear)#从渲染类型偏移到消光列表
        auto.click()
        time.sleep(1)
        auto.moveRel(xOffset=0, yOffset=19, duration=0.2, tween=auto.linear)#移动到消光
        auto.click()

    def click_silk(self):#点击丝绸材质
        auto.moveRel(xOffset=100, yOffset=0, duration=0.2, tween=auto.linear)#从渲染类型偏移到消光列表
        auto.click()
        time.sleep(1)
        auto.moveRel(xOffset=0, yOffset=38, duration=0.2, tween=auto.linear)#移动到丝绸
        auto.click()

    def click_shiny(self):#点击反光材质
        auto.moveRel(xOffset=100, yOffset=0, duration=0.2, tween=auto.linear)#从渲染类型偏移到消光列表
        auto.click()
        time.sleep(1)
        auto.moveRel(xOffset=0, yOffset=52, duration=0.2, tween=auto.linear)#移动到丝绸
        auto.click()

    def click_velvet(self):#点击绒材质
        auto.moveRel(xOffset=100, yOffset=0, duration=0.2, tween=auto.linear)#从渲染类型偏移到消光列表
        auto.click()
        time.sleep(1)
        auto.moveRel(xOffset=0, yOffset=72, duration=0.2, tween=auto.linear)#移动到丝绸
        auto.click()

    def click_user_settings(self): #点击偏好设置
        auto.click(x=conf_mouse["ClickUserSettings"]["add_one_1"]['x'], y=conf_mouse["ClickUserSettings"]["add_one_1"]['y'],clicks=conf_mouse["ClickUserSettings"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickUserSettings"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["ClickUserSettings"]["add_one_2"]['x'], y=conf_mouse["ClickUserSettings"]["add_one_2"]['y'],clicks=conf_mouse["ClickUserSettings"]["add_one_2"]['clicks'], interval=0.0,button=conf_mouse["ClickUserSettings"]["add_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_FullnessPoint(self):  #点击延展(点)
        auto.click(x=conf_mouse["ClickFullnessPoint"]["add_one_1"]['x'], y=conf_mouse["ClickFullnessPoint"]["add_one_1"]['y'],clicks=conf_mouse["ClickFullnessPoint"]["add_one_1"]['clicks'], interval=0.0,button=conf_mouse["ClickFullnessPoint"]["add_one_1"]['button'], duration=0.2, tween=auto.linear)

    def test_click_grade(self, x, y, style, savePath):
        auto.click(x=x, y=y, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        new = savePath + style + '_new.png'
        old = savePath + style + '_old.png'
        OperationFile().comparison_picture_allure(new, old, style, 50)

    def click_walk(self):  #点击版片行走模式
        auto.click(x=conf_mouse["Walk"]["click_one_1"]['x'], y=conf_mouse["Walk"]["click_one_1"]['y'],clicks=conf_mouse["Walk"]["click_one_1"]['clicks'], interval=0.0,button=conf_mouse["Walk"]["click_one_1"]['button'], duration=0.2, tween=auto.linear)
        auto.click(x=conf_mouse["Walk"]["click_one_2"]['x'], y=conf_mouse["Walk"]["click_one_2"]['y'],clicks=conf_mouse["Walk"]["click_one_2"]['clicks'], interval=0.0,button=conf_mouse["Walk"]["click_one_2"]['button'], duration=0.2, tween=auto.linear)

    def click_UVeditor(self):#点击UV编辑器
        auto.click(x=248, y=14, button='left', duration=0.2)
        auto.click(x=452, y=55, button='left', duration=0.2)


    def send_message(self, content, mobiles_wang=None, mobiles_chen=None, mobiles_shen=None):
        from common.studio_cloud import Style3DCloud
        conf = self.get_conf_mouse()
        self.rectangle_creat()
        self.click_save_as_sproj()
        version_name = 'version' + str(time.time()).replace(".", "")[0:11]
        version_unzip_path = os.path.join(OperationFile().get_garder_path('studio'), 'export')
        version_sproj_path = os.path.join(OperationFile().get_garder_path('studio'), 'export') + '\\' + version_name + ".sproj"
        pyperclip.copy(version_sproj_path)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(1)
        auto.press('enter')
        time.sleep(5)

        # auto.click(x=conf["Send_message"]["click_one_2"]["x"],y=conf["Send_message"]["click_one_2"]["y"],clicks=conf["Send_message"]["click_one_2"]["clicks"],button=conf["Send_message"]["click_one_2"]["button"], duration=0.2)
        # time.sleep(3)
        auto.click(x=conf["Send_message"]["click_one_1"]["x"],y=conf["Send_message"]["click_one_1"]["y"],clicks=conf["Send_message"]["click_one_1"]["clicks"],button=conf["Send_message"]["click_one_1"]["button"], duration=0.2)

        OperationFile().unzip_file(version_sproj_path, version_unzip_path)
        json_file = version_unzip_path + '\\' + "project.json"
        with open(json_file, 'r', encoding='utf-8') as f:
            cont = json.load(f)
        self.log.info(cont["_appVersion"])
        appVersion = cont["_appVersion"]
        Style3DCloud().send_message(content, appVersion, mobiles_wang, mobiles_chen, mobiles_shen)
if __name__ == '__main__':  # 运营此文件来验证写是否正确

    pass