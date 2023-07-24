import os
import sys
sys.path.append('../../../../all')
import time
from common.studio_auto import Style3DAuto
from common.logs import Log
from common.operation_file import OperationFile
import allure

@allure.feature('版本查看')
@allure.severity(allure.severity_level.CRITICAL)
class TestVersion:
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

    @allure.story('版本查看')
    def test_version(self):
        self.style.click_version()
        time.sleep(0.5)
        new = '\\version\\version_shownew.png'
        old = '\\version\\version_shownew.png'
        style = '版本查看'
        self.operationfile.comparison_picture_allure(new, old, style, 200, 760, 379, 1160, 660)
