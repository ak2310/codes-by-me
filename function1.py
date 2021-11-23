##def add(a,b):
##    sum=a+b
##    print(sum)
##def avg(a,b,c):
##    print((a+b+c)/3)

import math   
from math import sqrt,factorial,ceil,floor,gcd
print(ceil(16.6))
print(floor((17.2)))
x=factorial(16)
print(x)
print(gcd(20,30))

name="arjun,vijayan,rajani"
sep=' '
print(sep.join(name))#split for making a list and join for separating data

import array
arr=array.array('u',['a','b','c','d','e'])
arr.extend('x')
for ch in arr:
    print(ch)
import sys
#for element in arr:
    #print(element)
a=math.factorial(15698)
print(sys.getsizeof(a))
from array import *