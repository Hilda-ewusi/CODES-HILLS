import random
#the program is being asked to import a random number
guess=random.randint(1,99)
#the random number the computer is required to import should be an integer  ranging from 1 to 99
while guess:
    guess=random.randint(1,99)
#the random number is assigned to the variable "guess"
    hills=int(input("guess the number: "))
    ## this is allow the user guess the number
    if hills>guess:
        print("incorrect, your guess is too high")
    elif hills < guess:
        print("incorrect, your guess is too low")
    else :
        print(" congrats! you guessed right")
        break
# the above is to specify the conditions for the input and also display the information associated with each condition

