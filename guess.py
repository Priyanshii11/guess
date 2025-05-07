import random

def get_attempts_by_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        print("Great! You have selected Easy difficulty.")
        return 10
    elif choice == "2":
        print("Great! You have selected Medium difficulty.")
        return 5
    elif choice == "3":
        print("Great! You have selected Hard difficulty.")
        return 3
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        return 5

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    max_attempts = get_attempts_by_difficulty()
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Let's start the game!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess ({max_attempts - attempts} attempts left): "))
            attempts += 1
            
            if guess < number_to_guess:
                print(f"Incorrect! The number is greater than {guess}.")
            elif guess > number_to_guess:
                print(f"Incorrect! The number is less than {guess}.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True
                break
        except ValueError:
            print("Please enter a valid number.")

    if not guessed:
        print(f"\n❌ You've used all your chances. The correct number was {number_to_guess}.")
    
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    play_game()
