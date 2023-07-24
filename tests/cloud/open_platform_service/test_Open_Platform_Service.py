# -*- coding:utf-8 -*-
import requests, json, hashlib, pytest, unittest,re,random,time,decimal,functools,sys
import common.cloud_core as cores
import allure,os
import common.cloud_core_tool.get_config as get_configs

class PytestFixture(cores.All):

    #  @pytest.fixture(autouse=True)
    #  @allure.title("提交日志附件")
    #  def cleanup(self,request):
    #      def remove_test_dir():
    #          self.info("提交日志附件")
    #          self.send_attachment()
    #      request.addfinalizer(remove_test_dir)

    #  @pytest.fixture(scope="session")
    #  def home_url(self,pytestconfig):
    #      url = pytestconfig._getini("logging")
    #      print("\n读取到配置文件的url地址：%s" % url)
    #      return url

    @pytest.fixture(scope='class')
    def clear_config_fabric_detailed_data_record(self):
        # 清除config_fabric_detailed_data_record 下的数据
        self._eliminate_config_node_data(node_large="config_fabric_detailed_data_record")

    @pytest.fixture(scope="session",autouse=True)
    @allure.title("清除面料后端生成的数据")
    def delete_data(self,request):
        # 清除生成的数据
        def delete_fabric_supplier():
            # 清除供应商字段列表自动生成的数据
            r = self.central_scheduler_single("Open_Platform_Service.ids_16",debug=False)
            list_value = json.loads(r[0].text)["data"]["list"]["data"]
            for list_value_data in list_value:
                if "测试后端生成" in list_value_data["name"]:
                    self.central_scheduler_single("Open_Platform_Service.ids_设置中心--基础数据管理--面料--删除供应商字段可选值", debug=False, supplier_list_id = list_value_data["id"])

        def delete_waiting_delete_fabric_data():
            # 删除等待删除的面料数据
            def delete_field_optional_value():
                field_optional_value_list = eval(self.read_or_modify_config_data()["config_fabric_test_back_end_generate"]["wait_delete_field_optional_value_list"])
                for field_optional_values in field_optional_value_list:
                    r = self.central_scheduler_single("Open_Platform_Service.ids_获取设置中心--基础数据管理--面料--list类型字段--字段可选值列表", field_name = field_optional_values)
                    list_value = json.loads(r[0].text)["data"]["data"]
                    for list_value_data in list_value:
                        if "测试后端生成" in list_value_data["name"]:
                            self.central_scheduler_single("Open_Platform_Service.ids_基础数据--面料--删除字段的可选项列表数据", mid = list_value_data["id"])

                self.read_or_modify_config_data(node_large = "config_fabric_test_back_end_generate", node = "wait_delete_field_optional_value_list", value=[])
            def delete_field():
                fabric_id_list = eval(self.read_or_modify_config_data()["config_fabric_test_back_end_generate"]["delete_field_optional_value_relation_fabric_id"])
                for fabric_id in fabric_id_list:
                    self.central_scheduler_single("Open_Platform_Service.ids_删除平台面料", fabric_id = str(fabric_id))
                self.read_or_modify_config_data(node_large = "config_fabric_test_back_end_generate" , node = "delete_field_optional_value_relation_fabric_id", value = str([]))

            delete_field()
            delete_field_optional_value()

        def remove_test_dir():
            delete_fabric_supplier()
            delete_waiting_delete_fabric_data()

        request.addfinalizer(remove_test_dir)

    @pytest.fixture(scope="session", autouse=True)
    @allure.title("获取api_token和token")
    def get_token(self):
        self.global_setup_login()
        self.global_setup_api_login()

    @allure.title("勾选面料所有字段")
    def open_all_fields(self):
        "开启所有动态字段"
        category_r = self.central_scheduler_single("Open_Platform_Service.ids_9", debug=False)
        category_r_text=json.loads(category_r[0].text)
        global_setting_list = category_r_text["data"]["global_setting_list"]
        self.values = []
        for global_setting_list_value in global_setting_list:
            for items_value in global_setting_list_value["items"]:
                self.values.append({"key": items_value["key"]})
        self.central_scheduler_single("Open_Platform_Service.ids_11",debug=False)

    @pytest.fixture(scope='class')
    @allure.title("便利所有字段，给TestOpenResourceV2Fabric，生成“映射数据”和“分类数据”数据")
    def fixture_ergodic_parameter(self):
        # TestOpenResourceV2Fabric().ergodic_parameter()
        TestOpenResourceV2Fabric2().ergodic_parameter_write_config()

    @pytest.fixture(scope='class')
    @allure.title("便利自定义字段，给TestOpenResourceV2Fabric，生成“映射数据”和“分类数据”")
    def fixture_custom_ergodic_parameter(self):
        TestOpenResourceV2Fabric().ergodic_parameter(True)

    @allure.title("# 返回 config_fabric_dynamic_field_free_combination 所有节点数据")
    def return_list_config_fabric_dynamic_field_free_combination(self):
        # 返回 config_fabric_dynamic_field_free_combination 所有节点数据
        free_combination_data = self.read_or_modify_config_data()["config_fabric_dynamic_field_free_combination"]
        return [i for i in free_combination_data.values()]


