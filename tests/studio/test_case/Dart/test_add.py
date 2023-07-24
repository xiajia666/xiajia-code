import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('菱形省增加')
@allure.severity(allure.severity_level.CRITICAL)
class TestAdd:

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

    def setup_method(self):
        """ 不关闭工程，新建工程 """
        self.log.info('新建工程，初始化视角')
        self.style.click_new_project()

    def teardown_method(self):
        """不做操作，直接新建 """
        #避免失败，点击弹框确定按钮
        auto.click(x=conf["Dart"]["enter"]['x'], y=conf["Dart"]["enter"]['y'], clicks=conf["Dart"]["enter"]['clicks'], button=conf["Dart"]["enter"]['button'], duration=0.2)
        auto.press('q')
        self.log.info('结束该用例')

    @allure.story('可以在版片上新增菱形省')
    # 8.23能跑通
    def test_add_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_one_1"]['x'], y=conf["Dart"]["add_one_1"]['y'], clicks=conf["Dart"]["add_one_1"]['clicks'], button=conf["Dart"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_one_2"]['x'], y=conf["Dart"]["add_one_2"]['y'], clicks=conf["Dart"]["add_one_2"]['clicks'], button=conf["Dart"]["add_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '版片内新增菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('无法在版片外新增菱形省')
    def test_add_two(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_two_1"]['x'], y=conf["Dart"]["add_two_1"]['y'], clicks=conf["Dart"]["add_two_1"]['clicks'], button=conf["Dart"]["add_two_1"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '版片外新增菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["Dart"]["add_two_2"]['x'], y=conf["Dart"]["add_two_2"]['y'], clicks=conf["Dart"]["add_two_2"]['clicks'], button=conf["Dart"]["add_two_2"]['button'], duration=0.2)
        # auto.click(x=conf["Dart"]["add_two_3"]['x'], y=conf["Dart"]["add_two_3"]['y'],clicks=conf["Dart"]["add_two_3"]['clicks'], button=conf["Dart"]["add_two_3"]['button'], duration=0.2)

    @allure.story('对称版片/联动/边缘对称上新增菱形省，可以联动增加')
    def test_add_three(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_three_1"]['x'], y=conf["Dart"]["add_three_1"]['y'], clicks=conf["Dart"]["add_three_1"]['clicks'], button=conf["Dart"]["add_three_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_three_2"]['x'], y=conf["Dart"]["add_three_2"]['y'], clicks=conf["Dart"]["add_three_2"]['clicks'], button=conf["Dart"]["add_three_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '边缘对称新增菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('在版片内新增菱形省大小无法超出版片')
    def test_add_four(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_four_1"]['x'], y=conf["Dart"]["add_four_1"]['y'], clicks=conf["Dart"]["add_four_1"]['clicks'], button=conf["Dart"]["add_four_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_four_2"]['x'], y=conf["Dart"]["add_four_2"]['y'], clicks=conf["Dart"]["add_four_2"]['clicks'], button=conf["Dart"]["add_four_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '新增菱形省大小无法超出版片'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["Dart"]["add_four_3"]['x'], y=conf["Dart"]["add_four_3"]['y'], clicks=conf["Dart"]["add_four_3"]['clicks'], button=conf["Dart"]["add_four_3"]['button'], duration=0.2)

    @allure.story('无法在已有的菱形省上，再新增菱形省')
    def test_add_five(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_five_1"]['x'], y=conf["Dart"]["add_five_1"]['y'], clicks=conf["Dart"]["add_five_1"]['clicks'], button=conf["Dart"]["add_five_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_five_2"]['x'], y=conf["Dart"]["add_five_2"]['y'], clicks=conf["Dart"]["add_five_2"]['clicks'], button=conf["Dart"]["add_five_2"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_five_3"]['x'], y=conf["Dart"]["add_five_3"]['y'], clicks=conf["Dart"]["add_five_3"]['clicks'], button=conf["Dart"]["add_five_3"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_five_4"]['x'], y=conf["Dart"]["add_five_4"]['y'], clicks=conf["Dart"]["add_five_4"]['clicks'], button=conf["Dart"]["add_five_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '无法在已有的菱形省上，再新增菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["Dart"]["add_five_5"]['x'], y=conf["Dart"]["add_five_5"]['y'], clicks=conf["Dart"]["add_five_5"]['clicks'], button=conf["Dart"]["add_five_5"]['button'], duration=0.2)

    @allure.story('新增菱形省时，直接按键盘的enter可以添加成功，按esc可以取消')
    def test_add_six(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_six_1"]['x'], y=conf["Dart"]["add_six_1"]['y'], clicks=conf["Dart"]["add_six_1"]['clicks'], button=conf["Dart"]["add_six_1"]['button'], duration=0.2)
        auto.press('enter')
        time.sleep(0.5)
        style = '键盘的enter可以添加成功'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Dart"]["add_six_2"]['x'], y=conf["Dart"]["add_six_2"]['y'], clicks=conf["Dart"]["add_six_2"]['clicks'], button=conf["Dart"]["add_six_2"]['button'], duration=0.2)
        auto.press('esc')
        time.sleep(0.5)
        style = '键盘的esc可以取消'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('拖拽生成自定义大小的菱形省')
    def test_add_seven(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.mouseDown(x=conf["Dart"]["add_seven_1"]['x'], y=conf["Dart"]["add_seven_1"]['y'], button=conf["Dart"]["add_seven_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Dart"]["add_seven_2"]['x'], y=conf["Dart"]["add_seven_2"]['y'], button=conf["Dart"]["add_seven_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '拖拽生成自定义大小的菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('无法拖拽到版片外生成菱形省')
    def test_add_eight(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.mouseDown(x=conf["Dart"]["add_eight_1"]['x'], y=conf["Dart"]["add_eight_1"]['y'], button=conf["Dart"]["add_eight_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Dart"]["add_eight_2"]['x'], y=conf["Dart"]["add_eight_2"]['y'], button=conf["Dart"]["add_eight_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '无法拖拽到版片外生成菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.click(x=conf["Dart"]["add_eight_3"]['x'], y=conf["Dart"]["add_eight_3"]['y'], clicks=conf["Dart"]["add_eight_3"]['clicks'], button=conf["Dart"]["add_eight_3"]['button'], duration=0.2)

    @allure.story('快捷键生成菱形省')
    def test_add_nine(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        auto.hotkey('ctrl', 'e')
        auto.click(x=conf["Dart"]["add_nine_1"]['x'], y=conf["Dart"]["add_nine_1"]['y'], clicks=conf["Dart"]["add_nine_1"]['clicks'], button=conf["Dart"]["add_nine_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_nine_2"]['x'], y=conf["Dart"]["add_nine_2"]['y'], clicks=conf["Dart"]["add_nine_2"]['clicks'], button=conf["Dart"]["add_nine_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '快捷键生成菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('版片上新增的菱形省，复制版片后，有对应的菱形省信息')
    def test_add_ten(self):
        self.style.rectangle_creat()
        self.style.click_cloth_textured_surface2d()
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_ten_1"]['x'], y=conf["Dart"]["add_ten_1"]['y'], clicks=conf["Dart"]["add_ten_1"]['clicks'], button=conf["Dart"]["add_ten_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_ten_2"]['x'], y=conf["Dart"]["add_ten_2"]['y'], clicks=conf["Dart"]["add_ten_2"]['clicks'], button=conf["Dart"]["add_ten_2"]['button'], duration=0.2)
        auto.press('q')
        auto.press('9')
        auto.click(x=conf["Dart"]["add_ten_3"]['x'], y=conf["Dart"]["add_ten_3"]['y'], clicks=conf["Dart"]["add_ten_1"]['clicks'], button=conf["Dart"]["add_ten_3"]['button'], duration=0.2)
        auto.hotkey('ctrl', 'c')
        auto.hotkey('ctrl', 'v')
        auto.click(x=conf["Dart"]["add_ten_4"]['x'], y=conf["Dart"]["add_ten_4"]['y'], clicks=conf["Dart"]["add_ten_4"]['clicks'], button=conf["Dart"]["add_ten_4"]['button'], duration=0.2)
        auto.press('2')
        time.sleep(0.5)
        style = '版片上新增的菱形省，复制版片后，有对应的菱形省'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100)

    @allure.story('新增的菱形省支持撤销，恢复')
    def test_add_eleven(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["add_one_1"]['x'], y=conf["Dart"]["add_one_1"]['y'], clicks=conf["Dart"]["add_one_1"]['clicks'], button=conf["Dart"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["add_one_2"]['x'], y=conf["Dart"]["add_one_2"]['y'], clicks=conf["Dart"]["add_one_2"]['clicks'], button=conf["Dart"]["add_one_2"]['button'], duration=0.2)
        auto.hotkey('ctrl', 'z')
        time.sleep(0.5)
        style = '新增的菱形省支持撤销'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.hotkey('ctrl', 'y')
        time.sleep(0.5)
        style = '新增的菱形省支持恢复'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)