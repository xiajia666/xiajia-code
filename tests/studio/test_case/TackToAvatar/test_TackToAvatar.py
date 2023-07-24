import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.operation_file import OperationFile
import allure
import pytest
from common.logs import Log

#添加假缝
@allure.feature('假缝到模特')
@allure.severity(allure.severity_level.CRITICAL)
class Test_TackToAvatar:

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
        self.log.info("测试结束")
        self.style.close_style3D()

    @allure.story('假缝到模特: 1：假缝到模特面料透明 2：版片到模特假缝 ')
    def test_TackToAvatar(self):
        """
        假缝到模特
        """
        self.style.add_tshirt('T-Shirt')
        self.style.add_avatar('Man175.savt')
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_tack_to_avatar()
        auto.click(x=conf["TackToAvatar"]["show_one_1"]['x'], y=conf["TackToAvatar"]["show_one_1"]['y'],clicks=conf["TackToAvatar"]["show_one_1"]['clicks'],button=conf["TackToAvatar"]["show_one_1"]['button'], duration=0.2)
        time.sleep(1)
        style = '假缝到模特面料透明'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["TackToAvatar"]["add_one_1"]['x'], y=conf["TackToAvatar"]["add_one_1"]['y'],clicks=conf["TackToAvatar"]["add_one_1"]['clicks'],button=conf["TackToAvatar"]["add_one_1"]['button'], duration=0.2)
        time.sleep(1)
        style = '版片到模特假缝'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["TackToAvatar"]["add_two_1"]['x'], y=conf["TackToAvatar"]["add_two_1"]['y'],clicks=conf["TackToAvatar"]["add_two_1"]['clicks'],button=conf["TackToAvatar"]["add_two_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_two_2"]['x'], y=conf["TackToAvatar"]["add_two_2"]['y'],clicks=conf["TackToAvatar"]["add_two_2"]['clicks'],button=conf["TackToAvatar"]["add_two_2"]['button'], duration=0.2)
        time.sleep(1)
        style = '模特到版片假缝'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["TackToAvatar"]["add_three_1"]['x'], y=conf["TackToAvatar"]["add_three_1"]['y'],clicks=conf["TackToAvatar"]["add_three_1"]['clicks'],button=conf["TackToAvatar"]["add_three_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_three_2"]['x'], y=conf["TackToAvatar"]["add_three_2"]['y'],clicks=conf["TackToAvatar"]["add_three_2"]['clicks'],button=conf["TackToAvatar"]["add_three_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '只在版片上创建'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('q')
        self.style.click_tack_to_avatar()
        auto.click(x=conf["TackToAvatar"]["add_four_1"]['x'], y=conf["TackToAvatar"]["add_four_1"]['y'],clicks=conf["TackToAvatar"]["add_four_1"]['clicks'],button=conf["TackToAvatar"]["add_four_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_four_2"]['x'], y=conf["TackToAvatar"]["add_four_2"]['y'],clicks=conf["TackToAvatar"]["add_four_2"]['clicks'],button=conf["TackToAvatar"]["add_four_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '只在模特上创建'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('q')
        self.style.click_tack_to_avatar()
        auto.click(x=conf["TackToAvatar"]["add_five_1"]['x'], y=conf["TackToAvatar"]["add_five_1"]['y'],clicks=conf["TackToAvatar"]["add_five_1"]['clicks'],button=conf["TackToAvatar"]["add_five_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_five_2"]['x'], y=conf["TackToAvatar"]["add_five_2"]['y'],clicks=conf["TackToAvatar"]["add_five_2"]['clicks'],button=conf["TackToAvatar"]["add_five_2"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_five_3"]['x'], y=conf["TackToAvatar"]["add_five_3"]['y'],clicks=conf["TackToAvatar"]["add_five_3"]['clicks'],button=conf["TackToAvatar"]["add_five_3"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_five_4"]['x'], y=conf["TackToAvatar"]["add_five_4"]['y'],clicks=conf["TackToAvatar"]["add_five_4"]['clicks'],button=conf["TackToAvatar"]["add_five_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '相同位置创建'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["TackToAvatar"]["add_six_1"]['x'], y=conf["TackToAvatar"]["add_six_1"]['y'],clicks=conf["TackToAvatar"]["add_six_1"]['clicks'],button=conf["TackToAvatar"]["add_six_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["add_six_2"]['x'], y=conf["TackToAvatar"]["add_six_2"]['y'],clicks=conf["TackToAvatar"]["add_six_2"]['clicks'],button=conf["TackToAvatar"]["add_six_2"]['button'], duration=0.2)
        self.style.scroll_big_number(3)
        time.sleep(0.5)
        style = '场景管理查看新增假缝到模特'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 1577, 89, 1904, 444)

        auto.press('q')
        self.style.click_tack_to_avatar()
        auto.click(x=conf["TackToAvatar"]["add_seven_1"]['x'], y=conf["TackToAvatar"]["add_seven_1"]['y'],clicks=conf["TackToAvatar"]["add_seven_1"]['clicks'],button=conf["TackToAvatar"]["add_seven_1"]['button'], duration=0.2)
        auto.moveTo(x=conf["TackToAvatar"]["add_seven_2"]['x'], y=conf["TackToAvatar"]["add_seven_2"]['y'], duration=0.0, tween=auto.linear)
        auto.hotkey('ctrl', 'z')
        time.sleep(0.5)
        style = '添加时按ctrlz撤回'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        self.style.click_edit_tack()
        auto.mouseDown(x=conf["TackToAvatar"]["edit_one_1"]['x'], y=conf["TackToAvatar"]["edit_one_1"]['y'],button=conf["TackToAvatar"]["edit_one_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["edit_one_2"]['x'], y=conf["TackToAvatar"]["edit_one_2"]['y'],button=conf["TackToAvatar"]["edit_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '单选拖拽假缝'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.mouseDown(x=conf["TackToAvatar"]["edit_two_1"]['x'], y=conf["TackToAvatar"]["edit_two_1"]['y'],button=conf["TackToAvatar"]["edit_two_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["edit_two_2"]['x'], y=conf["TackToAvatar"]["edit_two_2"]['y'],button=conf["TackToAvatar"]["edit_two_2"]['button'], duration=0.2)
        auto.mouseDown(x=conf["TackToAvatar"]["edit_two_3"]['x'], y=conf["TackToAvatar"]["edit_two_3"]['y'],button=conf["TackToAvatar"]["edit_two_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["edit_two_4"]['x'], y=conf["TackToAvatar"]["edit_two_4"]['y'],button=conf["TackToAvatar"]["edit_two_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '多选拖拽假缝'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)


        auto.click(x=conf["TackToAvatar"]["edit_three_1"]['x'], y=conf["TackToAvatar"]["edit_three_1"]['y'],clicks=conf["TackToAvatar"]["edit_three_1"]['clicks'],button=conf["TackToAvatar"]["edit_three_1"]['button'], duration=0.2)
        auto.typewrite('33')
        auto.mouseDown(x=conf["TackToAvatar"]["edit_three_2"]['x'], y=conf["TackToAvatar"]["edit_three_2"]['y'],button=conf["TackToAvatar"]["edit_three_2"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["edit_three_3"]['x'], y=conf["TackToAvatar"]["edit_three_3"]['y'],button=conf["TackToAvatar"]["edit_three_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '假缝多选修改'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)

        auto.click(x=conf["TackToAvatar"]["edit_four_1"]['x'], y=conf["TackToAvatar"]["edit_four_1"]['y'],clicks=conf["TackToAvatar"]["edit_four_1"]['clicks'],button=conf["TackToAvatar"]["edit_four_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["edit_four_2"]['x'], y=conf["TackToAvatar"]["edit_four_2"]['y'],clicks=conf["TackToAvatar"]["edit_four_2"]['clicks'],button=conf["TackToAvatar"]["edit_four_2"]['button'], duration=0.2)
        auto.typewrite('55')
        auto.click(x=conf["TackToAvatar"]["edit_four_3"]['x'], y=conf["TackToAvatar"]["edit_four_3"]['y'],clicks=conf["TackToAvatar"]["edit_four_3"]['clicks'],button=conf["TackToAvatar"]["edit_four_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '假缝单选修改'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)

        auto.mouseDown(x=conf["TackToAvatar"]["show_two_1"]['x'], y=conf["TackToAvatar"]["show_two_1"]['y'],button=conf["TackToAvatar"]["show_two_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["show_two_2"]['x'], y=conf["TackToAvatar"]["show_two_2"]['y'],button=conf["TackToAvatar"]["show_two_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '多选假缝属性栏红色'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 449, 1914, 509)

        auto.press('z')
        auto.click(x=conf["TackToAvatar"]["del_one_1"]['x'], y=conf["TackToAvatar"]["del_one_1"]['y'],clicks=conf["TackToAvatar"]["del_one_1"]['clicks'], button=conf["TackToAvatar"]["del_one_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["del_one_2"]['x'], y=conf["TackToAvatar"]["del_one_2"]['y'],clicks=conf["TackToAvatar"]["del_one_2"]['clicks'], button=conf["TackToAvatar"]["del_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '取消对称轴'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('i')
        auto.click(x=conf["TackToAvatar"]["del_two_1"]['x'], y=conf["TackToAvatar"]["del_two_1"]['y'],clicks=conf["TackToAvatar"]["del_two_1"]['clicks'], button=conf["TackToAvatar"]["del_two_1"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["del_two_2"]['x'], y=conf["TackToAvatar"]["del_two_2"]['y'],clicks=conf["TackToAvatar"]["del_two_2"]['clicks'], button=conf["TackToAvatar"]["del_two_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '剪切'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.press('z')
        auto.mouseDown(x=conf["TackToAvatar"]["del_four_1"]['x'], y=conf["TackToAvatar"]["del_four_1"]['y'],button=conf["TackToAvatar"]["del_four_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["TackToAvatar"]["del_four_2"]['x'], y=conf["TackToAvatar"]["del_four_2"]['y'],button=conf["TackToAvatar"]["del_four_2"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["TackToAvatar"]["del_four_3"]['x'], y=conf["TackToAvatar"]["del_four_3"]['y'],clicks=conf["TackToAvatar"]["del_four_3"]['clicks'], button=conf["TackToAvatar"]["del_four_3"]['button'], duration=0.2)
        auto.click(x=conf["TackToAvatar"]["del_four_4"]['x'], y=conf["TackToAvatar"]["del_four_4"]['y'],clicks=conf["TackToAvatar"]["del_four_4"]['clicks'], button=conf["TackToAvatar"]["del_four_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '合并'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        self.style.click_edit_tack()
        auto.click(x=conf["TackToAvatar"]["del_three_1"]['x'], y=conf["TackToAvatar"]["del_three_1"]['y'],clicks=conf["TackToAvatar"]["del_three_1"]['clicks'], button=conf["TackToAvatar"]["del_three_1"]['button'], duration=0.2)
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf["TackToAvatar"]["del_three_2"]['x'], y=conf["TackToAvatar"]["del_three_2"]['y'],clicks=conf["TackToAvatar"]["del_three_2"]['clicks'], button=conf["TackToAvatar"]["del_three_2"]['button'], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        auto.press('del')
        time.sleep(0.5)
        style = 'shift多选删除假缝到模特'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

        auto.click(x=conf["TackToAvatar"]["show_three_1"]['x'], y=conf["TackToAvatar"]["show_three_1"]['y'],clicks=conf["TackToAvatar"]["show_three_1"]['clicks'], button=conf["TackToAvatar"]["show_three_1"]['button'], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["TackToAvatar"]["show_three_2"]['x'], y=conf["TackToAvatar"]["show_three_2"]['y'],clicks=conf["TackToAvatar"]["show_three_2"]['clicks'], button=conf["TackToAvatar"]["show_three_2"]['button'], duration=0.2)
        time.sleep(1.5)
        style = '放大视角选择假缝'
        new = '\\TackToAvatar\\'+style+'_new.png'
        old = '\\TackToAvatar\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 942, 382, 1359, 774)












