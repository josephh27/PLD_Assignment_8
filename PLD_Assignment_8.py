# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.
import random
import sys

#The function that will show the introduction with strings only.
def introduction():
    print("You will be a guest to a guessing game which you will need to predict 3 separate numbers correctly.")
    print("The following numbers you should be inputting must be in range 0-9 only.")
    print("//||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\\")

#The function which will retain the guessed numbers of the user.
def askNumbers():
    running = True
    while running:
        try:
            firstNumber = int(input("\nInput first number please: "))
            secondNumber = int(input("Input second number please: "))
            thirdNumber = int(input("Input third number please: "))
            break
        except:
            ("Please input proper integers")

    return firstNumber, secondNumber, thirdNumber

#This is where the random numbers are generated from.
#I also made the combination refresh itself after every game so it is going to be kind of hard to guess it.
def randomNumbers():
    firstRandom = random.randint(0, 9)
    secondRandom = random.randint(0, 9)
    thirdRandom = random.randint(0, 9)
    print(f"Correct numbers in any order were: {firstRandom}, {secondRandom}, and {thirdRandom}")
    return firstRandom, secondRandom, thirdRandom

#This function will evaluate whether the guessed 3 digit combination is right or not.
#Any order of inputted numbers is accepted since the game is already hard as it is.
def evaluation():
    from itertools import permutations
    global firstGen, secondGen, thirdGen, firstGuess, secondGuess, thirdGuess
    rightComb = permutations([firstGen, secondGen, thirdGen], 3)
    guessList = (firstGuess, secondGuess, thirdGuess)
    correct = 0
    for i in rightComb:
        print(i)
        if i == guessList:
            print("WINNER WINNER CHICKEN DINNER")
            correct = correct + 1

    if correct < 1:
        print("you lose")

    while True:
        response = input("try again? y/n? ").lower()
        print("")
        if response == "y":
            introduction()
            firstGuess, secondGuess, thirdGuess = askNumbers()
            firstGen, secondGen, thirdGen = randomNumbers()
            evaluation()
        elif response == "n":
            sys.exit()
        else:
            print("\"y\" or \"n\" only")


introduction()
firstGuess, secondGuess, thirdGuess = askNumbers()
firstGen, secondGen, thirdGen = randomNumbers()
evaluation()



