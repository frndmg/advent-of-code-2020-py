import fileinput
from functools import partial
from operator import eq, methodcaller

from fp import compose, fmap


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
            ),
        ),
    )(seats)

    print(
        max_seat_id,
    )


def compute_missing_seat_id(seats_ids):
    # lets go with the easy way, since we know how many seats can be
    N = 1028
    taken_seats_ids = [False for _ in range(N)]

    for seat_id in seats_ids:
        taken_seats_ids[seat_id] = True

    taken_seats_started = False
    for seat_id in range(N):
        if taken_seats_started and not taken_seats_ids[seat_id]:
            return seat_id
        elif not taken_seats_started and taken_seats_ids[seat_id]:
            taken_seats_started = True


def main2():
    seats = fileinput.input()

    missing_seat_id = compose(
        compute_missing_seat_id,
        fmap(
            compose(
                compute_seat_id,
                methodcaller('rstrip'),
            ),
        ),
    )(seats)

    print(
        missing_seat_id,
    )


if __name__ == '__main__':
    main2()
