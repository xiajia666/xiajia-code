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

@allure.feature('新增默认t-shirt')
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
        auto.press('q')
        self.log.info('结束该用例')


    @allure.story('新增默认t-shirt')
    def test_add_tshirt(self):
        self.style.click_import_dxf()
        dxf_path = os.path.join(self.operationfile.get_garder_path('studio'), 'sproj') + '\\' + "Male_T-Shirt.dxf"
        pyperclip.copy(dxf_path)
        time.sleep(1)
        auto.hotkey('ctrl','v')
        time.sleep(1)
        auto.press('enter')
        #导入dxf弹框点击重置,确定
        auto.click(x=conf["ImportDxfSubject"]["click_one_1"]['x'], y=conf["ImportDxfSubject"]["click_one_1"]['y'],clicks=conf["ImportDxfSubject"]["click_one_1"]['clicks'],button=conf["ImportDxfSubject"]["click_one_1"]['button'], duration=0.2)
        auto.click(x=conf["ImportDxfSubject"]["click_one_2"]['x'], y=conf["ImportDxfSubject"]["click_one_2"]['y'],clicks=conf["ImportDxfSubject"]["click_one_2"]['clicks'],button=conf["ImportDxfSubject"]["click_one_2"]['button'], duration=0.2)
        time.sleep(3)
        self.style.add_avatar('Man175.savt')
        auto.press('a')#显示安排点
        #安排版片
        auto.press('2')
        auto.click(x=conf["MakeClothes"]["make_one_1"]["x"], y=conf["MakeClothes"]["make_one_1"]["y"], clicks=conf["MakeClothes"]["make_one_1"]["clicks"],button=conf["MakeClothes"]["make_one_1"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_3"]["x"], y=conf["MakeClothes"]["make_one_3"]["y"], clicks=conf["MakeClothes"]["make_one_3"]["clicks"],button=conf["MakeClothes"]["make_one_3"]["button"], duration=0.2)
        auto.mouseDown(x=conf["MakeClothes"]["make_one_5"]["x"], y=conf["MakeClothes"]["make_one_5"]["y"],button=conf["MakeClothes"]["make_one_5"]["button"], duration=0.2)
        auto.mouseUp(x=conf["MakeClothes"]["make_one_6up"]["x"], y=conf["MakeClothes"]["make_one_6up"]["y"],button=conf["MakeClothes"]["make_one_6up"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_7"]["x"], y=conf["MakeClothes"]["make_one_7"]["y"], clicks=conf["MakeClothes"]["make_one_7"]["clicks"],button=conf["MakeClothes"]["make_one_7"]["button"], duration=0.2)
        auto.keyDown('shift')
        auto.click(x=conf["MakeClothes"]["make_one_35"]["x"], y=conf["MakeClothes"]["make_one_35"]["y"], clicks=conf["MakeClothes"]["make_one_35"]["clicks"],button=conf["MakeClothes"]["make_one_35"]["button"], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        auto.click(x=conf["MakeClothes"]["make_one_41"]["x"], y=conf["MakeClothes"]["make_one_41"]["y"], clicks=conf["MakeClothes"]["make_one_41"]["clicks"],button=conf["MakeClothes"]["make_one_41"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_43"]["x"], y=conf["MakeClothes"]["make_one_43"]["y"], clicks=conf["MakeClothes"]["make_one_43"]["clicks"],button=conf["MakeClothes"]["make_one_43"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_45"]["x"], y=conf["MakeClothes"]["make_one_45"]["y"], clicks=conf["MakeClothes"]["make_one_45"]["clicks"],button=conf["MakeClothes"]["make_one_45"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_47"]["x"], y=conf["MakeClothes"]["make_one_47"]["y"], clicks=conf["MakeClothes"]["make_one_47"]["clicks"],button=conf["MakeClothes"]["make_one_47"]["button"], duration=0.2)
        auto.mouseDown(x=conf["MakeClothes"]["make_one_49"]["x"], y=conf["MakeClothes"]["make_one_49"]["y"],button=conf["MakeClothes"]["make_one_49"]["button"], duration=0.2)
        auto.mouseUp(x=conf["MakeClothes"]["make_one_50up"]["x"], y=conf["MakeClothes"]["make_one_50up"]["y"],button=conf["MakeClothes"]["make_one_50up"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_51"]["x"], y=conf["MakeClothes"]["make_one_51"]["y"], clicks=conf["MakeClothes"]["make_one_51"]["clicks"],button=conf["MakeClothes"]["make_one_51"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_53"]["x"], y=conf["MakeClothes"]["make_one_53"]["y"], clicks=conf["MakeClothes"]["make_one_53"]["clicks"],button=conf["MakeClothes"]["make_one_53"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_55"]["x"], y=conf["MakeClothes"]["make_one_55"]["y"], clicks=conf["MakeClothes"]["make_one_55"]["clicks"],button=conf["MakeClothes"]["make_one_55"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_57"]["x"], y=conf["MakeClothes"]["make_one_57"]["y"], clicks=conf["MakeClothes"]["make_one_57"]["clicks"],button=conf["MakeClothes"]["make_one_57"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_59"]["x"], y=conf["MakeClothes"]["make_one_59"]["y"], clicks=conf["MakeClothes"]["make_one_59"]["clicks"],button=conf["MakeClothes"]["make_one_59"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_61"]["x"], y=conf["MakeClothes"]["make_one_61"]["y"], clicks=conf["MakeClothes"]["make_one_61"]["clicks"],button=conf["MakeClothes"]["make_one_61"]["button"], duration=0.2)
        auto.mouseDown(x=conf["MakeClothes"]["make_one_63"]["x"], y=conf["MakeClothes"]["make_one_63"]["y"],button=conf["MakeClothes"]["make_one_63"]["button"], duration=0.2)
        auto.mouseUp(x=conf["MakeClothes"]["make_one_64up"]["x"], y=conf["MakeClothes"]["make_one_64up"]["y"],button=conf["MakeClothes"]["make_one_64up"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_65"]["x"], y=conf["MakeClothes"]["make_one_65"]["y"], clicks=conf["MakeClothes"]["make_one_65"]["clicks"],button=conf["MakeClothes"]["make_one_65"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_67"]["x"], y=conf["MakeClothes"]["make_one_67"]["y"], clicks=conf["MakeClothes"]["make_one_67"]["clicks"],button=conf["MakeClothes"]["make_one_67"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_69"]["x"], y=conf["MakeClothes"]["make_one_69"]["y"], clicks=conf["MakeClothes"]["make_one_69"]["clicks"],button=conf["MakeClothes"]["make_one_69"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_71"]["x"], y=conf["MakeClothes"]["make_one_71"]["y"], clicks=conf["MakeClothes"]["make_one_71"]["clicks"],button=conf["MakeClothes"]["make_one_71"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_73"]["x"], y=conf["MakeClothes"]["make_one_73"]["y"], clicks=conf["MakeClothes"]["make_one_73"]["clicks"],button=conf["MakeClothes"]["make_one_73"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_75"]["x"], y=conf["MakeClothes"]["make_one_75"]["y"], clicks=conf["MakeClothes"]["make_one_75"]["clicks"],button=conf["MakeClothes"]["make_one_75"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_77"]["x"], y=conf["MakeClothes"]["make_one_77"]["y"], clicks=conf["MakeClothes"]["make_one_77"]["clicks"],button=conf["MakeClothes"]["make_one_77"]["button"], duration=0.2)
        auto.mouseDown(x=conf["MakeClothes"]["make_one_79"]["x"], y=conf["MakeClothes"]["make_one_79"]["y"],button=conf["MakeClothes"]["make_one_79"]["button"], duration=0.2)
        auto.mouseUp(x=conf["MakeClothes"]["make_one_80up"]["x"], y=conf["MakeClothes"]["make_one_80up"]["y"],button=conf["MakeClothes"]["make_one_80up"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_81"]["x"], y=conf["MakeClothes"]["make_one_81"]["y"], clicks=conf["MakeClothes"]["make_one_81"]["clicks"],button=conf["MakeClothes"]["make_one_81"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_83"]["x"], y=conf["MakeClothes"]["make_one_83"]["y"], clicks=conf["MakeClothes"]["make_one_83"]["clicks"],button=conf["MakeClothes"]["make_one_83"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_85"]["x"], y=conf["MakeClothes"]["make_one_85"]["y"], clicks=conf["MakeClothes"]["make_one_85"]["clicks"],button=conf["MakeClothes"]["make_one_85"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_87"]["x"], y=conf["MakeClothes"]["make_one_87"]["y"], clicks=conf["MakeClothes"]["make_one_87"]["clicks"],button=conf["MakeClothes"]["make_one_87"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_89"]["x"], y=conf["MakeClothes"]["make_one_89"]["y"], clicks=conf["MakeClothes"]["make_one_89"]["clicks"],button=conf["MakeClothes"]["make_one_89"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_91"]["x"], y=conf["MakeClothes"]["make_one_91"]["y"], clicks=conf["MakeClothes"]["make_one_91"]["clicks"],button=conf["MakeClothes"]["make_one_91"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_93"]["x"], y=conf["MakeClothes"]["make_one_93"]["y"], clicks=conf["MakeClothes"]["make_one_93"]["clicks"],button=conf["MakeClothes"]["make_one_93"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_95"]["x"], y=conf["MakeClothes"]["make_one_95"]["y"], clicks=conf["MakeClothes"]["make_one_95"]["clicks"],button=conf["MakeClothes"]["make_one_95"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_97"]["x"], y=conf["MakeClothes"]["make_one_97"]["y"], clicks=conf["MakeClothes"]["make_one_97"]["clicks"],button=conf["MakeClothes"]["make_one_97"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_99"]["x"], y=conf["MakeClothes"]["make_one_99"]["y"], clicks=conf["MakeClothes"]["make_one_99"]["clicks"],button=conf["MakeClothes"]["make_one_99"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_101"]["x"], y=conf["MakeClothes"]["make_one_101"]["y"], clicks=conf["MakeClothes"]["make_one_101"]["clicks"],button=conf["MakeClothes"]["make_one_101"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_103"]["x"], y=conf["MakeClothes"]["make_one_103"]["y"], clicks=conf["MakeClothes"]["make_one_103"]["clicks"],button=conf["MakeClothes"]["make_one_103"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_105"]["x"], y=conf["MakeClothes"]["make_one_105"]["y"], clicks=conf["MakeClothes"]["make_one_105"]["clicks"],button=conf["MakeClothes"]["make_one_105"]["button"], duration=0.2)
        auto.click(x=conf["MakeClothes"]["make_one_107"]["x"], y=conf["MakeClothes"]["make_one_107"]["y"], clicks=conf["MakeClothes"]["make_one_107"]["clicks"],button=conf["MakeClothes"]["make_one_107"]["button"], duration=0.2)
        auto.press('2')
        auto.press('space')
        time.sleep(10)
        style = '默认Tshirt缝纫模拟'
        new = '\\makeclothes\\' + style + '_new.png'
        old = '\\makeclothes\\' + style + '_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 300)



