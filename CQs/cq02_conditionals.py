"""Purpose is to try and guess the secret number """

__author__: str = "730814548"


# Since input is in the form of a str, make sure to convert to int and vice versa
def guess_a_number() -> None:
    """Establishes secret number and the responses to user_guess"""

    secret: int = 7
    user_guess: str = input("Guess a number: ")
    print("Your guess was " + user_guess)

    if int(user_guess) == secret:
        print("You got it!")
    elif int(user_guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
