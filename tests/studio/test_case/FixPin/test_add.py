import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure
import yaml
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())

@allure.feature('固定针增加')
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
        self.log.info('结束该用例')


    @allure.story('框选可以生成固定针（2D，3D，在不同的视角位置，固定针顶点上）')
    def test_add_one(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_fixpin_box()
        auto.press('2')
        auto.mouseDown(x=conf["FixPin"]["add_one_1"]['x'], y=conf["FixPin"]["add_one_1"]['y'],button=conf["FixPin"]["add_one_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_one_2"]['x'], y=conf["FixPin"]["add_one_2"]['y'],button=conf["FixPin"]["add_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_one_3"]['x'], y=conf["FixPin"]["add_one_3"]['y'],button=conf["FixPin"]["add_one_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_one_4"]['x'], y=conf["FixPin"]["add_one_4"]['y'],button=conf["FixPin"]["add_one_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '框选2D3D生成固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('在固定针单点可以生成固定针（2D，3D）')
    def test_add_two(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_fixpin_box()
        auto.press('2')
        auto.click(x=conf["FixPin"]["add_two_1"]['x'], y=conf["FixPin"]["add_two_1"]['y'], clicks=conf["FixPin"]["add_two_1"]['clicks'], button=conf["FixPin"]["add_two_1"]['button'], duration=0.2)
        auto.click(x=conf["FixPin"]["add_two_2"]['x'],y=conf["FixPin"]["add_two_2"]['y'], clicks=conf["FixPin"]["add_two_2"]['clicks'], button=conf["FixPin"]["add_two_2"]['button'], duration=0.2)
        self.style.scroll_big_number(7)
        auto.click(x=conf["FixPin"]["add_two_3"]['x'],y=conf["FixPin"]["add_two_3"]['y'], clicks=conf["FixPin"]["add_two_3"]['clicks'], button=conf["FixPin"]["add_two_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '单击2D3D生成固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('在净边固定针顶点双击，净边会生成一排固定针（2D，3D)')
    def test_add_three(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_fixpin_box()
        auto.press('2')
        auto.click(x=conf["FixPin"]["add_three_1"]['x'],y=conf["FixPin"]["add_three_1"]['y'], clicks=conf["FixPin"]["add_three_1"]['clicks'], button=conf["FixPin"]["add_three_1"]['button'], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["FixPin"]["add_three_2"]['x'],y=conf["FixPin"]["add_three_2"]['y'], clicks=conf["FixPin"]["add_three_2"]['clicks'], button=conf["FixPin"]["add_three_2"]['button'], duration=0.2)
        auto.click(x=conf["FixPin"]["add_three_3"]['x'],y=conf["FixPin"]["add_three_3"]['y'], clicks=conf["FixPin"]["add_three_3"]['clicks'], button=conf["FixPin"]["add_three_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '双击2D3D净边生成固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('在固定针双击可以生成固定针（2D，3D）')
    def test_add_four(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        self.style.click_fixpin_box()
        auto.press('2')
        auto.click(x=conf["FixPin"]["add_four_1"]['x'],y=conf["FixPin"]["add_four_1"]['y'], clicks=conf["FixPin"]["add_four_1"]['clicks'], button=conf["FixPin"]["add_four_1"]['button'], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["FixPin"]["add_four_2"]['x'],y=conf["FixPin"]["add_four_2"]['y'], clicks=conf["FixPin"]["add_four_2"]['clicks'], button=conf["FixPin"]["add_four_2"]['button'], duration=0.2)
        auto.click(x=conf["FixPin"]["add_four_3"]['x'],y=conf["FixPin"]["add_four_3"]['y'], clicks=conf["FixPin"]["add_four_3"]['clicks'], button=conf["FixPin"]["add_four_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '双击2D3D生成固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('按shift键可以多选固定针，反选固定针（2D, 3D）')
    def test_add_five(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_fixpin_box()
        auto.mouseDown(x=conf["FixPin"]["add_five_1"]['x'], y=conf["FixPin"]["add_five_1"]['y'],button=conf["FixPin"]["add_five_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_five_2"]['x'], y=conf["FixPin"]["add_five_2"]['y'],button=conf["FixPin"]["add_five_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_five_3"]['x'], y=conf["FixPin"]["add_five_3"]['y'],button=conf["FixPin"]["add_five_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_five_4"]['x'], y=conf["FixPin"]["add_five_4"]['y'],button=conf["FixPin"]["add_five_4"]['button'], duration=0.2)
        auto.keyDown('shift')  # 按下shift键
        auto.mouseDown(x=conf["FixPin"]["add_five_5"]['x'], y=conf["FixPin"]["add_five_5"]['y'],button=conf["FixPin"]["add_five_5"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_five_6"]['x'], y=conf["FixPin"]["add_five_6"]['y'],button=conf["FixPin"]["add_five_6"]['button'], duration=0.2)
        auto.mouseDown(x=conf["FixPin"]["add_five_7"]['x'], y=conf["FixPin"]["add_five_7"]['y'],button=conf["FixPin"]["add_five_7"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_five_8"]['x'], y=conf["FixPin"]["add_five_8"]['y'],button=conf["FixPin"]["add_five_8"]['button'], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        time.sleep(0.5)
        style = '2D3Dshift键可以多选固定针，反选固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('按ctrl键可以去除固定针(2D, 3D)')
    def test_add_six(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_fixpin_box()
        auto.mouseDown(x=conf["FixPin"]["add_six_1"]['x'], y=conf["FixPin"]["add_six_1"]['y'],button=conf["FixPin"]["add_six_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_six_2"]['x'], y=conf["FixPin"]["add_six_2"]['y'],button=conf["FixPin"]["add_six_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_six_3"]['x'], y=conf["FixPin"]["add_six_3"]['y'],button=conf["FixPin"]["add_six_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_six_4"]['x'], y=conf["FixPin"]["add_six_4"]['y'],button=conf["FixPin"]["add_six_4"]['button'], duration=0.2)
        auto.keyDown('ctrl')  # 按下ctrl键
        auto.mouseDown(x=conf["FixPin"]["add_six_5"]['x'], y=conf["FixPin"]["add_six_5"]['y'],button=conf["FixPin"]["add_six_5"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_six_6"]['x'], y=conf["FixPin"]["add_six_6"]['y'],button=conf["FixPin"]["add_six_6"]['button'], duration=0.2)
        auto.mouseDown(x=conf["FixPin"]["add_six_7"]['x'], y=conf["FixPin"]["add_six_7"]['y'],button=conf["FixPin"]["add_six_7"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_six_8"]['x'], y=conf["FixPin"]["add_six_8"]['y'],button=conf["FixPin"]["add_six_8"]['button'], duration=0.2)
        auto.keyUp('ctrl')  # 松开ctrl键
        time.sleep(0.5)
        style = '2D,3Dctrl键可以去除固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)







