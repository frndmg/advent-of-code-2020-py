import re
from operator import methodcaller

from fp import compose, fnone, tuple_map, tupled

LINE_RE = re.compile(r'^(\d+)-(\d+)\s(\D):\s(\D+)$')


def parse_line(line):
    return compose(
        tuple_map(int, int),
        fnone(methodcaller('groups')),
        LINE_RE.match,
    )(line)


def valid_password(line):
    aguments = parse_line(line)

    if aguments is None:
        raise ValueError(f'invalid line {line}')

    m, M, character, password = aguments

    return m <= password.count(character) <= M


def valid_password2(line):
    aguments = parse_line(line)

    if aguments is None:
        raise ValueError(f'invalid line {line}')

    i, j, character, password = aguments

    exists_on_i = password[i - 1] == character
    exists_on_j = password[j - 1] == character

    return exists_on_i ^ exists_on_j
