import os
import sys
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
import allure
import pytest
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile

@allure.feature('注释')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddAnnotation:

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


    @allure.story('框选注释')
    def test_choose_two(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        self.style.click_addannotation()
        auto.click(x=conf["Annotation"]["choose_two_1"]['x'],y=conf["Annotation"]["choose_two_1"]['y'], clicks=conf["Annotation"]["choose_two_1"]['clicks'], button=conf["Annotation"]["choose_two_1"]['button'], duration=0.2)
        auto.typewrite('33344')
        auto.click(x=conf["Annotation"]["choose_two_2"]['x'],y=conf["Annotation"]["choose_two_2"]['y'], clicks=conf["Annotation"]["choose_two_2"]['clicks'], button=conf["Annotation"]["choose_two_2"]['button'], duration=0.2)
        auto.typewrite('887777')
        auto.mouseDown(x=conf["Annotation"]["choose_two_3"]['x'], y=conf["Annotation"]["choose_two_3"]['y'],button=conf["Annotation"]["choose_two_3"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Annotation"]["choose_two_4"]['x'], y=conf["Annotation"]["choose_two_4"]['y'],button=conf["Annotation"]["choose_two_4"]['button'], duration=0.2)
        time.sleep(0.5)

        style = '框选注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 144, 311, 650, 812)

    @allure.story('新增注释，修改相应的属性，删除注释')
    def test_Annotation(self):
        self.style.rectangle_creat()
        self.style.focus_panorama()
        self.style.click_cloth_textured_surface2d()
        auto.press('2')
        self.style.click_addannotation()
        auto.click(x=conf["Annotation"]["outside_add"]['x'],y=conf["Annotation"]["outside_add"]['y'], clicks=conf["Annotation"]["outside_add"]['clicks'], button=conf["Annotation"]["outside_add"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '版片外点击注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_addannotation_warning_close()
        auto.click(x=conf["Annotation"]["inside_add_one"]['x'],y=conf["Annotation"]["inside_add_one"]['y'], clicks=conf["Annotation"]["inside_add_one"]['clicks'], button=conf["Annotation"]["inside_add_one"]['button'], duration=0.2)
        auto.typewrite('1234567890')
        time.sleep(0.5)
        auto.click(x=conf["Annotation"]["inside_add_two"]['x'], y=conf["Annotation"]["inside_add_two"]['y'], clicks=conf["Annotation"]["inside_add_two"]['clicks'], button=conf["Annotation"]["inside_add_two"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '增加注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Annotation"]["edit_annotation_choose"]['x'], y=conf["Annotation"]["edit_annotation_choose"]['y'], clicks=conf["Annotation"]["edit_annotation_choose"]['clicks'], button=conf["Annotation"]["edit_annotation_choose"]['button'], duration=0.2)
        auto.click(x=conf["Annotation"]["edit_annotation_name"]['x'], y=conf["Annotation"]["edit_annotation_name"]['y'], clicks=conf["Annotation"]["edit_annotation_name"]['clicks'], button=conf["Annotation"]["edit_annotation_name"]['button'], duration=0.2)
        auto.typewrite('852134')
        auto.click(x=conf["Annotation"]["edit_annotation_text"]['x'], y=conf["Annotation"]["edit_annotation_text"]['y'], clicks=conf["Annotation"]["edit_annotation_text"]['clicks'], button=conf["Annotation"]["edit_annotation_text"]['button'], duration=0.2)
        auto.typewrite('8888888')
        auto.mouseDown(x=conf["Annotation"]["edit_annotation_angle_dragfirst"]['x'], y=conf["Annotation"]["edit_annotation_angle_dragfirst"]['y'], button=conf["Annotation"]["edit_annotation_angle_dragfirst"]['button'])
        auto.mouseUp(x=conf["Annotation"]["edit_annotation_angle_dragend"]['x'], y=conf["Annotation"]["edit_annotation_angle_dragend"]['y'], button=conf["Annotation"]["edit_annotation_angle_dragend"]['button'])
        auto.click(x=conf["Annotation"]["edit_annotation_fontsize"]['x'], y=conf["Annotation"]["edit_annotation_fontsize"]['y'], clicks=conf["Annotation"]["edit_annotation_fontsize"]['clicks'], button=conf["Annotation"]["edit_annotation_fontsize"]['button'], duration=0.2)
        auto.typewrite('25')
        auto.press('enter')
        time.sleep(0.5)
        style = '修改注释属性'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Annotation"]["choose_more_one"]['x'], y=conf["Annotation"]["choose_more_one"]['y'], clicks=conf["Annotation"]["choose_more_one"]['clicks'], button=conf["Annotation"]["choose_more_one"]['button'], duration=0.2)
        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf["Annotation"]["choose_more_two"]['x'], y=conf["Annotation"]["choose_more_two"]['y'], clicks=conf["Annotation"]["choose_more_two"]['clicks'], button=conf["Annotation"]["choose_more_two"]['button'], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        time.sleep(0.5)
        style = 'shift多选注释属性栏查看'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 469, 1912, 683)

        auto.click(x=conf["Annotation"]["ten_one"]['x'], y=conf["Annotation"]["ten_one"]['y'], clicks=conf["Annotation"]["ten_one"]['clicks'], button=conf["Annotation"]["ten_one"]['button'], duration=0.2)
        self.style.click_addannotation_warning_close()
        auto.click(x=conf["Annotation"]["ten_three"]['x'], y=conf["Annotation"]["ten_three"]['y'], clicks=conf["Annotation"]["ten_three"]['clicks'], button=conf["Annotation"]["ten_three"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '多选后单选注释属性栏查看'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50, 1580, 469, 1912, 683)

        auto.keyDown('shift')  # 按下shift键
        auto.click(x=conf["Annotation"]["eleven_one"]['x'], y=conf["Annotation"]["eleven_one"]['y'], clicks=conf["Annotation"]["eleven_one"]['clicks'], button=conf["Annotation"]["eleven_one"]['button'], duration=0.2)
        auto.keyUp('shift')  # 松开shift键
        auto.mouseDown(x=conf["Annotation"]["eleven_two"]['x'], y=conf["Annotation"]["eleven_two"]['y'], button=conf["Annotation"]["eleven_two"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Annotation"]["eleven_three"]['x'], y=conf["Annotation"]["eleven_three"]['y'], button=conf["Annotation"]["eleven_three"]['button'], duration=0.2)
        auto.mouseUp(x=conf["Annotation"]["eleven_three"]['x'], y=conf["Annotation"]["eleven_three"]['y'], button=conf["Annotation"]["eleven_three"]['button'], duration=0.2)
        auto.click(x=conf["Annotation"]["eleven_four"]['x'], y=conf["Annotation"]["eleven_four"]['y'], clicks=conf["Annotation"]["eleven_one"]['clicks'], button=conf["Annotation"]["eleven_four"]['button'], duration=0.2)
        auto.typewrite('55555555')
        auto.press('enter')
        time.sleep(1)
        style = '多选注释拖拽到版片外'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Annotation"]["twelve_one"]['x'], y=conf["Annotation"]["twelve_one"]['y'], clicks=conf["Annotation"]["twelve_one"]['clicks'], button=conf["Annotation"]["twelve_one"]['button'], duration=0.2)
        auto.press('del')
        time.sleep(0.5)
        style = '多选删除注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Annotation"]["thirteen_one"]['x'], y=conf["Annotation"]["thirteen_one"]['y'], clicks=conf["Annotation"]["thirteen_one"]['clicks'], button=conf["Annotation"]["thirteen_one"]['button'], duration=0.2)
        auto.typewrite('66633344')
        auto.click(x=conf["Annotation"]["thirteen_two"]['x'], y=conf["Annotation"]["thirteen_two"]['y'], clicks=conf["Annotation"]["thirteen_two"]['clicks'], button=conf["Annotation"]["thirteen_two"]['button'], duration=0.2)
        self.style.scroll_big_number(14)#放大视角
        auto.click(x=conf["Annotation"]["thirteen_three"]['x'], y=conf["Annotation"]["thirteen_three"]['y'], clicks=conf["Annotation"]["thirteen_three"]['clicks'], button=conf["Annotation"]["thirteen_three"]['button'], duration=0.2)
        time.sleep(0.5)
        style = '放大缩小视角自适应'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.style.click_select()
        self.style.click_popbutton_show_addannotation()
        time.sleep(0.5)
        style = '2D视窗注释按钮'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        self.operationfile.delete_file_style('Annotation_dxf.dxf')  # 删除已存在的dxf文件
        self.style.click_export_dxf()
        annotation_dxf = os.path.join(self.operationfile.get_garder_path('studio'), 'export') + '\\' + 'Annotation_dxf.dxf'
        pyperclip.copy(annotation_dxf)
        time.sleep(2)
        auto.hotkey('ctrl','v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=conf["Annotation"]["fourteen_one"]['x'], y=conf["Annotation"]["fourteen_one"]['y'], clicks=conf["Annotation"]["fourteen_one"]['clicks'], button=conf["Annotation"]["fourteen_one"]['button'], duration=0.2)
        auto.click(x=conf["Annotation"]["fourteen_two"]['x'], y=conf["Annotation"]["fourteen_two"]['y'], clicks=conf["Annotation"]["fourteen_two"]['clicks'], button=conf["Annotation"]["fourteen_two"]['button'], duration=0.2)
        self.style.click_new_project()
        self.style.click_import_dxf()
        time.sleep(2)
        auto.hotkey('ctrl','v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(2)
        auto.click(x=conf["Annotation"]["fourteen_three"]['x'], y=conf["Annotation"]["fourteen_three"]['y'], clicks=conf["Annotation"]["fourteen_three"]['clicks'], button=conf["Annotation"]["fourteen_three"]['button'], duration=0.2)
        auto.click(x=conf["Annotation"]["fourteen_four"]['x'], y=conf["Annotation"]["fourteen_four"]['y'], clicks=conf["Annotation"]["fourteen_four"]['clicks'], button=conf["Annotation"]["fourteen_four"]['button'], duration=0.2)
        self.style.click_select()
        self.style.focus_panorama()
        self.style.click_addannotation()
        time.sleep(0.5)
        style = 'dxf导出查看注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 50)

        auto.click(x=conf["Annotation"]["fiveteen_one"]['x'], y=conf["Annotation"]["fiveteen_one"]['y'], clicks=conf["Annotation"]["fiveteen_one"]['clicks'], button=conf["Annotation"]["fiveteen_one"]['button'], duration=0.2)
        auto.press('del')
        time.sleep(0.5)
        style = '单选删除注释'
        new = '\\AddAnnotation\\'+style+'_new.png'
        old = '\\AddAnnotation\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style,  50, 144, 311, 650, 812)








