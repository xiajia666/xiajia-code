import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('菱形省选择，修改')
@allure.severity(allure.severity_level.CRITICAL)
class TestChoose:

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

    @allure.story('选择移动模式下，可以选择菱形省，对省菱形省进行缩放操作')
    def test_choose_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["choose_one_1"]['x'], y=conf["Dart"]["choose_one_1"]['y'], clicks=conf["Dart"]["choose_one_1"]['clicks'], button=conf["Dart"]["choose_one_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["choose_one_2"]['x'], y=conf["Dart"]["choose_one_2"]['y'], clicks=conf["Dart"]["choose_one_2"]['clicks'], button=conf["Dart"]["choose_one_2"]['button'], duration=0.2)
        auto.press('q')
        auto.click(x=conf["Dart"]["choose_one_3"]['x'], y=conf["Dart"]["choose_one_3"]['y'], clicks=conf["Dart"]["choose_one_3"]['clicks'], button=conf["Dart"]["choose_one_3"]['button'], duration=0.2)
        auto.mouseDown(x=conf["Dart"]["choose_one_4"]['x'], y=conf["Dart"]["choose_one_4"]['y'], button=conf["Dart"]["choose_one_4"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Dart"]["choose_one_5"]['x'], y=conf["Dart"]["choose_one_5"]['y'], button=conf["Dart"]["choose_one_5"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '选择移动模式下，可以选择菱形省，对省菱形省进行缩放操作'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('选择移动模式下，可以选择菱形省，对省菱形省进行旋转操作')
    def test_choose_two(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_Dart()
        auto.click(x=conf["Dart"]["choose_two_1"]['x'], y=conf["Dart"]["choose_two_1"]['y'], clicks=conf["Dart"]["choose_two_1"]['clicks'], button=conf["Dart"]["choose_two_1"]['button'], duration=0.2)
        auto.click(x=conf["Dart"]["choose_two_2"]['x'], y=conf["Dart"]["choose_two_2"]['y'], clicks=conf["Dart"]["choose_two_2"]['clicks'], button=conf["Dart"]["choose_two_2"]['button'], duration=0.2)
        auto.press('q')
        auto.click(x=conf["Dart"]["choose_two_3"]['x'], y=conf["Dart"]["choose_two_3"]['y'], clicks=conf["Dart"]["choose_two_3"]['clicks'], button=conf["Dart"]["choose_two_3"]['button'], duration=0.2)
        auto.mouseDown(x=conf["Dart"]["choose_two_4"]['x'], y=conf["Dart"]["choose_two_4"]['y'], button=conf["Dart"]["choose_two_4"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Dart"]["choose_two_5"]['x'], y=conf["Dart"]["choose_two_5"]['y'], button=conf["Dart"]["choose_two_5"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '选择移动模式下，可以选择菱形省，对省菱形省进行旋转操作'
        new = '\\Dart\\'+style+'_new.png'
        old = '\\Dart\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)