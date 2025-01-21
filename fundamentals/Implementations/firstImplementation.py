# simple number guessing game
import random as rnd
random_number = rnd.randrange(1,10)
guess = 0

while True:
    value_input = int(input("enter number between 1 to 10\n"))
    if value_input == random_number:
        print(f"you guessed within {guess} guessed")
    else:
        print("enter again!!")
        guess+=1
    if guess == 4:
        print(f"the number was{random_number}")
        break


