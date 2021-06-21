# -*- coding: utf-8 -*-

# 演示JSON格式数据的编解码
import json


# 1.json encode(dict --> json str)
jsonDict = {'One': '1', 'Two': '2'}
jsonDumps = json.dumps(jsonDict)
print(type(jsonDumps))
print(jsonDumps)


# 2.json decode(json str --> dict)
jsonLoads = json.loads(jsonDumps)
print(type(jsonLoads))
for key, value in jsonLoads.items():
    print(key, value)


# {
#     "translateResult": [
#         [
#             {
#                 "tgt": "你好",
#                 "src": "hello"
#             }
#         ]
#     ],
#     "errorCode": 0,
#     "type": "en2zh-CHS",
#     "smartResult": {
#         "entries": [
#             "",
#             "int. 喂；哈罗，你好，您好（表示问候， 惊奇或唤起注意时的用语）\r\n",
#             "n. （Hello）（法）埃洛（人名）\r\n"
#         ],
#         "type": 1
#     }
# }
