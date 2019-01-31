import requests

url = 'http://maoyan.com/board/4'
#调用
r = requests.get(url)
#输出 http 状态码
print(r)
#打印文本 F12
print(r.text)