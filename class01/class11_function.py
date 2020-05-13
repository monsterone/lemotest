# -*- coding: utf-8 -*-
# @Time     : 2020/3/16 22:46
# @Author   : Monster
# @Email    : 945534456@qq.com
# @File     : class11_function.py

#【11】python 内置函数
#print input len type str int float list range
#pop append insert keys split replace strip
#remove claer

#总结一下函数的特点：
#可以重复使用

#函数的语法：def 关键字
#函数名命名的规范：小写字母分开 不能以数字开头 不同的字母之间用下划线隔开
#def 函数名(参数1,参数2,参数3...):
    #函数体：你希望这个函数去给你实现什么功能？

#调用： 函数名()


#1 无参数
def da_lao():
    print("我是monster")

#调用函数
# da_lao()

#2 形参/位置参数
def da_lao(name): #形参/位置参数
    print(f"{name}我是monster")
    # print("{0}我是monster".format(name))

#调用函数
# da_lao("怪兽")
# da_lao("haha")


#3 默认参数
def da_lao(name="guaisou"): #默认参数
    print(f"{name}我是monster")

# da_lao("怪兽")
# da_lao()



#test:请把1-100的连续整数相加功能 写成一个函数
# 第一步：先用代码实现功能 还可以选取一组数据来证明自己的 是否正确
# 第二步：变成函数 加 def
# 第三步：想办法提高代码的复用性
def add(m,n,k=1):
    sum=0
    for i in range(m,n,k):
        sum+=i
    return sum

# print(add(1,101))


#镜像文字(练习题)
#字符串的 translate
#swapcase

#测试代码
if __name__ == '__main__':  #主程序的执行入口 只有当你在当前模块下执行的时候 才会执行

    print("开始执行")
    print(add(1,101))
    print("结束执行")