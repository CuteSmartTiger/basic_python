dic = {'e': 7,'a': 1, 'd': 4,  's': 5}
# 1.del  若只有一个键值对，删除后字典就消失了
del dic['d']
print(dic)

# 2.clear
dic = {'e': 7,'a': 1, 'd': 4,  's': 5}
print(dic.clear())  #None
print(dic)          #{}  返回一个空字典

# 3.pop
dic = {'e': 7,'a': 1, 'd': 4,  's': 5}
print(dic.pop('a','meiyou'))     #1  返回的是所删除的键值对的值
print(dic.pop('h','meiyou'))     #没有资格键，则返回默认值
print(dic)                        #{'e': 7, 'd': 4, 's': 5}



print('----------popitem----------')
# 4.popitem
di = {'e': 7,'a': 1,'d': 4, 's': 5}
print(di.popitem())     #以元组的形式返回，按升序排序后最右边的('s', 5)
print(di)               #{'e': 7, 'a': 1, 'd': 4}