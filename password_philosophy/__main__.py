import fileinput
import re

from fp import compose, count, ffilter

from . import valid_password, valid_password2


def main():
    lines = fileinput.input()

    valid_passwords_count = compose(
        count,
        ffilter(valid_password),
    )(lines)

    print(
        valid_passwords_count,
    )


def main2():
    lines = fileinput.input()

    valid_passwords_count = compose(
        count,
        ffilter(valid_password2),
    )(lines)

    print(
        valid_passwords_count,
    )


if __name__ == '__main__':
    # main()
    main2()
