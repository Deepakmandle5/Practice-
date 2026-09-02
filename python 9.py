  #find lenght of a string

word ="king ,kingdom"
print(len(word))
print(word[0:6])

tool ="hammer, knife,"
len1 = len(tool)
print("tool is a", len1, "letters words")

#slicing the sring

fruit = "apple" 
applelen =len(fruit)
print(applelen)
print(fruit[0:4])#include 0 but not 4
print(fruit[1:4])# include  1 but not 4
print (fruit[:5])
print(fruit[0:len(fruit)-3])
print(fruit[-1:-4])# don't print anything 
print(fruit[-3:-1])
