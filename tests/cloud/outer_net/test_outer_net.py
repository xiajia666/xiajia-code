import allure,pytest,requests,socket,json
import common.cloud_core as cores

@allure.feature("TEST_判断")
class TestText(cores.Core):
    """test_a测试"""
    def test_conclude_ip_whether_china(self):
        r=self.central_scheduler_single(excel_id="outer_net.ids_1")
        print(json.loads(r[0].text))
        ips=json.loads(r[0].text)["origin"]
        r=self.central_scheduler_single(excel_id="outer_net.ids_2",ips=ips)
        print(json.loads(r[0].text))
        country=json.loads(r[0].text)["country"]
        if country == "China":
            return False
        else:
            return True

if __name__ == '__main__':
    pytest.main(["-vs", "test_outer_net.py::TestText::test_1"])