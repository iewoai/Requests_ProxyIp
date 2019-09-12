#coding=utf-8
import requests
import random
import re
import time
user_agent_list = [
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
	"Opera/8.0 (Windows NT 5.1; U; en)",
	"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
	"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
]
'''
file = open("valid_ip_xicidaili.txt","r")
proxies_list = []
for line in file:
	proxies_list.append(line.strip().replace("\n",""))
proxy = {"https":random.choice(proxies_list)}
'''

def send_request(url):
	
	'''
	proxy = {"https":""}
	flag=0;
	while(flag==0):
		if(len(user_agent_list)==0):
			print("可用代理ip为空")
			return
		random_ip = random.choice(valid_proxy_ip)
		proxy['https'] = "https://"+random_ip
		headers = {"USER-AGENT":random.choice(user_agent_list),}
		try:
			response = requests.get(url,verify=False,headers=headers,proxies=proxy,timeout=(4,4))
		except requests.exceptions.ProxyError:
			print("代理ip无效"+proxy['https'])
			if random_ip in user_agent_list:
				user_agent_list.remove(random_ip)
		except requests.exceptions.ConnectTimeout:
			print("请求超时"+proxy['https'])
			if random_ip in user_agent_list:
				user_agent_list.remove(random_ip)
		except requests.exceptions.ReadTimeout:
			print("下载超时"+proxy['https'])
			if random_ip in user_agent_list:
				user_agent_list.remove(random_ip)
		else: 
			flag=1
			print("使用代理ip成功下载")
			time.sleep(2)
			
	return response
	'''

	headers = {"USER-AGENT":random.choice(user_agent_list),}
	try:
		response = requests.get(url,verify=False,headers=headers,timeout=(4,4))
		print(response.status_code)
	
	except requests.exceptions.ConnectTimeout:
		print("请求超时"+proxy['https'])
		if random_ip in user_agent_list:
			user_agent_list.remove(random_ip)
	except requests.exceptions.ReadTimeout:
		print("下载超时"+proxy['https'])
		if random_ip in user_agent_list:
			user_agent_list.remove(random_ip)
	else: 
		print("使用代理ip成功下载")
	return response

	


def store_result(response):
	url = re.findall(r"<td>(\d+\.\d+\.\d+\.\d+)</td>",response)
	port = re.findall(r"<td>(\d{1,6})</td>",response)
	file = open("all_ip_xicidaili.txt","a")
	for index,v in enumerate(url):
		file.write(v+":"+port[index]+"\n")
	file.close()



def get_valid_ip():
	
	#response = requests.get("https://www.baidu.com",proxies = proxy,timeout=0.001)
	file = open("all_ip_xicidaili.txt","r")
	for line in file:
		check_valid_ip(line) 
		
	

def check_valid_ip(ip):
	proxy={"https":""}
	proxy['https'] =ip.strip().replace("\n","")
	print(proxy)
	try:
		response = requests.get("https://www.baidu.cn",proxies = proxy,timeout=(1,1),verify=False)
	except requests.exceptions.ProxyError:
		print("代理ip无效")
	except requests.exceptions.ConnectTimeout:
		print("请求超时")
	except requests.exceptions.ReadTimeout:
		print("下载超时")
	else:
		
		if response.status_code==200:
			print("valid_ip:"+ip)
			f = open("valid_ip_xicidaili.txt","a")
			f.write(ip)
			f.close()


if __name__ == '__main__':
	#获取代理ip
	'''
	valid_ip_file = open("valid_ip_xicidaili.txt","r")
	valid_proxy_ip = [line.strip().replace("\n","") for line in valid_ip_file]
	valid_ip_file.close()
	
	for i in range(1,1000):
		print("开始爬取第"+str(i)+"个页面")	
		response = send_request("https://www.xicidaili.com/wn/"+str(i)).text
		store_result(response)
	'''
	get_valid_ip()
	
	