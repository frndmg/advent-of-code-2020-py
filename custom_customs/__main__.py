import fileinput
from functools import partial, reduce
from operator import methodcaller

from fp import compose, fmap

split_groups = methodcaller('split', '\n\n')


compute_yes_answers = compose(
    len,
    set,
    ''.join,
    methodcaller('split', '\n'),
)


how_many_questions_everyone_answered_yes = compose(
    len,
    partial(reduce, set.intersection),
    fmap(set),
    methodcaller('split', '\n'),
)


def main():
    text = ''.join(fileinput.input())

    count_sum = compose(
        sum,
        fmap(how_many_questions_everyone_answered_yes),
        split_groups,
    )(text)

    print(
        count_sum,
    )


if __name__ == '__main__':
    main()
