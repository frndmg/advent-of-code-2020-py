from functools import partial
from itertools import count, takewhile

from fp import compose, ffilter, length


def generate_path(rows_count):
    return zip(
        takewhile(lambda x: x < rows_count, count(1)),
        count(3, 3),
    )


def is_tree(pos, local_map):
    x, y = pos

    row = local_map[x]
    c = row[y % len(row)]

    return c == '#'


def count_trees(local_map):
    rows = local_map.split('\n')

    path = generate_path(len(rows))

    trees_count = compose(
        length,
        ffilter(partial(is_tree, local_map=rows)),
    )(path)

    return trees_count
