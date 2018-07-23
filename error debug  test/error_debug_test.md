##error debug  test

###概念
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作


###单元测试
- 先编写单元测试对象do_demo.py
示例
```
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 80 and self.score <=100:
            return 'A'
        elif self.score >=0 and self.score < 60:
            return  'C'
        else:
            raise ValueError
`
```

- 再写单元测试内容
```
from do_demo import Student
import unittest
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

```

- 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。    
- 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
- 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断
  ，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

##总结
- assertEqual 测试等价
- assertTrue(isinstance(d, dict)) 判断类型是否为真
- assertRaises(KeyError) 报错
