import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('剪切-素材消失')
@allure.severity(allure.severity_level.BLOCKER)
class TestCUT():

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

    @allure.story('one:jira-15560')
    def test_add_one(self):

        self.style.add_open_sproj('cut', '15560.sproj')
        self.style.click_edit_pattern()#编辑版片模式

        # 放大视角，中间对称轴，右键选择剪切，查看假缝没有消失
        auto.click(x=conf["CutMaterialDisappearance-15560"]["click_one1"]["x"], y=conf["CutMaterialDisappearance-15560"]["click_one1"]["y"], clicks=conf["CutMaterialDisappearance-15560"]["click_one1"]["clicks"],button=conf["CutMaterialDisappearance-15560"]["click_one1"]["button"], duration=0.2)
        self.style.scroll_big_number(6)
        auto.click(x=conf["CutMaterialDisappearance-15560"]["click_one11"]["x"], y=conf["CutMaterialDisappearance-15560"]["click_one11"]["y"], clicks=conf["CutMaterialDisappearance-15560"]["click_one11"]["clicks"],button=conf["CutMaterialDisappearance-15560"]["click_one11"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-15560"]["click_one13"]["x"], y=conf["CutMaterialDisappearance-15560"]["click_one13"]["y"], clicks=conf["CutMaterialDisappearance-15560"]["click_one13"]["clicks"],button=conf["CutMaterialDisappearance-15560"]["click_one13"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-15560'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-15256')
    def test_add_two(self):
        self.style.add_open_sproj('cut', '15256.sproj')
        self.style.click_edit_pattern()  # 编辑版片模式

        # 放大视角，中间对称轴，右键选择剪切，查看固定针没有消失
        auto.click(x=conf["CutMaterialDisappearance-15256"]["click_one_3"]["x"], y=conf["CutMaterialDisappearance-15256"]["click_one_3"]["y"], clicks=conf["CutMaterialDisappearance-15256"]["click_one_3"]["clicks"],button=conf["CutMaterialDisappearance-15256"]["click_one_3"]["button"], duration=0.2)
        self.style.scroll_big_number(3)
        auto.click(x=conf["CutMaterialDisappearance-15256"]["click_one_8"]["x"], y=conf["CutMaterialDisappearance-15256"]["click_one_8"]["y"], clicks=conf["CutMaterialDisappearance-15256"]["click_one_8"]["clicks"],button=conf["CutMaterialDisappearance-15256"]["click_one_8"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-15256"]["click_one_10"]["x"], y=conf["CutMaterialDisappearance-15256"]["click_one_10"]["y"], clicks=conf["CutMaterialDisappearance-15256"]["click_one_10"]["clicks"],button=conf["CutMaterialDisappearance-15256"]["click_one_10"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-15256'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-14257')
    def test_add_three(self):
        self.style.add_open_sproj('cut', '14257.sproj')
        self.style.click_edit_pattern()  # 编辑版片模式

        # 放大视角，系纽扣，合并两条线，勾勒轮廓模式下剪切
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_1"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_1"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_1"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(5)
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_36"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_36"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_36"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_36"]["button"], duration=0.2)
        # 按住shift
        auto.keyDown('shift')
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_57"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_57"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_57"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_57"]["button"], duration=0.2)
        # 松开shift
        auto.keyUp('shift')
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_69"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_69"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_69"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_69"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_71"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_71"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_71"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_71"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_73"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_73"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_73"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_73"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_75"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_75"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_75"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_75"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-14257"]["click_one_77"]["x"], y=conf["CutMaterialDisappearance-14257"]["click_one_77"]["y"], clicks=conf["CutMaterialDisappearance-14257"]["click_one_77"]["clicks"],button=conf["CutMaterialDisappearance-14257"]["click_one_77"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-14257'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-12999')
    def test_add_four(self):
        self.style.add_open_sproj('cut', '12999.sproj')
        self.style.click_edit_pattern()  # 编辑版片模式

        # 右键选择剪切，查看固定针没有消失
        auto.click(x=conf["CutMaterialDisappearance-12999"]["click_one_9"]["x"], y=conf["CutMaterialDisappearance-12999"]["click_one_9"]["y"], clicks=conf["CutMaterialDisappearance-12999"]["click_one_9"]["clicks"],button=conf["CutMaterialDisappearance-12999"]["click_one_9"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-12999"]["click_one_11"]["x"], y=conf["CutMaterialDisappearance-12999"]["click_one_11"]["y"], clicks=conf["CutMaterialDisappearance-12999"]["click_one_11"]["clicks"],button=conf["CutMaterialDisappearance-12999"]["click_one_11"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-12999'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')

    @allure.story('one:jira-8258')
    def test_add_five(self):
        self.style.add_open_sproj('cut', '8258.sproj')
        self.style.click_edit_pattern()  # 编辑版片模式

        auto.click(x=conf["CutMaterialDisappearance-8258"]["click_one_1"]["x"], y=conf["CutMaterialDisappearance-8258"]["click_one_1"]["y"], clicks=conf["CutMaterialDisappearance-8258"]["click_one_1"]["clicks"],button=conf["CutMaterialDisappearance-8258"]["click_one_1"]["button"], duration=0.2)
        self.style.scroll_big_number(7)
        auto.click(x=conf["CutMaterialDisappearance-8258"]["click_one_12"]["x"], y=conf["CutMaterialDisappearance-8258"]["click_one_12"]["y"], clicks=conf["CutMaterialDisappearance-8258"]["click_one_12"]["clicks"],button=conf["CutMaterialDisappearance-8258"]["click_one_12"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-8258"]["click_one_14"]["x"], y=conf["CutMaterialDisappearance-8258"]["click_one_14"]["y"], clicks=conf["CutMaterialDisappearance-8258"]["click_one_14"]["clicks"],button=conf["CutMaterialDisappearance-8258"]["click_one_14"]["button"], duration=0.2)
        auto.click(x=conf["CutMaterialDisappearance-8258"]["click_one_16"]["x"], y=conf["CutMaterialDisappearance-8258"]["click_one_16"]["y"], clicks=conf["CutMaterialDisappearance-8258"]["click_one_16"]["clicks"],button=conf["CutMaterialDisappearance-8258"]["click_one_16"]["button"], duration=0.2)
        time.sleep(3)
        style = 'jira-8258'
        new = '\\CUT\\' + style + '_new.png'
        old = '\\CUT\\' + style + '_new.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        auto.press('del')