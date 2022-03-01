#1. Lists are ordered sequences that can hold a variety og objects types.
#2. They use [] brackets and commas to separate objects in the list.
#    [1,2,3,4,5]
#3. Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off to them.

my_list = [1,2,3]

string_list = ['String' , 100, 23.2]
print(len(string_list))

my_indexing_list = ['one', 'two' , 'three']
print(my_indexing_list[0]) #indexing
print(my_indexing_list[1:])  #slicing
print(my_indexing_list + my_list) #Concatenation

#LISTS IS MUTABLE -> Elements can be changed

string_list[0] = "Aditya"
print(string_list)

#To add the new element at the end of the list


my_list.append(4)  #adds the element at the last to the list
print(my_list)

#To remove the item from the list we use pop method -> by default it has -1

my_list.pop()
print(my_list)  #deletes the element from the end of the list

#TO remove the item from any of the index we just pass the index of the string in the pop method

string_list.pop(0)
print(string_list)  #pops out the first element from the list

#SORT

sorting = [3,2,1,4,3,5,6,2,1,7,8]
sorting.sort()
print(sorting)  #sort the element

#Sorting of the list at place so if we try to store it anywhere then it will give nothing and it's type is Nonetype
sorting_list = sorting.sort()
print(sorting_list)  #Gives output as None

#REVERSE
sorting.reverse()
print(sorting)  #reverse the string

#To access the element in the nested list
a = [1,2,[3,4]] #want to access 4
print(a[2][1])  #gives 4
