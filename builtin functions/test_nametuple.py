from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

# 可以是列表，也可以是字符串，但字符串中需要用空格隔开
# Website = namedtuple('Website', ['name', 'url', 'founder'])
Website = namedtuple('Website', 'name url founder')

for website in websites:
    website = Website._make(website)
    print(website)
