
# Loop in python
# For loop

name = 'Shivam'
for i in name:
    print(i,end=", ")
# or    
name2 = 'Raghav'
for i in name2:
    print(i)

colors = [ "Red", "Green", "Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range (20):
    print ( k +1)

for k in range (1 , 201):    
    print(k)

for k in range ( 1, 501):
    print(k)
  
# while loop
i  = 0
while(i < 3):
    print(i)
    i = i+1
#or
i = 0
while( i<36):
    print(i)
    i= i+1

i = int(input("Enter the value:"))
while(i<=45):
    i = int(input("Enter the value:"))
    print(i)
print( "done with the loop condition")


count = 5
while(count>0):
    print(count)
    count = count - 1


# else with the while loop
count = 10
while (count>0):
    print (count)
    count = count - 1
else:
    print("I am inside else")


# Emulate Do while loop in python
while True:
    num = int(input("Enter the value: "))
    print(num)
    if not num > 0:
        break
