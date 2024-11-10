"""Practice w/ Conditionals"""


def less_than_10(num: int) -> None:  # bool:
    """Tell me if nhum is less than 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        # return True
        print("Small Number!")
    else:
        # return False
        print("BIG Number!")
    print("Have a nice day!!!")


less_than_10(num=3)


def should_i_eat(hungry: bool) -> None:
    """Tells  me to eat or not, based on hunger"""
    if hungry is True:  # conditional bool expression
        print("EAT FOOOOD! You'll starveeee")  # then block
    else:
        print("Do homework!!")  # else block
    print("yayyy")  # be happy eitehr way


should_i_eat(hungry=False)


def check_first_letter(word: str, letter: str) -> None:
    if letter == word[0]:
        print("match")
    else:
        print("no match! :C")


# can also be written with returns instead of print,
# but that means that the return is str
# also when calling you need to print if using returns


check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="s")
