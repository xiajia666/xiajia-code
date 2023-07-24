import sys
import yaml
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())


@allure.feature('延展(点)')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddFullnessPoint:

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
        auto.press('q')
        self.log.info('结束该用例')

    @allure.story('长方形版片上选择起终点新增延展')
    def test_add_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=conf["AddFullnessPoint"]["add_one_1"]['x'], y=conf["AddFullnessPoint"]["add_one_1"]['y'], clicks=conf["AddFullnessPoint"]["add_one_1"]['clicks'], button=conf["AddFullnessPoint"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_one_2"]['x'], y=conf["AddFullnessPoint"]["add_one_2"]['y'], clicks=conf["AddFullnessPoint"]["add_one_2"]['clicks'], button=conf["AddFullnessPoint"]["add_one_2"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_one_3"]['x'], y=conf["AddFullnessPoint"]["add_one_3"]['y'], clicks=conf["AddFullnessPoint"]["add_one_3"]['clicks'], button=conf["AddFullnessPoint"]["add_one_3"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_one_4"]['x'], y=conf["AddFullnessPoint"]["add_one_4"]['y'], clicks=conf["AddFullnessPoint"]["add_one_4"]['clicks'], button=conf["AddFullnessPoint"]["add_one_4"]['button'], duration=0.2)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=992, y=588, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  #右键弹框点击确定
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        self.style.focus_panorama()
        auto.press('2')
        time.sleep(1)
        style = '长方形版片上选择起终点新增延展'
        new = '\\fullnessPoint\\' + style + '_new.png'
        old = '\\fullnessPoint\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('对称版片新增延展')
    def test_add_two(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=conf["AddFullnessPoint"]["add_two_1"]['x'], y=conf["AddFullnessPoint"]["add_two_1"]['y'],clicks=conf["AddFullnessPoint"]["add_two_1"]['clicks'],button=conf["AddFullnessPoint"]["add_two_1"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_two_2"]['x'], y=conf["AddFullnessPoint"]["add_two_2"]['y'],clicks=conf["AddFullnessPoint"]["add_two_2"]['clicks'],button=conf["AddFullnessPoint"]["add_two_2"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_two_3"]['x'], y=conf["AddFullnessPoint"]["add_two_3"]['y'],clicks=conf["AddFullnessPoint"]["add_two_3"]['clicks'],button=conf["AddFullnessPoint"]["add_two_3"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_two_4"]['x'], y=conf["AddFullnessPoint"]["add_two_4"]['y'],clicks=conf["AddFullnessPoint"]["add_two_4"]['clicks'],button=conf["AddFullnessPoint"]["add_two_4"]['button'], duration=0.5)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=992, y=588, clicks=1, interval=0.0, button='left', duration=0.2,tween=auto.linear)  #
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        self.style.focus_panorama()
        time.sleep(1)
        style = '对称版片新增延展'
        new = '\\fullnessPoint\\' + style + '_new.png'
        old = '\\fullnessPoint\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('延展起终点在同一条净边上,延展崩溃bug16169')
    def test_add_three(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=conf["AddFullnessPoint"]["add_three_1"]['x'], y=conf["AddFullnessPoint"]["add_three_1"]['y'],clicks=conf["AddFullnessPoint"]["add_three_1"]['clicks'],button=conf["AddFullnessPoint"]["add_three_1"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_three_2"]['x'], y=conf["AddFullnessPoint"]["add_three_2"]['y'],clicks=conf["AddFullnessPoint"]["add_three_2"]['clicks'],button=conf["AddFullnessPoint"]["add_three_2"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_three_3"]['x'], y=conf["AddFullnessPoint"]["add_three_3"]['y'],clicks=conf["AddFullnessPoint"]["add_three_3"]['clicks'],button=conf["AddFullnessPoint"]["add_three_3"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_three_4"]['x'], y=conf["AddFullnessPoint"]["add_three_4"]['y'],clicks=conf["AddFullnessPoint"]["add_three_4"]['clicks'],button=conf["AddFullnessPoint"]["add_three_4"]['button'], duration=0.5)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=992, y=588, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  #
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        self.style.focus_panorama()
        time.sleep(1)
        style = '延展起终点在同一条净边上'
        new = '\\fullnessPoint\\' + style + '_new.png'
        old = '\\fullnessPoint\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('延展起终点在边缘对称两侧,延展崩溃bug16162')
    def test_add_four(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=conf["AddFullnessPoint"]["add_four_1"]['x'], y=conf["AddFullnessPoint"]["add_four_1"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_four_1"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_four_1"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_four_2"]['x'], y=conf["AddFullnessPoint"]["add_four_2"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_four_2"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_four_2"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_four_3"]['x'], y=conf["AddFullnessPoint"]["add_four_3"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_four_3"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_four_3"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_four_4"]['x'], y=conf["AddFullnessPoint"]["add_four_4"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_four_4"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_four_4"]['button'], duration=0.5)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=992, y=588, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  #
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        self.style.focus_panorama()
        time.sleep(1)
        style = '延展起终点在边缘对称两侧'
        new = '\\fullnessPoint\\' + style + '_new.png'
        old = '\\fullnessPoint\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

    @allure.story('延展终点在边缘对称的对称轴上')
    def test_add_five(self):
        self.style.add_tshirt('T-Shirt')
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_FullnessPoint()
        auto.click(x=conf["AddFullnessPoint"]["add_five_1"]['x'], y=conf["AddFullnessPoint"]["add_five_1"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_five_1"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_five_1"]['button'], duration=0.2)
        auto.click(x=conf["AddFullnessPoint"]["add_five_2"]['x'], y=conf["AddFullnessPoint"]["add_five_2"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_five_2"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_five_2"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_five_3"]['x'], y=conf["AddFullnessPoint"]["add_five_3"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_five_3"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_five_3"]['button'], duration=0.5)
        auto.click(x=conf["AddFullnessPoint"]["add_five_4"]['x'], y=conf["AddFullnessPoint"]["add_five_4"]['y'],
                   clicks=conf["AddFullnessPoint"]["add_five_4"]['clicks'],
                   button=conf["AddFullnessPoint"]["add_five_4"]['button'], duration=0.5)
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            auto.click(x=992, y=588, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)  #
        elif str(screen_width) == '2560':
            auto.click(x=1290, y=780, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        self.style.focus_panorama()
        time.sleep(1)
        style = '延展终点在边缘对称的对称轴上'
        new = '\\fullnessPoint\\' + style + '_new.png'
        old = '\\fullnessPoint\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)
