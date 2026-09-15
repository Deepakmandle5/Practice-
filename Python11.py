#if else statement in python

a = int(input("entrr your age:"))
print("your age is:", a)
if (a >18):
    print("you are eligible to vote")

else:
    print("you are not eligible to vote")

#conditional operators in python
# >,<,>=.<=,==,!=
#print(a>18) 
#print(a<=18)
#print(a==18)
#print(a!=18)

OrangesPrice = 150
budget = 170
if (OrangesPrice <=budget):
    print("we add 1 kg Oranges to the cart.")
else:
    print("we do not add the Oranges to the cart.")

#elif statements in python

num = int (input("Enter the value of num"))
if (num<0):
    print("Number is negetive.")
elif (num == 0):
    print("Number is zero")
elif ( num >= 50):
    print("Number is bigger")
else:
    print("Number is positiv.") 

# Nested if statement
Number = int(input("Enter the  value "))

if (Number < 0):
    print("Value is negative")
elif (Number > 0):
    if (Number <= 50):
       print("Value is between 1-50")
    elif (Number > 50 and Number <= 100):
        print ("Value is between 51-100")
    else:
        print("Value is greater than 100") 
else:
    print("Value is zero")