class TestOpenPlatformServiceRegister(PytestFixture):
    #  open/auth/register
    #  注册
    #  @pytest.fixture()

    def setup(self):
        self.config = self.read_or_modify_config_data(node_large=None)

    def teardown(self):
        pass

    def increment_config_data(self):
        '''更新数据'''
        lists = ["regisrer_uid", "regisrer_name", "regisrer_tel", "regisrer_email", "regisrer_introduction"]
        self._increasing_config_data("config_regisrer", lists)
        self.config = self.read_or_modify_config_data(node_large=None)

    def test_open_auth_register(self):
        '''“注册接口”正参数验证'''
        self.increment_config_data()

        r = self.central_scheduler_single("Open_Platform_Service.ids_1")
        assert r[1]
        sqlr_users_result = self.central_scheduler_single("sql.ids_1")
        self.job_id = sqlr_users_result[0][0]["job_id"]
        self.apartment_id = sqlr_users_result[0][0]["apartment_id"]
        sqlr_jobs_result = self.central_scheduler_single("sql.ids_2")
        sqlr_apartment_result = self.central_scheduler_single("sql.ids_3")

        self.name = self.config["config_regisrer"]["regisrer_name"]
        self.password = self.config["config_regisrer"]["regisrer_password"]
        r = self.central_scheduler_single("Open_Platform_Service.ids_2")
        assert sqlr_users_result[1] and sqlr_jobs_result[1] and sqlr_apartment_result[1] and r[1]

    def test_open_auth_register_value_None(self):
        '''“注册接口”正参数验证：job为None，apartment为空，tel为空，introduction为空'''
        self.increment_config_data()

        excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_1")
        excel_dict["data"]["job"] = ""
        excel_dict["data"]["apartment"] = ""
        excel_dict["data"]["tel"] = ""
        excel_dict["data"]["introduction"] = ""
        r = self.central_scheduler_single(excel_dict)
        assert r[1]
        sqlr_users_result=self.central_scheduler_single("sql.ids_4")
        assert r[1]and sqlr_users_result[1]

    #  @pytest.mark.skipif(cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_uid"] == "" or
    #                      cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_name"] == "" or
    #                      cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_email"] == "",
    #                      reason='异常数据为空，跳过该case')
    @pytest.mark.parametrize("abnormal_value",
                             [{"verification_values": {
                                 "uid": cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_uid"]},
                               "message": "", "error_code": 4},
                              {"verification_values": {
                                  "name": cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_name"]},
                               "message": "", "error_code": 4},
                              {"verification_values": {"email": "email测试汉字"},
                               "message": "", "error_code": 4}])
    def test_open_auth_register_abnormal(self, abnormal_value):
        '''“注册接口”异常参数验证：uid已存在，name已存在，email格式错误'''
        self.info(abnormal_value)
        for abnormal_value_keys in abnormal_value["verification_values"].keys():
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_1")
            excel_dict["data"][abnormal_value_keys] = abnormal_value["verification_values"][abnormal_value_keys]
            r = self.central_scheduler_single(excel_dict)
            assert r[1] == False and json.loads(r[0].text)["error_code"] == abnormal_value["error_code"]

    @pytest.mark.parametrize("abnormal_None",
                             [{"verification_values": {"app_id": ""}, "message": "", "error_code": 0},
                              {"verification_values": {"uid": ""}, "message": "", "error_code": 4},
                              {"verification_values": {"name": ""}, "message": "", "error_code": 4}])
    def test_open_auth_register_abnormal_None(self, abnormal_None):
        '''“注册接口”异常参数验证：app_id，uid，name必传参数为空'''

        self.info(abnormal_None)
        for abnormal_value_keys in abnormal_None["verification_values"].keys():
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_1")
            excel_dict["data"][abnormal_value_keys] = abnormal_None["verification_values"][abnormal_value_keys]
            r = self.central_scheduler_single(excel_dict)
            assert r[1] == False and json.loads(r[0].text)["error_code"]==abnormal_None["error_code"]


class TestOpenAuthBind(PytestFixture):
    #  /open/auth/bind
    def setup(self):
        self.config = self.read_or_modify_config_data(node_large=None)

    def teardown(self):
        pass

    def bind_register_data(self):
        '''获取invite_code--注册新员工'''
        self.register_user = self.config["config_basics"]["user"] + "_" + self.config["config_bind"]["identification"] + self.config["config_bind"]["count"] + "@162.com"

        ids_6_r = self.central_scheduler_single("Open_Platform_Service.ids_6",debug=True)
        self.invite_code=json.loads(ids_6_r[0].text)["data"]["code"]
        r = self.central_scheduler_single("Open_Platform_Service.ids_7",debug=False)
        self.read_or_modify_config_data(node_large="config_bind", node="register_user", value=self.register_user)
        lists = ["count"]
        self._increasing_config_data("config_bind", lists)

    def test_open_auth_bind(self):
        '''绑定接口，正流程验证'''
        self.bind_register_data()
        lists = ["regisrer_uid"]
        self._increasing_config_data("config_regisrer", lists)
        self.config = self.read_or_modify_config_data(node_large=None)
        r = self.central_scheduler_single("Open_Platform_Service.ids_3")
        assert r[1]
        sqlr = self.central_scheduler_single("sql.ids_5")
        assert sqlr[2]

    @pytest.mark.parametrize("abnormal_value", [{"verification_values": {"app_id": cores.Core().read_or_modify_config_data(node_large=None)["config_basics"]["app_id"]}, "message": "用户关系已绑定，请直接登录", "error_code": 0},
                                                {"verification_values": {"uid": cores.Core().read_or_modify_config_data(node_large=None)["config_regisrer"]["regisrer_uid"]}, "message": "用户关系已绑定，请直接登录", "error_code": 0},
                                                {"verification_values": {"name": cores.Core().read_or_modify_config_data(node_large=None)["config_bind"]["register_user"]}, "message": "用户关系已绑定，请直接登录", "error_code": 0}])
    def test_open_auth_bind_abnormal(self, abnormal_value):
        '''“绑定接口”异常参数验证：uid已存在，name已存在，app_id已存在'''
        self.info(abnormal_value)
        for abnormal_value_keys in abnormal_value["verification_values"].keys():
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_3")
            excel_dict["data"][abnormal_value_keys] = abnormal_value["verification_values"][abnormal_value_keys]
            r = self.central_scheduler_single(excel_dict)
            assert r[1] == False and json.loads(r[0].text)["error_code"]==abnormal_value["error_code"]

    @pytest.mark.parametrize("abnormal_None",[{"verification_values":{"app_id": ""},"message":"app_id错误","error_code":0},
                                              {"verification_values":{"uid": ""},"message":"uid不能为空","error_code":4},
                                              {"verification_values":{"name": ""},"message":"name不能为空","error_code":4}])
    def test_open_auth_bind_abnormal_None(self, abnormal_None):
        #  “注册接口”异常参数验证：app_id，uid，name必传参数为空
        self.info(abnormal_None)
        for abnormal_value_keys in abnormal_None["verification_values"].keys():
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_3")
            excel_dict["data"][abnormal_value_keys] = abnormal_None["verification_values"][abnormal_value_keys]
            r = self.central_scheduler_single(excel_dict)
            assert r[1] == False and json.loads(r[0].text)["message"]==abnormal_None["message"] and json.loads(r[0].text)["error_code"]==abnormal_None["error_code"]


class TestOpenAuthToken(PytestFixture):
    #  /open/auth/token
    def setup(self):
        self.config = self.read_or_modify_config_data(node_large=None)

    def teardown(self):
        pass

    def test_open_auth_token(self):
        '''正流程验证'''
        r = self.central_scheduler_single("Open_Platform_Service.ids_4")
        self.api_token = json.loads(r[0].text)["data"]["token"]
        assert r[1]
        assert json.loads(r[0].text)["data"]["expires_in"]==604800

    @pytest.mark.parametrize("abnormal_value",
                             [{"verification_values": {
                                 "app_id": cores.Core().read_or_modify_config_data(node_large=None)["config_basics"]["old_app_id"]},
                               "message": "", "error_code": 0},
                             {"verification_values": {
                                 "uid": cores.Core().read_or_modify_config_data(node_large=None)["config_basics"][
                                     "old_regisrer_uid"]},
                                 "message": "", "error_code": 0}
                             ])
    def test_open_auth_token_abnormal(self, abnormal_value):
        '''“注册接口”异常参数验证：app_id不是该账号，uid不是该账号'''
        self.info(abnormal_value)
        for abnormal_value_keys in abnormal_value["verification_values"].keys():
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_4")
            excel_dict["data"][abnormal_value_keys] = abnormal_value["verification_values"][abnormal_value_keys]
            r = self.central_scheduler_single(excel_dict)
            assert r[1] == False and json.loads(r[0].text)["error_code"]==abnormal_value["error_code"]

# 优化中
class TestOpenResourceV2Fabric2(PytestFixture):
    #  /open/resource/v2/fabric
    #  面料--创建

    def tick_field(self,tick_field_key):
        # 勾选字段
        def tick_all_key():
            # 勾选全部字段
            category_r = self.central_scheduler_single("Open_Platform_Service.ids_9")
            global_setting_list = json.loads(category_r[0].text)["data"]["global_setting_list"]
            values = []
            for global_setting_list_value in global_setting_list:
                for items_value in global_setting_list_value["items"]:
                    self.values.append({"key": items_value["key"]})
            self.central_scheduler_single("Open_Platform_Service.ids_11", request_log_grade = "debug", values = values)

        def untick_all_key():
            # 取消全部字段勾选
            self.central_scheduler_single("Open_Platform_Service.ids_11", request_log_grade = "debug", values = [{"key": "name"}, {"key": "internal_code"}])

        def tick_choice_key(key_list):
            # 指定字段勾选
            values = [{"key": key} for key in key_list]
            self.central_scheduler_single("Open_Platform_Service.ids_11" , request_log_grade = "debug", values = values)

        if tick_field_key == "all":
            # 勾选全部
            tick_all_key()

        if tick_field_key == "unall":
            # 取消勾选全部
            untick_all_key()

        if isinstance(tick_field_key,list):
            # 指定勾选
            tick_choice_key(tick_field_key)

    def test_open_resource_v2_fabric(self,clear_config_fabric_detailed_data_record):
        '''资源2.0--面料--创建,基础字段正流程验证'''

        # 自增面料名称的id
        excel_dict = self.get_excel_dict()

        # 关闭所有动态字段
        self.tick_field(tick_field_key = "unall")

        # 发出请求
        r = self.central_scheduler_single(excel_dict)
        assert r[1]

        # 记录请求数据，方便后续详情，列表等等的验证
        fabric_id = json.loads(r[0].text)["data"]["id"]
        self._info_config_sequence_node_data(node_large ="config_fabric_detailed_data_record", node_value = {"fabric_id":fabric_id, "request_data": self.get_excel_data_by_id("Open_Platform_Service.ids_8")["data"]})

        # 正常字段校验 ，name， internal_code ， external_id ， fabric_attr_param_access
        sqlr = self.central_scheduler_single("sql.ids_10", fabric_id = fabric_id)
        assert sqlr[2]
        # ，取出“接口字段”与“数据对应字段”映射关系
        # 文件地址校验，需要三个值：  db_field_name，fabric_id，verification_value
        # 1，lt_fabrics表关联lt_media的字段名（就是为了取id）
        # 2，fabric_id
        # 3，期望的数据
        api_name_mapping_db= eval(self.read_or_modify_config_data()["config_fabric_method"]["api_name_mapping_db"])
        for dict_keys in api_name_mapping_db.keys():
            sqlr = self.central_scheduler_single("sql.ids_21", db_field_name = api_name_mapping_db[dict_keys], fabric_id = fabric_id , verification_value = dict_keys)
            assert sqlr[2]

    def test_open_resource_v2_fabric_value_None(self,clear_config_fabric_detailed_data_record):
        '''“资源2.0--面料--创建”基础字段正流程验证：非必填为空'''

        # 关闭所有动态字段
        self.tick_field(tick_field_key = "unall")

        # 获取请求数据——非必填数据置为空
        excel_dict = self.get_excel_dict()
        excel_dict["data"]["thumbPath"] = ""
        excel_dict["data"]["bigThumbPath"] = ""
        excel_dict["data"]["model3dPath"] = ""
        excel_dict["data"]["xhrPath"] = ""
        del excel_dict["data"]["fabricAttrParamAccess"]

        # 发出请求
        r = self.central_scheduler_single(excel_dict)
        assert r[1]

        self.fabric_id = json.loads(r[0].text)["data"]["id"]
        # 添加请求数据到config_fabric_detailed_data_record 方便后续验证
        self._info_config_sequence_node_data(node_large ="config_fabric_detailed_data_record", node_value = {"fabric_id":self.fabric_id, "request_data": excel_dict})

        # 验证“面料名称”“面料编号”，其他都为空 无需验证
        sqlr = self.central_scheduler_single("sql.ids_11")
        assert sqlr[2]

    def add_field_optional_value(self, field_list_data, min_num_optional_value , all_num = 0):
        """给字段 新增不满足 数量的“可选值”"""
        for i in range(1, (min_num_optional_value - all_num) + 1):
            # 便利N遍 添加N个可选值
            # 先取出type_key，新增可选值接口地址需要拼上“type_key”，还有新增字段的"名称name" ，名称是不能重复的所以自增+1
            self._increasing_config_data("config_fabric", ["optional_value_name_id"])
            type_key = field_list_data["type_key"]
            # 拼接一下“可选值名称”让他唯一
            optional_value_name = field_list_data["show_name"] + "_" + self.read_or_modify_config_data()["config_fabric_method"]["optional_value_name_id"]
            self.central_scheduler_single("Open_Platform_Service.ids_14", type_key=type_key, optional_value_name = optional_value_name, request_log_grade="debug" )
        # 新增“可选值”后列表数据会变化，所以重新获取一下当前的列表数据
        r = self.central_scheduler_single("Open_Platform_Service.ids_9", request_log_grade="debug" )
        new_field_list = json.loads(r[0].text)["data"]["field_list"]
        # 重新获取后，找到对应字段的数据，返回
        for list_value in new_field_list:
            if list_value["key"] == field_list_data["key"]:
                return list_value

    def add_custom_field(self,items):
        """添加自定义字段"""
        show_name = "custom_" + items + "_" + str(self.read_or_modify_config_data()["config_fabric"]["custom_name_id"])
        self._increasing_config_data("config_fabric", ["custom_name_id"])
        self.config = self.read_or_modify_config_data()
        self.central_scheduler_single("Open_Platform_Service.ids_19", show_name=show_name, show_en_name=show_name, data_type=items, request_log_grade="debug")

    def add_supplier_field_optional_value(self,superfluous_field_list_data, min_num_optional_value):
        #  给supplier字段 新增不满足 数量的值
        # 获取供应商“可选值列表”，因为供应商字段是特殊处理的，所以要通过“可选值列表接口”获取
        r = self.central_scheduler_single("Open_Platform_Service.ids_16",  request_log_grade = "debug")
        list_value = json.loads(r[0].text)["data"]["list"]["data"]
        # 判断是否满足min_num_optional_value（最小“可选值”数量要求）
        if len(list_value) < min_num_optional_value:
            # 新增到满足要求
            for count in range(0, min_num_optional_value - len(list_value)):
                self.central_scheduler_single("Open_Platform_Service.ids_17",  request_log_grade = "debug", count = str(count))
        # 新增完成，获取最新的列表数据
        r = self.central_scheduler_single("Open_Platform_Service.ids_9",  request_log_grade = "debug")
        new_field_list_data = json.loads(r[0].text)["data"]["field_list"]
        for list_value in new_field_list_data:
            if list_value["key"] == superfluous_field_list_data["key"]:
                return list_value

    def ergodic_parameter_write_config(self,custom_field = False):
        # 便利所有参数，生成“映射数据”和“分类数据”，最终写入到配置文件
        def get_api_params():
            '''获取对外开发接口文档的参数'''
            r = self.central_scheduler_single("Open_Platform_Service.ids_12", request_log_grade = "debug")
            r_data = json.loads(r[0].text)["data"]["data"]
            extract_data = re.findall(r"\| (.+) \| ([a-z]+) \| (.+) \| (.+) \| (.+) \|\n", r_data)
            return extract_data

        def init_data():
            """初始化，勾选数据，列表数据，接口文档数据"""
            # 取消勾选全部动态字段
            self.tick_field(tick_field_key = "unall")
            # 没有“abnormal” 异常类型，我们就定义一个，把特殊的字段放置到里面，也就是无法建立映射关系的字段：如：带单位的字段，有大小值的字段
            mapping_data, classification_data = {"abnormal": []}, {"abnormal": {}}
            # 获取请求“设置中心》面料”接口数据
            category_r = self.central_scheduler_single("Open_Platform_Service.ids_9", request_log_grade = "debug")
            category_r_text=json.loads(category_r[0].text)
            # 获取面料列表field_list_data：“当前列表数据”；global_setting_list：获取“全部“勾选数据””
            field_list_data = category_r_text["data"]["field_list"]
            global_setting_list = category_r_text["data"]["global_setting_list"]
            # 获取对外开放接口数据
            api_params_data = get_api_params()
            return  field_list_data, global_setting_list, api_params_data

        def handler_custom_field(field_list_data, global_setting_list, api_params_data):
            """判断是否需要处理自定义字段"""
            # 获取自定义字段的分类；
            # establish_relationship_and_classification支持四个字段：
            # custom_field标识是否只用便利自定义字段，
            # global_setting_list所有勾选字段，
            # api_params_data即可文档数据，
            # field_list_data以及当前的列表数据
            mapping_data, classification_data = generate_mapping_data_and_classification_data(custom_field, field_list_data, global_setting_list, api_params_data)
            # 判断是否存在四个型["text", "number", "list", "checkbox"]，存在就使用，不存在就创建字段
            list_custom_type = eval(self.read_or_modify_config_data()["config_fabric_method"]["custom_type"])
            for list_custom_type_keys in list_custom_type:
                # 便利所有类型
                if (list_custom_type_keys in classification_data) == False:
                    self.add_custom_field(list_custom_type_keys)

        def write_config(mapping_data, classification_data):
            # “映射数据”和“分类数据”写入文件
            self.read_or_modify_config_data(node_large="config_fabric", node = "data_type_corresponding_data",value=str(mapping_data))
            for corresponding_data_value in classification_data.keys():
                self.read_or_modify_config_data(node_large="config_fabric", node = corresponding_data_value,value=str(classification_data[corresponding_data_value]))

        def generate_mapping_data_and_classification_data(custom_field, field_list_data, global_setting_list, api_params_data):
            """生成：mapping_data（映射数据）  和  classification_data（）"""
            values, mapping_data, classification_data = [], {"abnormal": []}, {"abnormal": {}}

            def return_filter_custom_field(custom_field, global_setting_list_value_name):
                """处理是否过滤自定义字段"""
                custom_name = self.read_or_modify_config_data()["config_fabric_method"]["custom_name"]
                if custom_field:
                    return global_setting_list_value_name == custom_name
                else:
                    return global_setting_list_value_name != custom_name

            def get_new_field_list_data(items_value):
                """勾选数据并获取最新列表数据"""
                # 把当前的字段勾选了
                values.append(items_value["key"])
                self.tick_field(tick_field_key=values)
                # 勾选之后，获取列表最新数据
                r = self.central_scheduler_single("Open_Platform_Service.ids_9", request_log_grade="debug")
                new_field_list_data = json.loads(r[0].text)["data"]["field_list"]
                return new_field_list_data

            def get_comparison_results_list(new_data, old_data):
                """新旧数据对比，多出的数据即使当前字段"""
                # 最新的列表数据与旧的列表数据，值都转换成字符串，方便通过集合做减法
                str_new_data = [str(i) for i in new_data]
                str_old_data = [str(i) for i in old_data]
                # 最新的列表数据与旧的列表数据，转换成集合做减法，多出的就是该字段的数据
                superfluous_field_list_data = list(set(str_new_data) - set(str_old_data))
                # 多出来的列表数据，放置到comparison_results列表返回
                comparison_results = []
                for list_datas in superfluous_field_list_data:
                    comparison_results.append(eval(list_datas))
                return comparison_results

            def add_optional_value(list_comparison_results):
                # 判断是否需要新增“可选值”
                new_list_comparison_results = []
                # 便利列表每一个值
                for list_value in list_comparison_results:
                    # 判断是否是“列表”/“多选” 是的话 同时判断“可选值”是否小于 min_num_optional_value  小于则，补齐数据
                    min_num_optional_value = int(self.read_or_modify_config_data()["config_fabric_method"]["min_num_optional_value"])
                    # 获取需要“可选值”的字段类型["list", "checkbox", "multi_percent_main_component", "supplier"]
                    add_data_types = self.read_or_modify_config_data()["config_fabric_method"]["add_data_types"]
                    if list_value["data_type"] in add_data_types:
                        if list_value["data_type"] == "supplier":
                            # supplier类型需要特殊处理
                            list_value = self.add_supplier_field_optional_value(list_value, min_num_optional_value)
                        elif list_value["type_key_count"] < min_num_optional_value:
                            # 判断可选值是否小于min_num_optional_value
                            list_value = self.add_field_optional_value(list_value, min_num_optional_value - list_value["type_key_count"])
                    # 把更新完的数据重新，加入到这个新的列表里
                    new_list_comparison_results.append(list_value)

                return new_list_comparison_results

            def return_mapping_data_and_classification_data(i_l_a_data_dict, items_value, list_comparison_results, api_file_comparison_results):
                """返回映射关系数据 和 按类型归类数据，mapping_data  和  classification_data"""
                # 判断是否是正常字段，还是异常字段（非正常关系的字段，如：带单位，大小值的字段，会被加入到“abnormal”分类里）
                if False not in [len(list_comparison_results) == 1, len(api_file_comparison_results)==1]:
                    try:
                        # 组合mapping_data 字典并根据类型分类
                        # 根据data_type 类型判断 归类，如果报错则证明此类型，还未添加，需要新增，让其形成一个分类
                        mapping_data[list_comparison_results[0]["data_type"]] = mapping_data[list_comparison_results[0]["data_type"]] + [{items_value["key"]:[items_value["key"],items_value["key"]+"_list",items_value["key"]+"_file"]}]
                        # “data_type”添加到“classification_data分类数据”
                        classification_data[list_comparison_results[0]["data_type"]].update(i_l_a_data_dict)
                    except BaseException:
                        # 创建一个映射列表
                        mapping_data[list_comparison_results[0]["data_type"]] = []
                        # 让对应类型，把映射关系存入该列表
                        mapping_data[list_comparison_results[0]["data_type"]] = mapping_data[list_comparison_results[0]["data_type"]] + [{items_value["key"]:[items_value["key"],items_value["key"]+"_list",items_value["key"]+"_file"]}]
                        # 创建分类数据字典
                        classification_data[list_comparison_results[0]["data_type"]] = {}
                        # 把分类字典放入其中
                        classification_data[list_comparison_results[0]["data_type"]].update(i_l_a_data_dict)
                else:
                    mapping_data["abnormal"].append({items_value["key"]:[items_value["key"],items_value["key"]+"_list",items_value["key"]+"_file"]})
                    classification_data["abnormal"].update(i_l_a_data_dict)

                return mapping_data , classification_data

            def main(custom_field, field_list_data, global_setting_list, api_params_data, mapping_data, classification_data):
                # 便利字段的五个分类：“产品基本信息”“产品属性信息”“产品详情信息”“产品核价信息”“自定义字段”
                # 动态字段：“产品基本信息”“产品属性信息”“产品详情信息”“产品核价信息”
                # 自定义字段：“自定义字段”
                for global_setting_list_value in global_setting_list:
                    # 判断是否仅执行自定义字段
                    if return_filter_custom_field(custom_field, global_setting_list_value["name"]):
                        # 便利分类下的所有字段
                        for items_value in global_setting_list_value["items"]:
                            # 过滤初始化过后,依然存在的基础字段：“名称”“内部编号”
                            if "'key': '%s'" %(items_value["key"]) in str(field_list_data):
                                continue

                            """勾选数据并获取最新列表数据"""
                            # 勾选字段并获取最新的列表数据
                            new_field_list_data = get_new_field_list_data(items_value)
                            # 最新的列表数据，与旧的列表数据做对比，多出的数据，就是当前勾选字段的列表数据
                            list_comparison_results = get_comparison_results_list(new_field_list_data, field_list_data)


                            """对比接口文档数据，多出的数据，即是文档数据"""
                            # 所作的“勾选数据”和“列表数据”，是否有效，都根据“接口文档是否出现新的字段”
                            effective_field=False
                            # 获取最新的接口文档数据
                            new_api_params_data = get_api_params()
                            # 最新的api文档数据，与旧的api文档数据做对比，多出的数据，就是当前勾选字段的api文档字段数据
                            api_file_comparison_results = get_comparison_results_list(new_api_params_data, api_params_data)
                            # 接口文档有多出的字段就是有效勾选
                            if api_file_comparison_results:
                                effective_field=True


                            """给对应类型的字段增加多个值"""
                            if effective_field:
                                # 判断是否是有效数据（即可文档出现了的数据）
                                list_comparison_results = add_optional_value(list_comparison_results)

                                # 三个值组合成为字典
                                i_l_a_data_dict = {}
                                i_l_a_data_dict[items_value["key"]] = items_value
                                i_l_a_data_dict[items_value["key"]+"_list"] = list_comparison_results
                                i_l_a_data_dict[items_value["key"]+"_file"] = api_file_comparison_results

                                self.info("**" * 10)
                                self.info(("字段勾选数据：", items_value))
                                self.info(("字段列表数据：", list_comparison_results))
                                self.info(("字段api文档列表数据：",api_file_comparison_results))


                                # if len(list_comparison_results) > 1:
                                #     self.info("**" * 10)
                                #     self.info(("异常字段勾选数据：", items_value))
                                #     self.info(("异常字段列表数据：", list_comparison_results))
                                #     self.info(("异常字段api文档列表数据：", api_file_comparison_results))

                                """生成映射关系数据 和 按类型归类数据，mapping_data  和  classification_data"""
                                # 判断是否是正常字段，还是异常字段（非正常关系的字段，如：带单位，大小值的字段，会被加入到“abnormal”分类里）
                                mapping_data, classification_data = return_mapping_data_and_classification_data(i_l_a_data_dict, items_value, list_comparison_results, api_file_comparison_results)

                            else:
                                # 对外开放接口不支持的字段
                                pass
                                # self.info("**" * 10)
                                # self.info(("不支持的字段勾选数据：", items_value))
                                # self.info(("不支持的字段列表数据：", list_comparison_results))
                                # self.info(("不支持的字段api文档列表数据：",api_file_comparison_results))

                            # 下一次循环新的数据将不再新
                            field_list_data = new_field_list_data
                            api_params_data = new_api_params_data

                return mapping_data, classification_data

            return main(custom_field, field_list_data, global_setting_list, api_params_data, mapping_data, classification_data)

        def main():
            # 初始化数据，获取初始化数据
            field_list_data, global_setting_list, api_params_data = init_data()

            # 如果是自定义字段，则特殊处理自定义字段
            if custom_field:
                handler_custom_field(field_list_data, global_setting_list, api_params_data)

            # 便利所有所有字段，获取“映射数据”和“分类数据”
            mapping_data, classification_data = generate_mapping_data_and_classification_data(custom_field, field_list_data, global_setting_list, api_params_data)

            # 写入mapping_data, classification_data 配置文件
            write_config(mapping_data, classification_data)

        main()

    def get_excel_dict(self):
        # 获取最新的excel_dict数据
        # 自增数据"externalId", "name", "internalCode"，保持唯一
        lists = ["externalId", "name", "internalCode"]
        self._increasing_config_data("config_fabric", lists)
        self.config = self.read_or_modify_config_data(node_large=None)
        # 读取最新的excel数据组成一个字典
        excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
        return excel_dict

    def return_type_corresponding_data(self, type):

        def get_necessary_data( type_corresponding_indexes, index_corresponding_data):
            # 处理type_corresponding_indexes，和index_corresponding_data 返回必要数据：
            # key_list："需要勾选的基础字段的key"，
            # api_field_name_list：接口文档字段名称list，
            # optional_value_list：有选项的字段的可选值，
            # list_type_key（sql验证必要数据）：是一个list，里面的value对应数据库中“lt_categories.type”，此值是sql定位到“列表可选值”数据的必要数据
            # list_field_all_data：/api/resource/category接口中的“data”--中的“field_linst”（field_linst中，就是列表所有的字段数据）--中的“该字段数据”
            key_list, api_field_name_list, optional_value_list, list_type_key, list_field_all_data = [], [], [], [], []
            for data_type_corresponding_data_value in type_corresponding_indexes:
                for list_key in data_type_corresponding_data_value.keys():
                    list_value = data_type_corresponding_data_value[list_key]
                    key_list.append(index_corresponding_data[list_value[0]]["key"])
                    try:
                        optional_value_list.append(index_corresponding_data[list_value[1]][0]["initial"])
                        list_type_key.append(index_corresponding_data[list_value[1]][0]["type_key"])
                        list_field_all_data.append(index_corresponding_data[list_value[1]][0])

                    except BaseException:
                        pass
                    api_field_name_list.append(index_corresponding_data[list_value[2]][0][0])
            return (key_list, api_field_name_list, optional_value_list, list_type_key, list_field_all_data)

        #  取出配置文件中"映射数据"
        type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))[type]
        #  取出配置文件中的 types 数据
        type_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"][type])

        # 获取需要勾选的值key_list，
        # 获取接口文档中的字段名称api_field_name
        # 选项的字段的可选值optional_value_list,
        # （sql验证必要数据）：是一个list，里面的value对应数据库中“lt_categories.type”，此值是sql定位到“列表可选值”数据的必要数据   list_type_key
        # 基础字段列表的“字段”的“所有数据”type_list_data
        key_list, api_field_name_list, optional_value_list, list_type_key, list_field_all_data = get_necessary_data(type_corresponding_indexes, type_data)

        #  勾选数据
        self.tick_field(key_list)

        return {"key_list": key_list, "api_field_name_list": api_field_name_list, "optional_value_list": optional_value_list, "list_type_key": list_type_key, "list_field_all_data": list_field_all_data}

    def test_open_resource_v2_fabric_dynamic_parameter(self,clear_config_fabric_detailed_data_record):
        """动态字段测试"""

        def test_text():
            # 测试文本

            def return_request_field_data(test_data, api_field_name_list_list):
                # 获取excel最新的数据
                excel_dict = self.get_excel_dict()
                # 便利“接口文档中的字段名称” 依次以key：value的形式添加测试数据，到请求数据data中
                for count,field_values in enumerate(api_field_name_list_list):
                    excel_dict["data"][field_values] = test_data
                #  标识name和internalCode 这是一个测试text类型的面料，为了方便接下去的接口校验/单独类型校验
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_%s" %("text")
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_%s" %("text")
                return excel_dict

            def verification_db_data(test_data, fabric_id, db_field_name_list):
                # 提交的数据对比数据库数据
                sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                assert sqlr[2]
                for db_name in db_field_name_list:
                    assert sqlr[0][0][db_name] == test_data

            def main():
                # 获取测试数据
                # 文本类型，至少需要3个数据：1，“数据库字段名”，2，“api文档接口字段名”，3，测试数据

                test_text_data = ["text测试中文_", "~!@#$%^&*()_+-=:;\"\'<>,.?/|\\","1234567890","lingdi","l1i2n3g4d5i"]


                # 获取启用的字段/同时也是db字段名：key_list
                # 获取接口文档中的字段名称api_field_name_list
                necessary_data = self.return_type_corresponding_data(type = "text")
                key_list, api_field_name_list = necessary_data["key_list"], necessary_data["api_field_name_list"]

                for test_data in test_text_data:
                    # 把测试数据，和接口字段名称，传给return_request_field_data，所有字段添加完成后，返回请求主体
                    excel_dict = return_request_field_data(test_data, api_field_name_list)
                    # 发出请求
                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    # 添加请求数据到config_fabric_detailed_data_record 方便后续验证
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record", node_value={"fabric_id": fabric_id, "request_data": excel_dict["data"]})
                    #  sql验证
                    verification_db_data(test_data = test_data, fabric_id = fabric_id, db_field_name_list = key_list)

            main()

        def test_list():
            # 测试列表
            def return_request_data(api_field_name_list, optional_value_list, test_api_generate):
                # list_optional_values（sql验证必要数据）：是一个list，里面的value是我上送的“列表可选值的name”，用来校验不同字段的“列表可选值name”，sql验证必要数据
                list_optional_values=[]

                # 获取请求基础数据
                excel_dict = self.get_excel_dict()

                # 便利所有列表字段，给列表字段，随机一个“列表可选值”
                for count,field_values in enumerate(api_field_name_list):
                    # 最后一次，让后端自己生成
                    if test_api_generate:
                        test_name = "测试后端生成" + "_" + str(self.read_or_modify_config_data()["config_fabric"]["externalId"])
                    else:
                        # “列表可选值”的总数内，随机数一个下标
                        randints = random.randint(0, len(optional_value_list[count]) - 1)
                        # 取出这个“列表字段”下标的“列表可选值”
                        list_count_randints = optional_value_list[count][randints]

                        # optional_value_list_count_randints_name，是“列表字段”下标的“列表可选值的name”
                        test_name = list_count_randints["name"]

                    # key：value的形式添加 【列表可选值的name】 到请求data中
                    excel_dict["data"][field_values] = test_name
                    # 把字段的name添加到“list_optional_values”，方便后面验证这个数据
                    list_optional_values.append(test_name)

                #  标识name和internalCode 这是一个测试 _list 类型的面料
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_list"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_list"

                return excel_dict, list_optional_values

            def verification_db_data(fabric_id, key_list, list_type_key, list_optional_values ):
                # 提交的数据对比数据库数据

                # 记录加标的形式便利list_type_key，以字段为单位 进行验证
                for count,i in enumerate(list_type_key):
                    # suitableYear需要特殊处理，因为“年份”虽然是个list，也有“列表可选值”，但是在“lt_fabrics”表中不是通过lt_categories.cid的方式关联到“lt_categories”表,而是直接把值写在了“lt_fabrics”表中，所以需要特殊处理
                    if i=="suitableYear":
                        # 如果是“测试后端生成_” 则不会写到库里，后端会把库里的值随机写一个，但是"列表可选值" 依然会被写进去
                        sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                        if "测试后端生成_" in  list_optional_values[count]:
                            # 校验“列表可选值”是否被写入进去
                            # assert str(sqlr[0][0]["suitable_year"]) == '2022'
                            sqlr = self.central_scheduler_single("sql.ids_20", fabric_id = fabric_id, list_type_key_value = "suitableYear")
                            assert list_optional_values[count] in  str(sqlr[0])
                        else:
                            # 校验“lt_fabrics” 的suitable_year 字段
                            assert str(sqlr[0][0]["suitable_year"]) == list_optional_values[count]
                    else:
                        # key_list_value，此值是sql定位到“列表可选值”数据的必要数据
                        # list_type_key_value，此值是“列表可选值的name”
                        key_list_value, list_type_key_value = key_list[count], i
                        sqlr = self.central_scheduler_single("sql.ids_17", fabric_id = fabric_id, key_list_value = key_list_value, list_type_key_value = list_type_key_value)
                        # sql验证是否成功，验证查询出来的name与 我们提交的name是不是一致
                        assert sqlr[0][0]["name"] == list_optional_values[count]

            def main():
                # 测试list类型至少需要：1，数据库字段数据；2，接口字段名称；3，“列表可选值”；4，“type_key”

                # 同时也是数据库字段名  key_list，
                # 获取接口文档中的字段名称  api_field_name_list

                # 选项的字段的可选值   optional_value_list,
                # type_key，list_type_key
                # 基础字段列表的“字段”的“所有数据” list_field_all_data

                necessary_data = self.return_type_corresponding_data(type = "list")
                key_list, api_field_name_list, optional_value_list, list_type_key = necessary_data["key_list"], necessary_data["api_field_name_list"], necessary_data["optional_value_list"], necessary_data["list_type_key"]

                # 测试次数
                test_frequency = 2
                for counts in range(test_frequency):
                    #判断是否最后一次，最后一次就是验证“测试接口自动生成数据”
                    last, test_api_generate = test_frequency - 1, False
                    if counts == last:
                        test_api_generate = True

                    # 处理请求数据
                    excel_dict, list_optional_values = return_request_data(api_field_name_list, optional_value_list, test_api_generate)

                    # 发出请求
                    r = self.central_scheduler_single(excel_dict)
                    # 校验请求是否成功
                    assert r[1]
                    # 获取响应回来的 fabric_id
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    # 添加请求数据到config_fabric_detailed_data_record 方便后续验证
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"]})

                    if test_api_generate:
                        # 因为最后清除“后端生成”数据时，“列表的可选值”要求不能有未删除的面料，使用该字段，所以需要把面料id也记录下来
                        self._add_config_list_data(node_large="config_fabric_test_back_end_generate", node = "delete_field_optional_value_relation_fabric_id" , add_value = [fabric_id])
                        # 需要删除的字段写入“待删除”列表，执行完成一并删除
                        self._add_config_list_data(node_large="config_fabric_test_back_end_generate",node="wait_delete_field_optional_value_list",add_value = list_type_key)

                    # 验证必要数据交给：verification_db_data
                    verification_db_data(fabric_id, key_list, list_type_key, list_optional_values)

            main()

        def test_multi_percent_main_component():
            #  测试成分

            # 至少需要4个数据：1，数据库字段数据；2，接口字段名称；3，“列表可选值”；4，“type_key”

            # 获取需要勾选的值  key_list，
            # 获取接口文档中的字段名称  api_field_name_list
            # 选项的字段的可选值   optional_value_list,
            # 基础字段列表的“字段”的“所有数据” list_field_all_data
            necessary_data = self.return_type_corresponding_data(type = "multi_percent_main_component")
            key_list, api_field_name_list, optional_value_list, list_type_key = necessary_data["key_list"], necessary_data["api_field_name_list"], necessary_data["optional_value_list"], necessary_data["list_type_key"]

            def send_and_check_interface_data(field_value,optional_value_list_count_randints,value_percent, test_api_generate = False):
                # 发送和检查接口数据
                # 获取基础请求数据
                excel_dict = self.get_excel_dict()

                # 请求数据
                # key：value的形式添加 【拼接的字符串】 到请求data中
                excel_dict["data"][api_field_name_list[0]] = field_value
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_component"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_component"

                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                # 添加请求数据到config_fabric_detailed_data_record 方便后续验证
                self._info_config_sequence_node_data(node_large = "config_fabric_detailed_data_record",node_value = {"fabric_id": fabric_id,"request_data": excel_dict["data"]})

                if test_api_generate:
                    # 因为最后清除“后端生成”数据时，“列表的可选值”要求不能有未删除的面料，使用该字段，所以需要把面料id也记录下来
                    self._add_config_list_data(node_large="config_fabric_test_back_end_generate", node = "delete_field_optional_value_relation_fabric_id" , add_value = [fabric_id])
                    # 需要删除的字段写入“待删除”列表，执行完成一并删除
                    self._add_config_list_data(node_large="config_fabric_test_back_end_generate",node="wait_delete_field_optional_value_list",add_value = list_type_key)


                # 执行sql 返回sql执行的结果
                sqlr = self.central_scheduler_single("sql.ids_14",fabric_id = fabric_id)

                assert sqlr[2]

                # 便利sql结果：“([{'name': '亚麻', 'percent': 1.0, 'group1': '正面'}, {'name': '羊驼毛', 'percent': 1.0, 'group1': '正面'}, {'name': '羊羔毛', 'percent': 1.0, 'group1': '正面'},... ”
                # 每个列表值 都是一个“成分值”
                for count,i in enumerate(sqlr[0]):
                    # 用我们传进来的optional_value_list_count_randints（“成分可选值的name”列表），依次取出对应值比对sql查询出来的“name”
                    # 用 value_percent（“百分比”和“正/反面” 组成的list） 中的[0]个坐标也就是“百分比” 取比对sql查询出来的“percent”
                    assert optional_value_list_count_randints[count] == i["name"],float(value_percent[count][0]) == i["percent"]
                    # 校验字段的正/分面是不是跟数据库一致
                    assert value_percent[count][1] == i["group1"]

            def generate_request_data_and_verification_data_single(positive_and_negative, proportion, test_name = None):
                # 生成“单”个“成份值”数据  和“验证数据”
                if test_name == None:
                    # “成分值”的总数内，随机数一个下标
                    randints = random.randint(0, len(optional_value_list[0]) - 1)
                    # 取出这个“成分列表”对应下标的“成分可选值”
                    optional_value_list_subscript_randints = optional_value_list[0][randints]
                    test_name = optional_value_list_subscript_randints["name"]

                # 拼接“正/反面”“positive_and_negative”
                # 拼接“百分比” “proportion”
                # 拼接“选中的成分可选值的name”“optional_value_list_count_randints”
                # 拼接成为“请求字段”的值
                field_value = positive_and_negative + ":" + str(proportion) + "%" + test_name
                # field_value    请求值，
                # [optional_value_list_subscript_randints["name"]]   选中的“成分可选值的name”组成一个list；为啥组成一个list，因为多个值的时候，也是list，为了让后面可以统一处理，转为统一的list格式
                # [[proportion,positive_and_negative]]   proportion：“百分比”和positive_and_negative：正/反面，组成一个list，方便后续验证数据的正确性；list同样是为了统一处理
                return field_value, [test_name], [[proportion,positive_and_negative]]

            def generate_request_data_and_verification_data_multiple(positive_and_negative, proportion):
                # 生成“多”个“成份值”数据  和“验证数据”

                def assemble_proportion_int_type(list_name):
                    # 组装请求数据field_value，验证数据list_name（多个成分“可选字段值的name”，组成的list），value_percent（对应“百分比” 组成的list）
                    value, value_percent = "", []
                    for i in list_name:
                        # 判断是否最后一次  百分比减去的“随机数量的列表值”的总数，就是最后一个值的百分比

                        if i == list_name[-1]:
                            # len(list_name)里包含这自己所以要+1 把自己去掉，自己是最后一次
                            value = value + str(proportion - len(list_name) + 1) + "%" + i
                            # 把一会要校验的百分比，和“正/反面”添加到列表
                            value_percent.append([proportion - len(list_name) + 1, positive_and_negative])
                            break
                        # value是以及拼接的字符串，i是“成分值” 1%是这个成分的百分之一
                        value = value + "1%" + i + ","
                        value_percent.append([1, positive_and_negative])

                    # “正/反面 ”拼接到“拼接的字符串”中
                    field_value = positive_and_negative + ":" + value
                    # 返回 field_value：拼接的字符串
                    # list_name“成分值组成的列表”
                    # value_percent 对应成分的“百分比”和“正/反面”组成的列表
                    return field_value, list_name, value_percent

                def assemble_proportion_float_type(list_name):
                    # 组装请求数据field_value，验证数据list_name（多个成分“可选字段值的name”，组成的list），value_percent（对应“百分比” 组成的list）
                    value, value_percent = "", []
                    for i in list_name:
                        # 判断是否最后一次  百分比减去的“随机数量的列表值”的总数，就是最后一个值的百分比
                        if i == list_name[-1]:
                            # len(list_name)里包含这自己所以要+1 把自己去掉，自己是最后一次
                            # 转换成0.01 拼接进value
                            transformation_float = (proportion - len(list_name) + 1) / 100
                            #把最后一个“值”拼接进去
                            value = value + str(transformation_float) + "%" + i
                            # 把最后一次 自己的 百分比 和 正/反面 添加到列表
                            value_percent.append([transformation_float, positive_and_negative])
                            break
                        # 转换成0.01 拼接进value
                        transformation_float = 1 / 100
                        # 支持中文“，” 英文","随机取一个
                        splice_symbo = random.choice(["，"])
                        value = value + str(transformation_float) + "%" + i + splice_symbo
                        #  百分比 和 正/反面 添加到列表,方便后面校验
                        value_percent.append([transformation_float, positive_and_negative])
                    # “正/反面 ”拼接到“拼接的字符串”中
                    field_value = positive_and_negative + ":" + value
                    # 返回 field_value：拼接的字符串
                    # list_name“成分值组成的列表”
                    # value_percent 对应成分的“百分比”和“正/反面”组成的列表
                    return field_value, list_name, value_percent

                proportion_type_float = False
                # proportion如果是float，类型则，按照float来进行处理
                if isinstance(proportion,float):
                    proportion_type_float = True
                    proportion = int(proportion * 100)

                # [random.randint(0, len(optional_value_list[0]) - 1) for test_data in range(random.randint(2, len(optional_value_list[0]) - 1))] 此为 一个生成器
                    # for test_data in range(random.randint(2, len(optional_value_list[0]) - 1))  循环2 - “成分值”的总数  次循环
                    # random.randint(0, len(optional_value_list[0]) - 1) “成分值”的总数内，随机数一个下标 添加到list
                # set 转成一个集合（为了去重）
                # 再转回list 方便下面  生成数据
                if len(optional_value_list[0]) >= 100:
                    # 担心有成分值超过100，整数的最大百分比是100，float可以支持到1w 但是每必要，统一封顶是100个成分
                    list_random_num = list(set([random.randint(0, 100 - 1) for _ in range(random.randint(2, 100 - 1))]))
                else:
                    list_random_num=list(set([random.randint(0, len(optional_value_list[0]) - 1) for _ in range(random.randint(2, len(optional_value_list[0]) - 1))]))

                # 用得到的 列表随机数  list_random_num  取出每个“成分列表”对应下标的“成分可选值的name” 生成一个列表list_name
                list_name=[optional_value_list[0][i]["name"] for i in list_random_num]

                #判断是校验小数，还是整数

                return assemble_proportion_float_type(list_name) if proportion_type_float else assemble_proportion_int_type(list_name)

            def open_100_close_back():
                # k开启100%  关闭反面;单个数据验证
                def transmit_proportion(proportion, test_name = None):
                    # proportion 百分比
                    # 标识这是一个“正面”
                    positive_and_negative = "正面"
                    # field_value    请求值，
                    # list_name 随机选中的“成分可选值的name” list类型
                    # “百分比”和“正/反面” 组成的list
                    field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative, proportion, test_name)
                    test_api_generate = False if test_name == None else True
                    # 把三个值 交给统一处理的方法  send_and_check_interface_data 把请求发出去，然后校验sql
                    send_and_check_interface_data(field_value, list_name, value_percent, test_api_generate)

                # 测试in型“百分比”
                transmit_proportion(100)
                # 测试“测试后端生成”
                transmit_proportion(100,"测试后端生成")
                # 测试小数型“百分比”
                transmit_proportion(100.00)

            def open_100_close_back_multiple():
                #  开启100%  关闭反面;多个数据验证
                positive_and_negative = "正面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def open_100_open_back():
                #  k开启100%  开启反面;单个数据验证
                def transmit_proportion(proportion, test_name = None):
                    # proportion 百分比
                    # 标识这是一个“正面”
                    positive_and_negative = "反面"
                    # field_value    请求值，
                    # list_name 随机选中的“成分可选值的name” list类型
                    # “百分比”和“正/反面” 组成的list
                    field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative, proportion, test_name)
                    test_api_generate = False if test_name == None else True
                    # 把三个值 交给统一处理的方法  send_and_check_interface_data 把请求发出去，然后校验sql
                    send_and_check_interface_data(field_value, list_name, value_percent, test_api_generate)

                # 测试in型“百分比”
                transmit_proportion(100)
                # 测试“测试后端生成”
                transmit_proportion(100,"测试后端生成")
                # 测试小数型“百分比”
                transmit_proportion(100.00)

            def open_100_open_back_multiple():
                #  k开启100%  开启反面;多个数据验证
                positive_and_negative = "反面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def open_100_open_back_multiple_blend():
                #  k开启100%  开启反面;多个数据验证,正反面都存在
                positive_and_negative = "正面"
                proportion = 100
                positive_field_value, positive_list_name, positive_value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)

                positive_and_negative = "反面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(positive_field_value + ";"+ field_value,positive_list_name + list_name, positive_value_percent + value_percent)

            def close_100_close_back():
                #  关闭100%  关闭反面;单个数据验证
                positive_and_negative = "正面"
                proportion = random.randint(1,99)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

                positive_and_negative = "正面"
                proportion = random.randint(101,1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def close_100_close_back_multiple():
                #  关闭100%  关闭反面;多个数据验证
                positive_and_negative = "正面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def close_100_open_back():
                #  关闭100%  开启反面;单个数据验证
                positive_and_negative = "反面"
                proportion = random.randint(1,99)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

                positive_and_negative = "反面"
                proportion = random.randint(101,1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def close_100_open_back_multiple():
                #  关闭100%  开启反面;多个数据验证
                positive_and_negative = "反面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(field_value, list_name, value_percent)

            def close_100_open_back_multiple_blend():
                #  关闭100%  开启反面;多个数据验证,正反面都存在
                positive_and_negative = "正面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                positive_field_value, positive_list_name, positive_value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)

                positive_and_negative = "反面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_interface_data(positive_field_value + ";"+ field_value,positive_list_name + list_name, positive_value_percent + value_percent)

            def main():
                #  开启100%  关闭反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=True, group_num=2)

                #  开启100%  关闭反面;单个数据验证
                open_100_close_back()

                #  开启100%  关闭反面;多个数据验证
                open_100_close_back_multiple()

                #  开启100%  开启反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=True,group_num=1)

                #  开启100%  开启反面;单个数据验证
                open_100_open_back()

                #  开启100%  开启反面;多个数据验证
                open_100_open_back_multiple()

                #  开启100%  开启反面;多个数据验证,正反面都存在
                open_100_open_back_multiple_blend()

                #  关闭100%  关闭反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=False,group_num=2)

                #  关闭100%  关闭反面;单个数据验证
                close_100_close_back()

                #  关闭100%  关闭反面;多个数据验证
                close_100_close_back_multiple()

                #  关闭100%  开启反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=False,group_num=1)

                #  关闭100%  开启反面;单个数据验证
                close_100_open_back()

                #  关闭100%  开启反面;多个数据验证
                close_100_open_back_multiple()

                #  关闭100%  开启反面;多个数据验证,正反面都存在
                close_100_open_back_multiple_blend()

            main()

        def test_number():
            # 测试数字

            def return_request_field_data(test_data, api_field_name_list_list):
                # 获取excel最新的数据
                excel_dict = self.get_excel_dict()
                # 便利“接口文档中的字段名称” 依次以key：value的形式添加测试数据，到请求数据data中
                for count,field_values in enumerate(api_field_name_list_list):
                    excel_dict["data"][field_values] = test_data
                #  标识name和internalCode 这是一个测试text类型的面料，为了方便接下去的接口校验/单独类型校验
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_%s" %("number")
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_%s" %("number")
                return excel_dict

            def verification_db_data(test_data, fabric_id, db_field_name_list):
                # 提交的数据对比数据库数据
                sqlr = self.central_scheduler_single("sql.ids_12",fabric_id = fabric_id)
                assert sqlr[2]
                # 便利每个字段
                for key_list_value in db_field_name_list:
                    # 数据库中大多数都是保留两位
                    float_value = float(round(decimal.Decimal(test_data), 2))
                    # 数据库中字段 也准换为“小数”对比数据
                    sqlr_number_value = float(sqlr[0][0][key_list_value])
                    if key_list_value == "tax_rate":
                        # （tax_rate）税率需要特殊处理 数据库中只保留6位
                        assert sqlr_number_value == float(decimal.Context(prec = 6).create_decimal(str(test_data)))
                    else:
                        # 否则正常验证
                        assert float_value == sqlr_number_value

            def main():
                # 文本类型，至少需要3个数据：1，“数据库字段名”，2，“api文档接口字段名”，3，测试数据
                test_number_data = [0,1,1510,3.1415926,99999.666]

                necessary_data = self.return_type_corresponding_data(type = "number")
                key_list, api_field_name_list = necessary_data["key_list"], necessary_data["api_field_name_list"]

                for test_data in test_number_data:
                    excel_dict = return_request_field_data(test_data, api_field_name_list)
                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"]})
                    verification_db_data(test_data = test_data, fabric_id = fabric_id, db_field_name_list = key_list)

            main()

        def test_checkbox():
            # 测试多选
            def return_request_data(api_field_name_list, optional_value_list, list_type_key, test_api_generate):
                # checkbox_list_type_key（方便sel验证）与list一样，为了定位数据的数据，因为每个字段的type_key都不一样 库里的设计就是根据type_key 去定位数据，唯一不同的是，多选可以选择多个值，所以要对应起来方便后面直接取值checkbox_list_type_key
                # list_optional_values（方便sql验证）是一个list，里面的value是我上送的“列表可选值的name”，用来校验不同字段的“列表可选值name”，sql验证必要数据
                checkbox_list_type_key, list_optional_values = [], []

                excel_dict = self.get_excel_dict()

                # 拼接接口支持的符号英文","
                splice_symbo = random.choice([","])

                for count, field_values in enumerate(api_field_name_list):
                    # 便利所有“接口文档中的字段key”
                    if test_api_generate:
                        list_name = ["测试后端生成"]
                        type_key_list = [list_type_key[count]]
                        list_name_value_str = "测试后端生成"
                    else:
                        # 控制随机的最大值，随机取出“字段的选项值”中的数据，最终转成没有重复的值
                        list_random_num = list(set([random.randint(0, len(optional_value_list[count]) - 1) for _ in range(random.randint(2, len(optional_value_list[count]) - 1))]))
                        list_name = [optional_value_list[count][list_value]["name"] for list_value in list_random_num]
                        # 把type_key 也拿出来，后面sql定位数据要用
                        type_key_list = [list_type_key[count] for _ in list_name]
                        # 用逗号拼接随机出来的“可选值name”成字符串
                        list_name_value_str = functools.reduce(lambda x, y: x + splice_symbo + y, list_name)


                    # 参数中加入到请求的data中
                    excel_dict["data"][field_values] = list_name_value_str
                    # 一会肯定是要验证的 所以把“type_key”添加到列表
                    checkbox_list_type_key.append(type_key_list)
                    # 同理值也是要验证的
                    list_optional_values.append(list_name)

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_checkbo"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_checkbo"

                return excel_dict, checkbox_list_type_key, list_optional_values

            def verification_db_data(fabric_id, key_list, checkbox_list_type_key, list_optional_values ):
                # 提交的数据对比数据库数据

                # 执行sql
                sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                # 便利每一个字段
                for count_list,validation_list in enumerate(list_optional_values):
                    key_list_value=key_list[count_list]
                    # 数据库中的多选值字段都是这个样的：'care_instruction': '3,5,6,7,8,9,10,11,12,14'
                    # 所以要用“,”分割
                    list_split_id=sqlr[0][0][key_list_value].split(",")
                    supplier_id=sqlr[0][0]["supplier_id"]
                    # 把我提交时候的“可选值name”都便利一下
                    for count_value,validation_value in enumerate(validation_list):
                        # 此时定位多选值的name需要三个数据：
                        # list_split_id_value: cid(也可以叫“列表分割的id的值”)
                        # list_type_key_value： type_key（就是字段唯一的类型，定位数据的重要数据之一）
                        # supplier_id ：面料 供应商id  不做太多介绍
                        list_split_id_value,list_type_key_value = list_split_id[count_value], checkbox_list_type_key[count_list][count_value]
                        # 三个值，传给我们的sql 查出数据库中的“可选值name”，跟我提交的一不一样
                        sqlrs = self.central_scheduler_single("sql.ids_18", list_split_id_value = list_split_id_value, list_type_key_value = list_type_key_value, supplier_id = supplier_id)
                        assert sqlrs[0][0]["name"] == validation_value

            def main():
                # 类型至少需要：1，数据库字段数据；2，接口字段名称；3，“列表可选值”；4，“type_key”

                # 获取需要勾选的值  key_list，
                # 获取接口文档中的字段名称  api_field_name_list
                # 选项的字段的可选值   optional_value_list,
                #  list_type_key
                necessary_data = self.return_type_corresponding_data(type = "checkbox")
                key_list, api_field_name_list, optional_value_list, list_type_key = necessary_data["key_list"], necessary_data["api_field_name_list"], necessary_data["optional_value_list"], necessary_data["list_type_key"]

                test_frequency = 2
                for counts in range(test_frequency):
                    # 判断是否最后一次，最后一次就是验证“测试接口自动生成数据”
                    last, test_api_generate = test_frequency - 1, False
                    if counts == last:
                        test_api_generate = True

                    excel_dict, checkbox_list_type_key, list_optional_values = return_request_data(api_field_name_list, optional_value_list, list_type_key, test_api_generate)
                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    # 加入到配置文件方便以后的联动接口验证
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"]})

                    if test_api_generate:
                        # 因为最后清除“后端生成”数据时，“列表的可选值”要求不能有未删除的面料，使用该字段，所以需要把面料id也记录下来
                        self._add_config_list_data(node_large="config_fabric_test_back_end_generate", node = "delete_field_optional_value_relation_fabric_id" , add_value = [fabric_id])
                        # 需要删除的字段写入“待删除”列表，执行完成一并删除
                        self._add_config_list_data(node_large="config_fabric_test_back_end_generate",node="wait_delete_field_optional_value_list",add_value = list_type_key)

                    verification_db_data(fabric_id, key_list, checkbox_list_type_key, list_optional_values)

            main()

        def test_supplier():
            #  测试供应商

            def return_request_data(optional_value, api_field_name_list, test_api_generate):
                excel_dict = self.get_excel_dict()

                # 获取“供应商字段--字段详情列表”数据的name
                optional_value_name = optional_value["name"]

                # key：value的形式添加 【“供应商字段--字段详情列表”数据的name】到请求data中
                excel_dict["data"][api_field_name_list[0]] = optional_value_name
                # 如果到了最后一个数据，也就是“测试后端生成”，就拼接一下这个面料的id，用来防止多次调用该方法，因为到测试结束的时候才会调用接口,清除“测试后端生成”的所有数据，不清的话数据会越来越多
                if test_api_generate:
                    optional_value_name = optional_value["name"] + "_" + str(self.config["config_fabric"]["externalId"])
                    # key：value的形式添加 添加到请求data中
                    excel_dict["data"][api_field_name_list[0]] = optional_value_name

                #  标识name和internalCode 这是一个测试_supplier类型的面料
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_supplier"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_supplier"

                return excel_dict,optional_value_name

            def verification_db_data(fabric_id, optional_value_name):
                # 执行sql
                sqlr = self.central_scheduler_single("sql.ids_13", fabric_id = fabric_id, supplier_name = optional_value_name)
                # sql验证是否成功
                assert sqlr[2]

            def main():
                # 测试list类型至少需要：1，数据库字段数据；2，接口字段名称；3，“可选值”

                necessary_data = self.return_type_corresponding_data(type="supplier")
                key_list, api_field_name_list = necessary_data["key_list"], necessary_data["api_field_name_list"]

                #  供应商是特殊处理的，列表接口中没有可选值的数据，所以要获取“可选值”列表
                r = self.central_scheduler_single("Open_Platform_Service.ids_16", debug=False)
                optional_value_list = json.loads(r[0].text)["data"]["list"]["data"]

                #  添加一个让后端自动生成的数据
                optional_value_list.append({"name":"测试后端生成"})

                #  依次上送“供应商字段--字段详情列表”中的每一个值
                for optional_value in optional_value_list:
                    # 判断是否是最后一次，最后一次留给“测试后端生成”
                    test_api_generate = False

                    if optional_value == optional_value_list[-1]:
                        test_api_generate = True

                    # 获取
                    excel_dict, optional_value_name = return_request_data(optional_value, api_field_name_list, test_api_generate)

                    # 发出请求
                    r = self.central_scheduler_single(excel_dict)
                    # 校验请求是否成功
                    assert r[1]
                    # 获取响应回来的 fabric_id
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    # 添加请求数据到config_fabric_detailed_data_record 方便后续验证
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"]})

                    verification_db_data(fabric_id, optional_value_name)

            main()
            
        def test_datetime():
            # 测试上传时间

           # 至少需要：1，数据库字段数据；2，接口字段名称；3，“测试数据”
            necessary_data = self.return_type_corresponding_data(type = "datetime")
            key_list, api_field_name_list = necessary_data["key_list"], necessary_data["api_field_name_list"]

            # 获取当天时间
            current_time = time.strftime("%Y-%m-%d", time.localtime())
            # 测试数据
            test_datetime_data = [current_time, "1931-09-18", "2022-12-01"]
            for times in test_datetime_data:
                # 加进请求数据中
                excel_dict = self.get_excel_dict()

                excel_dict["data"][api_field_name_list[0]] = times
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_datetime"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_datetime"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                # 留存请求数据
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"]})
                # sql验证
                sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id)
                sqlr_launch_time = sqlr[0][0][key_list[0]]
                assert str(sqlr_launch_time) == times

        def test_abnormal():
            # 异常数据的测试，也就是“非1：1：1”的数据
            def send_scope_max_min(key_data,field_list,field_file,test_methods, mins, maxs):
                # 测试范围“最大值”和“最小值”字段range_scope,weight_scope  门幅范围&克重范围
                self.tick_field([key_data["key"]])

                for field_value in test_methods:
                    excel_dict = self.get_excel_dict()

                    excel_dict["data"][mins] = field_value[0]
                    excel_dict["data"][maxs] = field_value[1]
                    # 面料名称和internalCode 署名
                    check_field_name = "_" + key_data["key"]
                    excel_dict["data"]["name"] = excel_dict["data"]["name"] + check_field_name
                    excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + check_field_name

                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict["data"],"abnormal": True,"abnormal_verification_field": {mins : str(float(decimal.Context(prec=6).create_decimal(str(field_value[0])))), maxs : str(float(decimal.Context(prec=6).create_decimal(str(field_value[1]))))}})
                    return fabric_id

            def send_moq_and_moq_note(field_data,field_list,field_file,test_methods):
                # 测试 起订量 和 起订量备注 字段
                self.tick_field([field_data["key"]])

                for field_value in test_methods:

                    excel_dict = self.get_excel_dict()

                    excel_dict["data"]["moq"] = field_value[0]
                    excel_dict["data"]["moqNote"] = field_value[1]

                    # 面料名称和internalCode 署名
                    check_field_name = "_" + field_data["key"]
                    excel_dict["data"]["name"] = excel_dict["data"]["name"] + check_field_name
                    excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + check_field_name

                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]

                    node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {"moq" : str(field_value[0]), "moqNote" : str(field_value[1])}}
                    self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                    return fabric_id

            def send_number_and_unit(key_data, field_list, field_file, test_methods):
                # 统一处理数据，请求发出去

                # 勾选数据
                self.tick_field([key_data["key"]])

                def find_number_and_unit():
                    # 判断谁数据，谁是单位

                    # 单位：field_list_unit（列表数据），     field_api_unit（接口文档字段数据）
                    # 数量：“field_list_number”（数量列表数据），       “field_api_number”（接口文档字段数据）
                    field_list_unit, field_list_number, field_api_unit, field_api_number = None,None,None,None
                    for count, i in enumerate(field_list):
                        # 如果是data_type类型是list  那你就是“单位列表数据”
                        if i["data_type"] == "list":
                            field_list_unit = i
                        else:
                            field_list_number = i
                        # 如果接口文档字段名中带有“Unit”或“unit” 那就是“接口文档字段数据”
                        if "Unit" in field_file[count][0] or "unit" in field_file[count][0]:
                            field_api_unit = field_file[count][0]
                        else:
                            field_api_number = field_file[count][0]
                    return field_list_unit, field_list_number, field_api_unit, field_api_number

                def split_methods_return_number_and_unit(field_value):
                    #  如果字段中带有生成单位，则拆分单位，返回最终要校验的：field_verification_unit（单位）,field_verification_number（数量）
                    field_verification_unit = None
                    if isinstance(field_value,str) and field_value[-6:] == "测试后端生成":
                        field_verification_unit, field_verification_number = field_value[-6:], field_value[:-6]
                        self._add_config_list_data(node_large="config_fabric_test_back_end_generate",node="wait_delete_field_optional_value_list",add_value = [field_list_unit["type_key"]])
                        return field_verification_unit,field_verification_number
                    return field_verification_unit, field_value

                # 单位：field_list_unit（列表数据），     field_api_unit（接口文档字段数据）
                # 数量：“field_list_number”（列表数据），       “field_api_number”（接口文档字段数据）
                field_list_unit, field_list_number, field_api_unit, field_api_number = find_number_and_unit()
                # 读取单位的“列表可选字段”
                field_list_unit_initial= field_list_unit["initial"]

                for field_value in test_methods:
                    # 获取基础的请求数据
                    excel_dict = self.get_excel_dict()

                    # 有些字段数据本身就支持带单位，但是后面又传了一个单位，就存在两个单位，后端是只存储数据上带的单位，所以要处理成数据上的单位，不然一会sql查询出来不一致 会失败
                    field_verification_unit, field_verification_number = split_methods_return_number_and_unit(field_value)

                    # 随机取出一个单位的“可选单位”
                    randints = random.randint(0, len(field_list_unit_initial) - 1)
                    # 字段数据就加入请求data中
                    excel_dict["data"][field_api_number] = field_value
                    # 单位就是我随机的单位，name拿出来赋值过去
                    unit_name = field_list_unit_initial[randints]["name"]
                    excel_dict["data"][field_api_unit] = unit_name

                    # 面料名称和internalCode 署名
                    check_field_name = "_" + key_data["key"]
                    excel_dict["data"]["name"] = excel_dict["data"]["name"] + check_field_name
                    excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + check_field_name
                    # go
                    r = self.central_scheduler_single(excel_dict)
                    assert r[1]
                    fabric_id = json.loads(r[0].text)["data"]["id"]
                    # field_list_unit：单位的列表数据
                    # field_list_number：数量的列表数据
                    # field_api_unit： 单位的接口文档数据
                    # field_api_number：数量的 接口文档数据
                    # fabric_id：创建的面料id
                    # field_verification_unit：一会sql要校验的单位
                    # field_verification_number： 一会sql要校验的数量
                    # unit_name：正常随机出来的单位
                    # excel_dict：请求的数据，用作记录
                    return field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict

            def abnormal_main():
                # 获取映射数据/分类数据
                mapping_data_abnormal = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["abnormal"]
                classification_data_abnormal = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["abnormal"])

                # 把每个字段都便利一遍
                for abnormal_indexes in mapping_data_abnormal:
                    # key拿出来也就是配置中的：“data_type_corresponding_data = {'abnormal': [{'range': ['range', 'range_list', 'range_file']}, {'range_scope': ['range_scope', 'range_scope_list', 'range_scope_file']},...”
                    abnormal_indexes_key = list(abnormal_indexes.keys())[0]
                    if abnormal_indexes_key == "range":
                        #  门幅&&门幅单位	range  decimal（8位）	保留两位    支持带单位	四舍五入

                        # abnormal_data里的，映射数据
                        # field_data勾选数据：field_list列表字段数据：field_file接口文档数据
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [0, 1, 1510, "12", "12测试后端生成", "12.1001测试后端生成", "12.555测试后端生成"]
                        # 便利测试数据
                        for field_value in test_methods:
                            # field_list_unit：单位的列表数据
                            # field_list_number：数量的列表数据
                            # field_api_unit： 单位的接口文档数据
                            # field_api_number：数量的接口文档数据
                            
                            # fabric_id：创建的面料id
                            # field_verification_unit：一会sql要校验的单位(优先信任该数据)
                            # field_verification_number： 一会sql要校验的数量
                            # unit_name：正常随机出来的单位（否则信任该数据）
                            # excel_dict请求的数据，用作记录
                            field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict = send_number_and_unit(field_data, field_list, field_file, [field_value])

                            # sql执行查询出当前数量的值
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                            field_db_data = sqlr[0][0][field_list_number["key"]]
                            # “数据库存储的数量”与  “要校验的数量”，保留两位
                            assert field_db_data == round(decimal.Decimal(field_verification_number), 2)
                            # 获取字段在lt_fabrics 表中的名称，也就是接口字段中的“key”
                            key_list_value = field_list_unit["key"]
                            # 获取字段类型，用来查执行sql
                            list_type_key_value = field_list_unit["type_key"]
                            sqlr = self.central_scheduler_single("sql.ids_17", fabric_id = fabric_id, key_list_value = key_list_value, list_type_key_value = list_type_key_value)
                            # 判断当前应该信任 “正常的单位”还是 “数据中带的单位”，数据中没有带 则校验“正常的单位”数据
                            assert_unit = unit_name if field_verification_unit == None else field_verification_unit
                            # 留存数据
                            node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {field_api_number : str(round(decimal.Decimal(field_verification_number), 2)),field_api_unit : str(assert_unit)}}
                            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                            # 验证数据
                            assert sqlr[0][0]["name"] == assert_unit

                    elif abnormal_indexes_key == "range_scope":
                        #  门幅范围（最大，最小）	range_scope_min    range_scope_max    float（6位）    无单位	    四舍五入
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [(1, 1), (1, 2), (1, 99.99), (2, 1), (99.99, 1),(3.1415926, 99.987654321), (1, 999999.5)]
                        for field_value in test_methods:
                            mins, maxs ="rangeScopeMin", "rangeScopeMax"
                            fabric_id = send_scope_max_min(field_data, field_list, field_file, [field_value], mins, maxs)
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                            assert sqlr[0][0]["range_scope_min"] == float(decimal.Context(prec=6).create_decimal(str(field_value[0]))), sqlr[0][0]["range_scope_max"] == float(decimal.Context(prec=6).create_decimal(str(field_value[1])))

                    elif abnormal_indexes_key == "weight":
                        #  克重&&克重单位 	weight  字符串varchar（100位）    支持带单位
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [0, 1, 1510, "12", "12测试后端生成", "12.1001测试后端生成", "10000.1234123"]
                        for field_value in test_methods:
                            field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict = send_number_and_unit(field_data, field_list, field_file, [field_value])
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id, debug=False)
                            field_db_data = sqlr[0][0][field_list_number["key"]]
                            assert field_db_data == str(field_verification_number)
                            key_list_value = field_list_unit["key"]
                            list_type_key_value = field_list_unit["type_key"]
                            sqlr = self.central_scheduler_single("sql.ids_17", fabric_id=fabric_id,key_list_value=key_list_value,list_type_key_value=list_type_key_value)
                            assert_unit = unit_name if field_verification_unit == None else field_verification_unit

                            node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {field_api_number : str(field_verification_number),field_api_unit : str(assert_unit)}}
                            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                            assert sqlr[0][0]["name"] == assert_unit

                    elif abnormal_indexes_key == "weight_scope":
                        #  克重范围（最大，最小）	range_scope_min    range_scope_max    float（6位）    无单位	 四舍五入
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [(1, 1), (1, 2), (1, 99), (1, 99.99), (2, 1), (99.99, 1), (50, 70),(3.1415926, 99.987654321), (1, 999999.5)]
                        for field_value in test_methods:
                            mins, maxs ="weightScopeMin", "weightScopeMax"
                            fabric_id = send_scope_max_min(field_data, field_list, field_file, [field_value], mins, maxs)
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                            assert sqlr[0][0]["weight_scope_min"] == float(decimal.Context(prec=6).create_decimal(str(field_value[0]))), sqlr[0][0]["weight_scope_max"] == float(decimal.Context(prec=6).create_decimal(str(field_value[1])))

                    elif abnormal_indexes_key == "yard_weight":
                        #  码重&&码重单位	yard_weight    float（6位）    支持带单位	四舍五入
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [0, 1, 1510, "12", "12测试后端生成", "12.1001测试后端生成", "10000.1234123"]
                        for field_value in test_methods:
                            field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict = send_number_and_unit(field_data, field_list, field_file, [field_value])
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id, debug=False)
                            field_db_data = sqlr[0][0][field_list_number["key"]]
                            assert field_db_data  == float(decimal.Context(prec=6).create_decimal(str(field_verification_number)))
                            key_list_value = field_list_unit["key"]
                            list_type_key_value = field_list_unit["type_key"]
                            sqlr = self.central_scheduler_single("sql.ids_17", fabric_id=fabric_id,key_list_value=key_list_value,list_type_key_value=list_type_key_value)
                            assert_unit = unit_name if field_verification_unit == None else field_verification_unit

                            node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {field_api_number : str(float(decimal.Context(prec=6).create_decimal(str(field_verification_number)))), field_api_unit:str(assert_unit)}}
                            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                            assert sqlr[0][0]["name"] == assert_unit

                    elif abnormal_indexes_key == "price":
                        #  成本价格&&报价单位	price	decimal（10位）	保留两位    不支持单位	四舍五入
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [0, 1, 1510, "12", "12", "12.1001", "10000.1234123"]
                        for field_value in test_methods:
                            field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict = send_number_and_unit(field_data, field_list, field_file, [field_value])
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id, debug=False)
                            field_db_data = sqlr[0][0][field_list_number["key"]]
                            assert field_db_data == round(decimal.Decimal(field_verification_number), 2)
                            key_list_value = field_list_unit["key"]
                            list_type_key_value = field_list_unit["type_key"]
                            sqlr = self.central_scheduler_single("sql.ids_17", fabric_id=fabric_id,key_list_value=key_list_value,list_type_key_value=list_type_key_value)

                            node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {field_api_number : str(round(decimal.Decimal(field_verification_number), 2)), field_api_unit : str(unit_name)}}
                            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                            assert sqlr[0][0]["name"] == unit_name

                    elif abnormal_indexes_key == "stock":
                        #  库存&&库存单位	stock	int（11位）	    不支持单位
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [0, 1, 1510, 999999]
                        for field_value in test_methods:
                            field_list_unit, field_list_number, field_api_unit, field_api_number, fabric_id, field_verification_unit, field_verification_number, unit_name, excel_dict = send_number_and_unit(field_data, field_list, field_file, [field_value])
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id, debug=False)
                            field_db_data = sqlr[0][0][field_list_number["key"]]
                            assert field_db_data == int(field_verification_number)
                            key_list_value = field_list_unit["key"]
                            list_type_key_value = field_list_unit["type_key"]
                            sqlr = self.central_scheduler_single("sql.ids_17", fabric_id=fabric_id,key_list_value=key_list_value,list_type_key_value=list_type_key_value)

                            node_value = {"fabric_id": fabric_id, "request_data": excel_dict["data"], "abnormal": True, "abnormal_verification_field": {field_api_number : str(int(field_verification_number)),field_api_unit : str(unit_name)}}
                            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value = node_value)
                            assert sqlr[0][0]["name"] == unit_name

                    elif abnormal_indexes_key == "moq":
                        #  起订量&&起订量备注	moq	moq_note	int（11位）varchar（255位）	    不支持单位
                        field_data = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][0]]
                        field_list = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][1]]
                        field_file = classification_data_abnormal[abnormal_indexes[abnormal_indexes_key][2]]
                        test_methods = [(1, "起订量备注"),(99, "起订量备注2"),(1510, "起订量备注3"), (1, 1), (1, "起订量备注67890"*20),(100000, "起订量备注67890"*20)]
                        for field_value in test_methods:
                            fabric_id = send_moq_and_moq_note(field_data,field_list,field_file,[field_value])
                            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id = fabric_id)
                            assert sqlr[0][0]["moq"] == field_value[0], sqlr[0][0]["moq_note"] == str(field_value[1])

            abnormal_main()

        def main():
            test_text()
            test_list()
            test_multi_percent_main_component()
            test_number()
            test_checkbox()
            test_supplier()
            test_datetime()
            test_abnormal()


        main()

    def test_open_resource_v2_fabric_dynamic_parameter_value_None(self,clear_config_fabric_detailed_data_record,fixture_ergodic_parameter):
        """动态字段值为空测试"""

        def test_text():
            test_methods = [""]
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["text"]
            text_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["text"])
            #  key_list,api_field_name_list,optional_value_list=self.get_necessary_data(type_corresponding_indexes,text_data)
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, text_data)
            key_list,api_field_name_list=generate_data_type_list_data[0],generate_data_type_list_data[1]
            self.tick_field(key_list)

            for i in test_methods:
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    excel_dict["data"][field_values] = i

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_text"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_text"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})
                #  sqlr = self.central_scheduler_single("sql.ids_12",verification_skip={"verification_len": True,"verification_non_null": False,"verification_data": True},fabric_id = self.fabric_id,fabric_verification_value = str(i))
                #  assert sqlr[2]

        def test_type_supplier():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["supplier"]
            supplier_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["supplier"])
            #  key_list, api_field_name_list,optional_value_list = self.get_necessary_data(type_corresponding_indexes, supplier_data)
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, supplier_data)
            key_list,api_field_name_list = generate_data_type_list_data[0],generate_data_type_list_data[1]
            self.tick_field(key_list)

            def get_supplier_value_data():
                r = self.central_scheduler_single("Open_Platform_Service.ids_16",debug=False)
                list_value=json.loads(r[0].text)["data"]["list"]["data"]
                if len(list_value)<3:
                    for count in range(len(list_value)+1,4):
                        self.central_scheduler_single("Open_Platform_Service.ids_17", debug=False,count=str(count))
                r = self.central_scheduler_single("Open_Platform_Service.ids_16", debug=False)
                list_value = json.loads(r[0].text)["data"]["list"]["data"]
                return list_value

            get_supplier_value_data()
            lists = ["externalId", "name", "internalCode"]
            self._increasing_config_data("config_fabric", lists)
            self.config = self.read_or_modify_config_data(node_large=None)
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
            excel_dict["data"][api_field_name_list[0]] = ""
            excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_supplier"
            excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_supplier"
            r = self.central_scheduler_single(excel_dict)
            assert r[1]
            fabric_id = json.loads(r[0].text)["data"]["id"]
            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def test_list():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["list"]
            list_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["list"])
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, list_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0],generate_data_type_list_data[1],generate_data_type_list_data[2],generate_data_type_list_data[3]

            self.tick_field(key_list)
            for i in range(0,3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    optional_value_list_count_randints=""
                    list_type_key.append(type_list_data[count]["type_key"])
                    excel_dict["data"][field_values] = optional_value_list_count_randints
                    list_optional_values.append(optional_value_list_count_randints)

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_list"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_list"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})

        def test_multi_percent_main_component():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["multi_percent_main_component"]
            multi_percent_main_component_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["multi_percent_main_component"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, multi_percent_main_component_data)
            key_list, api_field_name_list,optional_value_list, type_list_data = generate_data_type_list_data[0],generate_data_type_list_data[1],generate_data_type_list_data[2],generate_data_type_list_data[3]
            self.tick_field(key_list)

            def send_and_check_Interface_data(field_value,optional_value_list_count_randints,value_percent):
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")

                excel_dict["data"][api_field_name_list[0]] = ""
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_component"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_component"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})

            def generate_request_data_and_verification_data_single(positive_and_negative,proportion):
                # 单面数据处理
                randints = random.randint(0, len(optional_value_list[0]) - 1)
                optional_value_list_count_randints=optional_value_list[0][randints]
                field_value= positive_and_negative + ":" + str(proportion) + "%" + optional_value_list_count_randints["name"]
                return field_value,[optional_value_list_count_randints["name"]],[[proportion,positive_and_negative]]

            def generate_request_data_and_verification_data_multiple(positive_and_negative,proportion):
                list_random_num=list(set([random.randint(0, len(optional_value_list[0]) - 1) for i in range(random.randint(2, len(optional_value_list[0]) - 1))]))
                list_name=[optional_value_list[0][i]["name"] for i in list_random_num]
                value,value_percent="",[]
                for i in list_name:
                    if i == list_name[-1]:
                        value=value + str(proportion - len(list_name) + 1)+ "%" + i
                        value_percent.append([proportion - len(list_name) + 1,positive_and_negative])
                        break
                    value = value + "1%" + i + ","
                    value_percent.append([1,positive_and_negative])

                field_value = positive_and_negative + ":" + value
                return field_value,list_name,value_percent

            #  开启100 % 开启反面
            #  关闭100 % 关闭反面
            def open_100_close_back():
                # k开启100%  关闭反面;单个数据验证
                positive_and_negative = "正面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def open_100_close_back_multiple():
                #  开启100%  关闭反面;多个数据验证
                positive_and_negative = "正面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def open_100_open_back():
                #  k开启100%  开启反面;单个数据验证
                positive_and_negative = "反面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def open_100_open_back_multiple():
                #  k开启100%  开启反面;多个数据验证
                positive_and_negative = "反面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def open_100_open_back_multiple_blend():
                #  k开启100%  开启反面;多个数据验证,正反面都存在
                positive_and_negative = "正面"
                proportion = 100
                positive_field_value, positive_list_name, positive_value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)

                positive_and_negative = "反面"
                proportion = 100
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(positive_field_value + ";"+ field_value,positive_list_name + list_name, positive_value_percent + value_percent)

            def close_100_close_back():
                #  关闭100%  关闭反面;单个数据验证
                positive_and_negative = "正面"
                proportion = random.randint(1,99)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

                positive_and_negative = "正面"
                proportion = random.randint(101,1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def close_100_close_back_multiple():
                #  关闭100%  关闭反面;多个数据验证
                positive_and_negative = "正面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def close_100_open_back():
                #  关闭100%  开启反面;单个数据验证
                positive_and_negative = "反面"
                proportion = random.randint(1,99)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

                positive_and_negative = "反面"
                proportion = random.randint(101,1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_single(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def close_100_open_back_multiple():
                #  关闭100%  开启反面;多个数据验证
                positive_and_negative = "反面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(field_value, list_name, value_percent)

            def close_100_open_back_multiple_blend():
                #  关闭100%  开启反面;多个数据验证,正反面都存在
                positive_and_negative = "正面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                positive_field_value, positive_list_name, positive_value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)

                positive_and_negative = "反面"
                proportion = random.randint(len(optional_value_list[0]),1000)
                field_value, list_name, value_percent = generate_request_data_and_verification_data_multiple(positive_and_negative,proportion)
                send_and_check_Interface_data(positive_field_value + ";"+ field_value,positive_list_name + list_name, positive_value_percent + value_percent)

            def component_main():
                #  开启100%  关闭反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=True,group_num=2)

                #  开启100%  关闭反面;单个数据验证
                open_100_close_back()

                #  开启100%  关闭反面;多个数据验证
                open_100_close_back_multiple()

                #  开启100%  开启反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=True,group_num=1)

                #  开启100%  开启反面;单个数据验证
                open_100_open_back()

                #  开启100%  开启反面;多个数据验证
                open_100_open_back_multiple()

                #  开启100%  开启反面;多个数据验证,正反面都存在
                open_100_open_back_multiple_blend()

                #  关闭100%  关闭反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=False,group_num=2)

                #  关闭100%  关闭反面;单个数据验证
                close_100_close_back()

                #  关闭100%  关闭反面;多个数据验证
                close_100_close_back_multiple()

                #  关闭100%  开启反面;
                self.central_scheduler_single("Open_Platform_Service.ids_18", percent_main_component_limit=False,group_num=1)

                #  关闭100%  开启反面;单个数据验证
                close_100_open_back()

                #  关闭100%  开启反面;多个数据验证
                close_100_open_back_multiple()

                #  关闭100%  开启反面;多个数据验证,正反面都存在
                close_100_open_back_multiple_blend()


            component_main()
            #  randints = random.randint(0, len(optional_value_list[0]) - 1)
            #  optional_value_list_count_randints=optional_value_list[0][randints]
            #  field_value="正面:" + "100%" + optional_value_list_count_randints["name"]+";反面:"
            #  excel_dict["data"][api_field_name_list[0]] = field_value
            #  excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_component"
            #  excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_component"
            #  r = self.central_scheduler_single(excel_dict)

        def test_checkbox():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["checkbox"]
            checkbox_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["checkbox"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, checkbox_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0], generate_data_type_list_data[1], generate_data_type_list_data[2], generate_data_type_list_data[3]
            self.tick_field(key_list)
            for i in range(0,3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    list_random_num = list(set([random.randint(0, len(optional_value_list[count]) - 1) for value in range(random.randint(2, len(optional_value_list[count]) - 1))]))
                    list_name = [optional_value_list[count][list_value]["name"] for list_value in list_random_num]
                    type_key_list=[type_list_data[count]["type_key"] for list_name_value in list_name]
                    list_name_value_str = ""
                    excel_dict["data"][field_values] = list_name_value_str
                    list_type_key.append(type_key_list)
                    list_optional_values.append(list_name)

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_checkbo"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_checkbo"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})

        def test_datetime():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["datetime"]
            datetime_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["datetime"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, datetime_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0], generate_data_type_list_data[1], generate_data_type_list_data[2], generate_data_type_list_data[3]
            self.tick_field(key_list)

            lists = ["externalId", "name", "internalCode"]
            self._increasing_config_data("config_fabric", lists)
            self.config = self.read_or_modify_config_data(node_large=None)
            excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")

            current_time=time.strftime("%Y-%m-%d", time.localtime())
            excel_dict["data"][api_field_name_list[0]]=""
            excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_datetime"
            excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_datetime"
            r = self.central_scheduler_single(excel_dict)
            assert r[1]
            fabric_id = json.loads(r[0].text)["data"]["id"]
            self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

            sqlr = self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id)
            sqlr_launch_time = sqlr[0][0][key_list[0]]
            assert str(sqlr_launch_time) == current_time

        def main():
            #  self.ergodic_parameter()
            test_text()
            test_type_supplier()
            test_list()
            test_multi_percent_main_component()
            test_checkbox()
            test_datetime()

        main()

    @pytest.mark.parametrize("free_combination_data", PytestFixture().return_list_config_fabric_dynamic_field_free_combination(), scope="module")
    def test_free_combination(self,free_combination_data):
        self.open_all_fields()
        self.central_scheduler_single("Open_Platform_Service.ids_18", debug=False, percent_main_component_limit=False,group_num=1)
        lists = ["externalId", "name", "internalCode"]
        self._increasing_config_data("config_fabric", lists)
        self.config = self.read_or_modify_config_data(node_large=None)
        excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
        excel_dict["data"] = dict(excel_dict["data"],**eval(free_combination_data))
        r = self.central_scheduler_single(excel_dict)
        assert r[1]

    def test_open_resource_v2_fabric_custom_parameter(self,clear_config_fabric_detailed_data_record,fixture_custom_ergodic_parameter):
        "自定义字段测试"
        def test_text():
            test_methods = ["text测试中文_", 12534567890, 3.1415926, "~!@#$%^&*()_+-=:;\"\'<>,.?/|\\"]
            test_methods = ["text测试中文_", "~!@#$%^&*()_+-=:;\"\'<>,.?/|\\","1234567890","lingdi","l1i2n3g4d5i"]
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="custom_data_type_corresponding_data"))["text"]
            text_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["custom_text"])
            #  key_list,api_field_name_list,optional_value_list=self.get_necessary_data(type_corresponding_indexes,text_data)
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, text_data)
            key_list,api_field_name_list=generate_data_type_list_data[0],generate_data_type_list_data[1]
            self.tick_field(key_list)

            for i in test_methods:
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    excel_dict["data"][field_values] = i

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_%s" %("custom_text")
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_%s" %("custom_text")
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def test_number():
            test_methods=[0,1,1510,3.1415926,99999.555]
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["number"]
            number_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["number"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, number_data)
            key_list, api_field_name_list = generate_data_type_list_data[0],generate_data_type_list_data[1]
            self.tick_field(key_list)

            for i in test_methods:
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    excel_dict["data"][field_values] = i

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_number"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_number"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def test_list():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["list"]
            list_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["list"])
            #  key_list, api_field_name_list,optional_value_list = self.get_necessary_data(type_corresponding_indexes, list_data)
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, list_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0],generate_data_type_list_data[1],generate_data_type_list_data[2],generate_data_type_list_data[3]

            self.tick_field(key_list)
            for i in range(0,len(key_list) + 3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    randints=random.randint(0, len(optional_value_list[count])-1)
                    optional_value_list_count_randints=optional_value_list[count][randints]
                    list_type_key.append(type_list_data[count]["type_key"])
                    excel_dict["data"][field_values] = optional_value_list_count_randints["name"]
                    list_optional_values.append(optional_value_list_count_randints["name"])

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_list"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_list"
                r = self.central_scheduler_single(excel_dict)
                #  time.sleep(5)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def test_checkbox():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["checkbox"]
            checkbox_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["checkbox"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, checkbox_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0], generate_data_type_list_data[1], generate_data_type_list_data[2], generate_data_type_list_data[3]
            self.tick_field(key_list)
            for i in range(0,len(key_list) + 3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    list_random_num = list(set([random.randint(0, len(optional_value_list[count]) - 1) for value in range(random.randint(2, len(optional_value_list[count]) - 1))]))
                    list_name = [optional_value_list[count][list_value]["name"] for list_value in list_random_num]
                    type_key_list=[type_list_data[count]["type_key"] for list_name_value in list_name]
                    list_name_value_str = functools.reduce(lambda x, y: x + "," + y, list_name)
                    excel_dict["data"][field_values] = list_name_value_str
                    list_type_key.append(type_key_list)
                    list_optional_values.append(list_name)
                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_checkbo"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_checkbo"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def main():
            #  self.ergodic_parameter(True)
            test_text()
            test_number()
            test_list()
            test_checkbox()

        main()

    def test_open_resource_v2_fabric_custom_parameter_value_None(self,clear_config_fabric_detailed_data_record,fixture_custom_ergodic_parameter):
        "自定义字段为空测试"

        def test_text():
            test_methods = [""]
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["text"]
            text_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["text"])
            #  key_list,api_field_name_list,optional_value_list=self.get_necessary_data(type_corresponding_indexes,text_data)
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, text_data)
            key_list,api_field_name_list=generate_data_type_list_data[0],generate_data_type_list_data[1]
            self.tick_field(key_list)

            for i in test_methods:
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    excel_dict["data"][field_values] = i

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_text"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_text"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})

        def test_list():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["list"]
            list_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["list"])
            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, list_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0],generate_data_type_list_data[1],generate_data_type_list_data[2],generate_data_type_list_data[3]

            self.tick_field(key_list)
            for i in range(0,3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    optional_value_list_count_randints=""
                    list_type_key.append(type_list_data[count]["type_key"])
                    excel_dict["data"][field_values] = optional_value_list_count_randints
                    list_optional_values.append(optional_value_list_count_randints)

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_list"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_list"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id, "request_data": excel_dict})

        def test_checkbox():
            type_corresponding_indexes = eval(self.read_or_modify_config_data(node_large="config_fabric", node="data_type_corresponding_data"))["checkbox"]
            checkbox_data = eval(self.read_or_modify_config_data(node_large=None)["config_fabric"]["checkbox"])

            generate_data_type_list_data = self.get_necessary_data(type_corresponding_indexes, checkbox_data)
            key_list, api_field_name_list, optional_value_list, type_list_data = generate_data_type_list_data[0], generate_data_type_list_data[1], generate_data_type_list_data[2], generate_data_type_list_data[3]
            self.tick_field(key_list)
            for i in range(0,3):
                list_type_key,list_optional_values=[],[]
                lists = ["externalId", "name", "internalCode"]
                self._increasing_config_data("config_fabric", lists)
                self.config = self.read_or_modify_config_data(node_large=None)
                excel_dict = self.get_excel_data_by_id("Open_Platform_Service.ids_8")
                for count,field_values in enumerate(api_field_name_list):
                    list_random_num = list(set([random.randint(0, len(optional_value_list[count]) - 1) for value in range(random.randint(2, len(optional_value_list[count]) - 1))]))
                    list_name = [optional_value_list[count][list_value]["name"] for list_value in list_random_num]
                    type_key_list=[type_list_data[count]["type_key"] for list_name_value in list_name]
                    list_name_value_str = ""
                    excel_dict["data"][field_values] = list_name_value_str
                    list_type_key.append(type_key_list)
                    list_optional_values.append(list_name)

                excel_dict["data"]["name"] = excel_dict["data"]["name"] + "_checkbo"
                excel_dict["data"]["internalCode"] = excel_dict["data"]["internalCode"] + "_checkbo"
                r = self.central_scheduler_single(excel_dict)
                assert r[1]
                fabric_id = json.loads(r[0].text)["data"]["id"]
                self._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record",node_value={"fabric_id": fabric_id,"request_data": excel_dict})

        def main():
            #  self.ergodic_parameter(True)
            test_text()
            test_list()
            test_checkbox()

        main()



