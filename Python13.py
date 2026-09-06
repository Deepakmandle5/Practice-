#break 

for i in range (15):
    print("7 X",i+1,"=",7 * (i+1))
    if( i == 10):
        break
print("break statement work hear and loop breaks")    


for i in range (11):
    if(i==10):
        break
    print("11 X", i+1,"=", 11 * (i+1))
print("break statement work hear and loop breaks")

for i in  range (1,101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("x")
print("Thank you") 

#Continue

for i in range (15):
    if( i == 10):
      print("continue statement work hear and by skip the iteration")
      continue
    print("11 X",i,"=",11 * i)  

for i in range (15):
   if (i==11):
      print("skip the itration")
      continue
   print("7 X",i,"=",7 * i)

for i in (2,3,4,5,6,7,8,9):
    if(i%2!=0):
      continue
    print(i)
        continue
    print(i)
