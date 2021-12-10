#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random
import sys

#The function that will generate the right number.
#This one is easier aside from the fact that it is a single number, the correct number won't refresh after every number until you get it right.
def randomNumbers():
    rightNumber = random.randint(0,100)
    return rightNumber

#The function that will keep the user's answer.
def askUser():
    a1 = True
    print("\nReminder that there are no proper/improper fractions allowed and no decimals places allowed.")
    while a1:
        try:
            guess = int(input("Guess the number that ranges from 0 - 100 and you win 500 BUCKS! "))
            a1 = False
        except:
            print("Input a proper number as instructed.")
    return guess
    
#Evaluation of the number if you guessed it right or not.
def evaluation():
    global guessedNo, trueNumber
    if guessedNo == trueNumber:
        print("YOU WON! CLAIM YOUR PRIZE AT PUP STA. MESA! YEEHAW!")
        
    elif guessedNo > trueNumber:
        print("\nYour guess is greater than the random number")
        guessedNo = askUser()
        evaluation()

    elif guessedNo < trueNumber:
        print("\nYour guess is less than the random number")
        guessedNo = askUser()
        evaluation()



guessedNo = askUser()
trueNumber = randomNumbers()
evaluation()

