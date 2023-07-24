# -*- coding: utf-8 -*-
import sys
import os
import pyperclip
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('对称')
@allure.severity(allure.severity_level.CRITICAL)
class TestSymmetrical:

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

    @allure.story('边缘对称，23D添加归拔不联动')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/7892d7a8c9045ccc2265350e3b', name='STUDIO-6066')
    def test_symmetrical_one(self):
        self.style.rectangle_creat()
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦
        time.sleep(1)
        self.style.click_edit_pattern()
        auto.click(x=486, y=435, clicks=1, button='right', duration=0.2)  # 点击长方形右侧净边
        time.sleep(1)
        auto.click(x=530, y=498, clicks=1, button='right', duration=0.2)  # 点击边缘对称
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦
        auto.press('9')
        time.sleep(1)
        auto.click(x=1111, y=300, clicks=1, button='left', duration=0.2)
        auto.press('9')

        time.sleep(1)
        self.style.click_steam()
        auto.click(x=238, y=151, clicks=1, button='left', duration=0.2) # 设置收缩率
        auto.press('delete')
        auto.typewrite('50')
        time.sleep(1)
        auto.click(x=223, y=511, clicks=1, button='left', duration=0.2)  # 2D添加归拔
        time.sleep(1)
        auto.click(x=1338, y=630, clicks=1, button='left', duration=0.2)  # 3D添加归拔

        style = "STUDIO-6066，边缘对称，23D添加归拔不联动"
        new = "\\RunBug\\Symmetrical\\"+style+"_new.png"
        old = "\\RunBug\\Symmetrical\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('边缘对称，菱形省加缝纫线')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/4f9ea4f49decb26a9c93f2b6cf', name='STUDIO-3085')
    def test_symmetrical_two(self):
        self.style.rectangle_creat()
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦
        time.sleep(1)
        self.style.click_edit_pattern()
        auto.click(x=486, y=435, clicks=1, button='right', duration=0.2)  # 点击长方形右侧净边
        time.sleep(1)
        auto.click(x=530, y=498, clicks=1, button='right', duration=0.2)  # 点击边缘对称
        auto.click(x=765, y=160, clicks=1, button='left', duration=0.2)  # 点击空白处，使长方形失焦
        auto.press('9')
        time.sleep(1)
        auto.click(x=1111, y=300, clicks=1, button='left', duration=0.2)
        auto.press('9')

        time.sleep(1)
        self.style.click_Dart()
        auto.click(x=247, y=532, clicks=1, button='left', duration=0.2)  # 添加省
        auto.click(x=992, y=618, clicks=1, button='left', duration=0.2)  # 省弹框点击确定
        time.sleep(1)
        self.style.click_segment_sewing()
        auto.click(x=540, y=491, clicks=1, button='left', duration=0.2)  # 添加线缝纫
        auto.click(x=549, y=491, clicks=1, button='left', duration=0.2)  # 添加线缝纫

        style = "STUDIO-3085，边缘对称，菱形省加缝纫线"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('边缘对称，内部线上的明线凹痕对称显示')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/e5d5a7d3dabd920260106c388e',
                  name='STUDIO-2226')
    def test_symmetrical_three(self):
        self.style.add_open_sproj('sproj', 'STUDIO-2226.sproj')
        self.style.focus_panorama()
        self.style.click_segment_topstitch()

        time.sleep(1)
        auto.click(x=189, y=514, clicks=1, button='left', duration=0.2)  # 添加线明线
        auto.click(x=416, y=525, clicks=1, button='left', duration=0.2)  # 添加线明线
        auto.click(x=459, y=324, clicks=1, button='left', duration=0.2)  # 添加线明线

        style = "STUDIO-2226，边缘对称，内部线上的明线凹痕对称显示"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('对称版片，解除联动后，沿线系纽扣跑到单纽扣上了')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/c72f74ddc995c874a158547156',
                  name='STUDIO-1092')
    def test_symmetrical_four(self):
        self.style.add_open_sproj('sproj', 'STUDIO-1092.sproj')
        self.style.focus_panorama()

        auto.click(x=172, y=655, clicks=1, button='right', duration=0.2)  # 点击版片右键
        auto.click(x=227, y=92, clicks=1, button='left', duration=0.2)  # 点击解除联动
        auto.click(x=460, y=648, clicks=1, button='right', duration=0.2)  # 点击版片右键
        auto.click(x=517, y=145, clicks=1, button='left', duration=0.2)  # 点击解除联动

        auto.click(x=560, y=808, clicks=1, button='left', duration=0.2)  # 点击空白处

        style = "STUDIO-1092，对称版片，解除联动后，沿线系纽扣跑到单纽扣上了"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-7953勾勒模式选中基础线右键设为对称轴，因基础线上有明线数据，导致软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/10087a84b8ba2223a63cd72048',name='STUDIO-7953')
    def test_symmetrical_five(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7953.sproj')
        self.style.focus_panorama()
        self.style.click_trace()

        auto.click(x=396, y=617, clicks=1, button='right', duration=0.2)  # 点击基础线右键
        auto.click(x=448, y=683, clicks=1, button='left', duration=0.2)  # 点击设为对称轴

        style = "STUDIO-7953勾勒模式选中基础线右键设为对称轴，因基础线上有明线数据，导致软件崩溃"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-7885框选对称版片上的明线，右键解除联动')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d6ff8c550fa732c9c9615c1978',name='STUDIO-7885')
    def test_symmetrical_six(self):
        self.style.add_open_sproj('sproj', 'STUDIO-7885.sproj')
        self.style.focus_panorama()
        auto.press('9')
        self.style.click_edit_topstitch()

        auto.mouseDown(x=130, y=210, button='left')  # 框选明线
        auto.mouseUp(x=665, y=900, button='left', duration=0.2)
        time.sleep(1)

        auto.click(x=390, y=857, clicks=1, button='right', duration=0.2)  # hover明线右键
        auto.click(x=440, y=952, clicks=1, button='left', duration=0.2)  # 点击解除联动
        time.sleep(1)

        auto.mouseDown(x=680, y=895, button='left')  # 框选明线
        auto.mouseUp(x=407, y=200, button='left', duration=0.2)
        auto.press('Delete')
        time.sleep(1)

        style = "STUDIO-7885框选对称版片上的明线，右键解除联动"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-8136开启自动生成缝边，选择内部线设为对称轴，拦截提示因版片形态不同后，一直撤销软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/d10d8fc8450216fbd7c7a70432',name='STUDIO-8136')
    def test_symmetrical_seven(self):
        self.style.rectangle_creat()
        auto.press('9')
        self.style.click_addpoint()
        auto.click(x=146, y=552, clicks=1, button='left', duration=0.2)  # 点击净边加点
        time.sleep(1)

        self.style.click_addpen()
        auto.click(x=402, y=297, clicks=1, button='left', duration=0.2)  # 加内部线
        time.sleep(1)
        auto.doubleClick(x=402, y=809, interval=0.0, button='left', duration=0.2)
        time.sleep(1)

        self.style.click_edit_pattern()
        auto.click(x=402, y=559, clicks=1, button='right', duration=0.2)  # hover内部线右键
        auto.click(x=456, y=847, clicks=1, button='left', duration=0.2)  # 点击设为对称轴
        auto.click(x=1060, y=602, clicks=1, button='left', duration=0.2)  # 弹窗，点击确定
        auto.click(x=690, y=175, clicks=1, button='left', duration=0.2) # 点击空白处
        time.sleep(1)

        auto.keyDown('ctrl')
        auto.keyDown('z')
        auto.keyDown('z')
        auto.keyDown('z')
        auto.keyDown('z')
        auto.keyUp('ctrl')
        time.sleep(1)

        style = "STUDIO-8136开启自动生成缝边，选择内部线设为对称轴，拦截提示因版片形态不同后，一直撤销软件崩溃"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-1834两个边缘对称版片，生成里布层，选择顶点不在对称轴上的边合并，软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/55657fc8cb490b36b2996c4f9a',name='STUDIO-1834')
    def test_symmetrical_eight(self):
        self.style.add_open_sproj('sproj', 'STUDIO-1834.sproj')
        self.style.focus_panorama()
        self.style.click_edit_pattern()

        time.sleep(1)
        auto.keyDown('ctrl')
        auto.click(x=361, y=452, clicks=1, button='left', duration=0.2)  # 选择边
        auto.click(x=443, y=452, clicks=1, button='right', duration=0.2)  # 选择边右键
        auto.keyUp('ctrl')
        auto.click(x=500, y=525, clicks=1, button='left', duration=0.2)  # 点击合并
        time.sleep(1)


        style = "STUDIO-1834两个边缘对称版片，生成里布层，选择顶点不在对称轴上的边合并，软件崩溃"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('STUDIO-1332窗口3D，选择内部线右键生成对称线，软件崩溃')
    @allure.issue('https://devops.aliyun.com/projex/project/d3c48781beed8bf802085449eb/bug/04befffccdb65bbe3cfacb62fa',name='STUDIO-1332')
    def test_symmetrical_nine(self):
        self.style.add_open_sproj('sproj', 'STUDIO-1332.sproj')
        auto.click(x=870, y=580, clicks=1, button='left', duration=0.2)
        auto.press('9')
        self.style.focus_panorama()
        self.style.click_edit_pattern()

        time.sleep(1)
        auto.click(x=1354, y=271, clicks=1, button='right', duration=0.2)  # 选择边右键
        auto.click(x=1411, y=498, clicks=1, button='left', duration=0.2)  # 点击生成对称线
        auto.click(x=1261, y=249, clicks=1, button='left', duration=0.2)    # 选择对称线

        time.sleep(1)

        style = "STUDIO-1332窗口3D，选择内部线右键生成对称线，软件崩溃"
        new = "\\RunBug\\Symmetrical\\" + style + "_new.png"
        old = "\\RunBug\\Symmetrical\\" + style + "_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

