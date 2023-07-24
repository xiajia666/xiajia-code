import json
import os,sys
import requests
import yaml
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud
import allure
import pytest
import logging
#新增省
with open('../../../config/studio_mouse.yaml') as yaml_file:
    conf = yaml.safe_load(yaml_file.read())
with open('../../../config/studio_config.yaml', encoding='utf-8') as yaml_file:
    conf_config = yaml.safe_load(yaml_file.read())

@pytest.mark.skip
@allure.feature('平台云渲染对比')
@allure.severity(allure.severity_level.BLOCKER)
class Test_CloudRendr():

    def setup_class(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        self.operationfile.keep_window()
        self.style.start_style3D()
    def teardown_class(self):

        self.log.info("测试结束")
        self.style.close_style3D()

    @allure.story('平台云渲染和本地离线渲染对比')
    def test_add_one(self):
        Style3DAuto().add_open_sproj('upload', 'cloud_render.sproj')
        self.cloud.open_render_sproj('2')
        render_type = 'cpu'
        file_path = self.cloud.choose_render_filepath('cloud_render', 'cloud_render_cpu', render_type, 'off', 'jpg')
        self.cloud.assert_render_picture(file_path)
        id = self.cloud.get_upload_id('平台云渲染')
        url = conf_config["url"]["cloud_render_url"]
        headers = {"Content-Type": "application/json;charset=utf-8"}
        data = {
            "url": "https://www.style3d.com/", "user": "wangquan_qiye", "password": "63550626", "styleID": id,
            "type": "Single_Image", "data":
                {
                    "size_of_the_picture": {"W": "480", "H": "640"},
                    "Environment_setting": {"environment_type": "Background",
                                            "environment_data": {"colour_chart": "Background_color", "color": "True",
                                                                 "colour_code": "#FFFFFF"}},
                    "quality": {"Light": "Medium", "Materials": "Medium", "Noise": "0.05"}
                }
        }
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        self.log.info(r)
        self.cloud.get_cloudrender_download('平台云渲染', 'jpg')
        imgcloud_path = self.cloud.get_imgcloud_picture_path("平台云渲染", "cloud_render", 'jpg')[0]
        diff = self.cloud.cloudrender_picture_diff( imgcloud_path, file_path, 50, "直接平台云渲染", "平台云渲染图片", "本地离线渲染图片")
        self.log.info(diff)
        assert diff < 0.3