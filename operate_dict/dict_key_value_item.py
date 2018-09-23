dic = {'name':'liuhu','age':18,'e': 7,'a': 1, 'd': 4,  's': 5}
# 获取key
keys = dic.keys()
print(keys)
# dict_keys(['name', 'age', 'e', 'a', 'd', 's'])


# 获取value
values = dic.values()
print(values)
# dict_values(['liuhu', 18, 7, 1, 4, 5])

# 获取键值对 获取的是可迭代待对象，元素以元组的方式呈现
items = dic.items()
print(items)
# dict_items([('name', 'liuhu'), ('age', 18), ('e', 7), ('a', 1), ('d', 4), ('s', 5)])

# 遍历keys
for key in keys:
    print(key)

# 遍历values
for value in values:
    print(value)
# 遍历items
for item in items:
    print(item)
# 或者
for key,value in items:
    print(key,value)