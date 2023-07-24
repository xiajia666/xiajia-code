import os
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
import allure
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


@allure.feature('崩溃工程')
@allure.severity(allure.severity_level.BLOCKER)
class TestDump:

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

    @allure.story('jira17647, 打开后模拟，程序崩溃')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17647',name='jira16433')
    def test_dump_one(self):
        self.style.add_open_sproj('sproj', 'jira17647, 打开后模拟，程序崩溃.sproj')
        time.sleep(10)
        auto.press('space')
        time.sleep(15)
        style = "jira17647, 打开后模拟，程序崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('jira17398,  全选改粒子间距为15，程序崩溃')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17398',name='jira17398')
    def test_dump_two(self):
        self.style.add_open_sproj('sproj', 'jira17398,  全选改粒子间距为15，程序崩溃.sproj')
        time.sleep(10)
        auto.press('2')
        self.style.focus_panorama()
        time.sleep(3)
        auto.mouseDown(x=107, y=192,button='left', duration=0.2)  #框选版片
        auto.mouseUp(x=691, y=948,button='left', duration=0.2)
        time.sleep(10)
        auto.click(x=1873, y=565, button='left', duration=0.2)  # 点击粒子间距
        auto.typewrite('15')
        auto.press('enter')
        time.sleep(10)
        style = "jira17398,  全选改粒子间距为15，程序崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('Jira17420,改粒子度6后再改回5模拟，崩溃')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17420',name='17420')
    def test_dump_three(self):
        self.style.add_open_sproj('sproj', 'Jira17420,改粒子度后模拟，崩溃.sproj')
        time.sleep(10)
        auto.press('2')
        self.style.focus_panorama()
        auto.mouseDown(x=91, y=286,button='left', duration=0.2)  #框选版片
        auto.mouseUp(x=722, y=874,button='left', duration=0.2)
        time.sleep(5)
        auto.click(x=1873, y=565, button='left', duration=0.2)  # 点击粒子间距
        auto.typewrite('6')
        auto.press('enter')
        time.sleep(4)
        auto.click(x=1873, y=565, button='left', duration=0.2)  # 点击粒子间距
        auto.typewrite('5')
        auto.press('enter')
        time.sleep(4)
        auto.press('space')
        style = "Jira17420,改粒子度6后再改回5模拟，崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


