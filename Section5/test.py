#USE for, .split() and if to create a statement that will print out the words that starts with "S"

st = "Print only the words that start with s in this sentence"

sts = st.split()
for letter in sts:
    if letter[0] == 's':
        print(letter)

#USE range() to print all the even numbers from 0 to 10
result = [ x for x in range(0,11) if x%2==0]
print(result)

#USE A LIST COMPREHENSION TO CREATE A LIST OF ALL NUMBERS BETWEEN 1 to 50 THAT ARE DIVISIBLE BY 3

divide_3 = [x for x in range(1,50) if x%3==0]
print(divide_3)

#GO THROUGH THE STRING BELOW AND IF THE LENGTH IF A WORD IS EVEN PRINT "EVEN"

strs = 'Print every word in this sentence that has an even number of letters'
res = strs.split()
for letter in res:
    if len(letter)%2 == 0:
        print(letter + ' is even')


#WRITE A PROGRAM THAT PRINTS THE INTERGES FROM 1 to 100. 
#BUT FOR MULTIPLES OF THREE PRINT "Fizz" INSTEAD OF THE NUMBER,
#AND FOR THE MULTIPLES OF FIVE PRINT "Buzz".
#FOR NUMBER WHICH ARE MULTIPLES OF BOTH THREE AND FIVE PRINT "FizzBuzz"

for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBUzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)

#USE LIST COMPREHNESION TO CREATE A LIST OF THE FIRST LETTERS OF EVERY WORD IN THE STRING BELOW:

strsr = 'Create a list of the first letters of every eword in this string'
strr = strsr.split(" ")
rt = []
for letter in strr:
    rt.append(letter[0])
print(rt)

