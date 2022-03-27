#How python know that which variable is we refering to in out program?
#This is because of the scope of the variables in python
#python signifies the scope of the variables in the program by following the LEGB Rule


x = 25
def printer():
    x = 50
    return x
print(x) #This give the 25 
print(printer()) #this give the 50

#PYTHON FOLLOW THE LEGB RULE:
##L: Local ---Names assigned in any way within a function(def or lambda),and not declared global in that fuction
##E: Enclosing function locals --- Names in the local scope of any and all enclosing functions(def or lambda), from inner to outer
##G: Global(module) --- Names assigned at the top-level of a module file, or declared global in a def within the file
##B: Built-in(Python) --- Names preassigned in the built-in names module: open,range,SyntaxError,..

#LOCAL

lambda num:num**2 #num is local 

#ENCLOSING
name = 'THIS IS A GLOBAL STRING'
def greet():
    name = 'Sammy'

    def hello():
        print('Hello ' + name)
    hello()
greet()

#NOW IF WE COMMENT DOWN THE THINGS
name1 = 'THIS IS A GLOBAL STRING'
def greets():
    # name1 = 'Sammy'

    def hello():
        print('Hello ' + name1) #-> This give : Hello THIS IS A GLOBAL STRING
    hello()
greets()

#1. The python first look in the LOCAL
#2. Then python looks in the ENCLOSING
#3, Then python looks in the GLOBAL
#4. At last python looks in the build-in

##GLOBAL
name2 = 'THIS IS A GLOBAL STRING'
def greetss():
    ##ENCLOSING
    name2 = 'Sammy'

    def hello():
        name2 = 'I am LOCAL'
        print('Hello ' + name2) #-> This give : Hello THIS IS A GLOBAL STRING
    hello()
greetss()

