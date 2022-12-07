#Dheerendra Project
import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    l=user_action.lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    if l not in possible_actions:
        print("Oops!!! Please Enter a valid choice.")
        print("Restart the Program.")
        break
    else:
        pass
    
    print(f"You chose %s, computer chose %s."%(user_action,computer_action))

    if l == computer_action:
        print("Both players selected %s. It's a tie!"%(user_action))
    elif l == "rock":
        if l == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif l == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif l == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y" :
        print("Thankyou for Playing!")
        break


