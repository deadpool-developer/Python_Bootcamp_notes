#Often we inject a variable into the string for printing:
from unittest import result


my_name = "Aditya"
print("Hello " + my_name)

#There are multiple ways to fromat strings for printing variables in them,this is known as string interpolation

#Two methods are their to perform this:
#1. .format() method
#2. f-strings (formatted string literals) -> new method

# .format() method ->syntax: "String {}".format("Something that needs to be their in {}")

print("Hello everyone, my name is {} ".format("Aditya"))

# One advantage of using the format string is that, the elements are entered in the sequence in which they are passed

print("The {} {} {}".format("fox", "brown" , "quick"))
#this passes the same sequence as they are entered
#Now if we want to enter the words not in the order they are passed than pass the index in the {}

print("The {2} {1} {0}".format("fox", "brown" , "quick")) #this entered like the index passed
print("The {0} {0} {0}".format("fox", "brown" , "quick")) #we can repeat the values also

#if we do not want to pass the indexes and we want to assign the keywords

print("The {q} {b} {f}".format(f ="fox", b ="brown" ,q = "quick"))

# FLOAT FORMATING -> {value:width:precisionf}
result = 100/777
print(result)
print("The {r:1.3f}".format(r = result))  #width is used for whitespace
#The float fromating helps in making the float number precised


#F STRINGS -> python 3.6

name = "Aditya"
print(f"Hello, his name is {name}")