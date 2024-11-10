"""Finding how many times a character appears in a five-character word"""

__author__: str = "730814548"


def input_word() -> str:
    """Purpose is to prompt the user for a word and to check if that word is 5 chars"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Purpose is to prompt the use for a char and to make sure the input is 1 char"""
    one_char: str = input("Enter a single character:")
    if len(one_char) != 1:
        print("Error: Character must be a single character.")
        exit()
    return one_char


def contains_char(word: str, letter: str) -> None:
    """Purpose is to go through each index of word and record if it matches char"""
    print("Searching for " + letter + " in " + word)
    char_count: int = 0

    if letter == word[0]:
        char_count += 1
        print(letter + " found at index " + str(0))

    if letter == word[1]:
        char_count += 1
        print(letter + " found at index " + str(1))

    if letter == word[2]:
        char_count += 1
        print(letter + " found at index " + str(2))

    if letter == word[3]:
        char_count += 1
        print(letter + " found at index " + str(3))

    if letter == word[4]:
        char_count += 1
        print(letter + " found at index " + str(4))

    if char_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif char_count == 1:
        print(str(char_count) + " instance of " + letter + " found in " + word)
    else:
        # whenever trying to print numbers make sure to convert them to str first
        print(str(char_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Purpose is to efficiently call the necessary functions to run the program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()