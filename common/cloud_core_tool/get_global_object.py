import requests, json, hashlib, pytest, unittest
# import common.cloud_core as cores


class HandlerGlobalDict():
    __obj=None
    global_dict={}
    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def handler_dict(self,dict_key=None,dict_value=None):
        if dict_key == None and dict_value == None:
            return self.global_dict
        else:
            self.global_dict[dict_key]=dict_value
            return True

class HandlerGlobalObject():
    def handler_global(self, dict_key=None, dict_value=None):
        handler_global_dict=HandlerGlobalDict()
        return handler_global_dict.handler_dict(dict_key=dict_key,dict_value=dict_value)



