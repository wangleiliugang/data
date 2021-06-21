# -*- coding: utf-8 -*-


import json


strJson = '{"translateResult": [[{"tgt": "你好",	"src": "hello"}]]}'
jsonLoads = json.loads(strJson)
# print(type(jsonLoads))
print(jsonLoads["translateResult"][0][0]["tgt"])
