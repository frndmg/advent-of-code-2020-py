from functools import partial, reduce
from itertools import count, islice, takewhile
from operator import mul

from fp import compose, ffilter, fmap, length


def generate_path11(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(1)),
        count(1),
    )


def generate_path13(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(1)),
        count(3, 3),
    )


def generate_path15(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(1)),
        count(5, 5),
    )


def generate_path17(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(1)),
        count(7, 7),
    )


def generate_path21(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(2, 2)),
        count(1, 1),
    )


def is_tree(pos, local_map):
    x, y = pos

    row = local_map[x]
    c = row[y % len(row)]

    return c == '#'


def count_trees(local_map):
    local_map = local_map.split('\n')
    return count_trees_with_toboggan(local_map, generate_path13(len(local_map)))


def count_trees_with_toboggan(local_map, toboggan):
    trees_count = compose(
        length,
        ffilter(partial(is_tree, local_map=local_map)),
    )(toboggan)

    return trees_count


def multiply_trees_from_slopes(local_map, toboggans):
    return compose(
        partial(reduce, mul),
        fmap(partial(count_trees_with_toboggan, local_map)),
    )(toboggans)


def multiply_trees(local_map):
    local_map = local_map.split('\n')

    return multiply_trees_from_slopes(
        local_map,
        [
            generate_path11(len(local_map)),
            generate_path13(len(local_map)),
            generate_path15(len(local_map)),
            generate_path17(len(local_map)),
            generate_path21(len(local_map)),
        ]
    )
