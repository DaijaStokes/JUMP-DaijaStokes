# -*- coding: utf-8 -*-

#If and else   
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

myname="Andy"
if myname == 'Andy1':
    print("correct")
else:
    print("Error")
        
i = 20
if (i > 15): 
   print ("10 is less than 15") 
print ("I am Not in if") 


dig =20

if dig == 20:
    print ('Correct')
else:
    print ("error")


N = 16

if N%2 !=0:
    print("odd")
elif N%2 ==0 and (2<=N<=5):
    print("Even but within 2 and 5")
elif N%2 ==0 and (6<=N<=20):
    print("between 6 and 20 even")
elif N%2 ==0 and N>20:
    print("even more than 20")

i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15")
           
i = 20
if (i == 10): 
    print ("i is 10") 
elif (i == 15): 
    print ("i is 15") 
elif (i == 20): 
    print ("i is 20") 
else: 
    print ("i is not present") 

score_theory = 40
score_practical = 45
if(score_theory + score_practical > 100):
    print("Invalid score. Please check the input.")

score_theory = 60
score_practical = 20

if(score_theory > 50):
    print("Please check the input score for 'Theory'.") # Step 2.1
elif(score_practical > 50):
    print("Please check the input score for 'Practical'.")  # Step 2.2
else:
    print("Score validated. Your total is: ",score_theory + score_practical) # Step 3

#short    
if a > b: print("a is greater than b")

#if else short
print("A") if a > b else print("B")

#multiple else statements on the same line
print("A") if a > b else print("=") if a == b else print("B")
    
#Test if a is greater than b, AND if c is greater than a:
a =1
b=4
c=7

if c > b and b > a:
  print("Both conditions are True")
  
# OR condition
if c > b or b > a:
  print("At least one condition is True")

#nested if and else
num = -8

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
    
#Grouping using if and else
num = 150

if num >0 and num <= 10:
    print("between 0 and 10")
elif num >10 and num <= 100:
    print("between 10 and 100")
elif num >100:
    print("More than 100")


        
        
        

# Write a Python program to convert month name to a number of days.
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

month_name = "November"

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name")    
    
    
    
#Exercise ===================================================================

# 1 - if a is greater than b by 10 or more then print Yes else No
a = 50
b = 10

 
#2 
# check if num is positive or negative or zero and 
# display -ve, +ve or zero 
num = 0.03


# 3 check if the given remainder is odd or even and print it as odd,even
num = 6
b = 33%num

# if b

# elif

# else:
    
    