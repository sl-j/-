import scrapy
from bs4 import BeautifulSoup
from cnli.items import ans_quesItem
import json


num = 0
class NliSpider(scrapy.Spider):
    num = 0
    name = 'nli'
    start_urls= []
    allowed_domains = ['question.com']
    with open("C:\\Users\\13192\\cnli\\cnli\\spiders\\url.txt", "r") as f:
        for line in f.readlines():
            start_urls.append(line)


    def parse(self, response):
        flag = 0
        # num = 0
        # cnum = 0
        str_list = []
        filename = "gnli.json"
        g_dist = {}
        choices = []
        re = json.loads(response.text)
        for i in range(0,10):
            # print("第"+str(i+1)+"题：")
            stem = re["data"][i]["stem"]
            # print(stem)

            # 判断是否爬取到重复的题目
            with open("C:\\Users\\13192\\cnli\\gnli.json", encoding="utf-8") as f:
                for line in f.readlines():
                    # print(line)
                    if ("stem" in line):
                        str_list.append(line)
                        # print(line)
            for txt in str_list:
                if (stem in txt):
                    # cnum = cnum+1
                    # print("有重复题:"+stem)
                    flag = 1
                    continue
            if(flag == 1):
                continue
            else:
                flag = 0

            # print(re["data"][i])
            answer = re["data"][i]["answer"]
            for j in range(0,4):
                choices.append(re["data"][i]["choices"][j])



            g_dist["stem"] = stem
            g_dist["answer"] = str(answer)
            g_dist["choices"] = choices
            # print(g_dist)
            with open(filename,'a+',encoding="utf-8") as f:
                json.dump(g_dist,f,ensure_ascii=False,indent=2)
            choices.clear()
            str_list.clear()
            g_dist.clear()
        # NliSpider.num = NliSpider.num+1
        # print("爬取第"+NliSpider.num+"成功")




