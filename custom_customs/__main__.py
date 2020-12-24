import fileinput

from fp import compose, fmap
from operator import methodcaller

split_groups = methodcaller('split', '\n\n')


compute_yes_answers = compose(
    len,
    set,
    ''.join,
    methodcaller('split', '\n'),
)


def main():
    text = ''.join(fileinput.input())

    count_sum = compose(
        sum,
        fmap(compute_yes_answers),
        split_groups,
    )(text)

    print(
        count_sum,
    )


if __name__ == '__main__':
    main()
