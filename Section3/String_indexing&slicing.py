# string indexing means single index and slicing means subsequences.

mystring = "Hello World"

#grab single character -> indexing

print(mystring[0]) # -> H
print(mystring[8]) # -> r

#reverse indexing

print(mystring[-2]) # -> l

#SLICING 

print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[1:3])


#STEPS

print(mystring[::2])
print(mystring[::-1])  #reverse the string 
print(mystring[2::2])
