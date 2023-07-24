import os,sys
import yaml
sys.path.append('../../../../all')
import pyautogui as auto
import time
import allure
import pytest
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile


#添加假缝
@allure.feature('假缝')
@allure.severity(allure.severity_level.CRITICAL)
class Test_AddTack:

    def setup_class(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_class(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        self.log.info('结束该用例')

    @allure.story('假缝: 1：2D新增 2：3D新增 3：取消对称轴 4：剪切 5:2D,3D单独拖拽 6：2D多选拖拽 7：2D、3D假缝shift和ctrl删除'
                  '8: 相同位置新增及场景管理查看 9: 顶点新增假缝 10:假缝长度不一样属性栏红色 11: 假缝多选修改 12: 框选删除' )
    def test_AddTack(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_addtack()
        auto.click(x=conf["AddTack"]["one_1"]['x'], y=conf["AddTack"]["one_1"]['y'],clicks=conf["AddTack"]["one_1"]['clicks'],button=conf["AddTack"]["one_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["one_2"]['x'], y=conf["AddTack"]["one_2"]['y'],clicks=conf["AddTack"]["one_2"]['clicks'],button=conf["AddTack"]["one_2"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["one_3"]['x'], y=conf["AddTack"]["one_3"]['y'],clicks=conf["AddTack"]["one_3"]['clicks'],button=conf["AddTack"]["one_3"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["one_4"]['x'], y=conf["AddTack"]["one_4"]['y'],clicks=conf["AddTack"]["one_4"]['clicks'],button=conf["AddTack"]["one_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D3D版片内添加假缝'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["two_1"]['x'], y=conf["AddTack"]["two_1"]['y'],clicks=conf["AddTack"]["two_1"]['clicks'],button=conf["AddTack"]["two_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["two_2"]['x'], y=conf["AddTack"]["two_2"]['y'],clicks=conf["AddTack"]["two_2"]['clicks'],button=conf["AddTack"]["two_2"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["two_3"]['x'], y=conf["AddTack"]["two_3"]['y'],clicks=conf["AddTack"]["two_3"]['clicks'],button=conf["AddTack"]["two_3"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["two_4"]['x'], y=conf["AddTack"]["two_4"]['y'],clicks=conf["AddTack"]["two_4"]['clicks'],button=conf["AddTack"]["two_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D3D跨版片添加假缝'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["three_1"]['x'], y=conf["AddTack"]["three_1"]['y'],clicks=conf["AddTack"]["three_1"]['clicks'],button=conf["AddTack"]["three_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["three_2"]['x'], y=conf["AddTack"]["three_2"]['y'],clicks=conf["AddTack"]["three_2"]['clicks'],button=conf["AddTack"]["three_2"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["three_3"]['x'], y=conf["AddTack"]["three_3"]['y'],clicks=conf["AddTack"]["three_3"]['clicks'],button=conf["AddTack"]["three_3"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["three_4"]['x'], y=conf["AddTack"]["three_4"]['y'],clicks=conf["AddTack"]["three_4"]['clicks'],button=conf["AddTack"]["three_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D跨3D版片添加假缝'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["four_1"]['x'], y=conf["AddTack"]["four_1"]['y'],clicks=conf["AddTack"]["four_1"]['clicks'],button=conf["AddTack"]["four_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["four_2"]['x'], y=conf["AddTack"]["four_2"]['y'],clicks=conf["AddTack"]["four_2"]['clicks'],button=conf["AddTack"]["four_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D版片净边到版片内添加假缝'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["five_1"]['x'], y=conf["AddTack"]["five_1"]['y'],clicks=conf["AddTack"]["five_1"]['clicks'], button=conf["AddTack"]["five_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["five_2"]['x'], y=conf["AddTack"]["five_2"]['y'],clicks=conf["AddTack"]["five_2"]['clicks'], button=conf["AddTack"]["five_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D视窗起点净边处跨版添加假缝'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["six_1"]['x'], y=conf["AddTack"]["six_1"]['y'],clicks=conf["AddTack"]["six_1"]['clicks'], button=conf["AddTack"]["six_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["six_2"]['x'], y=conf["AddTack"]["six_2"]['y'],clicks=conf["AddTack"]["six_2"]['clicks'], button=conf["AddTack"]["six_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '假缝点击在版片外'
        new = '\\AddTack\\'+style+'_new.png'
        old = '\\AddTack\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('esc')
        auto.click(x=conf["AddTack"]["seven_1"]['x'], y=conf["AddTack"]["seven_1"]['y'],clicks=conf["AddTack"]["seven_1"]['clicks'], button=conf["AddTack"]["seven_1"]['button'], duration=0.2)
        auto.hotkey('ctrl', 'z')
        time.sleep(0.5)
        style = '添加时按ctrlz撤回'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100, 132, 459, 270, 667)

        auto.click(x=conf["AddTack"]["eight_1"]['x'], y=conf["AddTack"]["eight_1"]['y'],clicks=conf["AddTack"]["eight_1"]['clicks'], button=conf["AddTack"]["eight_1"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["AddTack"]["eight_2"]['x'], y=conf["AddTack"]["eight_2"]['y'],clicks=conf["AddTack"]["eight_2"]['clicks'], button=conf["AddTack"]["eight_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '2D顶点到版片内创建假缝'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["nine_1"]['x'], y=conf["AddTack"]["nine_1"]['y'],clicks=conf["AddTack"]["nine_1"]['clicks'], button=conf["AddTack"]["nine_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["nine_2"]['x'], y=conf["AddTack"]["nine_2"]['y'],clicks=conf["AddTack"]["nine_2"]['clicks'], button=conf["AddTack"]["nine_2"]['button'], duration=0.2)
        time.sleep(1)
        auto.click(x=conf["AddTack"]["nine_3"]['x'], y=conf["AddTack"]["nine_3"]['y'],clicks=conf["AddTack"]["nine_3"]['clicks'], button=conf["AddTack"]["nine_3"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["nine_4"]['x'], y=conf["AddTack"]["nine_4"]['y'],clicks=conf["AddTack"]["nine_4"]['clicks'], button=conf["AddTack"]["nine_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '相同位置创建假缝'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["ten_1"]['x'], y=conf["AddTack"]["ten_1"]['y'],clicks=conf["AddTack"]["ten_1"]['clicks'], button=conf["AddTack"]["ten_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["ten_2"]['x'], y=conf["AddTack"]["ten_2"]['y'],clicks=conf["AddTack"]["ten_2"]['clicks'], button=conf["AddTack"]["ten_2"]['button'], duration=0.2)
        self.style.scroll_big_number(5)
        time.sleep(0.5)
        style = '场景管理查看新增假缝'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 1579, 113, 1906, 444)

        self.style.click_edit_tack()
        auto.mouseDown(x=conf["AddTack"]["edit_one_1"]['x'], y=conf["AddTack"]["edit_one_1"]['y'],button=conf["AddTack"]["edit_one_1"]['button'], duration=0.2)
        time.sleep(2)
        auto.mouseUp(x=conf["AddTack"]["edit_one_2"]['x'], y=conf["AddTack"]["edit_one_2"]['y'],button=conf["AddTack"]["edit_one_2"]['button'], duration=0.2)
        auto.mouseDown(x=conf["AddTack"]["edit_one_3"]['x'], y=conf["AddTack"]["edit_one_3"]['y'],button=conf["AddTack"]["edit_one_3"]['button'], duration=0.2)
        time.sleep(2)
        auto.mouseUp(x=conf["AddTack"]["edit_one_4"]['x'], y=conf["AddTack"]["edit_one_4"]['y'],button=conf["AddTack"]["edit_one_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '拽版片上的假缝点2D3D'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.mouseDown(x=conf["AddTack"]["edit_two_1"]['x'], y=conf["AddTack"]["edit_two_1"]['y'],button=conf["AddTack"]["edit_two_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["edit_two_2"]['x'], y=conf["AddTack"]["edit_two_2"]['y'],button=conf["AddTack"]["edit_two_2"]['button'], duration=0.2)
        auto.mouseDown(x=conf["AddTack"]["edit_two_3"]['x'], y=conf["AddTack"]["edit_two_3"]['y'],button=conf["AddTack"]["edit_two_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["edit_two_4"]['x'], y=conf["AddTack"]["edit_two_4"]['y'],button=conf["AddTack"]["edit_two_4"]['button'], duration=0.2)
        auto.mouseDown(x=conf["AddTack"]["edit_two_5"]['x'], y=conf["AddTack"]["edit_two_5"]['y'],button=conf["AddTack"]["edit_two_5"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["edit_two_6"]['x'], y=conf["AddTack"]["edit_two_6"]['y'],button=conf["AddTack"]["edit_two_6"]['button'], duration=0.2)
        auto.mouseDown(x=conf["AddTack"]["edit_two_7"]['x'], y=conf["AddTack"]["edit_two_7"]['y'],button=conf["AddTack"]["edit_two_7"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["edit_two_8"]['x'], y=conf["AddTack"]["edit_two_8"]['y'],button=conf["AddTack"]["edit_two_8"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '多选拽版片上的假缝点2D3D'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["edit_three_1"]['x'], y=conf["AddTack"]["edit_three_1"]['y'],clicks=conf["AddTack"]["edit_three_1"]['clicks'], button=conf["AddTack"]["edit_three_1"]['button'], duration=0.2)
        auto.typewrite('20')
        time.sleep(1)
        auto.mouseDown(x=conf["AddTack"]["edit_three_2"]['x'], y=conf["AddTack"]["edit_three_2"]['y'],button=conf["AddTack"]["edit_three_2"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["edit_three_3"]['x'], y=conf["AddTack"]["edit_three_3"]['y'], button=conf["AddTack"]["edit_three_3"]['button'], duration=0.2)
        time.sleep(1)
        style = '假缝多选修改后查看属性栏'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)

        auto.mouseDown(x=conf["AddTack"]["show_one_1"]['x'], y=conf["AddTack"]["show_one_1"]['y'],button=conf["AddTack"]["show_one_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["show_one_2"]['x'], y=conf["AddTack"]["show_one_2"]['y'],button=conf["AddTack"]["show_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '假缝长度不一样属性栏红色'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)

        auto.click(x=conf["AddTack"]["edit_four_1"]['x'], y=conf["AddTack"]["edit_four_1"]['y'],clicks=conf["AddTack"]["edit_four_1"]['clicks'], button=conf["AddTack"]["edit_four_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["edit_four_2"]['x'], y=conf["AddTack"]["edit_four_2"]['y'],clicks=conf["AddTack"]["edit_four_2"]['clicks'], button=conf["AddTack"]["edit_four_2"]['button'], duration=0.2)
        auto.typewrite('88')
        auto.click(x=conf["AddTack"]["edit_four_3"]['x'], y=conf["AddTack"]["edit_four_3"]['y'],clicks=conf["AddTack"]["edit_four_3"]['clicks'], button=conf["AddTack"]["edit_four_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '假缝单选修改'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)
        auto.click(x=conf["AddTack"]["edit_four_4"]['x'], y=conf["AddTack"]["edit_four_4"]['y'],clicks=conf["AddTack"]["edit_four_4"]['clicks'], button=conf["AddTack"]["edit_four_4"]['button'], duration=0.2)

        auto.press('z')
        auto.click(x=conf["AddTack"]["del_one_1"]['x'], y=conf["AddTack"]["del_one_1"]['y'],clicks=conf["AddTack"]["del_one_1"]['clicks'], button=conf["AddTack"]["del_one_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["del_one_2"]['x'], y=conf["AddTack"]["del_one_2"]['y'],clicks=conf["AddTack"]["del_one_2"]['clicks'], button=conf["AddTack"]["del_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '取消对称轴'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('i')
        auto.click(x=conf["AddTack"]["del_two_1"]['x'], y=conf["AddTack"]["del_two_1"]['y'],clicks=conf["AddTack"]["del_two_1"]['clicks'], button=conf["AddTack"]["del_two_1"]['button'], duration=0.2)
        auto.click(x=conf["AddTack"]["del_two_2"]['x'], y=conf["AddTack"]["del_two_2"]['y'],clicks=conf["AddTack"]["del_two_2"]['clicks'], button=conf["AddTack"]["del_two_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '剪切'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        self.style.click_edit_tack()
        auto.mouseDown(x=conf["AddTack"]["del_three_1"]['x'], y=conf["AddTack"]["del_three_1"]['y'],button=conf["AddTack"]["del_three_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["AddTack"]["del_three_2"]['x'], y=conf["AddTack"]["del_three_2"]['y'],button=conf["AddTack"]["del_three_2"]['button'], duration=0.2)
        auto.press('del')
        time.sleep(0.5)
        style = '框选删除假缝2D3D同步'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["del_four_1"]['x'], y=conf["AddTack"]["del_four_1"]['y'],clicks=conf["AddTack"]["del_four_1"]['clicks'], button=conf["AddTack"]["del_four_1"]['button'], duration=0.2)
        auto.press('del')
        time.sleep(0.5)
        style = '单选删除假缝2D3D同步'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["del_five_1"]['x'], y=conf["AddTack"]["del_five_1"]['y'],clicks=conf["AddTack"]["del_five_1"]['clicks'], button=conf["AddTack"]["del_five_1"]['button'], duration=0.2)
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf["AddTack"]["del_five_2"]['x'], y=conf["AddTack"]["del_five_2"]['y'],clicks=conf["AddTack"]["del_five_2"]['clicks'], button=conf["AddTack"]["del_five_2"]['button'], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        auto.press('del')
        time.sleep(0.5)
        style = 'shift多选删除假缝2D3D同步'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["AddTack"]["show_two_1"]['x'], y=conf["AddTack"]["show_two_1"]['y'],clicks=conf["AddTack"]["show_two_1"]['clicks'], button=conf["AddTack"]["show_two_1"]['button'], duration=0.2)
        self.style.scroll_small_number(6)
        auto.click(x=conf["AddTack"]["show_two_2"]['x'], y=conf["AddTack"]["show_two_2"]['y'],clicks=conf["AddTack"]["show_two_2"]['clicks'], button=conf["AddTack"]["show_two_2"]['button'], duration=0.2)
        auto.keyDown('ctrl')  # 按下ctrl键
        auto.click(x=conf["AddTack"]["show_two_3"]['x'], y=conf["AddTack"]["show_two_3"]['y'],clicks=conf["AddTack"]["show_two_3"]['clicks'], button=conf["AddTack"]["show_two_3"]['button'], duration=0.2)
        auto.keyUp('ctrl')  # 松开ctrl键
        auto.press('del')
        time.sleep(0.5)
        style = '缩小视角选择假缝ctrl多选'
        new = '\\AddTack\\' + style + '_new.png'
        old = '\\AddTack\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)





