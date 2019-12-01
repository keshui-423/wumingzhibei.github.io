import requests
import re
import time
import random

class WenJuanXing:

     def __init__(self,url):
        self.wj_url = url
        self.post_url = None
        self.head = None
        self.cookie = None
        self.data = None


     def get_ktimes(self):
         return random.randint(5,18)

     def set_header(self):
         ip='{}.{}.{}.{}'.format(112,random.randint(64,68),random.randint(0,255),random.randint(0,255))
         self.header = {
             'X-Forwarded-For':ip,
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'
                       }

     def get_response(self):
         response=requests.get(url = self.wj_url,headers = self.header)
         self.cookie = response.cookies
         return response
        
     def get_jqnonce(self,response):
         jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}',response.text)
         return iqnonce.group()
                             
     def get_rn(self,response):
         rn = re.search(r'\d{9,10}\.\d{8}',response.text)
         return rn.group()
         
     def get_id(self,response):
         id = re.search(r'\d{8}',response.text)
         return id.group()
         
     def get_jqsign(self,ktimes,jqnonce):
         result =[]
         b =ktimes%10
         if b==0:
             b=1
         for char in list(jqnonce):
             f=ord(char)^b
             result.append(chr(f))
         return ''.join(result)
        
     def get_start_time(self,response):
         start_time = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}',response.text)
         return start_time.group()
     def set_post_url(self):
         self.set_header()
         response=self.get_response()
         ktimes=self.get_ktimes()
         jqnonce=self.get_jqnonce(response)
         rn=self.get_rn(response)
         id=self.get_id(response)
         jqsign=self.get_(ktimes,jqnonce)
         start_time=self.get_start_time(response)
         time_stamp='{}{}'.format(int(time.time()),random.randint(100,200))
         url="https://www.wjx.cn/joinnew/processjq.ashx?curid=39121259&starttime=2019%2F5%2F8%2015%3A37%3A35&source=directphone&submittype=1&ktimes=56&hlv=1&rn=717413028.85240527&t=1557301167565&jqnonce=4bf753e4-ad0c-4a9f-ac4d-5864b50b2ce1&jqsign=2d%60135c2%2Bgb6e%2B2g%3F%60%2Bge2b%2B3%3E02d36d4ec7"
         self.post_url=url
         print(self.post_url)
         
     def set_data(self):
         self.data={'submitdata':'1$1}2$1|2'}
         
     def post_data(self):
         self.set_data()
         response = requests.post(url=self.post_url,data=self.data,headers=self.headers,cookies=self.cookie)
         return response
        
     def run(self):
         self.set_post_url()
         result=self.post_data()
         print(result.content.decode())
         
     def mul_run(self,n):
         for i in range(n):
             time.sleep(0.1)
             self.run()

if __name__=='__main__':
    w=WenJuanXing('url')
    w.mul_run(100)
    
     
         

     
