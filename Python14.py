
#Function in python

def calculateaddition(a,b):
    add = (a+b)
    print (add)

def isGreater(a,b):
    if (a>b):
      print("First number is greater") 
    else:
       print("Second number is greater") 

def isodd(a,b):
    if (a%2!=0):
       print ("First number is odd")  
    else:
       print("first number is even")
    if (b%2!=0):
       print("Second number is odd")
    else:
       print("Second number is even") 

def isLesser(a,b):
   pass   

a = int(input("Enter the value:"))
b = int(input("Enter the value:"))
calculateaddition(a,b)
isGreater(a,b)
isodd(a,b)

c =  int(input("Enter the value:"))
d =  int(input("Enter the value:"))
calculateaddition(c,d)
isGreater(c,d)
isodd(c,d)
