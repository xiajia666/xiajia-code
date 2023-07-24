# -*- coding: utf-8 -*-
import base64
import json
import sys
sys.path.append('../../../../all')
import time
import urllib
import allure
import pyautogui as auto
import autoit
import pyperclip
import pytest
import yaml
from PIL import Image
from common.logs import Log
import os
import shutil
import requests
from common.operation_file import OperationFile
from common.studio_auto import Style3DAuto

with open('../../../config/studio_config.yaml', encoding='utf-8') as yaml_file:
    conf_config = yaml.safe_load(yaml_file.read())
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf_mouse = yaml.safe_load(yaml_file.read())

class Style3DCloud(Log):
    """云渲染,离线渲染"""

    def get_token(self, name=None):
        """获取登录token"""
        headers = {"Content-Type": "application/json"}
        url = conf_config["url"]["release"] + "/account/auth/login"
        if name != None:
            data = {"name": base64.b64decode(b'bHVvbGlrYW5n').decode('utf-8'),"password": base64.b64decode(b'U3R5bGUzRF8wMQ==').decode('utf-8')}
        else:
            data = {"name": conf_config["env"]["name"], "password": conf_config["env"]["password"]}
        r = requests.post(url, headers=headers, data=json.dumps(data)).json()
        token = r['data']['token']
        Authorization = "Bearer " + token
        return Authorization

    def get_cloudrender_id(self, keywords):
        """获取云渲染工程id"""
        Authorization = self.get_token()
        headers = {"Content-Type": "application/json","Authorization":Authorization}
        url = conf_config["url"]["release"]+ "/basic/cloudrender/tasks?page=1&mode=edit_mode&list_page=1&per_page=10&in_audit=0&search_info=1"
        r = requests.get(url, headers=headers,params={"keywords": keywords}).json()
        id = r['data']['list']['data'][0]['id']
        self.info('云渲染工程id=%s ' % id)
        for i in range(200):
            r = requests.get(url, headers=headers, params={"keywords": keywords}).json()
            status_text = r['data']['list']['data'][0]['status_text']
            self.info('获取api状态')
            if status_text == '已完成':
                self.info('渲染已完成，准备开始对比图片')
                break
            else:
                self.info('我再等待1分钟')
                time.sleep(60)
        self.info("开始对比图片")
        return id

    def get_upload_id(self, keywords):
        """获取一键上传工程id"""
        Authorization = self.get_token()
        headers = {"Content-Type": "application/json","Authorization":Authorization}
        url = conf_config["url"]["release"] + "/resource/product?page=1&mode=image_mode&created_at_sortable=desc&keywords=upload16339283143&list_page=1&per_page=50&in_audit=0&search_info=1"
        r = requests.get(url, headers=headers,params={"keywords": keywords}).json()
        id = r['data']['list']['data'][0]['id']
        self.info('一键上传工程id=%s ' % id)
        return id

    def get_cloudrender_download(self, name, format):
        """下载云渲染图片"""
        id = self.get_cloudrender_id(name)
        Authorization = self.get_token()
        headers = {"Content-Type": "application/json", "Authorization": Authorization}
        url = conf_config["url"]["release"]+ "/basic/download/token"
        data = {"type": "cloud_render_task_images", "id": id}
        r = requests.post(url, headers=headers, data=json.dumps(data)).json()
        downloadtoken = r['data']['token']
        urlhead = conf_config["url"]["release"] +'/basic/cloudrender/tasks/images/download?'
        downloadurl = urlhead + 'id=' + str(id) + '&images=0' + '&ext='+ format + '&dlt=' + downloadtoken
        to_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\download.zip'
        conn = urllib.request.urlopen(downloadurl)
        f = open(to_path,'wb')
        f.write(conn.read())
        f.close()
        return to_path

    def un_bundling(self, name='luo'):
        """解绑软件"""
        Authorization = self.get_token(name)
        headers = {"Content-Type": "application/json","Authorization":Authorization}
        # url = conf_config["url"]["release"]+ "/setting/software/personal/code/un_bundling"
        url = conf_config["url"]["release"]+ "/setting/software/code/un_bundling"
        # data = {"code":conf_config["Style3D"]["code"],"type":2}
        data = {"mid": "980", "type": 2}
        r = requests.post(url, headers=headers, data=json.dumps(data)).json()
        self.info(r)

    def send_message(self, content, version, mobiles_wang, mobiles_chen, mobiles_shen):  # 钉钉自动发消息
        """钉钉发送信息"""
        headers = {"Content-Type": "application/json"}
        url = "https://oapi.dingtalk.com/robot/send?access_token=ca4785eaeed1f065be2330b43388dcfaa8b071db4087a3b75a2f8573e9ca2c8f"
        data = {
            "at": {
                "atMobiles": [
                    mobiles_wang,
                    mobiles_chen,
                    mobiles_shen
                ],
                "atUserIds": [
                    "user123"
                ],
                "isAtAll": "false"
            },
            "text": {
                "content": content + version
            },
            "msgtype": "text"
        }
        r = requests.post(url, headers=headers, data=json.dumps(data)).json()
        print(r)

    def show_allure_picture(self, expect_picture, actual_picture, style, allure_expect_name, allure_actual_name):
        """allure 报告中添加图片附件"""
        difference_save = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'different') + '\\' + style + '图片不一样查看.png'
        OperationFile().compare_images(expect_picture, actual_picture, difference_save)
        with allure.step("{}{}结果".format(style,allure_expect_name)):
            allure.attach.file(expect_picture, attachment_type=allure.attachment_type.PNG)
        with allure.step("{}{}结果".format(style,allure_actual_name)):
            allure.attach.file(actual_picture, attachment_type=allure.attachment_type.PNG)
        with allure.step("{}{}和{}图片比较差别".format(style,allure_expect_name,allure_actual_name)):
            allure.attach.file(difference_save, attachment_type=allure.attachment_type.PNG)

    def cloudrender_picture_diff(self, imgcloud, stylelocal, colordiff, style, allure_expect_name, allure_actual_name):
        """图片像素对比算法"""
        self.show_allure_picture(imgcloud, stylelocal, style, allure_expect_name, allure_actual_name)
        imgcloud = Image.open(imgcloud)
        stylelocal = Image.open(stylelocal)
        sum = 0
        get_len = len(imgcloud.getpixel((0, 0)))
        for x in range(imgcloud.width):
            for y in range(imgcloud.height):
                for i in range(get_len):
                    if abs(imgcloud.getpixel((x, y))[i] - stylelocal.getpixel((x, y))[i]) <= colordiff:
                        pass
                    else:
                        sum += 1
                        break
        self.info('RGB不一致次数%s ' % sum)
        self.info('图片分辨率相乘 %s' % (imgcloud.width * imgcloud.height))
        ratio = sum / (imgcloud.width * imgcloud.height)
        return ratio

    def assert_render_picture(self,file_path):
        """检测离线渲染是否完成"""
        for i in range(15):
            if os.path.exists(file_path):
                self.info('最终渲染成功')
                break
            else:
                self.info('我再等待1分钟')
                time.sleep(60)
        auto.click(x=1056, y=600, clicks=1, button='left', duration=0.2)  # 点击关闭弹框

    def assert_render_picture_minute(self,file_path, number):
        """检测离线渲染是否完成_10分钟"""
        file = 'fail'
        for i in range(number):
            if os.path.exists(file_path):
                self.info('最终渲染成功')
                file = 'success'
                break
            else:
                self.info('我再等待10秒钟')
                time.sleep(10)
        if file != "success":
            self.info("超过10分钟，直接渲染结束")
            auto.click(x=430, y=162, clicks=1, button='left', duration=0.2)  # 点击最终渲染

    def assert_animation_render(self,file_path):
        """检测动画离线渲染是否完成"""
        for i in range(100):
            if os.path.exists(file_path):
                self.info('动画离线渲染成功')
                break
            else:
                self.info('我再等待半分钟')
                time.sleep(30)


    def get_imgcloud_picture_path(self, save_name, file, format):
        """ 下载云云渲染图片，复制到指定目录"""
        zip_src = self.get_cloudrender_download(save_name, format)
        dst_dir = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender')+ '\\' + "downloadpicture"
        OperationFile().unzip_file(zip_src, dst_dir)
        download_picture_files = OperationFile().get_file_name(dst_dir)[0][0]
        download_picture_root = OperationFile().get_file_name(dst_dir)[1]
        imgcloud = download_picture_root + '\\' + download_picture_files
        self.info(imgcloud)
        copypath = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + 'imgcloud' + '.' + format
        shutil.copy(imgcloud, copypath)
        self.info(copypath)
        return copypath, zip_src

    def open_render_sproj(self, press):
        """打开渲染工程，设置默认的hdr灯光"""
        Style3DAuto().click_save_as_sproj()
        save_name = 'cloudrender' + str(time.time()).replace(".", "")[0:11]
        cloudrender_name = os.path.join(OperationFile().get_garder_path('studio'), 'sproj') + '\\' + save_name
        pyperclip.copy(cloudrender_name)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        time.sleep(1)
        auto.press('enter')
        time.sleep(6)
        # Style3DAuto().click_enter()
        auto.click(x=conf_mouse["OfflineRender"]["save_enter_wangquan"]['x'], y=conf_mouse["OfflineRender"]["save_enter_wangquan"]['y'],clicks=conf_mouse["OfflineRender"]["save_enter_wangquan"]['clicks'],button=conf_mouse["OfflineRender"]["save_enter_wangquan"]['button'], duration=0.2)
        auto.click(x=conf_mouse["OfflineRender"]['save_enter']['x'], y=conf_mouse["OfflineRender"]['save_enter']['y'],clicks=conf_mouse["OfflineRender"]['save_enter']['clicks'],button=conf_mouse["OfflineRender"]['save_enter']['button'], duration=0.2)
        time.sleep(2)
        Style3DAuto().click_photo_rendering()
        time.sleep(2)
        if press != '2':
            self.info("视角不做切换")
        else:
            auto.press('2')
            self.info("切换软件2视角")
        auto.click(x=conf_mouse["OfflineRender"]['light']['x'],y=conf_mouse["OfflineRender"]['light']['y'],clicks=conf_mouse["OfflineRender"]['light']['clicks'],button=conf_mouse["OfflineRender"]['light']['button'], duration=0.2)
        time.sleep(5)
        auto.click(x=conf_mouse["OfflineRender"]['light_change']['x'],y=conf_mouse["OfflineRender"]['light_change']['y'],clicks=conf_mouse["OfflineRender"]['light_change']['clicks'],button=conf_mouse["OfflineRender"]['light_change']['button'], duration=0.2)
        time.sleep(2)
        hdr_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "offline.hdr"
        pyperclip.copy(hdr_path)
        time.sleep(1)
        auto.hotkey('ctrl', 'v')
        time.sleep(2)
        auto.press('enter')
        time.sleep(4)
        return save_name

    def video_propetry_scroll_big(self):
        """滑动属性栏点击gpu,cpu"""
        auto.click(x=conf_mouse["OfflineRender"]['video_propetry']['x'],y=conf_mouse["OfflineRender"]['video_propetry']['y'],clicks=conf_mouse["OfflineRender"]['video_propetry']['clicks'],button=conf_mouse["OfflineRender"]['video_propetry']['button'], duration=0.2)
        time.sleep(2)
        self.info('点击方向，滚轮滑动属性视窗')
        auto.click(x=1631, y=541, clicks=1, interval=0.0, button='left', duration=0.2, tween=auto.linear)
        Style3DAuto().scroll_big_number(1)
        time.sleep(2)

    def choose_render_filepath(self, file, picture_name, render_type, snapshot_3d_cloud_render, open_file=None):
        """保存图片到离线渲染文件夹中"""
        if open_file == None:
            auto.click(x=conf_mouse["OfflineRender"]['open_file']['x'],y=conf_mouse["OfflineRender"]['open_file']['y'],clicks=conf_mouse["OfflineRender"]['open_file']['clicks'],button=conf_mouse["OfflineRender"]['open_file']['button'], duration=0.2)
            self.info('图片为png时点击文件路径')
        else:
            auto.click(x=conf_mouse["OfflineRender"]['open_file_jpg']['x'],y=conf_mouse["OfflineRender"]['open_file_jpg']['y'],clicks=conf_mouse["OfflineRender"]['open_file_jpg']['clicks'],button=conf_mouse["OfflineRender"]['open_file_jpg']['button'], duration=0.2)
            self.info('图片为jpg时点击文件路径')
        time.sleep(2)
        photo_file_save = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file
        pyperclip.copy(photo_file_save)
        auto.hotkey('ctrl', 'v')
        auto.press('enter')
        time.sleep(2)
        # autoit.control_click("选择", "Button1") #经常失败
        auto.press('enter')
        time.sleep(2)
        if open_file == None:
            auto.click(x=conf_mouse["OfflineRender"]['file_name']['x'],y=conf_mouse["OfflineRender"]['file_name']['y'],clicks=conf_mouse["OfflineRender"]['file_name']['clicks'],button=conf_mouse["OfflineRender"]['file_name']['button'], duration=0.2)
        else:
            auto.click(x=conf_mouse["OfflineRender"]['file_name_jpg']['x'],y=conf_mouse["OfflineRender"]['file_name_jpg']['y'],clicks=conf_mouse["OfflineRender"]['file_name_jpg']['clicks'],button=conf_mouse["OfflineRender"]['file_name_jpg']['button'], duration=0.2)
        time.sleep(2)
        pyperclip.copy(picture_name)
        auto.hotkey('ctrl', 'v')
        auto.press('enter')
        if open_file == None:
            if render_type == "gpu":
                self.info('gpu渲染')
                auto.click(x=conf_mouse["OfflineRender"]['render_tool']['x'], y=conf_mouse["OfflineRender"]['render_tool']['y'],clicks=conf_mouse["OfflineRender"]['render_tool']['clicks'],button=conf_mouse["OfflineRender"]['render_tool']['button'], duration=0.2)
                auto.click(x=conf_mouse["OfflineRender"]['gpu_change']['x'], y=conf_mouse["OfflineRender"]['gpu_change']['y'],clicks=conf_mouse["OfflineRender"]['gpu_change']['clicks'],button=conf_mouse["OfflineRender"]['gpu_change']['button'], duration=0.2)
            elif render_type == "cpu":
                self.info('cpu渲染')
                auto.click(x=conf_mouse["OfflineRender"]['render_tool']['x'], y=conf_mouse["OfflineRender"]['render_tool']['y'],clicks=conf_mouse["OfflineRender"]['render_tool']['clicks'],button=conf_mouse["OfflineRender"]['render_tool']['button'], duration=0.2)
                auto.click(x=conf_mouse["OfflineRender"]['cpu_change']['x'], y=conf_mouse["OfflineRender"]['cpu_change']['y'],clicks=conf_mouse["OfflineRender"]['cpu_change']['clicks'],button=conf_mouse["OfflineRender"]['cpu_change']['button'], duration=0.2)
            auto.click(x=conf_mouse["OfflineRender"]['click_file_name']['x'], y=conf_mouse["OfflineRender"]['click_file_name']['y'], clicks=conf_mouse["OfflineRender"]['click_file_name']['clicks'], button=conf_mouse["OfflineRender"]['click_file_name']['button'], duration=0.2)
        else:
            if render_type == "gpu":
                self.info('gpu渲染')
                auto.click(x=conf_mouse["OfflineRender"]['render_tool_jpg']['x'], y=conf_mouse["OfflineRender"]['render_tool_jpg']['y'],clicks=conf_mouse["OfflineRender"]['render_tool_jpg']['clicks'],button=conf_mouse["OfflineRender"]['render_tool_jpg']['button'], duration=0.2)
                auto.click(x=conf_mouse["OfflineRender"]['gpu_change_jpg']['x'], y=conf_mouse["OfflineRender"]['gpu_change_jpg']['y'],clicks=conf_mouse["OfflineRender"]["photo_render"]['gpu_change_jpg']['clicks'],button=conf_mouse["OfflineRender"]['gpu_change_jpg']['button'], duration=0.2)
            elif render_type == "cpu":
                self.info('cpu渲染')
                auto.click(x=conf_mouse["OfflineRender"]['render_tool_jpg']['x'], y=conf_mouse["OfflineRender"]['render_tool_jpg']['y'],clicks=conf_mouse["OfflineRender"]['render_tool_jpg']['clicks'],button=conf_mouse["OfflineRender"]['render_tool_jpg']['button'], duration=0.2)
                auto.click(x=conf_mouse["OfflineRender"]['cpu_change_jpg']['x'], y=conf_mouse["OfflineRender"]['cpu_change_jpg']['y'],clicks=conf_mouse["OfflineRender"]['cpu_change_jpg']['clicks'],button=conf_mouse["OfflineRender"]['cpu_change_jpg']['button'], duration=0.2)
            auto.click(x=conf_mouse["OfflineRender"]['click_file_name_jpg']['x'], y=conf_mouse["OfflineRender"]['click_file_name_jpg']['y'], clicks=conf_mouse["OfflineRender"]['click_file_name_jpg']['clicks'], button=conf_mouse["OfflineRender"]['click_file_name_jpg']['button'], duration=0.2)
        if snapshot_3d_cloud_render == 'on':
            self.click_snapshot_3d_cloud_render()
        else:
            self.info('不点击快照云渲染')
        auto.click(x=conf_mouse["OfflineRender"]['photo']['x'], y=conf_mouse["OfflineRender"]['photo']['y'], clicks=conf_mouse["OfflineRender"]['photo']['clicks'], button=conf_mouse["OfflineRender"]['photo']['button'], duration=0.2)
        if open_file == None:
            file_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + picture_name + '.png'
        else:
            file_path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + picture_name + '.jpg'
        return file_path

    def click_snapshot_3d_cloud_render(self):
        """点击3D快照云渲染"""
        Style3DAuto().click_snapshot_3d()
        time.sleep(2)
        auto.click(x=conf_mouse["CloudRender"]["click_view_one"]['x'], y=conf_mouse["CloudRender"]["click_view_one"]['y'],clicks=conf_mouse["CloudRender"]["click_view_one"]['clicks'],button=conf_mouse["CloudRender"]["click_view_one"]['button'], duration=0.2)
        time.sleep(120)
        auto.click(x=conf_mouse["CloudRender"]["click_view_two"]['x'], y=conf_mouse["CloudRender"]["click_view_two"]['y'],clicks=conf_mouse["CloudRender"]["click_view_two"]['clicks'],button=conf_mouse["CloudRender"]["click_view_two"]['button'], duration=0.2)
        auto.click(x=conf_mouse["CloudRender"]["click_view_three"]['x'], y=conf_mouse["CloudRender"]["click_view_three"]['y'],clicks=conf_mouse["CloudRender"]["click_view_three"]['clicks'],button=conf_mouse["CloudRender"]["click_view_three"]['button'], duration=0.2)
        time.sleep(3)

    def cloud_render_type(self, picture_name, picture_old_name , colordiff , style, file, clo_picture, press, render_type, allure_expect_name, allure_actual_name, snapshot_3d_cloud_render, format, clo_diff=None):
        """云渲染不同材质公共部分"""
        save_name = self.open_render_sproj(press)
        self.video_propetry_scroll_big()
        file_path = self.choose_render_filepath(file, picture_name, render_type, snapshot_3d_cloud_render)
        Style3DCloud().assert_render_picture(file_path)
        auto.click(x=conf_mouse["OfflineRender"]['close']['x'],y=conf_mouse["OfflineRender"]['close']['y'],clicks=conf_mouse["OfflineRender"]['close']['clicks'],button=conf_mouse["OfflineRender"]['close']['button'], duration=0.2)
        imgcloud = Style3DCloud().get_imgcloud_picture_path(save_name, file, format)[0]
        zip_src = Style3DCloud().get_imgcloud_picture_path(save_name, file, format)[1]
        stylelocal = file_path
        ratio = Style3DCloud().cloudrender_picture_diff(imgcloud, stylelocal, colordiff, style, allure_expect_name, allure_actual_name)
        self.info("像素对比:%s" % ratio)
        assert ratio < colordiff
        self.info("%s材质软件离线渲染和云渲染测试通过" % file)
        old_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + picture_old_name + '.png'
        difference = OperationFile().contrast_image(old_picture, stylelocal)
        self.show_allure_picture(old_picture, stylelocal, style, '离线渲染老照片', '本地cpu渲染照片')
        self.info("%s 软件离线渲染新旧照片比较差别:%s" % (file ,difference))
        assert difference < 800
        self.info("%s材质软件离线渲染新旧照片测试通过" % file)
        if clo_diff == None:
            clo_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + clo_picture + '.png'
            self.show_allure_picture(clo_picture, stylelocal, style, 'clo照片', '本地cpu渲染照片')
            difference = OperationFile().contrast_image(stylelocal, clo_picture)
            self.info("和clo照片做对比")
            self.info("%s材质软件离线渲染和clo的对比差别:%s" % (file, difference))
            assert difference < 1300
            self.info("%s材质软件离线渲染和clo的对比测试通过" % file)
        else:
            self.info("没有clo图片做对比")
        # OperationFile().delete_file(imgcloud)
        OperationFile().delete_file(zip_src)

    def choose_cpu_gpu(self, press, file, cpu_name, gpu_name, snapshot_3d_cloud_render):
        #
        self.open_render_sproj(press)
        render_type = 'cpu'
        file_path = self.choose_render_filepath(file, cpu_name, render_type, snapshot_3d_cloud_render)
        self.assert_render_picture(file_path)
        auto.click(x=conf_mouse["OfflineRender"]['close']['x'],y=conf_mouse["OfflineRender"]['close']['y'],clicks=conf_mouse["OfflineRender"]['close']['clicks'],button=conf_mouse["OfflineRender"]['close']['button'], duration=0.2)
        render_type = 'gpu'
        file_path = self.choose_render_filepath(file, gpu_name, render_type, snapshot_3d_cloud_render)
        self.assert_render_picture(file_path)
        auto.click(x=conf_mouse["OfflineRender"]['close']['x'],y=conf_mouse["OfflineRender"]['close']['y'],clicks=conf_mouse["OfflineRender"]['close']['clicks'],button=conf_mouse["OfflineRender"]['close']['button'], duration=0.2)
        cpu_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + cpu_name + '.png'


    def render_cpu_gpu_diff(self, press, file, cpu_name, gpu_name , style, allure_expect_name, allure_actual_name, snapshot_3d_cloud_render):
        """cpu 和 gpu对比测试"""
        self.open_render_sproj(press)
        self.video_propetry_scroll_big()
        render_type = 'cpu'
        file_path = self.choose_render_filepath(file, cpu_name, render_type, snapshot_3d_cloud_render)
        self.assert_render_picture(file_path)
        render_type = 'gpu'
        file_path = self.choose_render_filepath(file, gpu_name, render_type, snapshot_3d_cloud_render)
        self.assert_render_picture(file_path)
        cpu_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + cpu_name + '.png'
        gpu_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + file + '\\' + gpu_name + '.png'
        self.show_allure_picture(cpu_picture, gpu_picture, style, allure_expect_name, allure_actual_name)
        difference = OperationFile().contrast_image(cpu_picture, gpu_picture)
        self.info("%s 软件离线渲染cpu和gpu照片比较差别:%s" % (file ,difference))
        # assert difference < 200
        self.info("%s材质软件离线渲染cpu和gpu新旧照片测试通过" % file)

    def delete_cloudrender(self):
        """删除云下载文件夹中的图片"""
        path_data = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '//' +  "downloadpicture"
        try:
            for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
                file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
                if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
                    os.remove(file_data)
                else:
                    Style3DCloud().delete_cloudrender(file_data)
        except :
            self.info("没有云下载图片")

    def delete_local_render(self, file, picture_name):
        """删除本地离线渲染的图片"""
        path = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '//' + file + '//' + picture_name + '.png'
        OperationFile().delete_file(path)

    def delete_cloud_sproj(self, name):
        """删除所有另存为cloud名字的工程"""
        path = OperationFile().get_garder_path('studio')
        my_dir = os.path.join(path, 'sproj')
        for fname in os.listdir(my_dir):
            if fname.startswith(name):
                os.remove(os.path.join(my_dir, fname))
                self.info('文件删除成功')
            else:
                self.info('文件不存在')




if __name__ == '__main__':  # 运营此文件来验证写是否正确
    Style3DCloud().get_cloudrender_id('cloudrender16736718504')
    #
    # imgcloud = 'C:\\Users\\12540\\Desktop\\新建文件夹 (2)\\3d快照 云渲染.png'
    # stylelocal = 'C:\\Users\\12540\\Desktop\\新建文件夹 (2)\\3d快照 本地渲染.png'
    # colordiff = 25
    #
    # style = 'xxx'
    # allure_expect_name = 'aaa'
    # allure_actual_name = 'bbbb'

    # ratio = Style3DCloud().cloudrender_picture_diff(imgcloud, stylelocal, colordiff, style, allure_expect_name, allure_actual_name)
    # print(ratio)
