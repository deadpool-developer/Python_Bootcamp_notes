#LESSER OF TWO EVENTS
##Write a function that returns the lesser of two given numbers if both numbers are even,but
##returns the greater if one or both are odd

from re import S


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min((a,b))
    else:
        return max((a,b))
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(3,5))
print(lesser_of_two_evens(10,4))

#ANIMAL CRACKERS
##Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    a = text.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#THE OTHER SIDE OF SEVEN
##Given a value. return a value that is twice as far away on the other side of 7
def other_side_seven(num):
    pass

#OLD MACDONALD
##Write a function that capitalize the first and fourth letters of a name

def old_macdonald(name):
    st = ''
    for i in range(len(name)):
        if i == 0 or i ==3:
            st += name[i].upper()
        else:
            st += name[i]
    return st

print(old_macdonald('macdonald'))
print(old_macdonald('aditya Saini'))

#MASTER YODA
##Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    a = text.split()
    b = a[::-1]
    return (" ").join(b)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#ALMOST THERE
##Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    if ((n<= 100 and n>=90) or (n>=101 and n<=110)):
        return True
    elif ((n<= 200 and n>=190) or (n>=201 and n<=210)):
        return True
    else:
        return False

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#LAUGHTER
##Write a function that counts the number of times a given pattern appears in a string, including overlap

def laughter(pattern,text):
    pass

print(laughter('hah','hahahah'))

#PAPER DOLL
##Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    st = ''
    for letter in text:
        st += letter*3
    return st

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

#BLACKJACK
##Given three integers between 1 and 11, if their sum is less than ir equal to 21, return their sum.
##If their sum exceeds 21 and there's an eleven, reduce the total sum by 10, Finally, if the sum(even after adjustment)
##exceeds 21, return 'BUST'

def blackjack(a,b,c):
    s = sum((a,b,c))
    if s<= 21:
        return s
    elif (s > 21 and (a==11 or b==11 or c==11)) :
        s -= 10
        if s > 21:
            return 'BUST'
        else:
            return s
    elif s > 21:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#SUMMER OF '69'
##Return the sum of the number in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
##(every 6 will be followed by at least one 9), Return 0 for no numbers

def summer_69(arr):
    pass
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))


#CHALLENGING PROBLEMS
##SPY GAME
###Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    pass