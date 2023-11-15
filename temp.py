# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# variable syntax 
# 1. a variable name shoul not start with numeral that to say a number or a 
#    spacial character unless its an underscore _
#    num, number, _number but not 1mumber or 1num or #num or $num or %num 
# 2. never use spacial key words as variable name forexample class, def, case
#    etc
# 3. a varible name shoul not start with a capital letter unless its a class 
#    name
# 4. never leave a space in avariable name eg my number that space btn
#   incase of such senario (composite name) you can you an underscore eg 
#   my_number or myNumber
# 5.always use relatable variable names  eg num1, num2 for numbers
# 6. 

#21st october 2023
#what is an operator is real world?
#define an operand

#delaring and initializing 
salary = 20000  #assigned an integer
print(f"salary assigned: {salary},{salary}" ) #f tells a computer that expect a variable ie format

tax = (salary*30)/100
#print("salary assigned: "+  salary )# you can not concatinate data not of same type

salary_ = "osman"  #assigned a string
print(salary)

print(f"salary assigned: {salary}" )

print("salary assigned: {salary}" )

print("salary assigned: ",  salary ) #with comma it does not matter int or string

# print("salary assigned: "+  salary ) #with a plus expect string
salaries = [] #a vaariable that is prepared to store more than one value and is 
              #prepared to be manuplated  its called a list
              # the values in the list are mutable 

#no manuplation and no mutability this variable is called a tupple
# whereas when you need to store values without duplication, this variable is called a set
# and without any order
# list are expensive because of there mutability ie memory expansion
set = () # identifying a set


#saturday 28th October 2023
#coding is the actual practice of writing code
#programming is broader than coding, it engalfs the coding
#group of statement maKe up a code
#single instruction to a computer make up a statement
# group of statements that are related to one another is called a block of code

#A named block of code is called a function e.g line 64,65 if block
#its fully contained e.g my_salary on line 67
# a function is also a variable though its extensible ie it can take on other 
# variables with in itself
# fuctions are memery consuming or costly compared to a loop 
#typesof function
# static and dynamic function
# when you create a function you have to call it
#A function is not called, its invoked

#A file of python is called a module or script and has an extension of .py
#A statemant that evaluates to something is called an expression

if salary <= 20000:
    print("My guy work harder")

def my_salary ():
    if salary <= 20000:
       print("Your BROKE!!!")
#      my_list = []

my_salary()

def my_salary2 (salary):
    if salary <= 20000:
        print("Your BROKE DALA")
























