"""EXO2 - Chardle - A cute step toward Wordle."""

__author__ = "730475190"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        """if length of word does not equal 5 then print Error message below"""
        print("Error: Word must contain 5 characters.")
        exit()  # to exit the program immediately if length of word not 5
    return word


def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        """if lenth of letter is not equal to 5 then print Error message below"""
        print("Error: Character must be a single character.")
        exit()  # exit program immediately if single character not given
    return letter


def contains_char(
    word: str, letter: str
) -> None:  # defining contans_char which is called in line 44
    print("Searching for " + letter + " in " + word)
    count = 0  # count variable to help with variable occurences

    for index in range(len(word)):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)  # concatenation
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)  # concatenation if true
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # same as above, concatenation if true


def main() -> None:
    """defning main, it returns none, next line is calling contains_char"""
    contains_char(word=input_word(), letter=input_letter())  # calling the function


if __name__ == "__main__":
    main()
