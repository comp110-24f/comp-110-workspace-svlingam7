__author__ = "730814548"


def mimic(message: str) -> str:
    """Purpose of the function is to copy the messge and send it back"""
    return message


def main() -> None:
    """Function will print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
