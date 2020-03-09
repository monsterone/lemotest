# -*- coding: utf-8 -*-
# @Time     : 2020/1/10 22:36
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class3_str.py

#【3】. 字符串的一些使用

# s = 'hello!'
# s=''  #空字符串

#1:字符串里面元素：单个字母 数字 单个字符 都称之为一个元素
#len(数据）统计数据的长度print（len(s)）
#2：字符串取值：字符串名[索引值]
#索引：从0开始标记
'''
print(s[5])  #正序
print(s[-1]) #倒叙
'''
#3：字符串取多个值：切片 字符串名[索引头:索引尾:步长] 步长默认为1

'''
print(s[1:5:1]) # 1 2 3 4 #取头不取尾 ello
print(s[2:4:2])
print(s[:]) #全取  hello!
print(s[:4]) #0 1 2 3 hell
print(s[3:]) # 3 4 5  lo!
'''
#小题目：请利用切片，倒序输出s的值，输出结果为!0lleh
'''
print(s[-1:-7:-1])
print(s[::-1])
'''

# s = ' hello!'
#4:字符串的分割  字符串.split(可以指定切割符，切割次数)
## 只有字符串有这个函数
##返回一个列表类型的函数（列表里的子元素都是字符串类型）
##指定的切割符  被切走
'''
print(s.split())  #['hello!']
print(s.split(" ")) #根据空格进行切割   #['', 'hello!']
print(s.split("e"))  #[' h', 'llo!']
print(s.split("l"))  #[' he', '', 'o!']
#可以指定切割次数
print(s.split("l",1))  #[' he', 'lo!']
'''


#5:字符串的替换  字符串.replace(指定替换值，新值,替换次数)
'''
s = 'hello!'
new = s.replace('l','@',2)  #可指定替换次数
print(new)
'''

#6:字符串的去除指定字符  字符串.strip(指定替换值)
'''
s = ' hello!'
#1:默认去掉空格  2:只能去掉头和尾的字符
print(len(s))  #7
new = s.strip()
print(len(new)) #6

new = s.strip("!")
print(new)
'''

#7:字符串的拼接  +   保证"+"左右两边的变量值类型要一致
s1 = 'python01'
s2 = '新年快乐'
s3 = 666 #整数   str(数字）---可以强制转化为str类型
print(s1+s2)  #拼接
print(s1,s2)  #分别输出
print(s1,s2,s3)
# print(s1+s2+s3) #ypeError: must be str, not int 数据类型不一致
print(s1+s2+str(s3))  #python01新年快乐666



#8:字符串格式化输出  % format
age = 18
name = '怪兽'
score = 99.99
# print("很帅的"+name+"今年"+age+"岁！")#TypeError: must be str, not int
# print("很帅的"+name+"今年"+str(age)+"岁！")

#格式化输出1：format 特点 {} 用"{}"来占坑
print("很帅的{},今年{}岁！".format(name,age))
print("很帅的{0},今年{1}岁！".format(name,age)) #0 1可不写，根据索引来

#格式化输出2：%  %s字符串  %d数字  %f浮点数
#%s可以填任何数字
#%d 只能填数字 整型 浮点数
#%f 可以填数字
print("2很帅的%s,今年%d岁！"%(name,age))

print("3很帅的%s,今年%d岁！考试考了%.2f"%(name,age,score)) #%.2f 小数点后保留2位

#格式化输出3:(【补充】)
print(f"4很帅的{name},今年{age}岁！")

#下节课：列表  元祖  运算符
#下下节课：条件 循环