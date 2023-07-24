import os
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
import allure
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


@allure.feature('形状修改')
@allure.severity(allure.severity_level.BLOCKER)
class TestShapeModification:

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


    @allure.story('合并')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17179', name='jira17179')
    def test_merge_one(self):
        self.style.add_open_sproj('sproj', 'jira17179，项目文件，合并后，版片表面翻转了.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=conf["Triangulation"]["merge_one_1"]["x"], y=conf["Triangulation"]["merge_one_1"]["y"], clicks=conf["Triangulation"]["merge_one_1"]["clicks"],button=conf["Triangulation"]["merge_one_1"]["button"], duration=0.2)
        auto.typewrite("z")
        auto.mouseDown(x=conf["Triangulation"]["merge_one_4"]["x"], y=conf["Triangulation"]["merge_one_4"]["y"],button=conf["Triangulation"]["merge_one_4"]["button"], duration=0.2)
        auto.mouseUp(x=conf["Triangulation"]["merge_one_5up"]["x"], y=conf["Triangulation"]["merge_one_5up"]["y"],button=conf["Triangulation"]["merge_one_5up"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["merge_one_6"]["x"], y=conf["Triangulation"]["merge_one_6"]["y"], clicks=conf["Triangulation"]["merge_one_6"]["clicks"],button=conf["Triangulation"]["merge_one_6"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["merge_one_8"]["x"], y=conf["Triangulation"]["merge_one_8"]["y"], clicks=conf["Triangulation"]["merge_one_8"]["clicks"],button=conf["Triangulation"]["merge_one_8"]["button"], duration=0.2)
        time.sleep(2)
        time.sleep(0.5)
        style = "jira17179，项目文件，合并后，版片表面翻转了"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('剪切1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17205', name='jira17205')
    def test_cut_one(self):
        self.style.add_open_sproj('sproj', 'jira17205， 剪切后，缝纫线异常.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=conf["Triangulation"]["cut_one_1"]["x"], y=conf["Triangulation"]["cut_one_1"]["y"], clicks=conf["Triangulation"]["cut_one_1"]["clicks"],button=conf["Triangulation"]["cut_one_1"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["cut_one_3"]["x"], y=conf["Triangulation"]["cut_one_3"]["y"], clicks=conf["Triangulation"]["cut_one_3"]["clicks"],button=conf["Triangulation"]["cut_one_3"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.typewrite("z")
        auto.click(x=conf["Triangulation"]["cut_one_9"]["x"], y=conf["Triangulation"]["cut_one_9"]["y"], clicks=conf["Triangulation"]["cut_one_9"]["clicks"],button=conf["Triangulation"]["cut_one_9"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["cut_one_11"]["x"], y=conf["Triangulation"]["cut_one_11"]["y"], clicks=conf["Triangulation"]["cut_one_11"]["clicks"],button=conf["Triangulation"]["cut_one_11"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["cut_one_13"]["x"], y=conf["Triangulation"]["cut_one_13"]["y"], clicks=conf["Triangulation"]["cut_one_13"]["clicks"],button=conf["Triangulation"]["cut_one_13"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Triangulation"]["cut_one_15"]["x"], y=conf["Triangulation"]["cut_one_15"]["y"], clicks=conf["Triangulation"]["cut_one_15"]["clicks"],button=conf["Triangulation"]["cut_one_15"]["button"], duration=0.2)
        self.style.scroll_small_number(1)
        auto.typewrite("b")
        auto.click(x=conf["Triangulation"]["cut_one_19"]["x"], y=conf["Triangulation"]["cut_one_19"]["y"], clicks=conf["Triangulation"]["cut_one_19"]["clicks"],button=conf["Triangulation"]["cut_one_19"]["button"], duration=0.2)
        time.sleep(2)
        style = "jira17205， 剪切后，缝纫线异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150, 66, 233, 733, 917)

    @allure.story('剪切1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17205', name='jira17205')
    def test_cut_two(self):
        self.style.add_open_sproj('sproj', 'jira15181，剪切后网格异常LD014-XY-FSF001.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=conf["Triangulation"]["cut_two_1"]["x"], y=conf["Triangulation"]["cut_two_1"]["y"], clicks=conf["Triangulation"]["cut_two_1"]["clicks"],button=conf["Triangulation"]["cut_two_1"]["button"], duration=0.2)
        auto.typewrite("z")
        auto.click(x=conf["Triangulation"]["cut_two_4"]["x"], y=conf["Triangulation"]["cut_two_4"]["y"], clicks=conf["Triangulation"]["cut_two_4"]["clicks"],button=conf["Triangulation"]["cut_two_4"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["cut_two_6"]["x"], y=conf["Triangulation"]["cut_two_6"]["y"], clicks=conf["Triangulation"]["cut_two_6"]["clicks"],button=conf["Triangulation"]["cut_two_6"]["button"], duration=0.2)
        time.sleep(2)
        style = "jira15181，剪切后网格异常LD014-XY-FSF001"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150, 66, 233, 733, 917)

    @allure.story('粒子度1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17510', name='jira17510')
    def test_particle_distance_one(self):
        self.style.add_open_sproj('sproj', 'jira17510，粒子度为5，精确模拟版片消失.sproj')
        time.sleep(15)
        auto.press('2')
        auto.press('space')
        time.sleep(15)
        style = "jira17510，粒子度为5，精确模拟版片消失"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150, 904, 300, 1500, 850)

    @allure.story('粒子度2')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17738', name='jira17738')
    def test_particle_distance_two(self):
        self.style.add_open_sproj('sproj', 'jira17738，两个细小板片粒子度改为1后，精确模拟软件崩溃.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.click(x=conf["Triangulation"]["particle_distance_two_1"]["x"], y=conf["Triangulation"]["particle_distance_two_1"]["y"], clicks=conf["Triangulation"]["particle_distance_two_1"]["clicks"],button=conf["Triangulation"]["particle_distance_two_1"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["particle_distance_two_3"]["x"], y=conf["Triangulation"]["particle_distance_two_3"]["y"], clicks=conf["Triangulation"]["particle_distance_two_3"]["clicks"],button=conf["Triangulation"]["particle_distance_two_3"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Triangulation"]["particle_distance_two_5"]["x"], y=conf["Triangulation"]["particle_distance_two_5"]["y"], clicks=conf["Triangulation"]["particle_distance_two_5"]["clicks"],button=conf["Triangulation"]["particle_distance_two_5"]["button"], duration=0.2)
        auto.typewrite("1")
        auto.press("enter")
        auto.click(x=conf["Triangulation"]["particle_distance_two_6"]["x"], y=conf["Triangulation"]["particle_distance_two_6"]["y"], clicks=conf["Triangulation"]["particle_distance_two_6"]["clicks"],button=conf["Triangulation"]["particle_distance_two_6"]["button"], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["Triangulation"]["particle_distance_two_10"]["x"], y=conf["Triangulation"]["particle_distance_two_10"]["y"], clicks=conf["Triangulation"]["particle_distance_two_10"]["clicks"],button=conf["Triangulation"]["particle_distance_two_10"]["button"], duration=0.2)
        time.sleep(10)
        style = "jira17738，两个细小板片粒子度改为1后，精确模拟软件崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150)

    @allure.story('设为对称轴')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17359', name='jira17359')
    def test_convert_to_symmetry_axis_one(self):
        self.style.add_open_sproj('sproj', 'jira17359设为对称轴后，三角化效果不理想.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.click(x=conf["Triangulation"]["convert_to_symmetry_axis_one_1"]["x"], y=conf["Triangulation"]["convert_to_symmetry_axis_one_1"]["y"], clicks=conf["Triangulation"]["convert_to_symmetry_axis_one_1"]["clicks"],button=conf["Triangulation"]["convert_to_symmetry_axis_one_1"]["button"], duration=0.2)
        auto.typewrite("z")
        auto.click(x=conf["Triangulation"]["convert_to_symmetry_axis_one_4"]["x"], y=conf["Triangulation"]["convert_to_symmetry_axis_one_4"]["y"], clicks=conf["Triangulation"]["convert_to_symmetry_axis_one_4"]["clicks"],button=conf["Triangulation"]["convert_to_symmetry_axis_one_4"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["convert_to_symmetry_axis_one_6"]["x"], y=conf["Triangulation"]["convert_to_symmetry_axis_one_6"]["y"], clicks=conf["Triangulation"]["convert_to_symmetry_axis_one_6"]["clicks"],button=conf["Triangulation"]["convert_to_symmetry_axis_one_6"]["button"], duration=0.2)
        auto.typewrite("i")
        auto.click(x=conf["Triangulation"]["convert_to_symmetry_axis_one_9"]["x"], y=conf["Triangulation"]["convert_to_symmetry_axis_one_9"]["y"], clicks=conf["Triangulation"]["convert_to_symmetry_axis_one_9"]["clicks"],button=conf["Triangulation"]["convert_to_symmetry_axis_one_9"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["convert_to_symmetry_axis_one_11"]["x"], y=conf["Triangulation"]["convert_to_symmetry_axis_one_11"]["y"], clicks=conf["Triangulation"]["convert_to_symmetry_axis_one_11"]["clicks"],button=conf["Triangulation"]["convert_to_symmetry_axis_one_11"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "jira17359设为对称轴后，三角化效果不理想"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 58, 287, 770, 820)

    @allure.story('延展')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-16938', name='jira16938')
    def test_fullness_one(self):
        self.style.add_open_sproj('sproj', 'jira16938,  选中内部线延展，版片炸裂（给开发）.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.click(x=conf["Triangulation"]["fullness_one_1"]["x"], y=conf["Triangulation"]["fullness_one_1"]["y"], clicks=conf["Triangulation"]["fullness_one_1"]["clicks"],button=conf["Triangulation"]["fullness_one_1"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["fullness_one_3"]["x"], y=conf["Triangulation"]["fullness_one_3"]["y"], clicks=conf["Triangulation"]["fullness_one_3"]["clicks"],button=conf["Triangulation"]["fullness_one_3"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["fullness_one_5"]["x"], y=conf["Triangulation"]["fullness_one_5"]["y"], clicks=conf["Triangulation"]["fullness_one_5"]["clicks"],button=conf["Triangulation"]["fullness_one_5"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["fullness_one_7"]["x"], y=conf["Triangulation"]["fullness_one_7"]["y"], clicks=conf["Triangulation"]["fullness_one_7"]["clicks"],button=conf["Triangulation"]["fullness_one_7"]["button"], duration=0.2)
        auto.click(x=conf["Triangulation"]["fullness_one_9"]["x"], y=conf["Triangulation"]["fullness_one_9"]["y"], clicks=conf["Triangulation"]["fullness_one_9"]["clicks"],button=conf["Triangulation"]["fullness_one_9"]["button"], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Triangulation"]["fullness_one_11"]["x"], y=conf["Triangulation"]["fullness_one_11"]["y"], clicks=conf["Triangulation"]["fullness_one_11"]["clicks"],button=conf["Triangulation"]["fullness_one_11"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "jira16938,选中内部线延展，版片炸裂（给开发）"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50, 56, 118, 748, 939)

    @allure.story('自交')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-16807', name='jira16807')
    def test_intersection_one(self):
        self.style.add_open_sproj('sproj', 'jira16807, 有个边缘对称版片，进行三角化操作后，会提示自交.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.click(x=conf["Triangulation"]["intersection_one_1"]["x"], y=conf["Triangulation"]["intersection_one_1"]["y"], clicks=conf["Triangulation"]["intersection_one_1"]["clicks"],button=conf["Triangulation"]["intersection_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        self.style.scroll_big_number(1)
        auto.typewrite("z")
        time.sleep(1)
        auto.mouseDown(x=conf["Triangulation"]["intersection_one_14"]["x"], y=conf["Triangulation"]["intersection_one_14"]["y"],button=conf["Triangulation"]["intersection_one_14"]["button"], duration=0.2)
        time.sleep(2)
        auto.mouseUp(x=conf["Triangulation"]["intersection_one_15up"]["x"], y=conf["Triangulation"]["intersection_one_15up"]["y"],button=conf["Triangulation"]["intersection_one_15up"]["button"], duration=0.2)
        time.sleep(2.5)
        style = "jira16807, 有个边缘对称版片，进行三角化操作后，会提示自交"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


