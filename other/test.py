# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import math
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
import requests,time,re

FILE = 'D:\\ptest\\IP6.txt'  # 读取的txt文件路径

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

def editUserAgent():
    
    #初始化
    #WIDTH = 320
    #HEIGHT = 640
    #PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI'
    #mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
    mobileEmulation = {"userAgent": UA}
    #prefs = {"profile.managed_default_content_settings.images": 2}

    #chrome配置
    #options.add_experimental_option("prefs", prefs)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_argument('--headless')
    #options.add_argument('--ignore-certificate-errors')
    options.add_argument("--proxy-server=http://"+proxy_ip())
    driver = webdriver.Chrome(executable_path='D:\ptest\chromedriver.exe', chrome_options=options)
    '''
    #测试UA
    driver.get('http://service.spiritsoft.cn/ua.html')
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')
    user_agent = soup.find_all('td', attrs={
        'style': 'height:40px;text-align:center;font-size:16px;font-weight:bolder;color:red;'})
    for u in user_agent:
        print(u.get_text().replace('\n', '').replace(' ', ''))
    #driver.close()
    time.sleep(10)
    '''
    #测试代理
    #driver.get("http://httpbin.org/ip")
    '''
    #打开网址
    eventlet.monkey_patch()
    with eventlet.Timeout(2,False):#设置超时时间为2秒
        driver.get("http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3")
        print('do openurl')
    print('跳过了openurl')
    '''
    #打开网站
    print('Go')
    driver.set_page_load_timeout(10)
    driver.get("http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3")

    #到页面底部通过点击验证
    #driver.implicitly_wait(3) #隐式等待
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    #print('do pre')
    selem_verify = driver.find_element_by_css_selector('.Vote8ClickButton.Vote8ClickButtonNormal').click()
    time.sleep(1)
    #print('do verify')

    #确定候选人
    element = driver.find_element_by_xpath("//*[@id='option_7740339']").click()
    #print('do choose')
    time.sleep(2)

    #投票
    element = driver.find_element_by_xpath("//*[@id='lbtnVote']").click()
    print('do vote')

    #结束退出处理
    #driver.delete_all_cookies()
    #driver.refresh()
    driver.delete_all_cookies()
    time.sleep(1)
    driver.quit()

if __name__ == '__main__':

    count = 0
    while count < 2: 
        try:
            editUserAgent()
            print('\nNext\n')
        except:
            pass
            print('\nFail\n')
