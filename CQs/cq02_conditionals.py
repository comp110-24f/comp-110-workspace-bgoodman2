"""Creating a number guessing game"""

__author__ = "730475190"


def guess_a_number() -> None:
    secret = 7
    # Prompt for the user input
    guess = int(input("Guess a number: "))

    # Print user guess shown in the trailhead and REPL
    print("Your guess was", guess)

    # Provides feedback based on the guess
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)

    return None


if __name__ == "__main__":
    guess_a_number()
