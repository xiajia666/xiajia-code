import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('省')
@allure.severity(allure.severity_level.CRITICAL)
class Test_AddNormalDart:

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

    @allure.story('省模式')
    def test_add_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_addnornamldart()
        auto.click(x=conf["AddNormanDart"]["add_one_1"]['x'],y=conf["AddNormanDart"]["add_one_1"]['y'], clicks=conf["AddNormanDart"]["add_one_1"]['clicks'], button=conf["AddNormanDart"]["add_one_1"]['button'], duration=0.2)
        auto.click(x=conf["AddNormanDart"]["add_one_8"]['x'],y=conf["AddNormanDart"]["add_one_8"]['y'], clicks=conf["AddNormanDart"]["add_one_8"]['clicks'], button=conf["AddNormanDart"]["add_one_8"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '省弹窗取消'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)


        self.style.click_addnornamldart()
        auto.click(x=conf["AddNormanDart"]["add_one_1"]['x'],y=conf["AddNormanDart"]["add_one_1"]['y'], clicks=conf["AddNormanDart"]["add_one_1"]['clicks'], button=conf["AddNormanDart"]["add_one_1"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '省的预览'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["AddNormanDart"]["add_one_2"]['x'], y=conf["AddNormanDart"]["add_one_2"]['y'],clicks=conf["AddNormanDart"]["add_one_2"]['clicks'],button=conf["AddNormanDart"]["add_one_2"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='250.49',interval=0.5)

        auto.click(x=conf["AddNormanDart"]["add_one_3"]['x'], y=conf["AddNormanDart"]["add_one_3"]['y'],clicks=conf["AddNormanDart"]["add_one_3"]['clicks'],button=conf["AddNormanDart"]["add_one_3"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='150.00', interval=0.5)

        auto.click(x=conf["AddNormanDart"]["add_one_4"]['x'], y=conf["AddNormanDart"]["add_one_4"]['y'],clicks=conf["AddNormanDart"]["add_one_4"]['clicks'],button=conf["AddNormanDart"]["add_one_4"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='120.00', interval=0.5)

        time.sleep(0.5)
        style = '修改输入框'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["AddNormanDart"]["add_one_5"]['x'], y=conf["AddNormanDart"]["add_one_5"]['y'],clicks=conf["AddNormanDart"]["add_one_5"]['clicks'],button=conf["AddNormanDart"]["add_one_5"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='30.00', interval=0.5)
        auto.click(x=conf["AddNormanDart"]["add_one_6"]['x'], y=conf["AddNormanDart"]["add_one_6"]['y'],clicks=conf["AddNormanDart"]["add_one_6"]['clicks'],button=conf["AddNormanDart"]["add_one_6"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='60.00', interval=0.5)
        time.sleep(0.5)
        style = '宽度联动1'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["AddNormanDart"]["add_one_4"]['x'], y=conf["AddNormanDart"]["add_one_4"]['y'],clicks=conf["AddNormanDart"]["add_one_4"]['clicks'],button=conf["AddNormanDart"]["add_one_4"]['button'], duration=0.2)
        self.style.click_backspace_number(8)
        auto.typewrite(message='30.00', interval=0.5)
        time.sleep(0.5)
        style = '宽度联动2'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_addnornamldartenter()
        time.sleep(0.5)
        style = '省弹窗确定'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_addnornamldart()
        auto.click(x=conf["AddNormanDart"]["add_one_7"]['x'],y=conf["AddNormanDart"]["add_one_7"]['y'], clicks=conf["AddNormanDart"]["add_one_7"]['clicks'], button=conf["AddNormanDart"]["add_one_7"]['button'], duration=0.2)
        auto.click(x=conf["AddNormanDart"]["add_one_9"]['x'],y=conf["AddNormanDart"]["add_one_9"]['y'], clicks=conf["AddNormanDart"]["add_one_9"]['clicks'], button=conf["AddNormanDart"]["add_one_9"]['button'], duration=0.2)
        self.style.click_addnornamldartenter()
        time.sleep(0.5)
        style = '不勾选自动缝合'
        new = '\\AddNormanDart\\' + style + '_new.png'
        old = '\\AddNormanDart\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)







