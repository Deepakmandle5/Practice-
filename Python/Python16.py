
#Tuples in python

tup1 = (1,3,5,7,9)
tup2 = (1,3)
tup3 = (20)
tup4 = (20,)

print(len(tup1))
print(type(tup1),tup1)
print(type(tup2),tup2)
print(type(tup3),tup3)
print(type(tup4),tup4)

#Tuple Index
tup = (2,4,6,8)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

#Negative indexing
print(tup[-4])
print(tup[-3])
print(tup[-2])
print(tup[-1])

#Check for item
if 2 in tup:
    print ("Yes")
else:
    print("No")

if 24  in tup:
    print("Yes")
else:
    print("No")

#Range of Index

Tupl = tup[0:3]
print(Tupl)

Tupl1 = tup1[:4]
print(Tupl1)

Tupl1 = tup1[4:]
print(Tupl1)

#concatenating two tuples
k = tup1 + tup2
print(k)

#Tuple method

Tup3 = (5,10,15,20)
print(len(Tup3))

print(max(Tup3))

print(min(Tup3))

print(sum(Tup3))

print(sorted(Tup3))

print(Tup3.count(5))

print(Tup3.index(15))

#Tuples are immutable
