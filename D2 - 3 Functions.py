# -*- coding: utf-8 -*-


# 1  
def testfn(x):
    return x**x

print(testfn(2))

# 2
def f(x,y):
    return x*y

print(f(3,4))


# 3
def hello(name="Richmond"):
#  name = str("Richmond")
  if name:
    print ("Good Morning " + str(name))
  else:
    print("Hello World") 
#  return 
  
hello('shail')

# 4
def run(y):
  for x in range(y):
     if x <= 2:
       print("less than eq 2")
     else:
       print(x+2)
run(50)


# 5
# Define plus() function
def plus(a=3,b = 2):
  return a + b
  
# Call plus() with only a parameter
plus(a=1)

# Call plus() with a and b parameters
plus(a=1, b=3)

# 6
# Define a  function to accept a variable number of arguments
def any(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum  
any(20,30,100,-200)

# 7
def greetings(x):
	"""This function greets to the person passed in as	parameter"""
	print("Hello, " + x + ". Good morning!")
   
greetings("Tangee")
greetings("Timani")
greetings("Ross")
any(10,20)

# 8
#Example 2
def cube(num):
	"""This function returns the cube of the entered number"""

	if num >= 0:
		return num*num*num
	else:
		return +(num*num*num)
    
cube(9)
cube(-9)
cube(724356827)


# 9 
#Passing value to a function
def my_function(country = "Canada"):
  print("I live in  " + country)

my_function("Canada")
my_function("India")
my_function()
my_function("Germany")


# 10
#Returning values
def my_function(x):
  return x * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

cube(10)

#11
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# 12
def greet(*names):
   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Debora","Mao","Steve","John")

# factorial - recursive functions
# An example of a recursive function to
# find the factorial of a number
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x in (0,1):
        return 1
    else:
        return (x * factorial(x-1))

num = 1
print("The factorial of", num, "is", factorial(num))	


# 13
def changeme( mylist ):

   mylist.append([1,2,3,4]);
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values of the function: ", mylist)

#Lambda function
x = lambda a: a*a
print(x(8))

x = lambda a,b: (a+b)/2
print (x(8,2))

x = lambda a,b,c: (a+b+c)/3
print(x(1,2,3))


#1
def nn(x,y):
    return x*y

nn(3,6)

#same thing done with lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)
print(mydoubler(11))

# 2
def cube(y): 
    return y*y*y
  
g = lambda x: x*x*x 

print(g(3)) 
print(cube(3))

# program that returns the odd numbers from an input list
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 


#The map() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item. Example:
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 

#The reduce() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new reduced result is returned. This performs a repetitive operation over the pairs of the list.
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 