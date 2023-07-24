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
import pytest
screen_width, screen_height = auto.size()

@allure.feature('2D快照')
@allure.severity(allure.severity_level.CRITICAL)
class Test2DSnapshot(Log):

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


    @allure.story('工程保存2D快照')
    def test_add_one(self):
        self.style.add_open_sproj('sproj', '2D_Snapshot.sproj')
        self.style.click_snapshot_2d()
        time.sleep(2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_1"]['x'], y=conf["ClickSnapshot2DOption"]["click_one_1"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_1"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_1"]['button'], duration=0.2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_10"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_10"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_10"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_10"]['button'], duration=0.2)
        auto.press("del")
        auto.typewrite("50")
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_2"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_2"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_2"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_2"]['button'], duration=0.2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_3"]['x'], y=conf["ClickSnapshot2DOption"]["click_one_3"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_3"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_3"]['button'], duration=0.2)
        auto.press("del")
        auto.typewrite("5")
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_4"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_4"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_4"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_4"]['button'], duration=0.2)
        auto.press("del")
        auto.typewrite("10")
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_5"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_5"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_5"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_5"]['button'], duration=0.2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_6"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_6"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_6"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_6"]['button'], duration=0.2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_7"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_7"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_7"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_7"]['button'], duration=0.2)
        style = '2D视窗截图查看'
        new = '\\2DSnapshot\\' + style + '_new.png'
        old = '\\2DSnapshot\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(2)

        #点击保存，输出2D快照
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            export_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', '2DSnapshot')+ '\\' + '2DSnapshot'
        elif str(screen_width) == '2560':
            export_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_2k', '2DSnapshot')+ '\\' + '2DSnapshot'
        elif str(screen_width) == '3840':
            export_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_2k', '2DSnapshot')+ '\\' + '2DSnapshot'
        pyperclip.copy(export_path)
        time.sleep(2)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_8"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_8"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_8"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_8"]['button'], duration=0.2)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(15)
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_9"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_9"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_9"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_9"]['button'], duration=0.2)# 关闭2D快照保存成功提示
        auto.press('esc')

        #比较图片，如果有不同则生成展示不同的图片
        new = export_path + '_齐色 0_M.tif'
        old = export_path + '_齐色 0_M_old.tif'
        print("!!!!!!!!!"+new)
        difference = (OperationFile().contrast_image(new, old))
        difference_save = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920',
                                       'different') + '\\' + style + '图片不一样查看.png'
        OperationFile().compare_images(new, old, difference_save)

        with allure.step("%s预期结果" % style):
            allure.attach.file(old, attachment_type=allure.attachment_type.PNG)
        with allure.step("%s实际结果" % style):
            allure.attach.file(new, attachment_type=allure.attachment_type.PNG)
        with allure.step("图片比较结果"):
            allure.attach("图片比较差别: %s" % difference, '%s图片比较差别' % style)
        if difference != 0:
            with allure.step("%s图片比较" % style):
                allure.attach.file(difference_save, attachment_type=allure.attachment_type.PNG)
        else:
            self.info("%s图片一样" % style)
            pass
        self.info("%s图片比较差别:%s" % (style, difference))
        # assert difference < differencevalue
        pytest.assume(difference < 200)
        self.info("%s图片测试通过" % style)

    @allure.story('无版片时保存')
    def test_add_two(self):
        #空工程保存，弹窗提示
        self.style.click_snapshot_2d()
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_11"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_11"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_11"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_11"]['button'], duration=0.2)
        style = '空工程保存'
        new = '\\2DSnapshot\\' + style + '_new.png'
        old = '\\2DSnapshot\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)
        time.sleep(5)

        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_9"]['x'],y=conf["ClickSnapshot2DOption"]["click_one_9"]['y'],clicks=conf["ClickSnapshot2DOption"]["click_one_9"]['clicks'],button=conf["ClickSnapshot2DOption"]["click_one_9"]['button'], duration=0.2)# 关闭2D快照保存成功提示
        auto.press('esc')

        #辅料、隐藏版片保存，弹窗提示
        self.style.add_open_sproj('sproj', '2D_Snapshot_null.sproj')
        self.style.click_snapshot_2d()
        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_11"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_11"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_11"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_11"]['button'], duration=0.2)
        style = '辅料及隐藏版片工程保存'
        new = '\\2DSnapshot\\' + style + '_new.png'
        old = '\\2DSnapshot\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 200)

        auto.click(x=conf["ClickSnapshot2DOption"]["click_one_9"]['x'],
                   y=conf["ClickSnapshot2DOption"]["click_one_9"]['y'],
                   clicks=conf["ClickSnapshot2DOption"]["click_one_9"]['clicks'],
                   button=conf["ClickSnapshot2DOption"]["click_one_9"]['button'], duration=0.2)  # 关闭2D快照保存成功提示
        auto.press('esc')