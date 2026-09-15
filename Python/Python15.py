
#List in python

Students = ["Ravi","Krishna", "Adi" ,"Arun","Raghav"]
Marks =[18, 15, 17, 19, 13]
print(Students)
print(Marks)

Nameswithmarks =["Ravi",18,"Krishna",15, "Adi",17 ,"Arun",19,"Raghav",13]
print (Nameswithmarks)

#List index
#Positive indexing
Num =[25, 37, 43, 49,]
print(Num)
print(Num[0])
print(Num[1])
print(Num[2])
print(Num[3])
#print(Num[4])don't print(Num[4])because index 4 not exist

#Negative indexing  
print(Num[-4])
print(Num[-3])
print(Num[-2])
print(Num[-1])
#print(Num[-5])don't print(Num[-5])because index -5 not exist

#Convert Negative to positive indexing
print(Num[-2])#negative indexing

print(Num[len(Num)-2])#positive indexing

print(Num[4-2])#positive indexing

print(Num[2])

#Check wheather an item present in list?

if 49 in Num:
    print("Yes")
else:
    print("No") 

if 50 in Num :
    print("Yes")
else:
    print("No")           

Name = [ "rahul", "mahesh","arav","arnav", "arun"]

if "rahul"in Name:
    print("Yes")
else:
    print("No") 

if "ra" in "rahul":
    print("Yes")    

#Range in indexing
print(Name)
print(Name[:])  
print(Name[2:5])# using positive indexing
print(Name[-5:-3])# using negative indexing
print(Name[1:4])
print(Name[1:4:2])  

#List comprehension
lst1 = [i for i in range(10)]
print(lst1)

lst2 = [i*i for i in range(10)]
print(lst2)

names =["Suresh","Rohit","Raghav","Jeet","Meet"]
nameWith_0 =[ item for item in names if(len(item)> 4)]
print(nameWith_0)

#List Method
#list.append()
#list.sort()
#list.sort(reverse = True)
#list.reverse()
#print(list.index())
#print(list.count())
#list.copy()
#list.insert()
#list.extend()
#list3 = list1 + list2

l1 = [1,2,3,4,5,6,7]
print(l1)
l1.append(8)
print(l1)

l2 = [25,22,1,5,17,97,56,]
print(l2)
l2.sort()# for ascending
print(l2)
l2.sort(reverse=True)#for decending
print(l2)

l3 = [1,3,5,7,9,5,5]
print(l3)
print(l3.index(5))
print(l3.count(5))
l3.reverse()
print(l3)

l4 = [2,4,6,8,10]
print(l4)
m = l4.copy()
print(m)

l5 =[11,12,13,14,15]
print(l5)
l5.insert(1,55)
print(l5)

m2 = (16,17,18)
l5.extend(m2)
print(l5)

#concatenating two lists
k = l5 + l1
print(k)


