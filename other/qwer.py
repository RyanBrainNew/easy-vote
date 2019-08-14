import requests
import json
import time
import re

url2 = 'http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3' #请求接口
req = requests.get(url2)#发送请求
print(req.text)#获取请求，得到的是json格式
#print(req.json())#获取请求，得到的是字典格式