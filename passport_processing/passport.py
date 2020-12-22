import re
from operator import methodcaller, contains
from functools import partial

from fp import compose, fmap


NEEDED_KEYS = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
)


def is_valid_passport(passport):
    return compose(
        all,
        fmap(partial(contains, passport)),
    )(NEEDED_KEYS)


def make_passport(text):
    return compose(
        dict,
        fmap(methodcaller('split', ':')),
        partial(re.split, r'\s'),
    )(text)
