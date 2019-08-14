# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import math
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
import requests,time


def editUserAgent():

    #WIDTH = 320
    #HEIGHT = 640
    #PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI'
    #mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
    mobileEmulation = {"userAgent": UA}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
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
    #打开网址
    driver.get("http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3")
    #elem_verify = driver.find_element_by_class_name("Vote8ClickButton Vote8ClickButtonNormal")
    #elem_verify = driver.find_element_by_css_selector("[class='Vote8ClickButton Vote8ClickButtonNormal']")
    #test
    #elem_verify = driver.find_element_by_xpath("//*[@id='content_pnlVerifyCode']/div/div[@class='Vote8ClickButton Vote8ClickButtonNormal']")
    #elem_verify = driver.find_element_by_css_selector('class="Vote8ClickButton Vote8ClickButtonNormal"').click()#包含整个类

    #到页面底部过点击验证
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print('do it')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('do it')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    selem_verify = driver.find_element_by_css_selector('.Vote8ClickButton.Vote8ClickButtonNormal').click()
    
    #element = driver.find_element_by_xpath("//input[@id='passwd-id']")
    #elem_verify = driver.find_element_by_link_text("排行")
    #elem_verify = driver.find_element_by_id("content_rptTopicList_rptOptions_0_imgOptionImage_2")
    #ActionChains(driver).move_to_element(elem_verify).click(elem_verify).perform()

    #选人
    time.sleep(1)
    element = driver.find_element_by_xpath("//*[@id='option_7740339']").click()
    time.sleep(1)
    #投票
    time.sleep(1)
    element = driver.find_element_by_xpath("//*[@id='lbtnVote']").click()
    time.sleep(1)
    print('do it')
    driver.delete_all_cookies()
    #第二轮
    driver.refresh()
    #driver.get("http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline&Topic_2890797_Page=3")
    #cookie= driver.get_cookies()
    #print cookie
    time.sleep(2)


if __name__ == '__main__':
    while True:
        editUserAgent()