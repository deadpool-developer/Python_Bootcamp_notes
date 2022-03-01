#1. Tuples are very similar to lists. However they have one ket=y difference -> Immutability (cannot be changed)
#2. Once an element is inside a tuple, it can not be reassigned
#3. Tuples use parenthesis : (1,2,3)

t = {1,2,3,4}
my_list = [1,2,3,4]

#indexing and slicing is similar to list

#Count/index in tuples

t1 = (1,1,2,1,3,4)
print(t1.count(1))  #returns the count of 1
print(t1.index(1))  #returns the first index
