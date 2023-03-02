import time

import pytest, yaml


# a='C:\Users\Administrator\Desktop\工具'
# print(a)
# a=[1,2,3,4,5,11,55,21,25,23,16]
# b=a[1:2]
# print(b)
# a='\'\'\'a\'\'\''
# print(a)
# a='"a"'
# print(a)
# a='wqeqe'
# b=2
# print('wqe+%s'%a+'+%d'%b)
# print(f'wqe+{a}+{b}')
# a=1
# b=1
# c,d=['1'],['2']
# print(a==b)
# print(a is not b)
# print(id(a))
# print(id(b))
# print(c==d)
# print(c is not d)
# print(id(c))
# print(id(d))
# a=False
# b=2
# if a:
#     print('123')
# else:
#     print('321')
# a=1
# b=2
# # if a>b:
# #     print('1')
# # else:
# #     print('2')
# c=3 if a>b else 4
# print(c)
# for i in range(1,5,2):
#     print(i)
# a=1
# while a<10:
#     a+=1
#     if a==5:
#         a+=1.5
#         print('里面的%s'%a)
#         continue
#     print(a)

# for i in range(0,11,2):
#     print(i)
#     a=a+i
#     print('a结果%d'%a)
# a=0
# b=0
# while a<11:
#     b=b+a
#     a+=2
#     print(b)
# from random import randint
# a=randint(1,5)
# for i in range(10):
#     a = randint(1,5)
#     print(a)
# b=0
# while b==0:
#     a = int(input('输入'))
#     if a<100:
#         print('小了')
#     elif a==100:
#         print('恭喜')
#         break
#     else:
#         print('大了')
# a=1
# print('asad',a)
# a=[i for i in range(10) if i%2==0]
# print(a)
# a=[]
# a.extend('weqewq')
# a.extend([1,2,3])
# a=[1,3,2,3]
# a.insert(0,'wqeqe')
# print(a)
# a=[1,2,3,4,5]
# a.pop(2)
# print(a)
# b=a.pop()
# print(b)
# print(a)
# a=[1,2,3,4,5,6,7,5,3,2,1]
# a.remove(3)
# print(a)
# a=['231','32131','1']
# a.sort(key=len)
# print(a)
# a=[]
# for i in range(0,11,2):
#     if i==2:
#         a.append(i+100)
#     else:
#         a.append(i)
# print(a)
# a=[i+100  if i==2 else i for i in range(0,11,2)    ]
# print(a)
# a=1,2,3,4,5
# print(type(a))
# a=tuple('wqeqwe')
# print(a)
# a=1,
# print(a)
# a=1,2,3
# b,c,d=4,5,6
# print(b,c,d)
# a={1,2,3}
# b=set('12234')
# c={x for x in range(10)}
# print(a,b,c)
# a=set()
# a.add('123')
# a.update('231321')
# print(a)
# a={1,2,3,4,5}
# a.remove(2)
# a.discard(3)
# print(a)
# a={3,6,2,4,5}
# a=set('qwesazcgtu')
# for i in range(20):
# print(a)
# a={1,2,3}
# b={4,5,1,2}
# print(a.difference(b))
# print(a - b)
# print(b - a)
# print(a.union(b))
# print(a | b)
# print(a.intersection(b))
# print(a & b)
# a={'as':'wqe','asd':'qwe'}
# b=dict([('1','2'),('4','5')])
# c=dict(a=1)
# print(type(a),a)
# print(b)
# print(c)
# d={x:y for x,y in [(1,2),(3,4)]}
# print(d)
# a={'as':'wqe','asd':'qwe'}
# c=a.keys()
# d=a.values()
# print(c,d)
# b=a.items()
# print(b)
# a={'as':'wqe','asd':'qwe'}
# a.get('123')
# a.pop('as')
# print(a)
# a={'qq':1,'ww':2,'33':3}
# c=[]
# for i,p in a.items():
#     if p>1:
#         c.append(i)
# print(c)
# a=[1,2,23,5,4,3,2,1,2,3,4,5,6,4,3,2,1,11,2,4,5,6]
# q=a.count(3)
# print(q)
# b={}
# for i in a:
#     if i not in b:
#         b[i]=1
#     else:
#         b[i]+=1
# print(b)
# a = {'q': 1, 'w': 2, 'r': 3}
# b = {}
# for z, x in a.items():
#     b[x] = z
# print(b)
# c = {x: z for z, x in a.items()}
# print(c)
# def a(b,c,d='123'):
#     print(b,c,d)
# a('2','3')
# a('6','7','0')
# def a(*args):
#     for i in args:
#         print(i)
# b=['2','3','4']
# a(b)
# a(*b)
# def a(b):
#     return b*b
# print(a(2))
# c=lambda x:x*x
# print(c(2))
# a=[('wqeq',23),('qwe',25),('zxc',11)]
# a.sort(key=lambda x:x[1])
# print(a)
# b = sorted(a, key=lambda x: x[1], reverse=True)
# print(b)
# class a():
#     def b(qq):
#         print('1')
#     def c(qq):
#         print('2')
# aa=a()
# a.c(aa)
# a = 1
# def say():
#     print ('调用了全局方法')
# class people:
#     a = 100
#     def say(self):
#         print ('调用了类的方法'  )
#     def do(self):
#         say()
#         self.say()
#         print ('a = ',a)
#         print ('self.a = ' , self.a)
# p = people()
# p.do()
# class a():
#     num=1
#     @classmethod
#     def a_1(cls):
#         print('类方法',cls.num)
#     def __init__(self):
#         a.num+=1
#     def b(self):
#         print('实例方法',self.num)
#     @staticmethod
#     def a_2():
#         print('静态方法')
# a.a_1()
# a1=a()
# a1.b()
# a.a_1()
# class a333():
#     num='123'
#     _num='789'
#     __num='456'
#
#     @property
#     def passwd1(self):
#         return self.__num
#
#     @passwd1.setter
#     def passwd1(self,qqq):
#         self.__num=qqq
# aa1=a333()
# aa1.passwd1='321'
# print(aa1.passwd1)
# class a():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class b(a):
#     def __init__(self,name,age,school):
#         super().__init__(name,age)
#         self.sch=school
# aa=b('名字','qqq','213')
# print(aa.name,aa.sch,aa.age)
# class a():
#     def qqq(self,name):
#         if name>10:
#             print('父类',name)
#         else:
#             print('小于10')
# class b(a):
#     def qqq(self,name):
#         if name<5:
#             print('子类',name)
#         else:
#             print('大于5')
# aa=b()
# aa.qqq(21)
# aa=1
# def a(qq,dd):
#     return qq/dd
# try:
#     print(a(1,1))
# # except ZeroDivisionError as e:
# #     print(e)
# #     print('移除')
# except IndexError:
#     print('异常2')
# else:
#     print('不知道啥异常')
# finally:
#     print('qweqwe')
# def a(num):
#     if num<0:
#         raise Exception('有点问题:',num)
#
# a(-1)
# class lxl_exece(Exception):
#     def __init__(self):
#         print('lxl')
#
# def a(num):
#     if num<0:
#         raise lxl_exece
#
# a(-1)
# def a(aa,bb):
#     reqq = aa + bb
#     return reqq
#
# num1=5
# num2=11
# num3=a(num1,num2)
# print(num3)
# with open('abc.txt','r',encoding='utf-8') as ss:
#     aa=ss.read()
#     print(aa)
#     bb=ss.readlines()
#     print(bb)
#     ss.seek(0)
#     bb=ss.readlines()
#     print(bb)
#     ss.close()
# with open('abc.txt','w+',encoding='utf-8') as ss:
#     a=ss.read()
#     print(a)
# def a():
#     dd=1
# print(a())
# import pytest
# @pytest.mark.parametrize('aaa,bbb',[('111','222'),('333','444'),('qwe','qwe')],
#                          ids=['请问','z阿斯顿2','请问'])
# def test1(aaa,bbb):
#     print(aaa+'qweeeeeeeeeeeeeee')
#     print(bbb)
# import pytest
# @pytest.mark.parametrize('a',[1,2,3,4,5])
# @pytest.mark.parametrize('b',[11,22,33,44,55])
# def test1(a,b):
#     print(a)
#     print(b)
# def test_d1(fix2,fix3):
#     assert 1==2
# def test_d2(fix2):
#     assert 1==1
#     print('用例之中'+'   '+fix2)
@pytest.mark.run(order=2)
def test_aa3():
    assert 1 == 1
    print('123')

@pytest.mark.flaky(reruns=5,reruns_delay=1)
@pytest.mark.run(order=1)
def test_aa1():
    assert 1 == 2
    time.sleep(1)
    print('456')


def test_aa2():
    with open('./yaa.yaml', 'r', encoding='utf-8') as f:
        f1 = yaml.safe_load(f)
        time.sleep(1)
        print(f1)
