#string methods in python
#upper(), lower(), rstrip(), split(),
#captalize(), center(), count()
#endeswith(), find(), index(),
#isalphanum(), isalpha(), istitle(), 
#isslower(), isprintable(), isspace()
# isstartswith(), title(), swapcase(),


'''sting are immmutable '''
x  = "Aeroplane"
print(x.upper())

print(x.lower())

y = "!! Rocket !!"
print(y.rstrip("!"))

print(y.replace("Rocket", "Missile"))

print(y.split(" "))

assingnment = "introduction to operating system"
print(assingnment.capitalize())

str1 = "Welcome to the webpage"
print(len(str1))#show the lenght of str1

print(len(str1.center(50)))#show the lenght of str1 after center 

print(str1.center(50))#str1 after center with 50 spaces

str2 = "Welcome to the application..."
print(str2.count("t"))# count the number of aplhabet 't' repeat in string

print(str2.endswith("..."))#check the string ends with "..." or not

print(str2.find("to")) #find the index of the first occurence of "to"

print(str2.index("the"))

str3 = "Drivingthecarisfun"

print(str3.isalnum())#check the string is alphanumeric or not

print(str3.isalpha())#check the string is alphabetic or not

print(str3.istitle())#check the first letter of the string is in capital or not

str4 ="drive the car is fun"

print(str4.islower())#check the string is in lower or not

print(str4.isprintable())#check the string is printable or not 

print(str4.isspace())#check the string is space or not

print(str4.startswith("drive"))#check the string starts with "drive" or not

print(str4.swapcase())#swap the case of the string(lower or upper)

print(str4.title())#covert the first letter of each word into capital letter
