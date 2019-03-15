__author__ = 'Administrator'
import requests
from bs4 import BeautifulSoup
import urllib.parse
import city
import connect_sql
import re,time,random
# citysd=input('输入城市：')
kw=input('请输入职位：')
def get_base_url(citysd):
    base_url=set()

    for page in range(0,1080,90):
        url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId={}&industry=10100&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=0&at=f38edef813274cf8823038715d190abc&rt=ba61610ecee246778ca5b2a38059e7c7&_v=0.07354195&userCode=669405652&x-zp-page-request-id=5d86485ad2674b3c84c0dcbf0cf66a18-1552101779862-65055'.format(page,citysd,kw)
        print(url)
        headers={

        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        resp=requests.get(url,headers=headers)
        print(resp.text)
        req=resp.json()
        url=req['data']['results']

        for i in range(len(url)):
            base_url.add(url[i]['positionURL'])
        print(base_url)
    return base_url


def get_message(citysd):
    base_url=get_base_url(citysd)

    while len(base_url)>0:
        url=base_url.pop()
        http=[]
        print(url)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        try:
            resp=requests.get(url,headers=headers,timeout=5)
            soup=BeautifulSoup(resp.text,'lxml')
            position=soup.find('div',class_='new-info').find('ul').find('li').text#职位1
            salary=soup.find('div',class_='new-info').find('ul').find('li',class_='info-money').text.strip('\n').strip('')#薪水1
            company=soup.find('li',class_='clearfix').find('div').find('a').text.strip('\n').strip('')#公司名称1
            time=soup.find('li',class_='clearfix').find('div').find('span').text#发布时间
            all=soup.find('li',class_='clearfix').find('div',class_='info-three l').text
            h=all.split('\n')
            # region=h[0]#区县1
            experience=h[2]#经验1
            education=h[3]#教育1
            number=h[4]#招聘人数1
            bright_spot=soup.find_all('script')
            a=str(bright_spot)
            b=re.compile(r'var JobWelfareTab =(.*?;)')
            k1=re.search(b,a)
            Job_highlights=(k1.group(1))#职位亮点
            job_requirements=soup.find('div',class_='pos-ul').text#职位要求
            address=soup.find('p',class_='add-txt').text#具体地址
            http.append(company)
            http.append(position)
            http.append(salary)
            http.append(citysd)
            http.append(address)
            http.append(experience)
            http.append(education)
            http.append(number)
            http.append(time)
            http.append(Job_highlights)
            http.append(job_requirements)
            # print(salary)
            # print(region)
            # print(k)
            # print(len(company))
            # print(len(position))
            # print(len(salary))
            # print(len(region))
            # print(len(address))
            # print(len(experience))
            # print(len(education))
            # print(len(number))
            # print(len(time))
            # print(len(Job_highlights))
            # print(len(job_requirements))
            print(len(http))
            for i in http:

                print(i)
            connect_sql.abc(http)
        except:
            pass

if __name__=='__main__':
    for citysd in city.area_dict:
        get_message(citysd)
        time.sleep(random.randrange(1,2))
