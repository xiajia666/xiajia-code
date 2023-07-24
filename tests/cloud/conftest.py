import sys,os
sys.path.append("../../../../cloud")
print(os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../all"))))
print(os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../all"))))
import common.cloud_core as cores
import json

class GlobalSetup(cores.Core):
    def global_setup_login(self):
        self.config = self.read_or_modify_config_data(node_large=None)
        self.cookies,self.token=self.return_token(self.config["config_basics"]["user"],self.config["config_basics"]["password"])

    def global_setup_api_login(self):
        r = self.central_scheduler_single("Open_Platform_Service.ids_4",debug=False)
        self.api_token = json.loads(r[0].text)["data"]["token"]
        self.handler_global("api_token", "Bearer " + self.api_token)

    # def log_level(self):
    #     self.change_log_level(file_level="debug", console_level="debug")


#
# global_setup=GlobalSetup()
# global_setup.global_setup_login()
# global_setup.global_setup_api_login()
# GlobalSetup().log_level()