#Immutability -> Strings are immutable data type in python

name = "Aditya"
#name[0] = "R" #this will give an error
# print(name)

#STRING CONCATENATION
#if we need to change the letter of the string then we have to use slicing and then we will concat the string with the + sign

last_letters = name[1:]
print(last_letters)
print("R" + last_letters)

#STRING MULTIPLICATION

letter = "z"
print(letter*10)

#String do not support integer and the string together
print(2+3)
print('2' + '3')

#String Methods

x = "Hi this is a string"
print(x.split()) #this splits the string wherever their is a whitespace
print(x.split('i')) #this splits a string wherever their is 'i' letter come

