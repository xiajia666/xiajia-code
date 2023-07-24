import openpyxl, configparser, pymysql, urllib, requests, json, os, re


class HandlerRequests():
    def send_get_request(self, excel_dict):
        if excel_dict["url"][:4] == "https":
            r = self.requests_session.put(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"], verify=True)
        else:
            r = self.requests_session.get(url=excel_dict["url"], params=excel_dict["data"], headers=excel_dict["headers"])
        r.encoding = 'UTF-8'
        return r

    def send_post_request(self, excel_dict):
        if excel_dict["url"][:4] == "https":
            r = self.requests_session.post(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"], verify=True)
        else:
            r = self.requests_session.post(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"])
        r.encoding = 'UTF-8'
        return r

    def send_put_request(self,excel_dict):
        if excel_dict["url"][:4] == "https":
            r = self.requests_session.put(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"], verify=True)
        else:
            r = self.requests_session.put(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"])
        r.encoding = 'UTF-8'
        return r

    def send_patch_request(self,excel_dict):
        if excel_dict["url"][:4] == "https":
            r = self.requests_session.patch(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"], verify=True)
        else:
            r = self.requests_session.patch(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"])
        r.encoding = 'UTF-8'
        return r

    def send_delete_request(self,excel_dict):
        if excel_dict["url"][:4] == "https":
            r = self.requests_session.delete(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"], verify=True)
        else:
            r = self.requests_session.delete(url=excel_dict["url"], data=json.dumps(excel_dict["data"]),headers=excel_dict["headers"])
        r.encoding = 'UTF-8'
        return r

    def request(self, excel_dict, cookies_session=None):
        self.requests_session = requests.session()
        if cookies_session != None:
            self.requests_session.cookies = cookies_session

        def handles_request():

            self.record_current_request_datas(current_request_url=excel_dict['url'],current_request_data=excel_dict['data'],current_request_headers=excel_dict['headers'])

            if excel_dict['type'] == 'get' or excel_dict['type'] == 'GET':
                return self.send_get_request(excel_dict)

            if excel_dict['type'] == 'POST' or excel_dict['type'] == 'post':
                return self.send_post_request(excel_dict)

            if excel_dict['type'] == 'PUT' or excel_dict['type'] == 'put':
                return self.send_put_request(excel_dict)

            if excel_dict['type'] == 'PATCH' or excel_dict['type'] == 'patch':
                return self.send_patch_request(excel_dict)

            if excel_dict['type'] == 'DELETE' or excel_dict['type'] == 'delete':
                return self.send_delete_request(excel_dict)

        return handles_request()
