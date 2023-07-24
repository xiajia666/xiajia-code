import os
import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('三角化检查')
@allure.severity(allure.severity_level.BLOCKER)
class Test_TriangulationCheck:

    def setup_method(self):
        global conf
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.log.info("测试开始")
        self.operationfile.change_mouse_position()
        conf = self.style.get_conf_mouse()
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info('测试结束，关闭软件')
        self.style.close_style3D()


    @allure.story('三角化检查，工程1')
    def test_add_one(self):
        self.style.add_open_sproj('sproj', 'jira17647, 打开后模拟，程序崩溃.sproj')
        time.sleep(20)
        self.style.click_user_settings()
        time.sleep(2)
        auto.click(x=conf["Triangulation"]["check_one_1"]['x'], y=conf["Triangulation"]["check_one_1"]['y'],clicks=conf["Triangulation"]["check_one_1"]['clicks'],button=conf["Triangulation"]["check_one_1"]['button'], duration=0.2)
        time.sleep(2)
        auto.click(x=conf["Triangulation"]["check_one_2"]['x'], y=conf["Triangulation"]["check_one_2"]['y'],clicks=conf["Triangulation"]["check_one_2"]['clicks'],button=conf["Triangulation"]["check_one_2"]['button'], duration=0.2)
        time.sleep(15)
        style = '工程检查1'
        new = '\\Triangulation\\'+style+'_new.png'
        old = '\\Triangulation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 582, 158, 1335, 500)









