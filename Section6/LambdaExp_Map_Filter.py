#MAP WORKING

num = [ 1,2,3,4]
def square(num):
    return num**2
print(list(map(square,num)))


mystring = ['Aditya', 'Aryan', 'Dhruv', 'Unzala', 'Soumya']
def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]
print(list(map(splicer,mystring)))


#FILTER FUNCTION WORKING

def check_even(num):
    return num%2==0
mynums = [1,2,3,4,5,6]
print(list(map(check_even,mynums))) #->[False, True, False, True, False, True]

#SO WE USE FILTER FUNCTION FOR THIS
print(list(filter(check_even,mynums))) #->[2, 4, 6]

#LAMBDA EXPRESSION -> Also called as anonymous function -> because it's some functionality is used one time

def sq(num):
    result = num**2
    return result
print(sq(9))

#To make it simple we use lambda expression
sq = lambda num:num**2 #-> lambda paramter: return
print(sq(9))

#Another example
print(list(map(lambda num:num**2,mynums)))

#Another example of the check_even function

print(list(filter(lambda num:num%2==0,mynums)))

#To grab the first letter of the string
print(list(map(lambda name:name[0],mystring)))