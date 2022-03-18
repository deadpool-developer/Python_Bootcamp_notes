from random import shuffle #-> do not return anything

example = [1,2,3,4,5,6]
shuffle(example)
print(example)

#CREATING GAME
##We can make shuffle return by creating a function
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#GUESS THE INDEX POSITION
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2 \n")
    return int(guess)

#CHECK IF THE GUESS IS CORRECT OR NOT
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong Guess!")
        print(mylist)

#INITIAL LIST
mylist = [' ', 'O', ' ']
#SHUFFLE LIST
mixed_list = shuffle_list(mylist)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(mixed_list,guess)
