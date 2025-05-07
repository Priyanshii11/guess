import random
import time

# Store high scores in memory
high_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}

def get_attempts_by_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        print("Great! You have selected Easy difficulty.\n")
        return 10, "easy"
    elif choice == "2":
        print("Great! You have selected Medium difficulty.\n")
        return 5, "medium"
    elif choice == "3":
        print("Great! You have selected Hard difficulty.\n")
        return 3, "hard"
    else:
        print("Invalid choice! Defaulting to Medium difficulty.\n")
        return 5, "medium"

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    max_attempts, level = get_attempts_by_difficulty()
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess ({max_attempts - attempts} attempts left): "))
            attempts += 1

            if guess == number_to_guess:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"🎉 Correct! You guessed the number in {attempts} attempts and {duration} seconds.")

                # High Score Tracker
                if high_scores[level] is None or attempts < high_scores[level]:
                    high_scores[level] = attempts
                    print("🏆 New High Score for", level.capitalize(), "mode!")

                guessed = True
                break
            elif abs(guess - number_to_guess) <= 10:
                print("❗Close! You're within 10 of the number.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    if not guessed:
        print(f"\n❌ Out of attempts! The number was {number_to_guess}.")

    print(f"Current High Scores: {high_scores}")
    print("Thanks for playing!\n")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
