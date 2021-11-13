# # This package will contain the spiders of your Scrapy project
# #
# # Please refer to the documentation for information on how to create and manage
# # your spiders.
# # for i in range(2, 12):
# #     url = "/html/body/div[1]/div[2]/div/div[2]/div[" + str(i) + "]/div/div/div[1]/span[2]/p/text()[1]"
# #     # items["questions"] = response.xpath(url)
# #     print(url)
# import json
#
#
#
#
# # str_list = []
# #
# #
# # with open("C:\\Users\\13192\\cnli\\gnli.json",encoding="utf-8") as f:
# #     for line in f.readlines():
# #         if("stem" in line):
# #             str_list.append(line)
# #
#
# #
# # for i in str_list:
# #     if(string in i):
# #       print("true")
#
#
# #模拟点击
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
#
# # driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# cookies = [
# # {
# #     # "domain": ".huatu.com",
# #     # "expirationDate": 1695784722,
# #     # "hostOnly": "false",
# #     # "httpOnly": "false",
# #     "name": "_ga",
# #     # "path": "/",
# #     # "sameSite": "unspecified",
# #     # "secure": "false",
# #     # "session": "false",
# #     # "storeId": "0",
# #     "value": "GA1.2.157522328.1632712723"
# #     # "id": 1
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 1632799122,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "_gid",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "GA1.2.1083892843.1632712723",
# #     "id": 2
# # },
# # {
# #     "domain": ".huatu.com",
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lpvt_4f180beef63b7369b078602c780ef656",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "true",
# #     "storeId": "0",
# #     "value": "1632712723",
# #     "id": 3
# # },
# # {
# #     "domain": ".huatu.com",
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lpvt_c5b3a7bc9cfb4e1133c856fee205fabd",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "true",
# #     "storeId": "0",
# #     "value": "1632712723",
# #     "id": 4
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 1664248722,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lvt_4f180beef63b7369b078602c780ef656",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1632712723",
# #     "id": 5
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 1664248722,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lvt_c5b3a7bc9cfb4e1133c856fee205fabd",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1632712723",
# #     "id": 6
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 7939912723,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "sensorsdata2015jssdkchannel",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D",
# #     "id": 7
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 7939930373,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "sensorsdata2015jssdkcross",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "%7B%22distinct_id%22%3A%2215713824706%22%2C%22first_id%22%3A%2217c2012cb55638-0e64ecd38ad9dd-c343365-2073600-17c2012cb566ba%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Fv.huatu.com%2Ftiku%2F%22%7D%2C%22%24device_id%22%3A%2217c2012cb55638-0e64ecd38ad9dd-c343365-2073600-17c2012cb566ba%22%7D",
# #     "id": 8
# # },
# # {
# #     "domain": ".huatu.com",
# #     "expirationDate": 1648437522,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UM_distinctid",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "17c25430988627-0472bf470e43da-c343365-1fa400-17c25430989873",
# #     "id": 9
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lpvt_f735d6529dbfd84e0e9d68fea4bb90a4",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "true",
# #     "storeId": "0",
# #     "value": "1632730374",
# #     "id": 10
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1664266373,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Hm_lvt_f735d6529dbfd84e0e9d68fea4bb90a4",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1632625675,1632712727",
# #     "id": 11
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635322373.278784,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_auth",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "d1G2h9pbbbm9sd6fe9yaJep6Z9C2If60Ibj2I604NeD4Mb08MaD1M554M8C2I2s1Im1vYmlsZSI6IjE1NzEzODI0NzA2IiwiZW1haWwiOiIiLCJuYW1lIjoiYXBwX3p0azE4ODUzNTA5MTAiLCJuaWNrIjoiMTU3JTJBJTJBJTJBJTJBNDcwNiIsInNpZ25hdHVyZSI6IiIsImFyZWEiOiItOSIsInN1YmplY3QiOjAsInN0YXR1cyI6IjEiLCJhdmF0YXIiOiJodHRwcyUzQSUyRiUyRnRpa3UuaHVhdHUuY29tJTJGY2RuJTJGaW1hZ2VzJTJGdmh1YXR1JTJGYXZhdGFycyUyRmRlZmF1bHQyLnBuZyIsInJlZ0Zyb20iOiIzIiwiZGV2aWNlVG9rZW4iOm51bGwsImNyZWF0ZVRpbWUiOiIxNjMxMDE4ODU1MDAwIiwidWNlbnRlcklkIjoiMjgyMzQ2NjEiLCJwaG9uZUdlbyI6IiVFNiVCMiVCMyVFNSU4RCU5NyVFNyU5QyU4MSVFOSU4MyU5MSVFNSVCNyU5RSVFNSVCOCU4MiIsInBsYW5UaW1lIjoiIiwicHJvZmVzc2lvbiI6IiIsImFwcGx5RGVsZXRlVGltZSI6MCwidW5hbWUiOiJhcHBfenRrMTg4NTM1MDkxMCIsInRva2VuIjoiZjI2ZTdmNDA0ZTJlNDIwOWIzY2M4YWU3YTQ2YTVkYWQiLCJxY291bnQiOiIxMCJ9",
# #     "id": 12
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635322373.278709,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_catgory",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1",
# #     "id": 13
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888538,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_id",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "244340390",
# #     "id": 14
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888553,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_qcount",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "10",
# #     "id": 15
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1695697677,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "HT_sc_f41114f3ecfa342590164bded47c5b07f528ac74",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1688f75eed7c4a4a.1632625677.1632730341.1632730341",
# #     "id": 16
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635322373.278743,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_sub",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "1",
# #     "id": 17
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635322373.278764,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_token",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "f26e7f404e2e4209b3cc8ae7a46a5dad",
# #     "id": 18
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888545,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ht_uname",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "app_ztk1885350910",
# #     "id": 19
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888566,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "jtoken",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOiIxNjMyNzEyNjk2IiwianRpIjoiTVRZek1qY3hNalk1Tmc9PSIsImV4cCI6IjE2MzUzMDQ2OTYiLCJ1bmFtZSI6ImFwcF96dGsxODg1MzUwOTEwIiwibmljayI6IjE1NyoqKio0NzA2In0.xNVXIXRxoYFD_BDMfG8eCABmOsPxPv07XhQpcc-Yrdg",
# #     "id": 20
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888488,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "Password",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "49ba59abbe56e057",
# #     "id": 21
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888523,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "synlogin",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "0",
# #     "id": 22
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888495,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "TruePassWord",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "5091776320593045",
# #     "id": 23
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.88856,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "ucId",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "15713824706",
# #     "id": 24
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888509,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UserFace",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "https%3A%2F%2Ftiku.huatu.com%2Fcdn%2Fimages%2Fvhuatu%2Favatars%2Fdefault2.png",
# #     "id": 25
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888453,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UserID",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "21144704",
# #     "id": 26
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888502,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UserLevel",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "4",
# #     "id": 27
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.888471,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UserName",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "app_ztk1885350910",
# #     "id": 28
# # },
# # {
# #     "domain": ".v.huatu.com",
# #     "expirationDate": 1635304696.88848,
# #     "hostOnly": "false",
# #     "httpOnly": "false",
# #     "name": "UserReName",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "157%2A%2A%2A%2A4706",
# #     "id": 29
# # },
# # {
# #     "domain": "v.huatu.com",
# #     "expirationDate": 1648455140,
# #     "hostOnly": "true",
# #     "httpOnly": "false",
# #     "name": "CNZZDATA443728",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "cnzz_eid%3D126803529-1632712341-null%26ntime%3D1632723141",
# #     "id": 30
# # },
# # {
# #     "domain": "v.huatu.com",
# #     "expirationDate": 1648455140,
# #     "hostOnly": "true",
# #     "httpOnly": "false",
# #     "name": "CNZZDATA580664",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "false",
# #     "storeId": "0",
# #     "value": "cnzz_eid%3D745457912-1632703876-null%26ntime%3D1632725476",
# #     "id": 31
# # },
# {
# #     "domain": "v.huatu.com",
# #     "hostOnly": "true",
# #     "httpOnly": "false",
#     "name": "PHPSESSID",
# #     "path": "/",
# #     "sameSite": "unspecified",
# #     "secure": "false",
# #     "session": "true",
# #     "storeId": "0",
#     "value": "bcm7sksofedf5dqfqd5uq5t8j5",
# #     "id": 32
# }
# ]
# # hearders = {
# #     "Accept": "application/json, text/plain, */*",
# #     "Accept-Encoding": "gzip, deflate",
# #     "Accept-Language": "zh-CN,zh;q=0.9",
# #     "Connection": "keep-alive",
# #     "Host": "ns.huatu.com",
# #     "Origin": "http://v.huatu.com",
# #     "Referer": "http://v.huatu.com/",
# #     "terminal": "3",
# #     "token": "f26e7f404e2e4209b3cc8ae7a46a5dad",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# # }
#
# profile = webdriver.ChromeOptions()
# profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# driver = webdriver.Chrome(chrome_options=profile)
#
# driver.get("http://v.huatu.com/tiku/")
# for cookie in cookies:
#     driver.add_cookie(cookie)
# # for key,value in hearders.items():
#
# js="document.getElementsByClassName('tiku_spcal_item_btn')[33].style.display='block'"
# # js="document.getElementsByClassName('tiku_spcal_item_btn').styles"
# # print(js)
#
# driver.execute_script(js)
# time.sleep(2)
# # el = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[2]/div[2]/article[2]/div[2]/ul/li[2]/span")
# el1 = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[2]/div[1]/div[2]").click()
# el = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[2]/div[2]/article[2]/div[2]/ul/li[1]/span")
# el.click()
# # options = Options()
# # options.binary_location = ‘/path/to/chrome.exe’
# # driver = webdriver.Chrome(executable_path='/path/to/chromedriver.exe',chrome_options=options)
# # driver.get('http://www.google.com/xhtml');
# # driver.quit();
#
#
#
#
#
#
#
with open("C:\\Users\\13192\cnli\gnli.json","r",encoding="utf-8") as f:
    num = 0
    lines = f.readlines()
    for line in lines:
        if "stem" in line:
            num = num + 1
    print(num)

