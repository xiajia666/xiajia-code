import requests,json,hashlib,pytest
import automation.all.common.cloud_core as cores
import allure

class Test_start(cores.Core):
    def test_mains(self):
        self.config = self.read_or_modify_config_data(node_large=None)


def main():
    pytest.main(["-vs","./open_platform_service/test_open_platform_service.py::TestText"])


if __name__ == '__main__':
    pytest.main(["-vs","./open_platform_service/test_open_platform_service.py::TestOpenPlatformServiceRegister::test_open_auth_register",
                 "./open_platform_service/test_open_platform_service.py::TestOpenPlatformServiceRegister::test_open_auth_register_value_None",
                 "./open_platform_service/test_open_platform_service.py::TestOpenPlatformServiceRegister::test_open_auth_register_test_abnormal",
                 "./open_platform_service/test_open_platform_service.py::TestOpenPlatformServiceRegister::test_open_auth_register_test_abnormal_None"
                 ])