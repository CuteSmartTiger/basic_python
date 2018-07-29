# 对字符的基本操作：
# 1.查找，分哪几类，捕获组的用法
# 2.替换   replace(),translate()
# 3.删除，strip，，
# 4.分割
# 5.取值
# 6.增加
# 7.疑问清单：正则中?:的用法;match与search的区别；如何将文件中各种语言转化为同一标准，然后输出不乱码


import re
# 1.findall()函数,查找匹配项,以列表的形式返回
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']



# sub()函数的用法，sub需要与re一起使用，可以接受字符串，也可以接受回调函数
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
# 'UPPER snake, lower snake, Mixed snake'


# 使用支撑函数（support function）根据文本内容大小写替换
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
# UPPER SNAKE, lower snake, Mixed Snake


# 2.实现最短匹配
str_pat = re.compile(r'\"(.*)\"')    #前面有r标识符，'\'不影响结果
str_pat1 = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']
print(str_pat1.findall(text2))

#最短匹配的用法
str_pat2 = re.compile(r'"(.*?)"')
print(str_pat2.findall(text2))


# 3.编写多行模式的正则表达式
# 方法一：
comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
comment2 = re.compile(r'/\*((.|\n)*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
             multiline comment */
 '''

print(comment1.findall(text1))
# [' this is a comment ']
print(comment2.findall(text1))
# [(' this is a comment ', ' ')]

print(comment1.findall(text2))


# 方法二：
# re.compile() 函数接受一个标志参数 re.DOTALL ，可以让正则表
# 达式中的点(.)匹配包括换行符在内的任意字符

comment3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment3.findall(text2))
# [' this is a\n multiline comment ']

print("\n")
# 删除或者替换
# 方法一：strip()的用法，出去两边的
t = '  ---liu--hello= ====   \n'
print(t.strip())
print(t.lstrip())
print(t.rstrip())
l= '-- -liu--hello= ===='
print(l.strip("-="))
print(l.lstrip("-="))
print(l.rstrip("-="))


print("repalce:")
# 方法二：replace

print(t.replace(' ', ''))

# 方法三：正则
x= '- - -liu- -hello= = =         =='
print(re.sub(r'\s+','e',x,6))
print(re.sub(r'-','e',x,2))
print(re.sub(r' ','',x))

# 若从文件中读取行并打印，进阶：改变目录位置，或者内容中有中文(目前尝试中文失败),
#无法对加""中的空字符进行strip操作
with open('./test.py') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)


# 一次处理多个对象，使用translate(),python2与python3不同
s = 'pýtĥöñ\fis\tawesome\r\n'
ss = 'python\fis\tawesome\r\n'

remap = {
   ord('\t') : ' ',
   ord('\f') : ' ',
   ord('\r') : None
 }
remap1 = {
   '\t' : ' ',
   '\f': ' ',
   '\r' : None
 }


a = s.translate(remap)
a1 = ss.translate(remap)
print(a)
print(a1)
a2=ss.translate(remap)
print(a2)

# 进阶方法，先删除指定字符串，然后按照要求进行映射转换
# str.translate(table)
# bytes.translate(table[, delete])
# bytearray.translate(table[, delete])
# table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
# deletechars -- 字符串中要过滤的字符列表

# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))