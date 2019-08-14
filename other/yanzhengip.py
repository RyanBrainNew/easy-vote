import requests
import random

#FILE = 'D:\\ptest\\IP.txt'  # 读取的txt文件路径
'''
# 获取代理IP
def proxy_ip():
ip_list = []
with open(FILE, 'r') as f:
while True:
line = f.readline()
if not line:
break
ip_list.append(line.strip())
ip_port = random.choice(ip_list)
#ip_port = ip_list[1]
return ip_port
'''
'''
def manage():
try:
#requests.get('http://wenshu.court.gov.cn/', proxies={"http":+proxy_ip()})
requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://113.120.34.70:34969"})
except:
print ('connect failed')
else:
print ('success')

if __name__ == '__main__':
proxy_ip()
#while True:
#    manage()
manage()
'''

try:
    requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://114.96.166.19:45149"})
except:
    print ('connect failed')
    return
else:
    print ('success')
    return