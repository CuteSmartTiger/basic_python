# datetime模块里有datetime类 date类  time类
import datetime
now = datetime.datetime.now()
today = datetime.datetime.today()

print(now)
print(today)
# 将now对象中的详细信息取出来
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.second)
print(now.microsecond)

print(today.month)


# 计算相差几天的日期
import datetime
t = datetime.datetime.today()
res = t + datetime.timedelta(days=14)
print(res,type(res))
# 2018-10-07 13:00:23.822713 <class 'datetime.datetime'>


# 计算两个日期时间差
first = datetime.datetime(2018,9,8,14,6,30)
print(first,type(first))

second = datetime.datetime(2018,9,10,14,6,30)
diff = second -first
print(diff,type(diff))
# 2 days, 0:00:00 <class 'datetime.timedelta'>
# 将差值转换为时间戳
c_time = diff.total_seconds()
print(c_time)
# 172800.0