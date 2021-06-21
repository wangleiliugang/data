import re


# 源格式：
strSrc = 'i=d%0A&from=AUTO&to=AUTO&smartresult=dict'
# 目标格式：
#       i:d%0A
#       from:AUTO
#       to:AUTO
#       smartresult:dict

strItems = re.findall('(?<=&)[\w\%=]+|[\w\%=]+(?=&)', strSrc)
print(strItems)
# ['i=d%0A', 'from=AUTO', 'to=AUTO', 'smartresult=dict']

for strItem in strItems:
    strOut = re.sub('=', ':', strItem)
    print(strOut)
