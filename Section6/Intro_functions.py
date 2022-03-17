#CREATING A CLEAN REPEATABLE CODE IS A KEY PART OF BECOMING AN EFFECTIVE PROGRAMMER
#FUNCTIONS ALOW US TO CREATE BLOCKS OF CODE THAT CAN BE EASILY EXECUTED MANY TIMES, WITHOUT NEEDING TO CONSTANTLY REWRITE THE ETIRE BLOCK OF CODE

#DEF keyword -> it tells the starting of the function
##always use snake_casing while writing a function name i.e use all the lower case letters with an underscore

def name_func():
    print("Hello")

name_func()


#TO PASS THE PARAMETER IN THE FUNCTION

def name_param(name):
    print("HELLO " + name)

name_param("ADITYA")

###################RETURN KEYWORD################
#TYPICALLY WE USE THE RETURN KEYWORD TO SEDN BACK THE RESULT OF THE FUNCTION, INSTEAD OF JUST PRINTING IT OUT
##RETURN ALLOWS US TO ASSIGN THE OUTPUT OF THE FUNCTION TO A NEW VARIABLE

def add_func(n1,n2):
    return n1 + n2
print(add_func(2,3))


#DIFFERENCE IN RETURN AND PRINT
# RETURN -> it saves the result in the variable
# PRINT ->  it prints the result and do not saves it