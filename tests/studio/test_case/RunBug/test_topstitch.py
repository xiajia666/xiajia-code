# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('明线')
@allure.severity(allure.severity_level.CRITICAL)
class TestTopstitch:

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

    @allure.story('明线崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug#viewIdentifier=1dedc5afd44979211cad516f&openWorkitemIdentifier=22e3c980bc29e5ae7e8dba366f', name='STUDIO-4987')
    def test_topstitch_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-4987，附件工程点击编辑明线模式软件崩溃.sproj', '2')
        self.style.focus_panorama()
        auto.click(x=conf["RunBug"]["topstitch_one_1"]["x"], y=conf["RunBug"]["topstitch_one_1"]["y"], clicks=conf["RunBug"]["topstitch_one_1"]["clicks"],button=conf["RunBug"]["topstitch_one_1"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_one_2"]["x"], y=conf["RunBug"]["topstitch_one_2"]["y"], clicks=conf["RunBug"]["topstitch_one_2"]["clicks"],button=conf["RunBug"]["topstitch_one_2"]["button"], duration=0.2)
        style = "STUDIO-4987，附件工程点击编辑明线模式软件崩溃"
        new = "\\RunBug\\Topstitch\\"+style+"_new.png"
        old = "\\RunBug\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('边缘对称增加明线，明线延伸')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/45455899c911134c0d9fc958be#viewIdentifier=1dedc5afd44979211cad516f', name='STUDIO-967')
    def test_topstitch_two(self):
        self.style.add_open_sproj('sproj', '边缘对称增加明线，明线延伸.sproj', '2')
        self.style.focus_panorama()
        auto.click(x=conf["RunBug"]["topstitch_two_1"]["x"], y=conf["RunBug"]["topstitch_two_1"]["y"], clicks=conf["RunBug"]["topstitch_two_1"]["clicks"],button=conf["RunBug"]["topstitch_two_1"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_two_3"]["x"], y=conf["RunBug"]["topstitch_two_3"]["y"], clicks=conf["RunBug"]["topstitch_two_3"]["clicks"],button=conf["RunBug"]["topstitch_two_3"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_two_7"]["x"], y=conf["RunBug"]["topstitch_two_7"]["y"], clicks=conf["RunBug"]["topstitch_two_7"]["clicks"],button=conf["RunBug"]["topstitch_two_7"]["button"], duration=0.2)
        time.sleep(1)
        style = "边缘对称增加明线，明线延伸"
        new = "\\RunBug\\Topstitch\\"+style+"_new.png"
        old = "\\RunBug\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-875明线凹痕')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/bc099fd0a3668de6ac829e562b#viewIdentifier=1dedc5afd44979211cad516f', name='STUDIO-875')
    def test_topstitch_three(self):
        self.style.add_open_sproj('sproj', 'STUDIO-875明线凹痕不对.sproj', '2')
        self.style.focus_panorama()
        auto.click(x=conf["RunBug"]["topstitch_three_1"]["x"], y=conf["RunBug"]["topstitch_three_1"]["y"], clicks=conf["RunBug"]["topstitch_three_1"]["clicks"],button=conf["RunBug"]["topstitch_three_1"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_3"]["x"], y=conf["RunBug"]["topstitch_three_3"]["y"], clicks=conf["RunBug"]["topstitch_three_3"]["clicks"],button=conf["RunBug"]["topstitch_three_3"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_5"]["x"], y=conf["RunBug"]["topstitch_three_5"]["y"], clicks=conf["RunBug"]["topstitch_three_5"]["clicks"],button=conf["RunBug"]["topstitch_three_5"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_7"]["x"], y=conf["RunBug"]["topstitch_three_7"]["y"], clicks=conf["RunBug"]["topstitch_three_7"]["clicks"],button=conf["RunBug"]["topstitch_three_7"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_9"]["x"], y=conf["RunBug"]["topstitch_three_9"]["y"], clicks=conf["RunBug"]["topstitch_three_9"]["clicks"],button=conf["RunBug"]["topstitch_three_9"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_11"]["x"], y=conf["RunBug"]["topstitch_three_11"]["y"], clicks=conf["RunBug"]["topstitch_three_11"]["clicks"],button=conf["RunBug"]["topstitch_three_11"]["button"], duration=0.2)
        auto.click(x=conf["RunBug"]["topstitch_three_13"]["x"], y=conf["RunBug"]["topstitch_three_13"]["y"], clicks=conf["RunBug"]["topstitch_three_13"]["clicks"],button=conf["RunBug"]["topstitch_three_13"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.mouseDown(x=conf["RunBug"]["topstitch_three_20"]["x"], y=conf["RunBug"]["topstitch_three_20"]["y"],button=conf["RunBug"]["topstitch_three_20"]["button"], duration=0.2)
        auto.mouseUp(x=conf["RunBug"]["topstitch_three_21up"]["x"], y=conf["RunBug"]["topstitch_three_21up"]["y"],button=conf["RunBug"]["topstitch_three_21up"]["button"], duration=0.2)
        time.sleep(1)
        style = "增加明线凹痕"
        new = "\\RunBug\\Topstitch\\"+style+"_new.png"
        old = "\\RunBug\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-6786明线凹痕')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/444724f7ef079699e92253e67a',name='STUDIO-6786')
    def test_topstitch_four(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6786明线凹痕位置不对.sproj', '2')
        self.style.focus_panorama()
        time.sleep(1)
        auto.mouseDown(x=880, y=550, button='left', duration=0.2)
        self.style.scroll_big_number(5)
        style = "开启明线凹痕，凹痕显示位置不对"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-5995明线凹痕---sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/67c31d36e0a8d52920aac8b888',name='STUDIO-5995')
    def test_topstitch_five(self):
        self.style.add_open_sproj('sproj', 'STUDIO-5995.sproj')
        time.sleep(2)
        style = "STUDIO-5995明线凹痕"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-3159明线的针间距设为负数后，再新增明线，软件会卡死-sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/22e3c980bc29e5ae7e8dba366f',name='STUDIO-3159')
    def test_topstitch_six(self):
        self.style.add_open_sproj('sproj', 'STUDIO-3159.sproj')
        self.style.focus_panorama()
        time.sleep(1)
        auto.click(x=1602, y=284, button='left', duration=0.2)  # 当前栏-明线
        auto.click(x=1650, y=179, button='left', duration=0.2)  # 皮革明线
        auto.click(x=1885, y=771, button='left', duration=0.2)  # 针间距
        self.style.click_backspace_number(8)
        auto.typewrite(message='-0.10', interval=0.5)
        auto.click(x=669, y=54, button='left', duration=0.2)  # 线段明线
        auto.click(x=409, y=292, button='left', duration=0.2)  # 新增
        time.sleep(15)
        style = "STUDIO-3159明线的针间距设为负数后，再新增明线，软件会卡死"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-2391附件工程由于明线错误，模拟后崩溃-sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/982ecc0b3fd1131feac438e630',name='STUDIO-2391')
    def test_topstitch_seven(self):
        self.style.add_open_sproj('sproj', 'STUDIO-2391.sproj')
        self.style.focus_panorama()
        time.sleep(1)
        self.style.click_normal_similate()
        time.sleep(15)
        style = "STUDIO-2391附件工程由于明线错误，模拟后崩溃"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


    @allure.story('STUDIO-747项目文件，明线异常，修改粒子间距为11以上后正常-wangquan')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/717d2f2599eeb12c7f1418f892',name='STUDIO-747')
    def test_topstitch_eight(self):
        self.style.add_open_sproj('sproj', 'STUDIO-747项目文件，明线异常，修改粒子间距为11以上后正常.sproj')
        time.sleep(10)
        style = "STUDIO-747项目文件，明线异常，修改粒子间距为11以上后正常"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 846, 277, 1546, 923)

    @allure.story('STUDIO-7910添加整圈明线，开启圆角崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/0985850ec9c8a431ed61706791',name='STUDIO-7910')
    def test_topstitch_nine(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7910.sproj')
        self.style.focus_panorama()
        time.sleep(1)
        self.style.click_free_topstitch()
        auto.doubleClick(x=135, y=607, button='left', duration=0.2) #双击添加整圈明线
        time.sleep(2)
        auto.click(x=1888, y=647, clicks=1, button='left', duration=0.2) #开启圆角
        time.sleep(1)
        style = "STUDIO-7910添加整圈明线，开启圆角崩溃"
        new = "\\RunBug\\Topstitch\\" + style + "_new.png"
        old = "\\RunBug\\Topstitch\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