class TestOpenResourceV2FabricFieldValue(PytestFixture):
    # open/resource/v2/fabric/{field}/{value}
    # 面料--精确搜索

    def test_open_resource_v2_fabric_field_value(self):
        pass


class TestOpenResourceV2FabricList(PytestFixture):
    #  /open/resource/v2/fabric
    #  面料--列表

    def test_open_resource_v2_fabric_list(self):
        r = self.central_scheduler_single("Open_Platform_Service.ids_20", id = "")
        self.info(json.loads(r[0].text))
        response_data_list_data = json.loads(r[0].text)["data"]["list"]["data"]

        for i in response_data_list_data:
            self.info(i)


class TestOpenResourceV2FabricId(PytestFixture):
    #  /open/resource/v2/fabric/{id}
    #  面料--查看


    def verification_request_and_response(self,request,response):
        for request_key in request.keys():
            self.debugs = True
            self.info(("请求/响应数据：",request,response))
            self.info(("校验字段：",request_key))
            self.info(("结果：",request[request_key],response[request_key]))

            if request_key=="constituentString":
                # 成分字段特殊处理
                request_value = str(request[request_key]).replace("正面:", "").replace("反面:", "").replace(";", "").replace("；","").replace(" ", "")
                response_value = str(response[request_key]).replace("正面:", "").replace("反面:", "").replace(";", "").replace("；","").replace(" ", "")
                assert request_value == response_value

            elif (request_key == "gauge" or request_key == "retailPrice" or request_key == "wastageRate" )and isinstance(request[request_key],float):
                request_value = float(round(float(request[request_key]), 2))
                assert str(request_value) == str(response[request_key])

            elif (request_key == "taxRate" ) and isinstance(request[request_key],float):
                request_value = float(decimal.Context(prec=6).create_decimal(str(request[request_key])))
                assert str(request_value) == str(response[request_key])

            else:
                assert str(request[request_key]) == str(response[request_key])

    def verification_abnormal_request_and_response(self,request,response):
        for request_key in request.keys():
            self.debugs = True
            self.info(("请求/响应数据：",request,response))
            self.info(("校验字段：",request_key))
            self.info(("结果：",request[request_key],response[request_key]))

            if request_key == "rangeString" or request_key == "rangeScopeMin" or request_key == "rangeScopeMax" or request_key == "weightScopeMin" or request_key == "weightScopeMax" or request_key == "yardWeightString" or request_key == "price" :
                request_value = float(request[request_key])
                assert request_value == float(response[request_key])

            else:
                assert str(request[request_key]) == str(response[request_key])

    def test_open_resource_v2_fabric_id(self):
        # 详情所有字段校验# 开启所有字段# 关闭100%  开启反面;
        self.open_all_fields()
        self.central_scheduler_single("Open_Platform_Service.ids_18", debug=False, percent_main_component_limit=False, group_num=1)
        config_fabric_detailed_data_record = self.read_or_modify_config_data()["config_fabric_detailed_data_record"]

        def _judge_abnormal(config_fabric_detailed_data_record_node):
            try:
                return config_fabric_detailed_data_record_node["abnormal"]
            except BaseException:
                return False

        for i in config_fabric_detailed_data_record.keys():
            config_fabric_detailed_data_record_node = eval(config_fabric_detailed_data_record[i])
            fabric_id = config_fabric_detailed_data_record_node["fabric_id"]
            r = self.central_scheduler_single("Open_Platform_Service.ids_20", debug = False, id = fabric_id)
            response_data_detail = json.loads(r[0].text)["data"]["detail"]
            request_data = config_fabric_detailed_data_record_node["request_data"]
            self.central_scheduler_single("sql.ids_12", fabric_id=fabric_id)
            if _judge_abnormal(config_fabric_detailed_data_record_node):
                new_dict = dict(config_fabric_detailed_data_record_node["request_data"],**config_fabric_detailed_data_record_node["abnormal_verification_field"])
                self.verification_abnormal_request_and_response(request = new_dict, response = response_data_detail)
            else:
                self.verification_request_and_response(request = request_data,response = response_data_detail)

    @pytest.mark.parametrize("abnormal_value", [
                                                {"fabric_id":cores.Core().read_or_modify_config_data()["config_fabric_other_user_fabric_id"] ["other_user_fabric_id"],"message": "面料不存在", "error_code": 404},
                                                {"fabric_id": cores.Core().read_or_modify_config_data()["config_fabric_other_user_fabric_id"] ["delete_fabric_id"], "message": "面料不存在", "error_code": 404},
                                                {"fabric_id": "1546498749614536498749849456", "message": "面料不存在", "error_code": 404},
                                                {"fabric_id": "0", "message": "面料不存在", "error_code": 404},
                                                ])
    def test_open_resource_v2_fabric_id_abnormal(self,abnormal_value):
        self.open_all_fields()
        self.central_scheduler_single("Open_Platform_Service.ids_18", debug=False, percent_main_component_limit=False, group_num=1)
        fabric_id = abnormal_value["fabric_id"]
        r = self.central_scheduler_single("Open_Platform_Service.ids_20", id = fabric_id)
        assert  abnormal_value["message"] == json.loads(r[0].text)["message"],abnormal_value["error_code"] == json.loads(r[0].text)["error_code"]



