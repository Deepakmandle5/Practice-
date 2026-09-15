
#Function Argument in python

#Default argument 
def name(fname, mname = "Arav",lname = "Singh") :
    print("Hello,", fname ,mname,lname)
name("Veer") 

#Key word argument
def name(fname,mname,lname):
    print("Good Morning,",fname,mname,lname)
name(fname ="Arnav", mname ="Veer",lname = "Singh")

#Required arguments
def name(fname,mname,lname = "Singh"):
    print("Good morning",fname,mname,lname)

name("Rohit", "Arnav") 

#Variable lenght Argument
#Arbitrary argument
def name(*name):
    print("Hey,",name[0],name[1],name[2])

name("Arun","Rohit","Singh")

 #Keyword Arbitrary argument
def name(**name):
   print("Heyy,",name["fname"], name["mname"],name["lname"])

name(mname = "Arun", lname = " Singh", fname ="Ravi")

#Return statment

def average (*number):
    sum=0
    for i in number :
      sum= sum +i
    return sum  / len (number)
c = average( 5,8,3,5,9)
print(c)
