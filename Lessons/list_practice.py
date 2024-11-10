"""basic syntax of lists"""

# example of empty list
my_numbers: list[float] = []  # Literal empty list
my_number: list[float] = list()  # co

# print(my_numbers)

# adding value to list
my_numbers.append(1.5)
my_numbers.append(2.3)

# print(my_numbers)

# String version
# ny_name: str= "" # literal empty string
# my_name_: str = str() # Constructor


# creating an already populated list
game_points: list[int] = [102, 86, 94]

print(game_points)

# can access each item through indexing
print(game_points[2])
# or
last_game: int = game_points[2]
print(last_game)

# Modifying list through indexing
game_points[1] = 72
print(game_points)

# string example of modifying through indexing
# class_num: str = "110"
# class_num[0]= 2
# not possible, lists can be changed but str are not

# chacking len of list
print(len(game_points))

# removing items from list
game_points.pop(1)
print(game_points)
# be careful when using pop in loops

# inserting a value into list
# game_points.insert(1, 57)
# print(game_points)


def display(int_list: list[int]) -> None:
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(game_points)

game_points.append(102)
print(game_points)
