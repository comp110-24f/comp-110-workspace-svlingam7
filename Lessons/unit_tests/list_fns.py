"""purpose"""


def get_first(fn_list: list[str]) -> str:
    """return first elem"""
    if len(fn_list) == 0:  # if empty input
        return ""
    return fn_list[0]


def remove_first(fn_list: list[str]):
    """removes first elem"""
    fn_list.pop(0)


def get_and_remove_first(fn_list: list[str]) -> str:
    """remove and return first elem"""
    # remove_first(fn_list=fn_list)
    # get_first(fn_list=fn_list)
    first_elem: str = fn_list[0]

    fn_list.pop(0)
    return first_elem


# word_list: list[str] = ["h", "e", "l", "l", "o"]

print(get_and_remove_first(["h", "e", "l", "l", "o"]))
