#While loop will continue to execute a block of code while some condition remains True.
#SYNTAX:
a = 2
while a > 0:
    #do_something
    print(a)
    a -= 1
else:
    #do something different
    print("Completed")

#BREAK KEYWORD

##Breaks out of the current closest enclosing loop
x = 0
while x<5:
    if x == 2:
        break
    print(x)
    x+=1



#CONTINUE KEYWORD

##Goes to the top of the closest enclosing loop
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a': #if we do not want to print the 'a' in the output
        continue     #this goes back to the for loop and read the next letter and prints it
    print(letter)

#PASS

##Does nothing at all
x = [1,2,3]
for item in x:
    pass  #Do nothing and use to avoid syntax error

print("End of my script")