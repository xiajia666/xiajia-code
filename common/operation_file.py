# -*- coding: utf-8 -*-
import time
import zipfile
import allure
import pyautogui as auto
import yaml
from PIL import ImageGrab
from PIL import Image
from PIL import ImageChops
import math
import operator
from functools import reduce
from common.logs import Log
import os
import shutil
import getpass
import pytest
import os.path as osp
# with open('../../../config/studio_config.yaml') as yaml_file:
#     conf_config = yaml.safe_load(yaml_file.read())


class OperationFile(Log):
    """ 文件操作"""

    def get_garder_path(self, filename): # data目录下存放素材的路径，软件使用studio，平台使用XXXX
        path = os.path.split(os.path.realpath(__file__))[0]
        garder = os.path.dirname(path)
        data_path = os.path.join(garder, 'data', filename)
        return data_path


    def get_file_name(self, file_dir): #
        for root, dirs, files in os.walk(file_dir):
            # print(root)  # 当前目录路径
            # print(dirs)  # 当前路径下所有子目录
            # print(files)  # 当前路径下所有非目录子文件
            return files, root

    def assert_file_exist(self, filepath):  #判断导出的文件是否存在
        if os.path.exists(filepath):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(filepath)
            # os.unlink(path)
            print('删除文件成功')
        else:
            print('文件不存在')  # 则返回文件不存在

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print('文件删除成功')
        else:
            print('文件不存在')

    def delete_file_style(self, filename): # 删除studio文件下的指定文件
        path = os.path.join(OperationFile().get_garder_path('studio'), 'export') + '\\' + filename
        OperationFile().delete_file(path)

    def del_file(self, path_data):  #只删除文件，不擅长文件夹
        for file in os.listdir(path_data):
            file_data = path_data + "\\" + file
            print(file_data)
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
            else:
                print(file_data)
                self.del_file(file_data)

    def open_txt(self, txtname, pathname):
        path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', pathname)
        txtpath = path + '\\'+ txtname +'.txt'
        print(txtpath)
        l = []
        for line in open(txtpath, encoding='utf-8'):
            l.append(line)
        return l
        close()

    def unzip_file(self, zip_src, dst_dir):
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, 'r')
            for file in fz.namelist():
                fz.extract(file, dst_dir)
            self.info('解压成功')
        else:
            self.info('This is not zip')

    def copy_file(self, old_path, new_path): #复制文件
        filelist = os.listdir(old_path)  # 列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
        for file in filelist:
            src = os.path.join(old_path, file)
            dst = os.path.join(new_path, file)
            shutil.copy(src, dst)

    def snapshotdialogImage_change(self, view): #快照视角改变
        user_name = getpass.getuser()
        version = conf_config["version"]["version_name"]
        if version == "TEST":
            file_path = 'C:\\Users\\'+ user_name +'\\AppData\\Local\\Style3DTest\\Preference'
        elif version == "PROD":
            file_path = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Style3D\\Preference'
        # file_path = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Style3D\\Preference' + '\\' + 'snapshotDialogImage.json'
        file_path = file_path + '\\' + 'snapshotDialogImage.json'
        OperationFile().delete_file(file_path)
        path = OperationFile().get_garder_path('studio')
        old_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender', view)
        new_path = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Style3D\\Preference'
        OperationFile().copy_file(old_path, new_path)


    def compare_images(self ,img1, img2, diff_save_location):
      """
      比较图片，如果有不同则生成展示不同的图片
      @参数一: path_one: 第一张图片的路径
      @参数二: path_two: 第二张图片的路径
      @参数三: diff_save_location: 不同图的保存路径
      """
      image_one = Image.open(img1)
      image_two = Image.open(img2)
      try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
        # 图片间没有任何不同则直接退出
          print("图片比较一样")
        else:
          diff.save(diff_save_location)
          print("图片比较不一样")
      except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
            "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
            "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
            "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e,text))

    def contrast_image(self, img1, img2): #图像直方图数据比较
      image1 = Image.open(img1)
      image2 = Image.open(img2)
      h1 = image1.histogram()
      h2 = image2.histogram()
      result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
      return result

    def open_yaml(self): #打开yaml，获取分辨率及坐标
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            with open('../../../config/studio_mouse.yaml') as yaml_file:
                conf_mouse = yaml.safe_load(yaml_file.read())
        elif str(screen_width) == '2560':
            with open('../../../config/studio_mouse_2k.yaml') as yaml_file:
                conf_mouse = yaml.safe_load(yaml_file.read())
        elif str(screen_width) == '3840':
            with open('../../../config/studio_mouse_4k.yaml') as yaml_file:
                conf_mouse = yaml.safe_load(yaml_file.read())
        return conf_mouse

    def change_proportion(self, key_value_all, proportion): #自动转换鼠标比例脚本
        for i in range(len(key_value_all)):
            key_value = list(key_value_all[i].values())
            for j in range(len(key_value)):
                x_value = (key_value[j]['x'])
                y_value = (key_value[j]['y'])
                x_proportion_f = x_value * proportion
                x_proportion= int(round(x_proportion_f, 0))
                key_value[j]['x'] = x_proportion
                y_x_proportion_f = y_value * proportion
                y_x_proportion = int(round(y_x_proportion_f, 0))
                key_value[j]['y'] = y_x_proportion

    def copy_resolution(self, resolution_name): #复制不同分辨率的rememberSetting
        path = os.path.split(os.path.realpath(__file__))[0]
        garder = os.path.dirname(path)
        old_path = os.path.join(garder, 'data', 'studio', 'resolution', resolution_name)
        new_path = os.path.join(garder, 'data', 'studio', 'preference')
        OperationFile().copy_file(old_path, new_path)

    def change_mouse_position(self): #根据分辨率自动转换鼠标坐标比例
        with open('../../../config/studio_mouse.yaml') as yaml_file:
            conf_mouse = yaml.safe_load(yaml_file.read())
        key_value_all = list(conf_mouse.values())
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            self.copy_resolution("resolution_1920")
        elif str(screen_width) == '2560':
            self.change_proportion(key_value_all, 1.33333)
            with open('../../../config/studio_mouse_2k.yaml', 'w') as f:
                yaml.safe_dump(data=conf_mouse, stream=f)
            self.copy_resolution("resolution_2k")
        elif str(screen_width) == '3840':
            self.change_proportion(key_value_all, 2)
            with open('../../../config/studio_mouse_4k.yaml', 'w') as f:
                yaml.safe_dump(data=conf_mouse, stream=f)
            self.copy_resolution("resolution_4k")

    def keep_window(self): #保存软件每次窗口与一些默认参数一致
        user_name = getpass.getuser()
        path =  os.path.split(os.path.realpath(__file__))[0]
        garder = os.path.dirname(path)
        old_path = os.path.join(garder, 'data', 'studio', 'preference')
        version = conf_config["version"]["version_name"]
        if version == "TEST":
            new_path = 'C:\\Users\\'+ user_name +'\\AppData\\Local\\Style3DTest\\Preference'
        elif version == "PROD":
            new_path = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Style3D\\Preference'
        OperationFile().copy_file(old_path, new_path)

    def add_picture(self, picturename):#增加图片，配置软件加图片使用
        path = OperationFile().get_garder_path('studio')
        picture_texture = path + '\\' + picturename
        time.sleep(2.5)
        auto.typewrite(picture_texture)
        time.sleep(1)
        auto.press('enter')
        auto.press('enter')#避免因为输入法无法按确定键

    def add_texture(self, picturename):#增加纹理图片，定位到颜色，再相对移动
        color_location = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920') + '\\color.png'  # 定位颜色位置
        try:
            color = auto.locateOnScreen(color_location)
            x, y = auto.center(color)
            auto.moveTo(x, y)
        except TypeError as e:
            print(e)
        auto.moveRel(xOffset=-60, yOffset=-30, duration=0.0, tween=auto.linear)
        time.sleep(1)
        auto.click()
        path = path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920')
        picture_texture = path + '\\' + picturename
        time.sleep(2.5)
        auto.typewrite(picture_texture)
        time.sleep(1)
        auto.press('enter')
        auto.press('enter')#避免因为输入法无法按确定键
        time.sleep(2)
        auto.press('enter')
        auto.press('enter')  # 避免因为输入法无法按确定键
        time.sleep(0.5)
        auto.press('enter')
        time.sleep(5)

    def comparison_picture(self,new, old, style , resolution, bboxstart, bboxystart, bboxend, bboxyend):
        """图片比较"""
        path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', resolution)
        path_new = path + new
        path_old = path + old
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            if bboxstart == None and bboxystart == None and bboxend == None and bboxyend == None:
                im = ImageGrab.grab(bbox=(2, 92, 1580, 1014))
            else:
                im = ImageGrab.grab(bbox=(bboxstart, bboxystart, bboxend, bboxyend))
            im.save(path_new)
        elif str(screen_width) == '2560':
            if bboxstart == None and bboxystart == None and bboxend == None and bboxyend == None:
                im = ImageGrab.grab(bbox=(364, 192, 2195, 1390))
            else:
                im = ImageGrab.grab(bbox=(int(round(bboxstart*1.3, 0)), int(round(bboxystart*1.3, 0)), int(round(bboxend*1.3, 0)), int(round(bboxyend*1.3, 0))))
            im.save(path_new)
        elif str(screen_width) == '3840':
            if bboxstart == None and bboxystart == None and bboxend == None and bboxyend == None:
                im = ImageGrab.grab(bbox=(279, 148, 1641, 1034))
            else:
                im = ImageGrab.grab(bbox=(int(round(bboxstart*2, 0)), int(round(bboxystart*2, 0)), int(round(bboxend*2, 0)), int(round(bboxyend*2, 0))))
            im.save(path_new)
        difference = (OperationFile().contrast_image(path_new, path_old))
        difference_save = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', resolution, 'different') + '\\' + style + '图片不一样查看.png'
        OperationFile().compare_images(path_new, path_old, difference_save)
        return difference, difference_save


    def comparison_picture_resolution(self, new, old, style , bboxstart= None, bboxystart= None, bboxend= None, bboxyend= None):
        """不同分辨率图片比较"""
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            return self.comparison_picture(new, old, style , 'picture_diff_1920', bboxstart, bboxystart, bboxend, bboxyend)
        elif str(screen_width) == '2560':
            return self.comparison_picture(new, old, style , 'picture_diff_2k', bboxstart, bboxystart, bboxend, bboxyend)
        elif str(screen_width) == '3840':
            return self.comparison_picture(new, old, style , 'picture_diff_4k', bboxstart, bboxystart, bboxend, bboxyend)

    def comparison_picture_difference(self,new, old, style, bboxstart=None, bboxystart=None, bboxend=None, bboxyend=None):
        differencelist = OperationFile().comparison_picture_resolution(new, old, style, bboxstart, bboxystart, bboxend, bboxyend)
        print(differencelist)
        difference = differencelist[0]
        screen_width, screen_height = auto.size()
        if str(screen_width) == '1920':
            path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920')
        elif str(screen_width) == '2560':
            path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_2k')
        elif str(screen_width) == '3840':
            path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_2k')
        return path,differencelist

    def comparison_picture_allure(self, new, old, style, differencevalue, bboxstart=None, bboxystart=None, bboxend=None, bboxyend=None):
        """
        比较图片，将图片存到allure报告中
        全局控制比较断言，适用于ui变化跑预期图片结果
        """
        difference_data = self.comparison_picture_difference(new, old, style, bboxstart, bboxystart, bboxend, bboxyend)
        path = difference_data[0]
        allure_new = path + new
        allure_old = path + old
        difference = difference_data[1][0]
        allure_difference_save = difference_data[1][1]
        with allure.step("%s预期结果" % style):
            allure.attach.file(allure_old, attachment_type=allure.attachment_type.PNG)
        with allure.step("%s实际结果" % style):
            allure.attach.file(allure_new, attachment_type=allure.attachment_type.PNG)
        with allure.step("图片比较结果"):
            allure.attach("图片比较差别: %s" % difference, '%s图片比较差别' % style)
        if difference != 0:
            with allure.step("%s图片比较" % style):
                allure.attach.file(allure_difference_save, attachment_type=allure.attachment_type.PNG)
        else:
            self.info("%s图片一样" % style)
            pass
        self.info("%s图片比较差别:%s" % (style, difference))
        # assert difference < differencevalue
        pytest.assume(difference < differencevalue)
        self.info("%s图片测试通过" % style)
        return difference
    def failed_run_again(s, t, n): #unittest中失败重跑
        def decorator(xingfangfa):
            print(xingfangfa)

            def wrapper(*a, **w):
                for i in range(n):
                    try:
                        print('-------------------\nNum:', i)
                        re = xingfangfa(*a, **w)
                        print('success \n-------------------')
                        return re
                    except Exception:
                        print('have a error ')
                        t(*a)
                        s(*a)
                        print('\n-------------------')
                raise Exception('跑了多次也失败')

            return wrapper
        return decorator


if __name__ == '__main__':  # 运营此文件来验证写是否正确

    pass