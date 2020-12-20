from bisect import bisect_left
from functools import partial, reduce
from operator import itemgetter, mul

from fp import compose, fnone, tupled


def pairsum(s, xs):
    d = set()

    for x in xs:
        if s - x in d:
            return x, s - x

        d.add(x)


def tripletesum(s, xs):
    n = len(xs)
    xs = sorted(xs)

    for i in range(n):
        for j in range(i + 1, n):
            x, y = itemgetter(i, j)(xs)

            k = bisect_left(xs, s - x - y)

            # BUG: you have to verify that k != i and k != j

            z = xs[k]

            if x + y + z == s:
                return x, y, z


def tripletesum2(s, xs):
    # NOTE: this is completely wrong

    n = len(xs)
    i = 0
    j = n - 1
    xs = sorted(xs)

    while i < j:
        x, y = itemgetter(i, j)(xs)

        k = bisect_left(xs, s - x - y, i + 1, j)

        z = xs[k]

        check = x + y + z

        # print(
        #     f'bounds: ({i}){x}, ({j}){y} lookfor: {s - x - y} found: ({k}){z}, {check} {xs}',
        # )

        if check == s:
            return x, y, z
        elif check > s:
            j -= 1
        else:
            i += 1


def pairsum2(s, xs, lo, hi):
    # assume xs sorted

    while lo < hi:
        a, b = itemgetter(lo, hi)(xs)

        check = a + b

        # print(
        #     f'bounds: ({lo}){a} ({hi}){b} lookfor: {s} {check} {xs}',
        # )

        if check == s:
            return lo, hi
        elif check < s:
            lo += 1
        else:
            hi -= 1


def tripletesum3(s, xs):
    xs = sorted(xs)
    n = len(xs)

    for i in range(n - 2):
        t = pairsum2(s - xs[i], xs, i + 1, n - 1)

        if t is not None:
            return itemgetter(i, *t)(xs)


def reportrepair(reports):
    return compose(
        fnone(partial(reduce, mul)),
        partial(pairsum, 2020),
    )(reports)


def reportrepair2(reports):
    return compose(
        fnone(partial(reduce, mul)),
        partial(tripletesum3, 2020),
    )(reports)
