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

@allure.feature('版片行走基本流程')
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


    @allure.story('版片行走基本流程')
    def test_add_one(self):

        self.style.add_open_sproj('walk', '版片行走.sproj')
        self.style.click_walk()
        auto.click(x=conf["Walk"]["add_one_1"]['x'], y=conf["Walk"]["add_one_1"]['y'],button=conf["Walk"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["Walk"]["add_one_2"]['x'], y=conf["Walk"]["add_one_2"]['y'],button=conf["Walk"]["add_one_2"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '点击移动版片'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Walk"]["add_one_3"]['x'], y=conf["Walk"]["add_one_3"]['y'],button=conf["Walk"]["add_one_3"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '点击固定版片'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Walk"]["add_one_4"]['x'], y=conf["Walk"]["add_one_4"]['y'],button=conf["Walk"]["add_one_4"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '左键打断点'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Walk"]["add_one_5"]['x'], y=conf["Walk"]["add_one_5"]['y'],button=conf["Walk"]["add_one_5"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '鼠标行走长度大于绘制版片周长'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Walk"]["add_one_6"]['x'], y=conf["Walk"]["add_one_6"]['y'],button=conf["Walk"]["add_one_6"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '打断点后行走长度大于静止版片长度的一半'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Walk"]["add_one_7"]['x'], y=conf["Walk"]["add_one_7"]['y'],button=conf["Walk"]["add_one_7"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '可以跨版片行走'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.press('esc')
        time.sleep(0.5)
        style = '点击esc退出行走'
        new = '\\walk\\' + style + '_new.png'
        old = '\\walk\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)