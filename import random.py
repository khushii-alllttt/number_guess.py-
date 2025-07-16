import random

def play_game(lower=1, upper=100):
    """Play one round of the guessing game."""
    secret = random.randint(lower, upper)
    attempts = 0
    print(f"\nI'm thinking of a number between {lower} and {upper}. Try to guess it!")
    print("Type 'q' to quit this round.\n")

    while True:
        guess_text = input("Your guess: ").strip().lower()
        if guess_text == 'q':
            print(f"You quit. The number was {secret}.")
            return None  # No score for quitting

        # Validate numeric input
        if not guess_text.isdigit():
            print("Please enter a whole number (or 'q' to quit).")
            continue

        guess = int(guess_text)
        if guess < lower or guess > upper:
            print(f"Out of range! Enter a number between {lower} and {upper}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            return attempts  # Return score


def choose_range():
    """Optional difficulty selection."""
    print("\nChoose difficulty:")
    print("1) Easy  (1–50)")
    print("2) Normal (1–100)")
    print("3) Hard  (1–500)")
    print("4) Custom range")
    choice = input("Select 1-4 (default 2): ").strip()

    if choice == '1':
        return 1, 50
    elif choice == '2' or choice == '':
        return 1, 100
    elif choice == '3':
        return 1, 500
    elif choice == '4':
        while True:
            try:
                low = int(input("Lower bound: ").strip())
                high = int(input("Upper bound: ").strip())
                if low >= high:
                    print("Lower must be less than upper. Try again.")
                    continue
                return low, high
            except ValueError:
                print("Enter valid integers.")
    else:
        print("Invalid choice; using Normal (1–100).")
        return 1, 100


def main():
    print("=== Number Guessing Game ===")
    best_score = None

    while True:
        low, high = choose_range()
        attempts = play_game(low, high)

        if attempts is not None:  # player guessed correctly
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏅 New best score!")
            if best_score is not None:
                print(f"Current best: {best_score} attempt{'s' if best_score != 1 else ''}.")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
