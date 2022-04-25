import requests
import re

from requests import Session, Request
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

data = {
    'name': 'germey',
    'age': 25
}

# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json())
# print(type(r.json()))

# r = requests.get('https://static1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://static1.scrape.center/', headers=headers)
# print(r.text)


# data = {'name': 'germey', 'age': '25'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)


# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

## file upload
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("https://httpbin.org/post", files=files)
# print(r.text)


# session 维持 所以，利用 Session，可以做到模拟同一个 Session 而不用担心 Cookies 的问题。它通常用于模拟登录成功之后再进行下一步的操作。
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# https请求时候忽略证书,如果想永久等待，可以直接将 timeout 设置为 None，或者不设置直接留空，因为默认是 None。这样的话，如果服务器还在运行，但是响应特别慢，那就慢慢等吧，它永远不会返回超时错误的。其用法如下：
# r = requests.get("https://static2.scrape.center/", verify=False, timeout=2)
# print(r.status_code)

## 身份认证
# r = requests.get('https://static3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# print(r.text)


# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#                'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)

# 设置代理，为防止大量请求被封，需要设置代理  pip3 install "requests[socks]"

# Prepared Request
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepare_req = s.prepare_request(req)
r = s.send(prepare_req)
print(r.text)
