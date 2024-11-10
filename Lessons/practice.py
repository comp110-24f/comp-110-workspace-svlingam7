print("Snippert A result below:")


def get_ticket_price() -> int:
    age: int = int(input("What is your age? "))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_price())


print("Snippert B result below:")


def get_ticket_priceB() -> int:
    age: int = int(input("What is your age? "))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_priceB())


print("Snippert C result below:")


def get_ticket_priceC() -> int:
    age: int = int(input("What is your age? "))
    if age <= 12 or age > 60:
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_priceC())


print("Snippert D result below:")


def get_ticket_priceD() -> int:
    age: int = int(input("What is your age? "))
    if age <= 12:
        price: int = 5
    elif age <= 60:
        price: int = 10
    return price


print(get_ticket_priceD())
