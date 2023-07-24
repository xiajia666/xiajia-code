import configparser, pymysql
from common.cloud_core_tool import get_config
import common.logs as logs

class HandlerDatabase():

    def handler_sql(self, sql, sections="config_mysql"):
        # 输入一个sql，执行后返回
        def read_ini():
            Import = configparser.ConfigParser()
            Import.read(get_config.HandlerConfig().get_config_address(), encoding="utf-8")
            return dict(Import.items(sections))

        def modify(sql):
            connect = pymysql.connect(host=self.connect_ini["host"], user=self.connect_ini["user"],
                                      password=self.connect_ini["password"], db=self.connect_ini["db"],
                                      port=int(self.connect_ini["port"]), charset=self.connect_ini["charset"])
            cursor = connect.cursor()
            cursor.execute(sql)
            # Result = library_cursor.fetchall()
            connect.commit()
            connect.close()
            cursor.close()
            return "成功"

        def query(sql):
            connect = pymysql.connect(host=self.connect_ini["host"], user=self.connect_ini["user"],
                                      password=self.connect_ini["password"], db=self.connect_ini["db"],
                                      port=int(self.connect_ini["port"]), charset=self.connect_ini["charset"])
            cursor = connect.cursor()
            cursor.execute(sql)
            column = cursor.description
            list = []
            while True:
                result = cursor.fetchone()
                if result == None:
                    break
                else:
                    column_name = {}
                    for count, name in enumerate(column):
                        column_name[name[0]] = result[count]
                    list.append(column_name)
            connect.close()
            cursor.close()
            return list

        def execute_sql(sql):
            self.connect_ini = read_ini()
            if "SELECT" in sql  or "select" in sql:
                try:
                    logs.Log().info(("执行sql", sql))
                except BaseException:
                    pass
                sqlr = query(sql)
                try:
                    logs.Log().info(("sql查询结果", sqlr))
                except BaseException:
                    pass
                return sqlr
            else:
                return modify(sql)

        # sql="SELECT * FROM lt_open_users WHERE user_id=(SELECT id FROM lt_users WHERE `name`='%s');" % (self.config["config_bind"]["register_user"])
        return execute_sql(sql)

    def sql_data_verification(self, sqlr, verification_dict, all_verification_result=True):
        """处理sql执行后的期望"""
        # self.info(("数据库表数据",verification_dict))
        verification_dict_result = {"verification_len": None,
                                    "verification_non_null": [None],
                                    "verification_data": [None]}
        all_result = True
        if isinstance(verification_dict["verification_data"],str) and verification_dict["verification_data"] != None:
            verification_dict["verification_data"]=eval(verification_dict["verification_data"])

        if verification_dict["verification_len"] != '' and verification_dict["verification_len"] != None:
            verification_len_result = len(sqlr) == verification_dict["verification_len"]
            len_result_verification = verification_len_result == all_verification_result

            if len_result_verification == False:
                all_result = False
            verification_dict_result["verification_len"] = len_result_verification

        verification_dict_list = []
        for sqlr_dict in [sqlr[0]]:
            non_null_result_list = []
            if verification_dict["verification_non_null"] != [] and verification_dict["verification_non_null"] != None:
                for non_null_value in verification_dict["verification_non_null"]:
                    non_null_result = sqlr_dict[non_null_value] != None and sqlr_dict[non_null_value] != ''
                    non_null_result_result_verification = non_null_result == all_verification_result
                    if non_null_result_result_verification == False:
                        all_result = False
                    non_null_result_list.append(non_null_result_result_verification)
                verification_dict_result["verification_non_null"] = non_null_result_list

            verification_data_result_list = []
            if verification_dict["verification_data"] != [] and verification_dict["verification_data"] != None:
                for verification_dict_value in verification_dict["verification_data"]:
                    verification_dict_value_result = verification_dict_value == all_verification_result
                    if verification_dict_value_result == False:
                        all_result = False
                    verification_data_result_list.append(verification_dict_value_result)
                verification_dict_result["verification_data"] = verification_data_result_list
            verification_dict_list.append(verification_dict_result)

        # self.info(("表数据对比dict结果，结果", verification_dict_list, all_result))
        return verification_dict_list, all_result

    def handler_sql_pre(self,excel_dict):
        if excel_dict['pre'] != None:
            for pre_list_value in excel_dict["pre"]:
                try:
                    eval(pre_list_value)
                except BaseException:
                    exec(pre_list_value)
            for eval_value in ["sql"]:
                try:
                    self.excel_dict[eval_value]=eval(excel_dict[eval_value])
                except BaseException:
                    pass

    def handler_excel_sql(self,excel_dict,all_verification_result,verification_skip):
        self.excel_dict=excel_dict
        self.handler_sql_pre(self.excel_dict)
        self.sqlr=self.handler_sql(self.excel_dict["sql"])
        # logs.Log().info(("sql执行结果", self.sqlr))
        verification_dict = {"verification_len": self.excel_dict["verification_len"],"verification_non_null": self.excel_dict["verification_non_null"],"verification_data": self.excel_dict["verification_data"]}
        for vs in verification_skip.keys():
            if verification_skip[vs] == False:
                verification_dict[vs] = None

        sql_data_verifications=self.sql_data_verification(self.sqlr, verification_dict, all_verification_result)
        logs.Log().info((self.sqlr,sql_data_verifications[0],sql_data_verifications[1]))
        return self.sqlr,sql_data_verifications[0],sql_data_verifications[1]

class OperationMysql(object):
    def establish_connection(self, sections="config_mysql"):
        def read_ini():
            Import = configparser.ConfigParser()
            Import.read(get_config.HandlerConfig().get_config_address(), encoding="utf-8")
            return dict(Import.items(sections))

        self.connect_ini = read_ini()

        self.connect = pymysql.connect(host=self.connect_ini["host"], user=self.connect_ini["user"],
                                       password=self.connect_ini["password"], db=self.connect_ini["db"],
                                       port=int(self.connect_ini["port"]), charset=self.connect_ini["charset"])
        self.cursor = self.connect.cursor()

    def execute_sql(self, sql):
        def modify(sql):
            self.cursor.execute(sql)
            self.connect.commit()
            return True

        def query(sql):
            self.cursor.execute(sql)
            column = self.cursor.description
            list = []
            while True:
                result = self.cursor.fetchone()
                if result == None:
                    break
                else:
                    column_name = {}
                    for count, name in enumerate(column):
                        column_name[name[0]] = result[count]
                    list.append(column_name)

            return list

        def execute_sql(sql):
            select = sql[:6]
            if select == "SELECT" or select == "select":
                sqlr = query(sql)
                return sqlr
            else:
                return modify(sql)

        return execute_sql(sql)

    def close_mysql(self):
        self.connect.close()
        self.cursor.close()

if __name__ == '__main__':
    sql = 'SELECT id FROM lt_users WHERE `name`="admin05";'