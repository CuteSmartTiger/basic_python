# L-Local  函数内的命名空间 作用范围：当前整个函数体范围
# E-Enclosing function locals 外部嵌套函数的命名空间  作用范围：闭包
# G-Global  全局命名空间  作用范围： 当前模块
# B-Builtin 内建模块命名空间    作用范围：所有模块
# python中没有块级作用域 比如if while for后面的代码块
# LEGB规则：L -> E ->G ->B 的顺序进行查找，从内往外查找

