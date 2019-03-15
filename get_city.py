__author__ = 'Administrator'
import requests,random,json
from bs4 import BeautifulSoup
import time
import datetime
from fake_useragent import UserAgent
import uuid
now = datetime.datetime.now()
timeStamp = int(now.timestamp()*1000)
geshi = "%Y%m%d%H%M%S"
time1 = datetime.datetime.strftime(now,geshi)
ua=UserAgent()
uid=str(uuid.uuid4())
print(uid)
session = requests.Session()
url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
data={'first':'false',
'pn':30,
'kd':'java'
}
headers={
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-type':'application/json;charset=utf-8 ',
            'Cookie':'user_trace_token=20181102145432-bafe4e8f-916e-4cf3-979c-d91872be2428; _ga=GA1.2.286303898.1541141667; LGUID=20181102145433-27312db1-de6c-11e8-85c5-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167f903300346a-00c2502816494e-454c092b-2073600-167f903300465e%22%2C%22%24device_id%22%3A%22167f903300346a-00c2502816494e-454c092b-2073600-167f903300465e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; WEBTJ-ID=20190228101943-16931e6805a20b-0900ed8535c6d4-454c092b-2073600-16931e6805c191; JSESSIONID=ABAAABAAAIAACBIAE612655DD3DB8A50E5FD30F196F2B9B; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; X_MIDDLE_TOKEN=d422c5d6d227b98ddd04ad2bf96b8faf; _gid=GA1.2.1517398484.1552023170; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552037507,1552041163,1552042417,1552095851; TG-TRACK-CODE=index_search; SEARCH_ID=724ded75b2e243459babc896c522b179; LGSID=20190309101442-197aeb6b-4211-11e9-8cf9-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist%255Fjava%253FlabelWords%253D%2526fromSearch%253Dtrue%2526suginput%253D%26t%3D1552095861%26_ti%3D1; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D183.129.162.42; LG_LOGIN_USER_ID=04b1a113c206db7930a507eb971a0a0b1e748216814dfb4a; _putrc=12F032920E3D35DD; login=true; unick=%E4%BD%99%E6%B2%BB%E7%BF%94; hasDeliver=45; gate_login_token=5d654a8058344f49475a9e0f8a3d014859d88edefb07c7d7; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; LGRID=20190309101524-32fd6923-4211-11e9-8cf9-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552097717',
            'Host':'www.lagou.com' ,
            'Referer':'https://www.lagou.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


resp=session.post(url,data=data,headers=headers)
resp.encoding='utf-8'
# resp1=requests.get('https://fanyi.baidu.com/',proxies={'http':a})
print(resp.json())