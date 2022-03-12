#Syntax of for loop

my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)


my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)
    print('Hello')


#check for the even

for num in my_list:
    if num%2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')


#Sum of all the numbersv
list_Sum = 0
for num in my_list:
    list_Sum += num
print(list_Sum)

#Itrating over the strings

my_string = "Hello World"
for letter in my_string:
    print(letter)

#Iterating over the tuples

tup = (1,2,3)
for item in tup:
    print(item)

#Tuples unpacking

unpack = [(1,2),(3,4),(5,6),(7,8)]
print(len(unpack))  #returns 4

#if we write the for loop like this 
for item in unpack:
    print(item)    #this will return the tuples.

#But if we want to extraxt the numbers out of the tuples we write

for (a,b) in unpack:
    print(a)
    print(b)  


#ITERATE OVER THE DICTIONARY

d = {'k1':1, 'k2':2, 'k3': 3}
#for item in d:  -> returns the key
for item in d.items():
    print(item)  #returns the key value pairs in the form of tuples

#To print the key /  value of the dictionary

for key, value in d.items():
    print(value) #returns the value 
    print(key)  #return the keys

for value in d.values():  #to return the values only
    print(value)