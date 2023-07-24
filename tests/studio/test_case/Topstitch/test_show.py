import sys
sys.path.append('../../../../all')
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('明线显示')
@allure.severity(allure.severity_level.CRITICAL)
class TestShow:

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

    @allure.story('线段明线hover蓝色显示')
    def test_show_one(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_segment_topstitch()
        auto.moveTo(x=conf["Topstitch"]["show_one_1"]['x'], y=conf["Topstitch"]["show_one_1"]['y'],duration=0.0, tween=auto.linear)
        time.sleep(0.5)
        style = "线段明线hover蓝色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Topstitch"]["show_one_2"]["x"], y=conf["Topstitch"]["show_one_2"]["y"], clicks=conf["Topstitch"]["show_one_2"]["clicks"],button=conf["Topstitch"]["show_one_2"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "线段明线增加黄色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Topstitch"]["show_one_3"]["x"], y=conf["Topstitch"]["show_one_3"]["y"], clicks=conf["Topstitch"]["show_one_3"]["clicks"],button=conf["Topstitch"]["show_one_3"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "线段明线增加后红色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)


    @allure.story('自由明线hover蓝色显示')
    def test_show_two(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_free_topstitch()
        auto.click(x=conf["Topstitch"]["show_two_1"]["x"], y=conf["Topstitch"]["show_two_1"]["y"], clicks=conf["Topstitch"]["show_two_1"]["clicks"],button=conf["Topstitch"]["show_two_1"]["button"], duration=0.2)
        auto.moveTo(x=conf["Topstitch"]["show_two_2"]['x'], y=conf["Topstitch"]["show_two_2"]['y'],duration=0.0, tween=auto.linear)
        time.sleep(0.5)
        style = "自由明线hover蓝色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Topstitch"]["show_two_3"]["x"], y=conf["Topstitch"]["show_two_3"]["y"], clicks=conf["Topstitch"]["show_two_3"]["clicks"],button=conf["Topstitch"]["show_two_3"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "自由明线增加黄色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_edit_topstitch()
        auto.click(x=conf["Topstitch"]["show_two_4"]["x"], y=conf["Topstitch"]["show_two_4"]["y"], clicks=conf["Topstitch"]["show_two_4"]["clicks"],button=conf["Topstitch"]["show_two_4"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "自由明线增加后红色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

    @allure.story('缝纫线明线hover蓝色显示')
    def test_show_three(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        auto.press('2')
        self.style.click_segment_sewing()
        auto.click(x=conf["Topstitch"]["show_three_1"]["x"], y=conf["Topstitch"]["show_three_1"]["y"], clicks=conf["Topstitch"]["show_three_1"]["clicks"],button=conf["Topstitch"]["show_three_1"]["button"], duration=0.2)
        auto.click(x=conf["Topstitch"]["show_three_2"]["x"], y=conf["Topstitch"]["show_three_2"]["y"], clicks=conf["Topstitch"]["show_three_2"]["clicks"],button=conf["Topstitch"]["show_three_2"]["button"], duration=0.2)
        self.style.click_seamline_topstitch()
        auto.click(x=conf["Topstitch"]["show_three_3"]["x"], y=conf["Topstitch"]["show_three_3"]["y"], clicks=conf["Topstitch"]["show_three_3"]["clicks"],button=conf["Topstitch"]["show_three_3"]["button"], duration=0.2)
        auto.moveTo(x=conf["Topstitch"]["show_three_4"]['x'], y=conf["Topstitch"]["show_three_4"]['y'],duration=0.0, tween=auto.linear)
        time.sleep(0.5)
        style = "缝纫线明线hover蓝色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Topstitch"]["show_three_5"]["x"], y=conf["Topstitch"]["show_three_5"]["y"], clicks=conf["Topstitch"]["show_three_5"]["clicks"],button=conf["Topstitch"]["show_three_5"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "缝纫线明线增加黄色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_edit_topstitch()
        auto.click(x=conf["Topstitch"]["show_three_6"]["x"], y=conf["Topstitch"]["show_three_6"]["y"], clicks=conf["Topstitch"]["show_three_6"]["clicks"],button=conf["Topstitch"]["show_three_6"]["button"], duration=0.2)
        time.sleep(0.5)
        style = "缝纫线明线增加后红色显示"
        new = "\\Topstitch\\"+style+"_new.png"
        old = "\\Topstitch\\"+style+"_old.png"
        self.operationfile.comparison_picture_allure(new, old, style, 50)




