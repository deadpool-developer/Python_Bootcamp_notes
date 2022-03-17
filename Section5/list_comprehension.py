#When we append the list item using the for loop, instead of using the for loop we use list compreshension

from ctypes import resize


mylist = []
mylist_items = "Hello Aditya"

for letter in mylist_items:
    mylist.append(letter)

print(mylist)  # --> ['H', 'e', 'l', 'l', 'o', ' ', 'A', 'd', 'i', 't', 'y', 'a']

#USING LIST COMPREHENSION
mylist_comp = [letter for letter in mylist_items]
print(mylist_comp)   #--> ['H', 'e', 'l', 'l', 'o', ' ', 'A', 'd', 'i', 't', 'y', 'a']

#PRINT EVEN NUMBER
number_list = [0,1,2,3,4,5,6,7,8,9,10,11]
my = [x for x in number_list if x%2==0]
print(my)

#TO RPINT THE TEMPERATURE IN FAHRENHEIT
celcius= [0,10,20,34.5]
fahren = [((9/5)*temp + 32) for temp in celcius]
print(fahren)

#IF_ELSE IN LIST COMPRENSHION
##It is not advisable to write one liner code as it is hard to read 

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

#NESTED LOOPS IN LIST COMPREHNESHION

mys = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mys.append(x*y)

print(mys)

##WITH LIST COMPR

myl = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(myl)