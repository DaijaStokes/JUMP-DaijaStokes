# -*- coding: utf-8 -*-

import numpy as np

#Regular list

list1 = [10, 20, 30, 40, 50, 100]
list2 = [100, 200, 300, 400, 500,1000]
list2+10
list3= list1+list2

#Numpy arrays
a  = np.array([1,9,8,3])
c  = np.array(list2)

#Mathematical operations on arrays
a + 10
a*10

#Compare the array operations with list operations
list1*3
list1+10 #Error

#Adding anot
list1.append(200)
print(list1)

a.append(200)#Error

#Removing an element from a list vs  array
list1.pop(3)
a.pop(2) #Error
b = np.delete(a,1)
list1.remove(10)
a=a.remove(9) #error

from array import *
array1 = array('i', [10,20,30,40,50])

array1.insert(1,60)

print(array1)
for x in array1:
 print(x)

#Array operations
import numpy 
a= numpy.array([1,2,3,4])
b = numpy.array([5,6,7,8])

a1= numpy.array([a+b])
a2= numpy.array([b - a])
a3= numpy.array([a*b])

a5= numpy.array([a%b])
a6= numpy.array([a**b])

c = a+b
print(a+b)

print (a1)
print(a2)
print(a3)
#print(a4)
print(a5)
print(a6)

#Concatenation of arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.concatenate([x, y])

print(z)

#Splitting a list
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [2, 5])

print(x1, x2, x3)

#RESHAPING AN ARRAY
arr1 = np.array([1, 2, 3])
arr2 =arr1.reshape(1,3)    