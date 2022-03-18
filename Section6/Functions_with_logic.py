#MODULUS OPERATOR

print(2 % 2)
print(3 % 2)
print(41 % 40)
print(20 % 2)

def even_check(number):
    result = number % 2==0
    return result
print(even_check(20))
print(even_check(21))


#TO CHECK IF A LIST CONTAIN AN EVEN NUMBER, IF DO, RETURN TRUE ELSE NOTHING

def check_even_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            pass
print(check_even_list([2,1,3,4,5,2])) #gives True

#IF WE WANT TO RETURN FALSE IF NO EVEN IS THERE THAN WE WILL DO THE FOLLOWING THING

def check_even_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            pass
        #loop all the number and if condition is not met than it will return False
    return False
print(check_even_list([1,3,5])) #gives False

#RETURN ALL THE EVEN NUMBER

def append_even_number(num_list):
    even_number = []
    for number in num_list:
        if number %2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number
print(append_even_number([2,1,3,4,2,5,6,4,7,8]))