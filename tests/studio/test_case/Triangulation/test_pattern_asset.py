import os
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
import allure
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


@allure.feature('版片附属物')
@allure.severity(allure.severity_level.BLOCKER)
class TestPatternAsset:

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


    @allure.story('缝边')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-15487', name='jira15487')
    def test_seam_allowance_one(self):
        self.style.add_open_sproj('sproj', 'jira15487, 因为缝边，点击2D快照，程序崩溃.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        self.style.click_snapshot_2d()
        time.sleep(4)
        style = "jira15487, 因为缝边，点击2D快照，程序崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('明线1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-15468', name='jira15468')
    def test_topstitch_one(self):
        self.style.add_open_sproj('sproj', 'jira15468, 明线异常，少了一部分.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=547, y=516, clicks=1, button='left', duration=0.2)  # 点击长方型版片
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('9')
        auto.press('enter')
        time.sleep(5)
        style = "jira15468, 明线异常，少了一部分"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('明线2')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17558', name='jira17558')
    def test_topstitch_two(self):
        self.style.add_open_sproj('sproj', 'jira17558，明线导致模拟崩溃.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=1344, y=58, clicks=1, button='left', duration=0.2)  # 点击模拟
        time.sleep(20)
        style = "jira17558，明线导致模拟崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('明线3')
    @allure.issue('hhttps://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d2817712862a00b329f3cb5ef9', name='STUDIO-6272')
    def test_topstitch_three(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6272，项目文件打开后，明线网格异常.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=464, y=514, clicks=1, button='left', duration=0.2)  # 点击版片
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('9')
        auto.press('enter')
        time.sleep(5)
        style = "STUDIO-6272，项目文件打开后，明线网格异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('嵌条')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-3235', name='jira3235')
    def test_piping_one(self):
        self.style.add_open_sproj('sproj', 'jira3235嵌条在工程的边上创建时，拉链会发生位移变化.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_piping()
        auto.click(x=1010, y=181, clicks=1, button='left', duration=0.2)  # 在3D添加嵌条
        auto.click(x=1309, y=181, clicks=2, button='left', duration=0.2)  # 在3D添加嵌条
        time.sleep(5)
        style = "jira3235嵌条在工程的边上创建时，拉链会发生位移变化"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150, 66, 233, 733, 917)

    @allure.story('贴边')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-15680', name='jira15680')
    def test_binding_one(self):
        self.style.add_open_sproj('sproj', 'jira15680, 加贴边后边缘对称，三角化网格异常.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.press('z')
        auto.click(x=643, y=518, clicks=1, button='right', duration=0.2)  # 点击净边
        auto.click(x=686, y=586, clicks=1, button='left', duration=0.2)  # 生成边缘对称
        time.sleep(2)
        style = "jira15680, 加贴边后边缘对称，三角化网格异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150, 904, 300, 1500, 850)

    @allure.story('图案1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-16139', name='jira16139')
    def test_graphic_one(self):
        self.style.add_open_sproj('sproj', 'jira16139, 版片有洞的情况下，图案横跨洞两侧，则会导致图案三角化异常.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.mouseDown(x=88, y=322, button='left', duration=0.2)
        auto.mouseUp(x=712, y=789, button='left', duration=0.2)
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('9')
        auto.press('enter')
        time.sleep(5)
        style = "jira16139, 版片有洞的情况下，图案横跨洞两侧，则会导致图案三角化异常"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150)

    @allure.story('图案2')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17729', name='jira17729')
    def test_graphic_two(self):
        self.style.add_open_sproj('sproj', 'jira17729，版片粒子度为3时，图案显示不全.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.mouseDown(x=88, y=322, button='left', duration=0.2)
        auto.mouseUp(x=712, y=789, button='left', duration=0.2)
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('3')
        auto.press('enter')
        auto.click(x=991, y=605, clicks=1, button='left', duration=0.2)  # 弹框点击是
        time.sleep(5)
        style = "jira17729，版片粒子度为3时，图案显示不全.sproj"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 150)

    @allure.story('粘衬条1')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-15326', name='jira15326')
    def test_seam_taping_one(self):
        self.style.add_open_sproj('sproj', 'jira15326, 因为粘衬条，选择净边，生成等距内部线，间距5mm，使用延伸，点击确定后，程序崩溃.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.press('2')
        auto.press('z')
        auto.click(x=320, y=333, clicks=1, button='left', duration=0.2)  # 选择净边
        auto.keyDown('shift')
        auto.click(x=455, y=348, clicks=1, button='left', duration=0.2)  # 选择净边
        auto.keyUp('shift')
        auto.click(x=455, y=348, clicks=1, button='right', duration=0.2)  # 右键
        auto.click(x=504, y=465, clicks=1, button='left', duration=0.2)  # 生成等距内部线
        auto.typewrite('5')
        auto.click(x=832, y=585, clicks=1, button='left', duration=0.2)  # 点击使用延伸
        auto.click(x=840, y=617, clicks=1, button='left', duration=0.2)  # 点击延伸到净边
        auto.click(x=993, y=664, clicks=1, button='left', duration=0.2)  # 点击确定
        time.sleep(5)
        style = "jira15326, 因为粘衬条，选择净边，生成等距内部线，间距5mm，使用延伸，点击确定后，程序崩溃"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('粘衬条2')
    @allure.issue('http://192.168.30.199:8080/browse/STYLE3D-17214', name='jira17214')
    def test_seam_taping_two(self):
        self.style.add_open_sproj('sproj', 'jira17214，净边有粘衬条，前片6粒子间距时，内部线边上网格破洞（给开发）.sproj')
        time.sleep(15)
        self.style.focus_panorama()
        auto.click(x=505, y=566, clicks=1, button='left', duration=0.2)  # 点击长方型版片
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('7')
        auto.press('enter')
        time.sleep(2)
        auto.click(x=1886, y=574, clicks=1, button='left', duration=0.2)  # 点击修改粒子间距
        auto.typewrite('6')
        auto.press('enter')
        time.sleep(5)
        style = "jira17214，净边有粘衬条，前片6粒子间距时，内部线边上网格破洞（给开发）"
        new = "\\Triangulation\\"+style+"_new.png"
        old = "\\Triangulation\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 100)

