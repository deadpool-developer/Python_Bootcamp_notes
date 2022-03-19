# *args is the argument -> treated as a tuple -> it is an arbitrary choice -> we can name it *spam or anthing
# **kwargs is the keyword argument 

def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(40,60,100,100,100))

#We have to pass the number of paramter that we needed to assign to the sum 
#But we we exceed the parameter in the calling function it will give the error.
#To resolve this we use *args as the function argument

def args_func(*args):
    return sum(args) * 0.05

print(args_func(40,60,100))

#NOW WE CAN ADD AS MANY PARAMTER AS WE WANT TO AND IT WILL NOT GIVE ANY ERROR

###############################################################################################

# **kwargs is used for the keyword argument -> return the dictionary of the arguments

def kwarg_func(**kwargs):
    print(kwargs) # -> {'fruit': 'apple', 'veggies': 'veg'}
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
kwarg_func(fruit = 'apple',veggies = 'veg') # -> python do not give any error for thr veggies

