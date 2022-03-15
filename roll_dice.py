import random

roll = random.randint(1,2,3,4,5,6)
# print("The computer rolled a " + str(roll))

guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))