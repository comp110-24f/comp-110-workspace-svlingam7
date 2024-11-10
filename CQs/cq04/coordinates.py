"""purpose is to create coords"""

__author__: str = "730814548"


def get_coords(xs: str, ys: str) -> None:
    """purpose is to pair up each of the characters in the strs"""
    idx_x: int = 0

    while idx_x < len(xs):
        idx_y: int = 0  # have to have tgis inside the first loop so hat it will reset

        while idx_y < len(ys):
            print("(" + xs[idx_x] + "," + ys[idx_y] + ")")
            idx_y += 1

        idx_x += 1  # make sure this is out of the 2nd while loop
