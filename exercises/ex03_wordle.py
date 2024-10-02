"""wordle game, so funnn"""

__author__ = "730475190"


def input_guess(length: int) -> str:
    """Prompt the user for a guess until it matches the specified length."""
    print("Enter a " + str(length) + " character word: ", end="")
    guess = input()
    while len(guess) != length:  # only enter the while loop if this is true
        print("That wasn't " + str(length) + " chars! Try again: ", end="")
        guess = input()
    # only have something to return once you recieve "false" and skip the while loop
    return guess


def contains_char(word: str, char: str) -> bool:
    """Return True if char is in word, otherwise False."""
    assert len(char) == 1  # Ensure char is a single character
    index = 0
    found = False
    while index < len(word):
        if word[index] == char:
            found = True
        index += 1
    return found


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis based on guess vs secret."""
    assert len(guess) == len(secret)
    result = ""
    index = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    turns = 6
    current_turn = 1
    while current_turn <= turns:
        print("=== Turn " + str(current_turn) + "/" + str(turns) + " ===")
        guess = input_guess(len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            print("You won in " + str(current_turn) + "/" + str(turns) + " turns!")
            return

        current_turn += 1

    print("X/" + str(turns) + " - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
