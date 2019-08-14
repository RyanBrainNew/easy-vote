from urllib import request
import requests
import json,time,re


all_url = []  # 存储IP地址的容器
# 代理IP的网址
url = "http://www.89ip.cn/tqdl.html?api=1&num=30&port=&address=&isp="
r = requests.get(url=url)
all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
with open("D:\\PCode\\IP.txt", 'w') as f:
    for i in all_url:
        f.write(i)
        f.write('\n')

