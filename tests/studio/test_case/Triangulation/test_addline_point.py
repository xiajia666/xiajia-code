import os
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
import allure
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


@allure.feature('版片上增加线，点，移动')
@allure.severity(allure.severity_level.BLOCKER)
class TestAddlinePoint:

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
        self.style.send_message("Style3D 三角化专项测试开始，本次测试版本号：", "18069806966")

    @allure.story('表面翻转')
    def test_flip_normal_one(self):
        self.style.add_open_sproj('sproj', 'jira17388表面翻转.sproj')
        time.sleep(10)
        auto.press('2')
        auto.click(x=conf["Triangulation"]["flip_normal_one_1"]["x"], y=conf["Triangulation"]["flip_normal_one_1"]["y"], clicks=conf["Triangulation"]["flip_normal_one_1"]["clicks"],button=conf["Triangulation"]["flip_normal_one_1"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["flip_normal_one_3"]["x"], y=conf["Triangulation"]["flip_normal_one_3"]["y"], clicks=conf["Triangulation"]["flip_normal_one_3"]["clicks"],button=conf["Triangulation"]["flip_normal_one_3"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["flip_normal_one_5"]["x"], y=conf["Triangulation"]["flip_normal_one_5"]["y"], clicks=conf["Triangulation"]["flip_normal_one_5"]["clicks"],button=conf["Triangulation"]["flip_normal_one_5"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "jira17388表面翻转"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('点')
    def test_point_one(self):
        self.style.add_open_sproj('sproj', 'jira17546，版片点太多，导致模拟崩溃.sproj')
        time.sleep(15)
        auto.press('2')
        self.style.focus_panorama()
        auto.mouseDown(x=conf["Triangulation"]["point_one_1"]["x"], y=conf["Triangulation"]["point_one_1"]["y"],button=conf["Triangulation"]["point_one_1"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Triangulation"]["point_one_2up"]["x"], y=conf["Triangulation"]["point_one_2up"]["y"],button=conf["Triangulation"]["point_one_2up"]["button"], duration=0.2)
        time.sleep(4)
        auto.click(x=conf["Triangulation"]["point_one_3"]["x"], y=conf["Triangulation"]["point_one_3"]["y"], clicks=conf["Triangulation"]["point_one_3"]["clicks"],button=conf["Triangulation"]["point_one_3"]["button"], duration=0.2)
        auto.typewrite("19")
        auto.click(x=conf["Triangulation"]["point_one_7"]["x"], y=conf["Triangulation"]["point_one_7"]["y"], clicks=conf["Triangulation"]["point_one_7"]["clicks"],button=conf["Triangulation"]["point_one_7"]["button"], duration=0.2)
        auto.press('space')
        time.sleep(10)
        style = "jira17546，版片点太多，导致模拟崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('基础线')
    def test_baseline_one(self):
        self.style.add_open_sproj('sproj', 'jira17552, 基础线重叠，勾勒了三角化异常，模拟后，3D版片断开了.sproj')
        time.sleep(15)
        auto.press('2')
        self.style.focus_panorama()
        auto.click(x=conf["Triangulation"]["baseline_one_1"]["x"], y=conf["Triangulation"]["baseline_one_1"]["y"], clicks=conf["Triangulation"]["baseline_one_1"]["clicks"],button=conf["Triangulation"]["baseline_one_1"]["button"], duration=0.2)
        auto.mouseDown(x=conf["Triangulation"]["baseline_one_3"]["x"], y=conf["Triangulation"]["baseline_one_3"]["y"],button=conf["Triangulation"]["baseline_one_3"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Triangulation"]["baseline_one_4up"]["x"], y=conf["Triangulation"]["baseline_one_4up"]["y"],button=conf["Triangulation"]["baseline_one_4up"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["baseline_one_5"]["x"], y=conf["Triangulation"]["baseline_one_5"]["y"], clicks=conf["Triangulation"]["baseline_one_5"]["clicks"],button=conf["Triangulation"]["baseline_one_5"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.press("i")
        auto.click(x=conf["Triangulation"]["baseline_one_15"]["x"], y=conf["Triangulation"]["baseline_one_15"]["y"], clicks=conf["Triangulation"]["baseline_one_15"]["clicks"],button=conf["Triangulation"]["baseline_one_15"]["button"], duration=0.2)
        auto.press("enter")
        auto.press("space")
        time.sleep(10)
        style = "jira17552, 基础线重叠，勾勒了三角化异常，模拟后，3D版片断开了"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


    @allure.story('内部线')
    def test_internalline_one(self):
        self.style.add_open_sproj('sproj', 'jira16713,  内部线位置，网格破洞.sproj')
        time.sleep(15)
        auto.press('2')
        self.style.focus_panorama()
        auto.click(x=conf["Triangulation"]["internalline_one_1"]["x"], y=conf["Triangulation"]["internalline_one_1"]["y"], clicks=conf["Triangulation"]["internalline_one_1"]["clicks"],button=conf["Triangulation"]["internalline_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.mouseDown(x=conf["Triangulation"]["internalline_one_11"]["x"], y=conf["Triangulation"]["internalline_one_11"]["y"],button=conf["Triangulation"]["internalline_one_11"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Triangulation"]["internalline_one_12up"]["x"], y=conf["Triangulation"]["internalline_one_12up"]["y"],button=conf["Triangulation"]["internalline_one_12up"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["internalline_one_13"]["x"], y=conf["Triangulation"]["internalline_one_13"]["y"], clicks=conf["Triangulation"]["internalline_one_13"]["clicks"],button=conf["Triangulation"]["internalline_one_13"]["button"], duration=0.2)
        auto.press("space")
        time.sleep(2)
        auto.press("space")
        auto.click(x=conf["Triangulation"]["internalline_one_17"]["x"], y=conf["Triangulation"]["internalline_one_17"]["y"], clicks=conf["Triangulation"]["internalline_one_17"]["clicks"],button=conf["Triangulation"]["internalline_one_17"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.click(x=conf["Triangulation"]["internalline_one_23"]["x"], y=conf["Triangulation"]["internalline_one_23"]["y"], clicks=conf["Triangulation"]["internalline_one_23"]["clicks"],button=conf["Triangulation"]["internalline_one_23"]["button"], duration=0.2)
        time.sleep(2)
        style = "jira16713,  内部线位置，网格破洞"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 130, 300, 700, 900)



    @allure.story('jira15787，由于内部线间距太小，又有缝纫线，导致模拟后三角化异常-内部线2')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-14640',name='jira15787')
    def test_internalline_two(self):
        self.style.add_open_sproj('sproj', 'jira15787，由于内部线间距太小，又有缝纫线，导致模拟后三角化异常.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.mouseDown(x=240, y=366,button='left', duration=0.2)  #框选版片
        auto.mouseUp(x=559, y=429,button='left', duration=0.2)
        auto.click(x=1873, y=565, button='left', duration=0.2)  # 点击粒子间距
        auto.typewrite('6')
        auto.press('enter')
        time.sleep(2)
        auto.click(x=341, y=366, button='left', duration=0.2)  # 点击放大视角查看2D版片网格
        self.style.scroll_big_number(13)
        time.sleep(2)
        style = "jira15787，由于内部线间距太小，又有缝纫线，导致模拟后三角化异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 96, 397, 1536, 800)

    @allure.story('jira14640, 对齐到净边后缝纫线异常-内部线对齐到净边')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-14640',name='jira14640')
    def test_extend_to_outline_one(self):
        self.style.add_open_sproj('sproj', 'jira14640, 对齐到净边后缝纫线异常.sproj')
        self.style.focus_panorama()
        auto.press('z')
        auto.click(x=596, y=736, button='right', duration=0.2)  # 点击内部线右键
        auto.click(x=656, y=593, button='left', duration=0.2)  # 点击对齐
        auto.click(x=782, y=588, button='left', duration=0.2)  # 点击对齐到净边
        time.sleep(4)
        style = "jira14640, 对齐到净边后缝纫线异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 130, 300, 700, 900)

    @allure.story('jira16433，袖子版片，右键点击移动到里面后，帽子版片三角化不正确--移动到里面')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-16433',name='jira16433')
    def test_superimpose_under_one(self):
        self.style.add_open_sproj('sproj', 'jira16433，袖子版片，右键点击移动到里面后，帽子版片三角化不正确.sproj')
        self.style.focus_panorama()
        auto.click(x=440, y=336, button='left', duration=0.2)  # 点击放大视角查看2D版片网格
        self.style.scroll_big_number(7)
        auto.click(x=1021, y=813, button='right', duration=0.2)  #3D右键点击版片
        auto.click(x=1069, y=665, button='right', duration=0.2)  #点击移动到里面
        time.sleep(4)
        style = "jira16433，袖子版片，右键点击移动到里面后，帽子版片三角化不正确"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 96, 397, 1536, 800)

