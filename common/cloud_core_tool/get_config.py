import openpyxl, configparser, pymysql, urllib, requests, json, os, re, sys


class MyParser(configparser.RawConfigParser):
    "Inherit from built-in class: ConfigParser"
    def optionxform(self,optionstr):
        "Rewrite without lower()"
        return optionstr


class HandlerConfig():
    node_data_num=1


    def get_config_address(self):
        try:
            address = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))) +"\\config\\" + self.read_or_modify_config_data(address=os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))) + r"\config\config.ini",node_large="config_basics")["config_path"]
        except BaseException:
            config_ini = "config.ini"
            config_ini_path = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))) + "\\config\\"
            config_ini_config_path = self.read_or_modify_config_data(address = config_ini_path + config_ini )["config_basics"]["config_path"]
            address = config_ini_path + config_ini_config_path
        # print(__file__)
        # print(os.path.realpath(__file__))
        # print(os.path.dirname(os.path.realpath(__file__)))
        # print(os.path.split(os.path.realpath(__file__))[0])
        # print(os.path.abspath(__file__))
        return address

    def read_or_modify_config_data(self, address=None, node_large=None, node=None, value=None):
        "read_or_modify_config_data"
        # 读取或写入，address配置文件地址，node_large大节点名称[config_mysql],node小节点名称host
        # value写入的值,不为None则为时读取
        address = self.get_config_address() if address == None else address
        config = MyParser()
        config.read(address, encoding="utf-8")

        def reads(node_large):
            if node_large == None:
                all_dict = {}
                for i in config.sections():
                    all_dict[i] = reads(i)
                return all_dict

            return dict(config.items(node_large)) if node == None and value == None else config.get(node_large, node)

        def into():
            config.set(node_large, node, value)
            config.write(open(address, "w", encoding="utf-8"))
            return True

        return reads(node_large) if value == None else into()

    def delete_config_data(self, address=None, node_large=None, node=None):
        address = self.get_config_address() if address == None else address
        config = MyParser()
        config.read(address, encoding="utf-8")
        config.remove_option(node_large,node)
        config.write(open(address, "w", encoding="utf-8"))

    def _increasing_config_data(self, node_large, lists):
        # 自增_increasing_config_data
        original_result = [lists, ]
        result = []
        for i in lists:
            config_value = self.read_or_modify_config_data(node_large=node_large, node=i)
            if "_" in config_value:
                split_value = config_value.split("_")
                split_value[-1] = str(int(split_value[-1]) + 1)
                values = "_".join(split_value)
                self.read_or_modify_config_data(node_large=node_large, node=i, value=str(values))
                result.append(values)
            else:
                try:
                    values = int(config_value) + 1
                    self.read_or_modify_config_data(node_large=node_large, node=i, value=str(values))
                    result.append(values)
                except BaseException:
                    if "@" in config_value:
                        split_value = config_value.split("@")
                        split_value[0] = str(int(split_value[0]) + 1)
                        values = "@".join(split_value)
                        self.read_or_modify_config_data(node_large=node_large, node=i, value=str(values))
                        result.append(values)
            self.read_or_modify_config_data(node_large=node_large, node="old_" + i, value=str(config_value))
        original_result.append(result)
        return True

    def record_current_request_datas(self,**kwargs):
        for key in kwargs.keys():
            old=self.read_or_modify_config_data(node_large="config_current_request", node=key)
            self.read_or_modify_config_data(node_large="config_current_request", node="old_" + key, value=str(old))
            self.read_or_modify_config_data(node_large="config_current_request", node=key, value=kwargs[key])

    def _eliminate_config_node_data(self,node_large):
        node_large_data=self.read_or_modify_config_data(node_large=node_large)
        for i in node_large_data.keys():
            self.delete_config_data(node_large = node_large,node = i)

    def _info_config_sequence_node_data(self, node_large, node_value):

        node_large_data = self.read_or_modify_config_data(node_large=node_large)
        def not_null():
            node_key_list = list(node_large_data.keys())
            node_key_list.sort()
            node_key_value_split_list=node_key_list[-1].split("_")
            node_key_value_split_list[-1] = str(int(node_key_value_split_list[-1]) + 1)
            join_node = "_".join(node_key_value_split_list)
            self.read_or_modify_config_data(node_large = node_large, node = join_node, value = node_value)

        def not_null_num():
            self.read_or_modify_config_data(node_large=node_large, node="node_data_" + str(self.node_data_num), value=node_value)
            self.node_data_num = self.node_data_num + 1
        def _null():
            self.read_or_modify_config_data(node_large = node_large, node = "node_data_1", value = node_value)
            self.node_data_num = self.node_data_num + 1

        not_null_num() if node_large_data != {} else _null()

    def _add_config_list_data(self, node_large, node, add_value):
        node_list_data = eval(self.read_or_modify_config_data()[node_large][node])
        node_list_data = node_list_data + add_value
        self.read_or_modify_config_data(node_large = node_large, node = node, value = str(node_list_data))






if __name__ == '__main__':
    HandlerConfig()._info_config_sequence_node_data(node_large="config_fabric_detailed_data_record", node_value="123456")
