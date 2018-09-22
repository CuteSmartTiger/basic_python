# 定义字典的另外一种方法：
# 调用字典类或者实例的fromkeys方法
# 字典的键是不可变类型,理解字典的键必须唯一的理由，根据其存储原理与查找原理来决定的
r = [1,2,3,4]
d = 'adescf'
print(dict.fromkeys(r))     #{1: None, 2: None, 3: None, 4: None}
print(dict.fromkeys(d,5))  #{'a': 5, 'd': 5, 'e': 5, 's': 5, 'c': 5, 'f': 5}


# 批量修改键值对，后来者覆盖前面的
person = {'name':'liuhu','age':18}
dic = {'e': 7,'a': 1, 'd': 4,  's': 5}
res = person.update(dic)
print(res)      #None
print(person)  #{'name': 'liuhu', 'age': 18, 'e': 7, 'a': 1, 'd': 4, 's': 5}

# 修改单一键值对
person['name'] = 'nana'