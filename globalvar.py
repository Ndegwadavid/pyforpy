x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() #this will take the variable x and use it 

#method 2
#when havign two variables inside a code for example the code below


x = "awesome"  #we have this variable 

def myfunc():
  x = "fantastic"    #we have also thi s variable
  print("Python is " + x)

myfunc()
#scenario3
print("Python is " + x) #in this case we have added another variable 
#this time rounf the first variable inside the fuction will be stored locally whereas the 
#other variable will be made globally (the  fantastic value will be made global)
