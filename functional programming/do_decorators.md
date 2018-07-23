##装饰器


####概念
```
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

补充：decorator就是一个  返回函数   的高阶函数，在理解返回函数的基础上在理解装饰器
```
#####代码解析
```
请看代码实例
```
####代码实例
- 编写一个可以传参与可以不传参的装饰器
```
from inspect import isfunction
from functools import wraps
# 定义可以输入参数或者不出入参数的装饰器
def log_test(test):
    # 判断test是函数，然后进行装饰器的运行
    if isfunction(test):
        #wraps的使用，保留了调用函数的name属性名不发生变化
        @wraps(test)
        def wrapper(*args, **kwargs):
            print('直接调用了函数')
            return test(*args, **kwargs)
        return wrapper
    # 如果test存在
    else:
        def decorat(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                print('装饰器接受的传递参数:%s'%test)
                return func(*args,**kwargs)
            return wrapper
        return decorat

@log_test
def now_sum(*args):
    a=0
    for i in args:
        a+=i
    return a

print(now_sum(1,2,3,4))
```

####应用场景
- 1.需要登录方可进行相关操作
```
def login_required(func):
   # 使用wraps保留func的相关信息，使用前需要from functools import wraps导入
   @wraps(func)
   #由于定义（）中的名称需要一致，考虑到多个地方将用到这个函数，所以用*args,**kwargs
   def inner(*args,**kwargs):
       # 通过session中的user_id是否存在，来判断用户是否已经登陆，若登陆则
       if config.BACK_USER_ID in session:
           # 若已经登录，则返回相关信息
           return func(*args,**kwargs)
       else:
           # 若没有登陆，则跳转初始页面
           return redirect(url_for('back.login'))
   # 返回inner结果
   return inner


# # 解释说明装饰器的功能
# @login_required
# def index():
#     return "cms.index"
# # 结果
# index=login_required(index)=inner
# # 等同于方法
# index(username)== inner(usrename)
```


- 2.后台权限管理限制
```
# 由于直接输入地址可以访问后台，所以需要设置访问权限设置，这里定义装饰器
# 第一个def  用来传入参数
def permission_required(permission):
   # outter为主要的装饰器功能
   def outter(func):
       @wraps(func)
       def inner(*args,**kwargs):
           # 获取用户信息
           user=g.back_user
           # 进行传入的权限参数与实际模型中计算后的权限二进制数值进行判断，调用has_permissions函数
           if user.has_permissions(permission):
               return func(*args,**kwargs)
           else:
               return redirect(url_for('back.index'))
       #针对outter函数返回inner结果
       return inner
   # 返回outter,对调用的函数进行装饰
   return outter
```
