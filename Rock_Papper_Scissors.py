import random 

user_wins = 0
computer_wins = 0
Options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/paper/scissors or q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in Options:
        continue

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissor:2    
    computer_pick = Options[random_number]
    print("computer picked",computer_pick,".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
