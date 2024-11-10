"""Practicing different ways to use Dictionaries """

__author__: str = "730814548"


def invert(input: dict[str, str]) -> dict[str, str]:
    """To switch the places of the key and value"""
    inverted_dict: dict[str, str] = {}

    for key in input:

        if input[key] in inverted_dict:  # if the key already exists then error
            raise KeyError("Duplicate keys cannot exist")

        # otherwise the og value will now become the key
        # and og key will become the value
        inverted_dict[input[key]] = key
    return inverted_dict

    # for i in range(0,len(input)):
    #     dupe = input[i]
    #     if dupe = input[]


# testing invert fn

# print(invert({"a": "z", "b": "y", "c": "x"}))
# print(invert({"apple": "cat"}))
# print(invert({"kris": "jordan", "michael": "jordan"}))


# def favorite_color(input: dict[str, str]) -> str:
#     """purpose of fn"""
#     occurs: int = 0
#     colors_list: list[str] = []
#     most: str = ""

#     for key in input:
#         colors_list.append(input[key])

#     for color in colors_list:
#         index: int = 1
#         occurs = 0

#         while index < len(colors_list):
#             color: str = colors_list[0]
#             if color == colors_list[index]:
#                 occurs += 1
#             index += 1


# def favorite_color(input: dict[str, str]) -> str:  # need to memory diagram this!
#     """purpose"""

#     colors: list[str] = []
#     color_occur: dict[str, int] = {}
#     for key in input:
#         colors.append(input[key])

#     index: int = 0
#     occur: int = 1

#     # while index < len(colors) - 1:
#     #     occur = 1

#     #     if colors[index] == colors[index + 1]:  # and (index != len(colors) - 1):
#     #         occur += 1
#     #     color_occur[colors[index]] = occur
#     #     index += 1

#     color: str = ""

#     for key in color_occur:
#         most: int = 0

#         if most < color_occur[key]:
#             most = color_occur[key]
#             color = key
#     return color


def favorite_color(input: dict[str, str]) -> str:
    """checking to see what color was most said as one's favorite
    and then returning it"""

    pop_color: str = ""
    color_occur: dict[str, int] = {}
    # occurances: list[int] = []

    for name in input:
        if input[name] in color_occur:
            # orginally had color_occur[name] += 1
            # but that was not correct bc that is referring to the key not the value
            color_occur[input[name]] += 1
        else:
            color_occur[input[name]] = 1  # because if added it must occur at least once

    # for key in color_occur:
    #     occurances.append(color_occur[key])

    # index: int = 0
    biggest_num: int = 0

    for color in color_occur:
        if color_occur[color] > biggest_num:
            biggest_num = color_occur[color]
            pop_color = color

        # pop_color would be "" because it has not been updated to a color yet
        elif color_occur[color] == biggest_num and pop_color == "":
            pop_color = color
    return pop_color


# testing fav colors fn

# print(
#     favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
# )  # returns blue
# print(
#     favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"})
# )  # returns yellow
# print(
#     favorite_color(
#         {
#             "Marc": "yellow",
#             "Ezri": "blue",
#             "Kris": "yellow",
#             "Bill": "yellow",
#         }  # returns yellow
#     )
# )

# print(
#     favorite_color({"Marc": "blue", "Ezri": "yellow", "Kris": "blue"})
# )  # returns blue

# print(
#     favorite_color({"Marc": "yellow", "Ezri": "green", "Kris": "blue"})
# )  # needs to return yellow


def count(input: list[str]) -> dict[str, int]:
    """keeping track of how many times an item appears in a list"""

    counted: dict[str, int] = {}

    for elem in input:
        # if elem exists in counted already then the count will increase by 1
        if elem in counted:
            counted[elem] += 1
        else:
            # set to 1 because if it is being added then it must occur at least once
            counted[elem] = 1
    return counted


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """To put words in a list according to their first character"""
    a_to_z: dict[str, list[str]] = {}

    index: int = 0
    word: str = ""
    first_char: str = ""

    while index < len(word_list):
        word = word_list[index]
        # needs to add .lower() so that the capital letters do not mess the fn up
        first_char = word[0].lower()

        if first_char not in a_to_z:
            # needs to initalize an empty list so that the words could be added
            a_to_z[first_char] = []
        a_to_z[first_char].append(word)  # can use append because of list

        # if first_char in a_to_z:
        #     a_to_z[first_char] += word
        # elif:
        #     a_to_z[first_char] += word

        index += 1
    return a_to_z


# testing alphabetizer fn

# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))

# result= {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}

# print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))

# results= {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """To update the list based on the day and which student attended that day"""
    if day not in input:
        input[day] = []  # init empty list so that students can be added
    if student not in input[day]:  # had to use input[day] to refer to the list
        input[day].append(student)


# testing update_attendance
# attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(attendance_log, "Tuesday", "Vrinda")
# update_attendance(attendance_log, "Wednesday", "Kaleb")
# update_attendance(attendance_log, "Wednesday", "Kaleb")
# print(attendance_log)
