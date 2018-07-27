import re
# findall()函数,查找匹配项,以列表的形式返回
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


