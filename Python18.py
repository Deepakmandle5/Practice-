
# Tuples operations for manupulating tuples

Tuple =("Ram","Raghav","Shivam","Hari","Rahul")
temp =list(Tuple)

temp.append("Rohit") # add item

temp.pop(3) # remove item

temp[2]="Robert" # change item

Tuple = tuple(temp)
print(Tuple)

Tuple1 =(1,2,3,2,4,5,6,7,3,5,6,8,)
res = Tuple1.count(4)
print('Count of 4 in Tuple1 is:',res)
res1 =Tuple1.index (3)
print('Index of 3 in Tuple1 is:',res1)
res2 = Tuple1.index(3,6,10)
print('Index of 3 in Tuple1 is;',res2)
