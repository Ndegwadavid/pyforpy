#the data types in python are 
str #txt type
int , float , complex  #numeric type
list , tuple , range #sequence type
dict #mapping type
set , frozenset #set type
bool #boolean types
bytearray , bytes ,  memoryview #binary types

#to get the dat type we do a 
x = 5
print(type(x)) #this will print the dat type of the variable

#setting the dat type 
x = "Hello World"
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x)) #this will print list

#memory dat type view
x = memoryview(bytes(5))
print(x)
print(type(x))

#there is a difference between a list and a tuple 
x = ("Aplle" , "Banana", "Apple") #this is a tuple and uses brackets
x = ["Aplle" , "Banana", "Apple"] #this is a list and uses block brackets
x = x = {"Aplle" , "Banana", "Apple"} #this is a set and uses curly braces

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x: #frozen dat types
print(type(x)) 




