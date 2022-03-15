import random

player = input("Please enter your name. \n")
print("Hello ", player)
    
def main(): 
    computer_guess = random.randint(1,100)
    player_guess = 0
    while player_guess != computer_guess:
        player_guess = int(input("Please enter your guess.\n"))
        if player_guess > computer_guess:
            print("Your guess is too high")
        elif player_guess < computer_guess:
            print("Your guess is too low")

    print("You guessed correctly.")
        

    




#     greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player