if __name__ == '__main__':
    #  pytest.main(["-vs","test_Open_Platform_Service.py::TestOpenResourceV2FabricId::test_open_resource_v2_fabric_id","--alluredir", "allure_json"])
    #  pytest.main(["-vs", "test_Open_Platform_Service.py::TestOpenResourceV2Fabric::test_free_combination","--alluredir", "allure_json"])
    #  pytest.main(["-vs", "test_Open_Platform_Service.py::TestOpenPlatformServiceRegister", "--alluredir", "allure_json"])
    #  os.system("allure generate allure_json -o allure_html --clean")

    #  pytest.main(["-vs", "test_Open_Platform_Service.py::TestResourceV2Fabric::test_open_resource_v2_fabric_dynamic_parameter"])
    #  pytest.main(["-vs","test_Open_Platform_Service.py::TestResourceV2Fabric::test_test_open_resource_v2_fabric_dynamic_parameter"])
    #  pytest.main(["-vs", "./test_open_platform_service.py::TestOpenAuthBind::test_open_auth_bind"])

    #  pytest.main(["-vs","test_Open_Platform_Service.py::test_open_resource_v2_fabric_dynamic_parameter","--alluredir=test"])
    pytest.main(["-vs", "test_Open_Platform_Service.py::TestOpenResourceV2Fabric2::test_open_resource_v2_fabric_dynamic_parameter","--alluredir", "allure_json"])
    #  os.system("allure generate allure_json -o allure_html --clean")
