import fileinput
from functools import partial
from operator import eq, methodcaller

from fp import compose, fmap
from utils import sneak


def follow_coor(coor, is_left, lo, hi):
    if lo >= hi:
        return hi

    middle = (lo + hi) // 2
    x, *coor = coor

    if is_left(x):
        return follow_coor(coor, is_left, lo, middle)
    else:
        return follow_coor(coor, is_left, middle + 1, hi)


def compute_row(coor):
    return follow_coor(coor, partial(eq, 'F'), 0, 127)


def compute_col(coor):
    return follow_coor(coor, partial(eq, 'L'), 0, 7)


def compute_seat_id(seat):
    row = compute_row(seat[:7])
    col = compute_col(seat[-3:])

    return row * 8 + col


def main():
    seats = fileinput.input()

    max_seat_id = compose(
        max,
        fmap(
            compose(
                compute_seat_id,
                methodcaller('rstrip'),
            )
            ),
        ),
    )(seats)

    print(
        max_seat_id,
    )


if __name__ == '__main__':
    main()
