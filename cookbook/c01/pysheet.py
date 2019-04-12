#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 1.1 new in python3
# 1.1.1 print is a function
print("this is a function")

# 1.1.2 String is unicode
s = 'care'
print(type(s))
print(s.encode('utf-8'))
print(s.encode('utf-8').decode('utf-8'))
print(len([_c for _c in 'care']))

# 1.1.3 Division Operator
print(1/2)
print(1//2)
print(1./2)

from __future__ import division
print(1/2) 
#0.5
print(1//2) 
#0

# 1.1.4 New dict implementation
import sys
sys.getsizeof({str(i):i for i in range(1000)})

# 1.1.5 Keyword-Only Arguments
def f(a,b, *, kw):
    print(a,b,kw)

f(1,2,kw=3)

# 1.1.6
class ParentCls(object):
    def foo(self):
        print("call parent")

class ChildCls(ParentCls):
    def foo(self):
        super().foo()
        print("call child")

p = ParentCls()
c = ChildCls()

p.foo()
c.foo()

# 1.1.7 remove <>

a = "python3"
print(a != "python2")

# 1.1.8 BDFL retirement

#from __future__ import barray_as_FFLUFL
#1<>2

# 1.1.9 Not allow from module import * inside function
#def f():
#    from os import *

# 1.1.10 add nonlocal keyword
def outf():
    o = "out"
    def inf():
        nonlocal o
        o = "change out"
    inf()
    print(o)

outf()
# change out

# 1.1.11 Extended iterable unpacking
a, *b, c = range(5)
print(a,b,c)
for a, *b in [(1,2,3),(4,5,6,7)]:
    print(a,b)

# 1 [2,3]
# 4 [5,6,7]

# 1.1.12 General unpacking
print(*[1,2,3],4,*[5,6])
[*range(4),4]

def func(*a,**k):
    print(a)
    print(k)

func(*[1],*[4,5],**{"foo":"FOO"},**{"bar":"BAR"})
# (1,4,5)
# {'foo':'FOO','bar':'BAR'}

# 1.1.13 Function annotations
import types
generator = types.GeneratorType
def fib(n: int) -> generator:
    a,b = 0,1
    for _ in range(n):
        yield a
        b,a = a+b,b

[f for f in fib(10)]
# [0,1,1,2,3,5,8,13,21,34]

# 1.1.14 Variable annotaions
# new in Python 3.6
from typing import List
x: List[int] = [1,2,3]
print(x)
#[1,2,3]

from typing import List,Dict
class Cls(object):
    x: List[int] = [1,2,3]
    y: Dict[str,str] = {"foo":"bar"}

o = Cls()
print(o.x)
print(o.y)

# 1.1.15 Core support for typing module and generic types
# new in Python 3.7
from typing import Generic, TypeVar
from typing import Iterable

T = TypeVar('T')
class C(Generic[T]): ... 

def funcg(l: Iterable[C[int]]) -> None:
    for i in l:
        print(i)

funcg([1,2,3])
'''
1
2
3
'''

from typing import Iterable
class CC:
    def __class_getitem__(cls,item):
        return f"{cls.__name__}[{item.__name__}]"

def funcc(l: Iterable[CC[int]])->None:
    for i in l:
        print(i)

funcc([1,2,3])

# 25+19 

