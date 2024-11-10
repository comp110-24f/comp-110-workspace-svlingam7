"""Purpose is to combine the strings"""

__author__: str = "730814548"


def concat(str_1: str, str_2: str) -> str:
    """purpose is to concatenate the two strings together"""
    return str_1 + str_2


if __name__ == "__main__":
    # was global variables
    word1: str = "happy"
    word2: str = "tuesday"

    # calling concat w/ the globals as parameters
    print(concat(word1, word2))
