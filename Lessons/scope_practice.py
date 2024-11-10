"""scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """nn"""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if char != msg[index]:
            copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    # global variable-> was one before put into if statement
    word: str = "yoyo"
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
