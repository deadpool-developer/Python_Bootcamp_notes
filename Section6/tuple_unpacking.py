#UNPACKING THE TUPLES

prices = [('apple',100), ('grapes',60), ('oranges',80)]
for fruit , price in prices:
    print(fruit,price)

#WE HAVE TO FING THE HIGHEST WORKING HOUR EMPLOYEE FROM THE LIST OF THE TUPLES WITH THEIR NAME AND WORKING HOURS AS THE RESULT

work_hours = [('Aditya', 1000), ('Aryan' , 200) ,('Dhruv',500)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
            
        else:
            pass
    return (employee_of_month,current_max) 
print(employee_check(work_hours))
name, hours = employee_check(work_hours) #we can do tuple unpacking while the function call
print(name)
print(hours)