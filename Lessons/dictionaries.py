"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evals to # of entries

print(len(ice_cream))  # prints 3


# add key val entry by directly assigning to key

ice_cream["mint"] = 3

print(ice_cream)


# access entries by their key

print(ice_cream["chocolate"])  # prints 12


# test of "PBJ" is a key in ice_cream

has_pbj: bool = "PBJ" in ice_cream


# removing entry from dict
# to remove we use pop method an dgive it a key
ice_cream.pop("strawberry")

print(ice_cream)


# to iterate over every key in a loop-> use a for in loop

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders!")
