# -*- coding: utf-8 -*-
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('UV编辑器')
@allure.severity(allure.severity_level.CRITICAL)
class TestUVeditor:

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

    @allure.story('所有版片安排2D位置后自动排布，会有两个版片重叠了--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/1bf580d6b087cd183253fa7dfd', name='STUDIO-3915')
    def test_UVeditor_one(self):
        self.style.add_open_sproj('sproj', 'STUDIO-3915.sproj')
        time.sleep(3)
        self.style.click_UVeditor()
        self.style.focus_panorama()
        auto.click(x=447, y=221, button='left', duration=0.2)  # 点击空白处
        auto.hotkey('ctrl', 'a')
        auto.click(x=115, y=111, button='left', duration=0.2)  # 自动排布
        time.sleep(2)
        style = "STUDIO-3915，所有版片安排2D位置后自动排布，会有两个版片重叠了"
        new = "\\RunBug\\UVeditor\\"+style+"_new.png"
        old = "\\RunBug\\UVeditor\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('修改移动弹窗中的数据，无法直接使用键盘移动--sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/3a536cdd40ede8e909297181e3', name='STUDIO-3150')
    def test_UVeditor_two(self):
        self.style.add_tshirt('Female_T-Shirt')
        self.style.click_UVeditor()
        self.style.focus_panorama()
        time.sleep(0.5)
        auto.click(x=89, y=111, button='left', duration=0.2)
        auto.click(x=964, y=574, button='left', duration=0.2)
        self.style.click_backspace_number(5)
        auto.typewrite(message='1.00', interval=0.5)
        time.sleep(0.5)
        auto.click(x=577, y=559, button='left', duration=0.2)
        auto.press('up')
        style = "STUDIO-3150，修改移动弹窗中的数据，无法直接使用键盘移动"
        new = "\\RunBug\\UVeditor\\"+style+"_new.png"
        old = "\\RunBug\\UVeditor\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    # @allure.story('当加载类型是“添加”时，UV乱了--sne')
    # @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/0254abf38ccc986fa5a0f8bb2e', name='STUDIO-375')
    # def test_UVeditor_three(self):
    #     self.style.add_add_sproj('sproj', 'STUDIO-375.sproj')
    #     time.sleep(5)
    #     auto.click(x=967, y=380, button='left', duration=0.2)
    #     self.style.click_UVeditor()
    #     self.style.focus_panorama()
    #     time.sleep(1)
    #     style = "STUDIO-375，当加载类型是“添加”时，UV乱了"
    #     new = "\\RunBug\\UVeditor\\"+style+"_new.png"
    #     old = "\\RunBug\\UVeditor\\"+style+"_new.png"
    #     self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('右键“所有UV安排到0-1坐标位置”，在UV编辑器中，版片消失-sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/508e657bc1745f5ee80be8ab85', name='STUDIO-6665')
    def test_UVeditor_four(self):
        self.style.add_open_sproj('sproj', 'STUDIO-6665.sproj')
        time.sleep(3)
        self.style.click_UVeditor()
        auto.click(x=219, y=321, button='right', duration=0.2)  # 点击空白处
        auto.click(x=252, y=338, button='left', duration=0.2)
        auto.click(x=995, y=602, button='left', duration=0.2)
        time.sleep(2)
        style = "STUDIO-6665，右键“所有UV安排到0-1坐标位置”，在UV编辑器中"
        new = "\\RunBug\\UVeditor\\"+style+"_new.png"
        old = "\\RunBug\\UVeditor\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('附件工程切换到法线图模式，软件卡死-sne')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/5c659a5eb6f483c9e58b1f79b1',name='STUDIO-8406')
    def test_UVeditor_five(self):
        self.style.add_open_sproj('sproj', 'STUDIO-8406.sproj')
        time.sleep(3)
        self.style.click_UVeditor()
        auto.click(x=30, y=112, button='left', duration=0.2)
        auto.click(x=29, y=148, button='left', duration=0.2)
        time.sleep(15)
        style = "STUDIO-8406，附件工程切换到法线图模式，软件卡死"
        new = "\\RunBug\\UVeditor\\" + style + "_new.png"
        old = "\\RunBug\\UVeditor\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)