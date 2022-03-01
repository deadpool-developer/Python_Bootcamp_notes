#1. Sets are unordered collections of unique elements.
#2. Meaning there can only be one representative of the same object

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)  #do not repeat it in the set

print(s)  #print the number in {} -> do not contain key:value pairs and only contain number.
print(set([1,1,2,3]))