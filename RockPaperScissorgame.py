import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user == 'exit':
            break
        if user not in choices:
            print("Invalid choice.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

play_game()

