"""purpose is to import the other functions and call them"""

__author__: str = "730814548"

from CQs.cq04.concatenation import concat

from CQs.cq04.coordinates import get_coords

x: str = input(get_coords)
y: str = input(get_coords)

print(concat(x, y))
