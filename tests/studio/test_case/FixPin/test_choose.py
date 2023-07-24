import sys
sys.path.append('../../../../all')
print (sys.path)
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure
import yaml
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())

@allure.feature('固定针选择')
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
        self.log.info('结束该用例')

    @allure.story('在场景管理点击隐藏固定针，在固定针模式下，点击固定针，有相应的定位球')
    @allure.issue('http://192.168.31.3:8080/browse/STYLE3D-11658',name='STYLE3D-11658')
    def test_choose_seven(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_fixpin_box()
        auto.press('2')
        auto.mouseDown(x=conf["FixPin"]["choose_seven_1"]['x'], y=conf["FixPin"]["choose_seven_1"]['y'], button=conf["FixPin"]["choose_seven_1"]['button'], duration=0.2)
        auto.mouseUp(x=conf["FixPin"]["choose_seven_2"]['x'], y=conf["FixPin"]["choose_seven_2"]['y'], button=conf["FixPin"]["choose_seven_2"]['button'], duration=0.2)
        auto.press('q')
        auto.click(x=conf["FixPin"]["choose_seven_3"]['x'], y=conf["FixPin"]["choose_seven_3"]['y'], clicks=conf["FixPin"]["choose_seven_3"]['clicks'], button=conf["FixPin"]["choose_seven_3"]['button'], duration=0.2)
        auto.click(x=conf["FixPin"]["choose_seven_4"]['x'], y=conf["FixPin"]["choose_seven_4"]['y'], clicks=conf["FixPin"]["choose_seven_4"]['clicks'], button=conf["FixPin"]["choose_seven_4"]['button'], duration=0.2)
        auto.click(x=conf["FixPin"]["choose_seven_5"]['x'], y=conf["FixPin"]["choose_seven_5"]['y'],clicks=conf["FixPin"]["choose_seven_5"]['clicks'], button=conf["FixPin"]["choose_seven_5"]['button'],duration=0.2)
        self.style.click_fixpin_box()
        auto.click(x=conf["FixPin"]["choose_seven_6"]['x'], y=conf["FixPin"]["choose_seven_6"]['y'], clicks=conf["FixPin"]["choose_seven_6"]['clicks'], button=conf["FixPin"]["choose_seven_6"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '固定针隐藏后点击显示控制球'
        new = '\\fixpin\\' + style + '_new.png'
        old = '\\fixpin\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)










