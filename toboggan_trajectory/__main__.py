import fileinput

from . import count_trees, multiply_trees


def main():
    local_map = ''.join(fileinput.input())

    trees_count = count_trees(local_map)

    print(
        trees_count,
    )


def main2():
    local_map = ''.join(fileinput.input())

    trees_multiplied = multiply_trees(local_map)

    print(
        trees_multiplied,
    )


if __name__ == '__main__':
    # main()
    main2()
