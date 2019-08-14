import requests
import json
import time
import re
import random
# 请求头信息

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI',
}

# post表单网址
url1 = "http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3"
params = {
'OptionSearchTopicID': 2890797,
'OptionSearchKeyword': 90,
'from': 'timeline',
'Topic_2890797_Page': 3
}
#get验证
url2 = 'http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3' #请求接口


# 获取代理IP
def proxy_ip():
    FILE = 'D:\\ptest\\IP.txt'  
    ip_list = []
    with open(FILE, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            ip_list.append(line.strip())
    ip_port = random.choice(ip_list)
    return ip_port

def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址
    url = "http://www.89ip.cn/tqdl.html?api=1&num=30&port=&address=&isp="
    r = requests.get(url=url)
    all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
    with open("D:\\ptest\\IP.txt", 'w') as f:
        for i in all_url:
            f.write(i)
            f.write('\n')
    return all_url

# 计数器
count = 0
while count < 2:
    proxies = {"http": proxy_ip()}
    try:
        #req = requests.get(url2)#发送请求
        #print(req.text)#获取请求，得到的是json格式
        r = requests.post(url=url1, data=params, headers=headers, proxies=proxies, timeout=10)
        if(r.json()['flag'] == True):
            count += 1
            print("成功投票%d次！" % (count))
        print(r.json())
    except Exception as reason:
        print("错误原因是：", reason)