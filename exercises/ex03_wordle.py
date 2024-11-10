"""Creating wordle from scratch"""

__author__: str = "730814548"


def input_guess(secret_word_len: int) -> str:
    """To determine if the length of the user's input matches the secret word's len"""

    # when using f-strings, there is no need for "" and/ or +
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    if len(guess) == secret_word_len:
        return guess

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess  # needs to be returned since we declared the return type


def contains_char(secret_word: str, char_guess: str) -> bool:
    """To see if a certain char is contained within the secret word"""
    assert len(char_guess) == 1  # makes sure that the char len will always be one

    index: int = 0

    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True

        index += 1  # idx will increase no matter the result so that loop will progress
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """To codify the results of whether or not the user's guess has chars
    that match the secret word in emojis"""

    # makes sure that the fn will only run if the lens match up
    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emojis: str = ""

    index: int = 0

    while index < len(secret_word):
        # occurs when the char is contained and in the right spot
        if user_guess[index] == secret_word[index]:
            emojis += GREEN_BOX

        # occurs when char is contained in the word somewhere
        elif contains_char(secret_word=secret_word, char_guess=user_guess[index]):
            emojis += YELLOW_BOX

        # occurs when the char is not in the word at all
        else:
            emojis += WHITE_BOX
        index += 1  # index must always increase so that loop continues
    return emojis


def main(secret: str) -> None:
    """Entrypoint of program and the main game loop"""
    turn_num: int = 1  # acts like an index
    result: bool = False  # will help determine whether the game is won or not

    # needed a new local var to store the user's guesses
    guessed_word: str = ""

    # both conditions need to be true to enter the loop
    while (result is False) and (turn_num <= 6):
        print(f"=== Turn {turn_num}/6 ===")
        guessed_word = input_guess(len(secret))
        print(emojified(user_guess=guessed_word, secret_word=secret))

        if guessed_word == secret:
            result = True
            print(f"You won in {turn_num}/6 turns!")

        turn_num += 1

        if turn_num > 6:  # b/c after the 6th turn turn_num will == 7
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
