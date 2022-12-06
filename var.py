x = 5
y = "Hello world"

print(x)
print(y)

#print("good morning my neighbours")

#comments in python are indented with the #value

print("good morning my people") #this is a comment 


#a case where a variable changes with immediate even if they had been set
x = 4    # x is a type of int
x = "sally" #x is now a type of string 
print(x)
#this case the value printed will be sally 

#if we want the above not to happen we can specify the data type of a variable through casting
x = str(3)  #string will be in quotation marks 
y = int(3)   # does not change literally
z = float(3)  #this will be 3.0 beacuse floats are reuslted to decimal 

#GIVING VARIABLES NAMES
#variables rules in python:
"""
                          variable must start with a letter or underscore
                          cannot start with a number
                          are case sensitive
                          cannot contain non alfaneumerics and non alphabets
                          """
                          #example
myvar = "John"
my_var =  "John"
my_var = "John"
myVar = "John"
print(myvar)
print(my_var)
