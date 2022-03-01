#1. Dictionaries are unordered mappings for stroing objects. Previously we saw how lists store objects in an ordered sequence,dictionaries use a key-value pairing instead
#2. Dictionaries use curly braces and colons to signify the keys and their associated values.
    #{'key1' : 'value1' , 'key2', 'value2'}

#3. So when to choose a list and when to choose a dictionary.
# ~ About using dictionaries: 
            #1. Objects retrieved by key name
            #2. Umordered and can not be sorted.
    #So, when you need to perform fast retrieval of the values we use dictionary as we do not need to know its exact indexed location and you just need to know the key:value pair


# ~ About using lists:
            #1. Objects retrieved by location
            #2. Ordered sequence can be indexed or sliced.


#Dictionary helps in faster retreival of the data without knowing the exact index
my_dict = {"apple" : 200 , "oranges" : 20, "grapes" : 50}
print(my_dict["apple"])

#Dictionaries can hold -> int, float, lists, strings

d = {"k1" : 123, "k2" : [0,1,2] , "k3" : {"insidekey" : 100}}
print(d['k2'])  #gives the list
print(d['k3']['insidekey'])  #gives the value 100

#To add the new key:value pair in the dictionary 
d["k4"] = 300
print(d) # adds it in the dictionary

#To change the value of the key in the dictionary
d['k1'] = "New value added"
print(d)

#To get the keys of the dictionary

print(d.keys())  #gives the keys -> list
print(d.values()) #gives the values -> list

#To get all the key:values in the pair

print(d.items()) #gives the tuples

