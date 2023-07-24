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

@allure.feature('固定针删除')
@allure.severity(allure.severity_level.CRITICAL)
class TestDelete:

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


    @allure.story('右键删除选择的固定针(2D, 3D)')
    def test_add_eight(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_fixpin_box()
        # 在2D/3D添加固定针
        auto.mouseDown(x=conf["FixPin"]["add_eight_1"]['x'], y=conf["FixPin"]["add_eight_1"]['y'],button=conf["FixPin"]["add_eight_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_eight_2"]['x'], y=conf["FixPin"]["add_eight_2"]['y'],button=conf["FixPin"]["add_eight_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_eight_3"]['x'], y=conf["FixPin"]["add_eight_3"]['y'],button=conf["FixPin"]["add_eight_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_eight_4"]['x'], y=conf["FixPin"]["add_eight_4"]['y'],button=conf["FixPin"]["add_eight_4"]['button'], duration=0.2)
        # 3D选择固定针右键删除
        auto.click(x=conf["FixPin"]["add_eight_5"]['x'], y=conf["FixPin"]["add_eight_5"]['y'],clicks=conf["FixPin"]["add_eight_5"]['clicks'], button=conf["FixPin"]["add_eight_5"]['button'],duration=0.2)
        auto.click(x=conf["FixPin"]["add_eight_6"]['x'], y=conf["FixPin"]["add_eight_6"]['y'],clicks=conf["FixPin"]["add_eight_6"]['clicks'], button=conf["FixPin"]["add_eight_6"]['button'],duration=0.2)
        time.sleep(0.5)
        # 2D选择固定针右键删除
        auto.click(x=conf["FixPin"]["add_eight_7"]['x'], y=conf["FixPin"]["add_eight_7"]['y'],clicks=conf["FixPin"]["add_eight_7"]['clicks'], button=conf["FixPin"]["add_eight_7"]['button'],duration=0.2)
        auto.click(x=conf["FixPin"]["add_eight_8"]['x'], y=conf["FixPin"]["add_eight_8"]['y'],clicks=conf["FixPin"]["add_eight_8"]['clicks'], button=conf["FixPin"]["add_eight_8"]['button'],duration=0.2)
        time.sleep(0.5)
        style = '2D,3D右键删除选择的固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('右键删除所有固定针(2D, 3D)')
    def test_add_night(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_fixpin_box()
        # 在2D/3D添加固定针
        auto.mouseDown(x=conf["FixPin"]["add_night_1"]['x'], y=conf["FixPin"]["add_night_1"]['y'],button=conf["FixPin"]["add_night_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_night_2"]['x'], y=conf["FixPin"]["add_night_2"]['y'],button=conf["FixPin"]["add_night_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_night_3"]['x'], y=conf["FixPin"]["add_night_3"]['y'],button=conf["FixPin"]["add_night_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_night_4"]['x'], y=conf["FixPin"]["add_night_4"]['y'],button=conf["FixPin"]["add_night_4"]['button'], duration=0.2)
        # 3D右键删除所有固定针
        auto.click(x=conf["FixPin"]["add_night_5"]['x'], y=conf["FixPin"]["add_night_5"]['y'],clicks=conf["FixPin"]["add_night_5"]['clicks'], button=conf["FixPin"]["add_night_5"]['button'],duration=0.2)
        auto.click(x=conf["FixPin"]["add_night_6"]['x'], y=conf["FixPin"]["add_night_6"]['y'],
                   clicks=conf["FixPin"]["add_night_6"]['clicks'], button=conf["FixPin"]["add_night_6"]['button'],
                   duration=0.2)
        time.sleep(0.5)
        style = '2D,3D右键删除所有固定针'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('取消对称轴，固定针不消失')
    def test_add_ten(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_fixpin_box()
        # 在2D/3D添加固定针
        auto.mouseDown(x=conf["FixPin"]["add_ten_1"]['x'], y=conf["FixPin"]["add_ten_1"]['y'],
                       button=conf["FixPin"]["add_ten_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_ten_2"]['x'], y=conf["FixPin"]["add_ten_2"]['y'],
                     button=conf["FixPin"]["add_ten_2"]['button'], duration=0.2)
        time.sleep(0.5)
        auto.mouseDown(x=conf["FixPin"]["add_ten_3"]['x'], y=conf["FixPin"]["add_ten_3"]['y'],
                       button=conf["FixPin"]["add_ten_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["add_ten_4"]['x'], y=conf["FixPin"]["add_ten_4"]['y'],
                     button=conf["FixPin"]["add_ten_4"]['button'], duration=0.2)
        self.style.click_edit_pattern()
        # 取消对称轴
        auto.click(x=conf["FixPin"]["add_ten_5"]['x'], y=conf["FixPin"]["add_ten_5"]['y'],
                   clicks=conf["FixPin"]["add_ten_5"]['clicks'], button=conf["FixPin"]["add_ten_5"]['button'],
                   duration=0.2)
        auto.click(x=conf["FixPin"]["add_ten_6"]['x'], y=conf["FixPin"]["add_ten_6"]['y'],
                   clicks=conf["FixPin"]["add_ten_6"]['clicks'], button=conf["FixPin"]["add_ten_6"]['button'],
                   duration=0.2)
        time.sleep(0.5)
        style = '取消对称轴，固定针不消失'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)







