import random

actions = ['rock', 'paper', 'scissor']
user_count = 0
computer_count = 0

while True:
    user_choice = input("Enter your choice: (rock, paper, scissor) ")
    program_choice = random.choice(actions)
    print(f"Your choice: {user_choice}, Computer choice: {program_choice}\n")

    if user_choice == program_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if program_choice == "scissor":
            print("You win!")
            user_count += 1
        else:
            print("You lose!")
            computer_count += 1
    elif user_choice == "paper":
        if program_choice == "rock":
            print("You win!")
            user_count += 1
        else:
            print("You lose!")
            computer_count += 1
    elif user_choice == "scissor":
        if program_choice == "paper":
            print("You win!")
            user_count += 1
        else:
            print("You lose!")
            computer_count += 1

    play_again = input('Play again? (y/n) ')
    if play_again.lower() == 'n':
        break

if user_count == computer_count:
    print("Final match draw")
elif user_count > computer_count:
    print("User wins")
else:
    print("Computer wins")

print("Computer score:", computer_count)
print("User score:", user_count)
         