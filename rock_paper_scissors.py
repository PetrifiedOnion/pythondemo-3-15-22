import random
ai_choice = random.choice(["scissors", "rock", "paper"])
user_choice = input("Do you want - rock, paper or scissors?\n")

if ai_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and ai_choice == "scissors":
    print("YOU ARE VICTORIOUS!")
elif user_choice == "paper" and ai_choice == "rock":
    print("YOU ARE VICTORIOUS!")
elif user_choice == "scissors" and ai_choice == "paper":
    print("YOU ARE VICTORIOUS!")
else:
    print("YOU ARE DEFEATED! YOU SHALL NEVER RISE FROM THE ASHES OF YOUR HUMILIATION >:D")