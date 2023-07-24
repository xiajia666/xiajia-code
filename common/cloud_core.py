import configparser, pymysql, os, hashlib, json, requests
from common.cloud_core_tool import get_config, get_database, get_global_object
from common import logs, get_data, request

class Core(get_config.HandlerConfig, get_data.HandlerExcel, request.HandlerRequests, logs.Log, get_database.HandlerDatabase, get_global_object.HandlerGlobalObject):
    headers = {'Accept': 'application/json,text/plain,*/*'}

    def get_all_path(self):
        """返回all的当前地址"""
        return os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) + "\\"

    def encryption_parameters(self, data, keys):
        """md5加密参数encryption_MD5_parameters"""
        data = dict(sorted(data.items()))
        strs = ""
        for key_value in data.keys():
            if data[key_value] != "":
                strs = strs + key_value + "=" + data[key_value] + "&"
        strs = strs + "key=%s" % (keys)
        md = hashlib.md5()
        md.update(strs.encode(encoding='utf-8'))
        return md.hexdigest().upper()

    def central_scheduler_single(self, excel_id, cookies_session = None, host = None, all_verification_result = True, debug = True, request_log_grade = "INFO", verification_skip={"verification_len": True,"verification_non_null": True,"verification_data": True},**kwargs):
        """根据excelid查询出对应数据并处理，返回响应数据及期望验证"""
        self.kwargs,self.debugs,self.cookies_session =kwargs,debug,cookies_session

        """excel_id处理为excel_dict"""
        if isinstance(excel_id, dict):
            self.excel_dict = excel_id
        else:
            self.excel_dict = self.get_excel_data_by_id(excel_id)
        self.debug((str(self.excel_dict["ids"])+"--excel数据",self.excel_dict))

        """sql处理"""
        if  self.excel_dict["type"] == "sql" or self.excel_dict["type"] == "SQL":
            return self.sql_verification(self.excel_dict,all_verification_result,verification_skip)

        """前置"""
        self.handler_pre(self.excel_dict)

        """接口地址拼接"""
        if self.excel_dict["url"][:4] != 'http':
            if host != None:
                self.excel_dict["url"] = host + self.excel_dict["url"]
            else:
                self.excel_dict["url"] = self.read_or_modify_config_data(node_large="config_basics", node="host_api") + self.excel_dict["url"]

        """请求"""
        if isinstance(self.excel_dict['headers'], dict) == False:
            self.excel_dict["headers"] = self.handler_headers(self.excel_dict["headers"])
        self.r = self.request(excel_dict=self.excel_dict, cookies_session=self.cookies_session)


        self.request_log( request_log_grade = request_log_grade, message = (str(self.excel_dict["ids"]) + "--请求数据", self.excel_dict['url'], self.excel_dict['data'], self.excel_dict['headers']))

        try:
            textr = json.loads(self.r.text)
        except BaseException:
            textr = self.r.text
        self.record_current_request_datas(current_request_return=textr)

        self.request_log(request_log_grade=request_log_grade, message=(str(self.excel_dict["ids"])+"--响应数据", textr))

        """后置"""
        self.handler_after(self.excel_dict)

        """期望"""
        if self.excel_dict['verification'] != None:
            verification_handle_result = self.handler_verification(self.excel_dict)
            return self.r, verification_handle_result

        self.debug(("响应状态", self.r, True))
        return self.r, True

    def sql_verification(self,excel_dict,all_verification_result,verification_skip):
        self.excel_dict=excel_dict
        return self.handler_excel_sql(self.excel_dict, all_verification_result,verification_skip)

    def handler_pre(self, excel_dict):
        """前置处理"""
        if excel_dict['pre'] != None:
            for pre_list_value in excel_dict["pre"]:
                self.debug(("前置处理",pre_list_value))
                try:
                    eval(pre_list_value)
                except BaseException:
                    exec(pre_list_value)
            for eval_value in ["url", "data", "headers"]:
                try:
                    self.excel_dict[eval_value]=eval(excel_dict[eval_value])
                except BaseException:
                    pass

    def handler_after(self, excel_dict):
        """后置处理"""
        if excel_dict['after'] != None:
            for after_list_value in excel_dict["after"]:
                try:
                    eval(after_list_value)
                except BaseException:
                    exec(after_list_value)

    def handler_verification(self, excel_dict):
        """期望处理"""
        result_data = {}
        verifications = True
        try:
            for list_value in excel_dict["verification"]:
                results = eval(list_value)
                self.debug(("期望list_value结果", list_value, results))
                result_data[list_value] = results
                if results != True:
                    verifications = False
            verification_result = {excel_dict["ids"]: result_data}
            self.debug(("all期望结果11", verification_result))
            return verifications
        except BaseException:
            return False

    def handler_headers(self, headers_txt):
        """处理headers,返回标准字典"""
        headers_split_list = headers_txt.split("\n")
        headers_dicts = {}
        for count, list_value in enumerate(headers_split_list):
            list_value = list_value.replace(" ", "")
            list_value = list_value.replace("\t", "")
            division = list_value.split(":", 1)
            headers_dicts[division[0]] = division[1]
        return headers_dicts

    def request_log(self,request_log_grade, message):
        # 请求根据等级划分到不同日志里
        if request_log_grade.upper() == "DEBUG":
            self.debug(message)

        if request_log_grade.upper() == "INFO":
            self.info(message)

        if request_log_grade.upper() == "WARNING":
            self.warning(message)

        if request_log_grade.upper() == "ERROR":
            self.error(message)

        if request_log_grade.upper() == "CRITICAL":
            self.critical(message)


class Login(Core):

    def global_setup_login(self):
        # 全局的正常平台登录
        self.config = self.read_or_modify_config_data(node_large=None)
        try:
            self.old_name ==False
        except BaseException:
            self.old_name=None
        if self.config["config_basics"]["user"] == self.old_name:
            pass
        else:
            self.config = self.read_or_modify_config_data(node_large=None)
            self.cookies,self.token=self.return_token(self.config["config_basics"]["user"],self.config["config_basics"]["password"])
            self.old_name=self.config["config_basics"]["user"]

    def global_setup_api_login(self):
        # 全局的api接口登录
        try:
            self.old_api_name == None
        except BaseException:
            self.old_api_name = None

        if self.old_api_name != None:
            pass
        else:
            r = self.central_scheduler_single("Open_Platform_Service.ids_4",debug=False)
            self.api_token = json.loads(r[0].text)["data"]["token"]
            self.handler_global("api_token", "Bearer " + self.api_token)
            self.old_api_name=self.handler_global()["api_token"]

    def return_token(self,name, password):
        cookies_session = requests.session()
        self.name = name
        self.password = password
        r=self.central_scheduler_single("Open_Platform_Service.ids_2",debug=False)
        self.debug(("获取token：", json.loads(r[0].text)))
        self.handler_global("cookies", cookies_session.cookies)
        self.handler_global("token", "Bearer " + json.loads(r[0].text)["data"]["token"])
        return cookies_session.cookies, "Bearer " + json.loads(r[0].text)["data"]["token"]



class All(Login):
    pass