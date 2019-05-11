#coding=utf-8
#by www.zhangteng.xyz
#2019.5.11
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


head={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
#发送get请求并得到结果
def searchphone(phone):

	url = 'http://www.ip138.com:8080/search.asp?mobile='+phone+'&action=mobile'
	
	req= requests.get(url,headers=head)  #发送请求

	req.encoding = 'gbk'

	soup = BeautifulSoup(req.text,'html.parser')

	html = soup.prettify()

	tab = soup.find_all('td',attrs={'class':'tdc2'})

	print('您查询的手机号码段: ')
	print(tab[0])
	print('卡号归属地: ')
	print(tab[1])
	print('卡 类 型: ')
	print(tab[2])
	print('区 号: ')
	print(tab[3])
	print('邮 编: ')
	print(tab[4])


if __name__ == '__main__':
	tel=str(sys.argv[1])
	searchphone(tel)