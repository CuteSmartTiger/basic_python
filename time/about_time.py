import time

# 获取当前时间戳
t = time.time()
print(t)   #1537676269.568997  单位是秒
y = t/(60*60*24*365)
c_y = 1970+y
print(c_y)  #2018.759394646404


# 时间戳转化为格式化时间
hg = time.ctime(t)
print(hg)
# Sun Sep 23 12:25:28 2018


# 获取时间元组
tuple_time = time.localtime()
print(tuple_time)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=23, tm_hour=12, tm_min=21,
# tm_sec=38, tm_wday=6, tm_yday=266, tm_isdst=0)


# 时间元组转化为格式化时间
format_tuple_time = time.asctime(tuple_time)
print(format_tuple_time)
# Sun Sep 23 12:26:56 2018

print('------------将时间元组转化为时间戳--------')
c_time = time.mktime(tuple_time)
print(c_time)
# 1537677479.0

print('------------自定义时间格式化 :将时间元组转化为格式化的时间日期--------')
# 自定义时间格式化 :将时间元组转化为格式化的时间日期
show_time = time.strftime('%Y-%m-%d  %H:%M:%S',tuple_time)
print(show_time)   #2018-09-23  12:31:03


print('------------自定义时间格式化 :将时间日期转化为格式化的时间元组--------')
# 自定义时间格式化 :将时间日期转化为格式化的时间元组
change_format_to_tuple_time = time.strptime('2018-09-23  12:31:03','%Y-%m-%d  %H:%M:%S')
print(change_format_to_tuple_time)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=23, tm_hour=12, tm_min=31, tm_sec=3, tm_wday=6, tm_yday=266, tm_isdst=-1)

