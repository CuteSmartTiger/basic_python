#encoding:utf-8
import json

t = ((1,'a','blahblah'),(2,'b','blahblah'),(3,'c','blahblah'))
key = ('pmid', 'title', 'abstract')

d = [dict(zip(key, value)) for value in t]
res_json = json.dumps(d)
print res_json
# [{"pmid": 1, "abstract": "blahblah", "title": "a"}, {"pmid": 2, "abstract": "blahblah", "title": "b"}, {"pmid": 3, "abstract": "blahblah", "title": "c"}]

source = ((1,'a','blahblah'),(2,'b','blahblah'),(3,'c','blahblah'))
result = map(lambda x: dict(zip(('pmid', 'title', 'abstract'), x)), source)
print result
# 单引号为字典
# [{'pmid': 1, 'abstract': 'blahblah', 'title': 'a'}, {'pmid': 2, 'abstract': 'blahblah', 'title': 'b'}, {'pmid': 3, 'abstract': 'blahblah', 'title': 'c'}]
print json.dumps(result)
# 双引号为json