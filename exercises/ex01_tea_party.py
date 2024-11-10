"""Used to plan tea parties using the amount of guests attending """

__author__: str = "730814548"


# When trying to combine a str and int make sure to convert the int value into a str
# Other wise it will just result in errors
# Also remember to equate the main function parameter to the other functions' parameters
def main_planner(guests: int) -> None:
    """Acts as the place to call the other functions"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Will figure out the # of tea bags needed based on the people attending"""
    return people * 2


# 1.5 is a float so the result of the expression will also result in a float
# So the result of the expression must be changed into int to match the return type
def treats(people: int) -> int:
    """Will figure out the # of treats needed based on # of teas drunk"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Will figure out cost based on # of teas and treats needed"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending? ")))
