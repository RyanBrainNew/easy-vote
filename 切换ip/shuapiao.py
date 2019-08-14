from urllib import request
import requests
import json,time,re

headers = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI'
}

url = "http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3"
params = {'__EVENTTARGET': 'ctl00$content$lbtnVote',
'__EVENTARGUMENT': '',
'__VIEWSTATE':'/wEPDwUKMTA3MjEwMDM5MGRkodKGvAL63OrhGhVIdsFya2sjaeg=',
'__VIEWSTATEGENERATOR': 'C9E13C34',
'ctl00$content$rptTopicList$ctl00$tbOptionSearchInput': '',
'VoteOption_2890797': '7740339',
'ctl00$content$rptTopicList$ctl00$hiddenTopicID': '2890797',
'hiddenVote8ClickValidateCode': ['1561479249','31a61e5d9f8b9b9a67ce0b93205f7427'],
'ctl00$content$ucVerifyCode$hiddenVerifyCodeModeInfo': ['8','cd913f587d1b92fc4fbed4a5d29a5269'],
'ctl00$content$hiddenRefererUrl': 'http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=4',
'ctl00$content$hiddenTimeStampEncodeString': ['1561479246','889eee36aaeac6b03e7817cb52f46af6'],
'ctl00$content$hiddenLatitude': '',
'ctl00$content$hiddenLongitude': '',
'ctl00$content$hiddenGeoLocationEncode': ''
}


def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址
    url = "http://www.89ip.cn/tqdl.html?api=1&num=30&port=&address=&isp="
    r = requests.get(url=url)
    all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
    with open("D:\\PCode\\IP.txt", 'w') as f:
        for i in all_url:
            f.write(i)
            f.write('\n')
    return all_url

# 计数器
count = 0
while count < 4000:
    all_url = WriteIPadress()
    for i in all_url:
        proxies = {"http": i}
        try:
            r = requests.post(url=url, data=params, headers=headers, proxies=proxies, timeout=20)
            if(r.json()['flag'] == True):
                count += 1
                print("成功投票%d次！" % (count))
            print(r.json())
        except Exception as reason:
            print("错误原因是：", reason)
