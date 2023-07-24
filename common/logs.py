import logging,os,time
import allure,pytest
import common.cloud_core_tool.get_config as get_configs

class HandlerLogObject():
    "日志的创建"
    __obj, log=None,None
    def __new__(cls):
        cls.__obj = object.__new__(cls) if cls.__obj == None else cls.__obj
        return cls.__obj

    def establish_log(self,level = "DEBUG"):
        "创建log"
        self.log = logging.getLogger()
        self.log.setLevel(level)

    def handler_log_consoles(self,level = "DEBUG"):
        "日志器添加到控制台"
        consoles = logging.StreamHandler()
        consoles.setLevel(level)
        consoles.setFormatter(self.get_formatter()[0])
        return consoles

    def handler_log_file(self,level = "DEBUG"):
        "日志添加到文件"
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_path = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) + "\\" + "log\\"
        log_file_name = log_path + rq + '.log'
        files = logging.FileHandler(log_file_name, mode='a', encoding='utf-8')
        files.setLevel(level)
        files.setFormatter(self.get_formatter()[1])
        return files

    def get_formatter(self):
        "设置Formatter格式"
        file_formatter = '%(asctime)s-%(funcName)s-%(threadName)s- %(levelname)s: %(message)s'
        console_formatter= '%(funcName)s:%(message)s'
        console_fmt = logging.Formatter(fmt = file_formatter)
        file_fmt = logging.Formatter(fmt = console_formatter)
        return console_fmt, file_fmt

    def get_log(self,file_level = "DEBUG",console_level = "INFO"):
        "返回日志实例对象"
        self.establish_log(file_level)
        self.log.addHandler(self.handler_log_consoles(console_level))
        self.log.addHandler(self.handler_log_file(file_level))
        return self.log


class Allure_Enclosure():
    "用例日志"
    allure_log_data, __obj = "", None

    def __new__(cls):
        cls.__obj = object.__new__(cls) if cls.__obj == None else cls.__obj
        return cls.__obj

    def allure_log(self, log_data=None):
        self.allure_log_data = self.allure_log_data if log_data == None else self.allure_log_data+"<p>%s</p>"%(str(log_data))
        return self.allure_log_data


class Log():
    file_level = get_configs.HandlerConfig().read_or_modify_config_data()["config_log"]["file_level"]
    console_level = get_configs.HandlerConfig().read_or_modify_config_data()["config_log"]["console_level"]
    log = HandlerLogObject().get_log(file_level.upper(),console_level.upper())

    def debug(self, message):
        self.log.debug(message)
        # Allure_Enclosure().allure_log()

    def info(self, message):
        self.log.info(message)
        Allure_Enclosure().allure_log(str(message))

    def warning(self, message):
        self.log.warning(message)
        Allure_Enclosure().allure_log(str(message))

    def error(self, message):
        self.log.error(message)
        Allure_Enclosure().allure_log(str(message))

    def critical(self, message):
        self.log.critical(message)
        Allure_Enclosure().allure_log(str(message))

    def send_attachment(self):
        allure_log_data = Allure_Enclosure().allure_log()
        allure.attach(allure_log_data, '附件日志', allure.attachment_type.HTML)
        Allure_Enclosure().allure_log_data = ""
        return allure_log_data


class AutomaticSendAllureAttachment(Log):
    "按用例自动提交日志到Allure报告里，继承此方法即可"
    @pytest.fixture(autouse=True)
    @allure.title("提交日志附件")
    def cleanup(self,request):
        def remove_test_dir():
            self.info("提交日志附件")
            self.send_attachment()
        request.addfinalizer(remove_test_dir)

