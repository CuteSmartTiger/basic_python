# -*- encoding: utf-8 -*-


import requests

url= 'http://cwzx.shdjt.com/cwcx.asp'
res =requests.get(url)
# response=res.json()
# print res.text
print res.content