import re
from functools import partial
from operator import contains, methodcaller

from fp import (apply, compose, const, fmap, fnone, identity, swap, tuple_map,
                tupled)

NEEDED_KEYS = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
)


def between(lo, hi):
    return lambda x: lo <= x <= hi


byr_validator = compose(
    between(1920, 2002),
    int,
)

iyr_validator = compose(
    between(2010, 2020),
    int,
)

eyr_validator = compose(
    between(2020, 2030),
    int,
)


def get_height_validator(unit):
    if unit == 'cm':
        return between(150, 193)
    elif unit == 'in':
        return between(59, 76)
    else:
        return const(False)  # invalid unit


hgt_validator = compose(
    fnone(
        compose(
            tupled(apply),
            tuple_map(get_height_validator, int),
            swap,
            methodcaller('groups'),
        ),
        default=False,
    ),
    re.compile(r'^(\d+)(cm|in)$').match,
)

hcl_validator = compose(
    bool,
    re.compile(r'^#[0-9a-f]{6}$').match,
)

ecl_validator = compose(
    bool,
    re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$').match,
)

pid_validator = compose(
    bool,
    re.compile(r'^[0-9]{9}$').match,
)


KEYS_RULES = (
    ('byr', byr_validator),
    ('iyr', iyr_validator),
    ('eyr', eyr_validator),
    ('hgt', hgt_validator),
    ('hcl', hcl_validator),
    ('ecl', ecl_validator),
    ('pid', pid_validator),
)


def is_valid_passport(passport):
    return compose(
        all,
        fmap(partial(contains, passport)),
    )(NEEDED_KEYS)


def is_valid_passport2(passport):
    return compose(
        all,
        fmap(
            compose(
                tupled(apply),
                swap,
                tuple_map(passport.get, fnone),
            ),
        ),
    )(KEYS_RULES)


def make_passport(text):
    return compose(
        dict,
        fmap(methodcaller('split', ':')),
        re.compile(r'\s').split,
    )(text)
