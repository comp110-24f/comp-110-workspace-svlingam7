# print("first function:")


# def total_cost(price: int, tax_rate: float):
# print(price + (price * tax_rate))


# print(total_cost(price=100, tax_rate=0.07))


# print("Second function:")


# def total_cost2(price: int, tax_rate: float):
# return price + (price * tax_rate)


# print(total_cost2(price=100, tax_rate=0.07))


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
