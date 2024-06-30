import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        if user_choice == 'quit':
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        # Display scores
        print(f"\nCurrent Scores - You: {user_score}, Computer: {computer_score}")

    print("\nThanks for playing! Final Scores:")
    print(f"You: {user_score}, Computer: {computer_score}")

# Run the game
play_game()
