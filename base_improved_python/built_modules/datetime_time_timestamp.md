####对象及相关之间的关系
 - datetime
```
>>> import datetime
>>> s=datetime.datetime.now()
>>> s
datetime.datetime(2018, 7, 1, 18, 26, 55, 333661)

>>> type(s)
<class 'datetime.datetime'>
```

- timestamp
```
>>> import time
>>> time.time()
1530441007.3834014
```

- time tuple
```
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2018, tm_mon=7, tm_mday=2, tm_hour=7, tm_min=54, tm_sec=3, tm_wday=0, tm_yday=183, tm_isdst=0)
```

- string
```
>>> import datetime
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'2018-07-02 08:11:26'
{以上同样为关系转换，datetime转换为string格式}
```


- date
```
>>> import datetime
>>> datetime.datetime.now().date()
datetime.date(2018, 7, 2)
```

#####datetime的基本操作
- 获取当前时间（datetime）
```
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2018, 7, 1, 18, 26, 55, 333661)
```
- 获取当天date
```
>>> datetime.date.today()
datetime.date(2018, 7, 2)
```
- 获取明天
```
>>> datetime.date.today()+datetime.timedelta(days=1)
datetime.date(2018, 7, 3)
```
- 获取前4天
```
>>> datetime.datetime.now() - datetime.timedelta(days=4)
datetime.datetime(2018, 6, 28, 13, 16, 44, 903813)
```
- 获取当天开始时间
```
>>> datetime.datetime.combine(datetime.date.today(), datetime.time.min)
datetime.datetime(2018, 7, 2, 0, 0)
```
- 获取当天结束时间
```
>>> datetime.datetime.combine(datetime.date.today(), datetime.time.max)
datetime.datetime(2018, 7, 2, 23, 59, 59, 999999)
```
- 获取两个时间差
```
>>> (datetime.datetime(2018, 7, 2, 0, 0)-datetime.datetime.now()).total_seconds()
-48034.549842
```
- 获取本周最后一天
```
>>> today.weekday()
0
>>> today = datetime.date.today()
>>> today
datetime.date(2018, 7, 2)
>>> sunday = today + datetime.timedelta(6-today.weekday())
>>> sunday
datetime.date(2018, 7, 8)
```
- 获取本月最后一天
```
>>> import calendar
>>> today = datetime.date.today()
>>> _,last_day_num = calendar.monthrange(today.year,today.month)
>>> _
6
>>> last_day_num
31
>>> last_day = datetime.date(today.year, today.month, last_day_num)
>>> last_day
datetime.date(2018, 7, 31)

```
- 获取上月最后一天
```
>>> import datetime
>>> today = datetime.date.today()
>>> first = datetime.date(day=1,month=today.month,year=today.year)
>>> lastMonth = first - datetime.timedelta(days=1)
>>> lastMonth
datetime.date(2018, 6, 30)
```

####关系转化

#####datetime <=> string
 - datetime -> string
```
>>> import datetime
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'2018-07-02 13:52:58'
```
- string -> datetime
```
>>> import datetime
>>> datetime.datetime.strptime("2018-7-2 13:55:10", "%Y-%m-%d %H:%M:%S")
datetime.datetime(2018, 7, 2, 13, 55, 10)
```
######datetime <=> timetuple
- datetime -> timetuple
```
>>> import datetime
>>> datetime.datetime.now().timetuple()
time.struct_time(tm_year=2018, tm_mon=7, tm_mday=2, tm_hour=13, tm_min=57, tm_sec=41, tm_wday=0, tm_yday=183, tm_isdst=-1)
```
- timetuple -> datetime
```
timetuple => timestamp => datetime [看后面datetime<=>timestamp]
```
##### datetime <=> date
- datetime -> date
```
>>> import datetime
>>> datetime.datetime.now().date()
datetime.date(2018, 7, 2)
```
- date -> datetime
```
>>> datetime.date.today()
datetime.date(2018, 7, 2)
>>> today = datetime.date.today()
>>> datetime.datetime.combine(today,datetime.time())
datetime.datetime(2018, 7, 2, 0, 0)
>>> datetime.datetime.combine(today,datetime.time.min)
datetime.datetime(2018, 7, 2, 0, 0)
```
#####datetime <=> timestamp
- datetime -> timestamp
```
>>> now = datetime.datetime.now()
>>> timestamp = time.mktime(now.timetuple())
>>> timestamp
1530511741.0
```
- timestamp -> datetime
```
>>> datetime.datetime.fromtimestamp(1530511741.0)
datetime.datetime(2018, 7, 2, 14, 9, 1)
```
