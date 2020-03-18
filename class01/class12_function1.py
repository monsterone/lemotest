# -*- coding: utf-8 -*-
# @Time     : 2020/3/17 22:52
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class12_function1.py

#【12】 函数   (参数)

##位置参数、默认参数
"""
def add(m,n,k=1): #形参/位置参数
    sum=0
    for i in range(m,n,k):
        sum+=i
    print("最后的结果值：{0}".format(sum))

add(1,10,2)  #实际参数  #25
#默认情况下：按顺序赋值

add(m=1,k=10,n=2)      #1


#默认参数(def add(m,n,k=1)，默认参数必须放在位置参数后面
add(1,10) #可以少

# def add(m,n=4,k=1)
# add(2,k=1) #这样可以跳过n,n有默认值
"""
#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------

# return 当你调用函数的时候 就会返回一个值 return后面的表达式
# return 在函数里面相当于一个结束符号 表示函数到此为止 后面的代码不会执行
#什么时候用？

def add(m,n,k=1):
    sum=0
    for i in range(m,n,k):
        sum+=i
    return sum

# print("return返回的值",add(1,101))

#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------
##动态参数/不定长参数 *args arguments
#在函数内部体现为元祖
def make_sandwich(a,b,c,d):
    print("您的三明治包含了{0}、{1}、{2}、{3}".format(a,b,c,d))
# make_sandwich("生菜","鸡蛋","培根","牛肉")

def make_sandwich2(*args):
    # print(args)
    all=""
    for item in args:
        all+=item
        all+=" 、"
    print("您的三明治包含了"+all)

# make_sandwich2("生菜","鸡蛋","培根","牛肉")

#---------------->>>>>>>>>分割线<<<<<<<<<<<<<--------------
##关键字参数 key-value  **kwargs key word  必须加**
#在函数体现为字典
def kw_function(**kwargs):
    print(kwargs)

# kw_function(x=1,y=2) #{'x': 1, 'y': 2}


def add_all_num(a,*L,**kwargs):
    print(L)  #元祖    #(2, 3, 4, 5, 6)
    sum=0
    for item in L:
        sum+=item
    print("字典和为",sum)  #字典和为 20
    print("a的值",a)       #a的值 1
    print("kwargs值",kwargs)

add_all_num(1,2,3,4,5,6,x=1,y=2)
