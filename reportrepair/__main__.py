import fileinput

from fp import compose, fmap

from . import reportrepair, reportrepair2


def main():
    lines = fileinput.input()

    repair = compose(
        reportrepair,
        list,
        fmap(int),
    )(lines)

    print(
        repair,
    )


def main2():
    lines = fileinput.input()

    repair = compose(
        reportrepair2,
        list,
        fmap(int),
    )(lines)

    print(
        repair,
    )


if __name__ == '__main__':
    # main()
    main2()
