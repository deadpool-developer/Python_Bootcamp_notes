#RANGE FUNCTION 

mylist = [1,2,3]
for i in range(0,11,2): 
    print(i)

print(list(range(0,11,2)))  #returns the list of the even numbers


#ENUMERATE FUNCTION

#Without using enumerate
index_count = 0
for letter in "abcde":
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1
#OUTPUT
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

#Using enumerate function
word = "abcde"

for item in enumerate(word):
    print(item)              #returns the tuples

#OUTPUT
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

for i,v in enumerate(word):  #tuple unpacking
    print(v)
    print(i)



#ZIP FUNCTION -> Similar to the jacket zip -> zip up the things

list1 = [1,2,3,4]
list2 = ['a','b','c','d']
list3 = [100,200,300]

for item in zip(list1,list2,list3):
    print(item)

#OUTPUT

# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)

###If the list is uneven, the list with the shortest data will be considered

print(list(zip(list1,list2,list3)))
#[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

###we can also unpack it

#IN KEYWORD

print('x' in [1,2,3])   #list

print('a' in ' a world')  #string

print('mykey' in {'mykey' : 345})   #dictionary

d = {'mykey':345}
print(345 in d.values())  #dictionary values


#MIN & MAX function

a = [2,4,3,1,32,4,4,2,2,11,23,4,44]
print(min(a))
print(max(a))

#RANDOM LIBRARY

##Shuffle 
from random import shuffle

myshuffle = [1,2,3,4,5,6,7,8,9,10]
shuffle(myshuffle)
print(myshuffle)  ##this shuffles the elements in the lists and do not return anything

##To generate random integer

from random import randint

print(randint(0,100))  ##prints the random number between 0-100

##
