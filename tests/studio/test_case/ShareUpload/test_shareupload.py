import os
import sys
import yaml
sys.path.append('../../../../all')
import pyperclip
import pyautogui as auto
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
from selenium import webdriver
import allure
with open('../../../config/studio_config.yaml', encoding='utf-8') as yaml_file:
    conf_config = yaml.safe_load(yaml_file.read())

@allure.feature('一键上传')
@allure.severity(allure.severity_level.CRITICAL)
class Test_ShareUpload:

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

    @allure.story('一键上传查看')
    def test_add_one(self):
        self.style.add_open_sproj('sproj', 'upload.sproj')
        self.style.click_share_upload()
        time.sleep(5)
        style = '一键上传界面查看'
        new = '\\ShareUpload\\'+style+'_new.png'
        old = '\\ShareUpload\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 100, 532, 117, 1387, 922)

        auto.click(x=conf["ShareUpload"]["add_one_1"]['x'], y=conf["ShareUpload"]["add_one_1"]['y'],clicks=conf["ShareUpload"]["add_one_1"]['clicks'],button=conf["ShareUpload"]["add_one_1"]['button'], duration=0.2)
        time.sleep(40)
        auto.click(x=conf["ShareUpload"]["add_one_2"]['x'], y=conf["ShareUpload"]["add_one_2"]['y'],clicks=conf["ShareUpload"]["add_one_2"]['clicks'],button=conf["ShareUpload"]["add_one_2"]['button'], duration=0.2)
        auto.click(x=conf["ShareUpload"]["add_one_3"]['x'], y=conf["ShareUpload"]["add_one_3"]['y'],clicks=conf["ShareUpload"]["add_one_3"]['clicks'],button=conf["ShareUpload"]["add_one_3"]['button'], duration=0.2)
        time.sleep(40)
        auto.click(x=conf["ShareUpload"]["add_one_4"]['x'], y=conf["ShareUpload"]["add_one_4"]['y'],clicks=conf["ShareUpload"]["add_one_4"]['clicks'],button=conf["ShareUpload"]["add_one_4"]['button'], duration=0.2)
        upload_name = 'upload' + str(time.time()).replace(".", "")[0:11]
        auto.click(x=conf["ShareUpload"]["add_one_5"]['x'], y=conf["ShareUpload"]["add_one_5"]['y'],clicks=conf["ShareUpload"]["add_one_5"]['clicks'],button=conf["ShareUpload"]["add_one_5"]['button'], duration=0.2)
        pyperclip.copy(upload_name)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        auto.click(x=conf["ShareUpload"]["add_one_6"]['x'], y=conf["ShareUpload"]["add_one_6"]['y'],clicks=conf["ShareUpload"]["add_one_6"]['clicks'],button=conf["ShareUpload"]["add_one_6"]['button'], duration=0.2)
        time.sleep(2)
        auto.hotkey('ctrl', 'v')
        auto.click(x=conf["ShareUpload"]["add_one_7"]['x'], y=conf["ShareUpload"]["add_one_7"]['y'],clicks=conf["ShareUpload"]["add_one_7"]['clicks'],button=conf["ShareUpload"]["add_one_7"]['button'], duration=0.2)
        auto.click(x=conf["ShareUpload"]["add_one_8"]['x'], y=conf["ShareUpload"]["add_one_8"]['y'],clicks=conf["ShareUpload"]["add_one_8"]['clicks'],button=conf["ShareUpload"]["add_one_8"]['button'], duration=0.2)
        auto.click(x=conf["ShareUpload"]["add_one_9"]['x'], y=conf["ShareUpload"]["add_one_9"]['y'],clicks=conf["ShareUpload"]["add_one_9"]['clicks'],button=conf["ShareUpload"]["add_one_9"]['button'], duration=0.2)
        self.style.tab_big_number(25)
        auto.click(x=conf["ShareUpload"]["add_one_10"]['x'], y=conf["ShareUpload"]["add_one_10"]['y'],clicks=conf["ShareUpload"]["add_one_10"]['clicks'],button=conf["ShareUpload"]["add_one_10"]['button'], duration=0.2)
        auto.click(x=conf["ShareUpload"]["add_one_11"]['x'], y=conf["ShareUpload"]["add_one_11"]['y'],clicks=conf["ShareUpload"]["add_one_11"]['clicks'],button=conf["ShareUpload"]["add_one_11"]['button'], duration=0.2)
        time.sleep(15)#等待工程上传到平台
        self.driver = webdriver.Chrome()
        self.driver.get(conf_config["url"]["selenium_url"])
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_name('user').send_keys(conf_config["env"]["name"])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@type="password"]').send_keys(conf_config["env"]["password"])
        time.sleep(2)
        self.driver.find_element_by_css_selector(conf["ShareUpload"]["login"]["css"]).click()  # 登录
        time.sleep(10)
        exist = self.driver.find_elements_by_css_selector('.footer .new-feature.ivu-btn.ivu-btn-primary.ivu-btn-small')
        if len(exist) != 0:
            self.driver.find_element_by_css_selector('.footer .new-feature.ivu-btn.ivu-btn-primary.ivu-btn-small').click()
        else:
            print("没有新版弹框提示框")
        time.sleep(3)
        # self.driver.find_element_by_css_selector(conf["ShareUpload"]["pull_down"]["css"]).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(conf["ShareUpload"]["style"]["xpath"]).click()
        time.sleep(2)
        exist = self.driver.find_elements_by_css_selector(conf["ShareUpload"]["newcloth"]['css'])
        if len(exist) != 0:
            self.driver.find_element_by_css_selector(conf["ShareUpload"]["newcloth"]['css']).click()
        else:
            self.log.info("没有新款提示框")
        self.driver.find_element_by_css_selector(conf["ShareUpload"]["serach"]['css1']).send_keys(upload_name)  # 搜索
        self.driver.find_element_by_css_selector(conf["ShareUpload"]["serach"]['css2']).click()
        time.sleep(6)
        search_list = self.driver.find_element_by_css_selector(conf["ShareUpload"]["search_click"]['css'])  #点击搜索结果
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", search_list)
        time.sleep(25)
        style = '平台查看'
        new = '\\ShareUpload\\'+style+'_new.png'
        old = '\\ShareUpload\\'+style+'_old.png'
        self.operationfile.comparison_picture_allure(new, old, style, 800, 92, 158, 1623, 973)
        self.driver.find_element_by_xpath(conf["ShareUpload"]["quit"]['xpath']).click()
        delete_show_list = self.driver.find_element_by_css_selector(conf["ShareUpload"]["delete_show"]['css'])  # 点击删除
        self.driver.execute_script("arguments[0].click();", delete_show_list)
        time.sleep(4)
        self.driver.find_element_by_xpath(conf["ShareUpload"]["delete"]['xpath']).click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(conf["ShareUpload"]["delete_confirm"]['css']).click()
        time.sleep(4)