# 第一个注释
'''
多行注释
'''
"""
多行注释
"""
print("Hello,Python!")
if True:
    print("True")
else:
    print("false")
# 多行语句
# total = item_one + \
#         item_two + \
#         item_three
# 在[],{},()中的多行语句，不需要使用反斜杠(\),例如
# total = ['item_one','item_two','item_three',
#          'item_four']
"""
1、数字类型Number：整数，布尔型，浮点数和复数(complex 1.1+2.2j)
2、字符串(string) - 使用三引号指定多行，单引号和双引号一样;
    转义符"\"的使用：人"this is line with \n" 则\n会被显示而不是换行
    Python中字符串不能改变
    Pyton没有独立的字符类型，一个字符就是长度为1的字符串
    截取的语法格式变量[头下标：尾下标：步长]
"""
word = '字符串'
sentence = "一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
str = 'Runaob123456789'
print(str)
print(str[0:-1]) #输出第一个到倒数第二个的所有字符串
print(str[0]) #输出字符串第一个字符
print(str[2:5]) #输出第三个开始到第五个的字符串
print(str[2:]) #输出从第三个开始到最后的所有字符
print(str[1:8:2]) #输出从第二个开始到第五个且每隔两个的字符
print(str * 2)
print(str + "哈哈哈")
print('-------------------------------------------')
print('hello\nrunoob') #使用反斜杆(\)+n转义特殊字符
print(r'hello\nrunoob') #在字符串面前添加1个
# print('\n')  # 加r输出\n
# input("\n\n按下 enter键后退出")
# 同一行显示多条语句,用”;“分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 缩进相同的一组语句构成一个代码块，我们称之为代码组。多个语句构成代码组
# 首行以关键字开始，以冒号(:)结束，该行之后的一行或多行代码构成代码组。
# 我们将首行以及后面的代码组称为一个自居
if True:
    print("1")
elif False:
    print("2")
else:
    print("cnm")
# print 输出默认换行，如果不需要换行，则需要在变量末尾加上end = ""
print('-------------')
x="a"
y="b"
print(x,end=" ")
print(y,end=" ")

# import 与from...import
"""
在python用import或者from import导入响应的模块.
将整个模块(somemodule)导入，格式为import somemodule
从某个模块导入某个函数，格式为：from somemodule import somefunction

"""