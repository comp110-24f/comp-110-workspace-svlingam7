"""Purpose is to find the amount of times a character occurs in a phrase"""

__author__: str = "730814548"


def num_instances(phrase: str, search_char: str) -> int:
    """Goes through the phrase character by character to see if it matches the search"""
    index: int = 0  # has to start at zero
    char_count: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            char_count += 1
            index += 1
        else:
            index += 1  # have to make sure that the index increases no matter what
    return char_count
