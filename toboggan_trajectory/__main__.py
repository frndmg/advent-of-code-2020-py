import fileinput

from . import count_trees


def main():
    local_map = ''.join(fileinput.input())

    trees_count = count_trees(local_map)

    print(
        trees_count,
    )


if __name__ == '__main__':
    main()
