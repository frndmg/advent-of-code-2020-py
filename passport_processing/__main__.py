import fileinput
from operator import methodcaller
from fp import compose, ffilter, fmap, length

from .passport import is_valid_passport, make_passport, is_valid_passport2


def process_passports():
    text = ''.join(fileinput.input())

    valid_passports_count = compose(
        length,
        ffilter(is_valid_passport),
        fmap(make_passport),
        methodcaller('split', '\n\n'),
    )(text)

    print(
        valid_passports_count,
    )


def process_passports2():
    text = ''.join(fileinput.input())

    valid_passports_count = compose(
        length,
        ffilter(is_valid_passport2),
        fmap(make_passport),
        methodcaller('split', '\n\n'),
    )(text)

    print(
        valid_passports_count,
    )


if __name__ == '__main__':
    process_passports2()
