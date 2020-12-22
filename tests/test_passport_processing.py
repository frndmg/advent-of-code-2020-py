from passport_processing.__main__ import process_passports, process_passports2
from passport_processing.passport import (hgt_validator, is_valid_passport,
                                          make_passport)


def test_make_passport():
    assert make_passport(
        'a:b c:d\n'
        'e:1 k:True'
    ) == dict(a='b', c='d', e='1', k='True')


def test_is_valid_passport():
    assert is_valid_passport(
        dict(
            hcl='#ae17e1',
            iyr='2013',
            eyr='2024',
            ecl='brn',
            pid='760753108',
            byr='1931',
            hgt='179cm',
        )
    )

    assert not is_valid_passport(
        dict(
            hcl='#ae17e1',
            eyr='2024',
            ecl='brn',
            pid='760753108',
            byr='1931',
            hgt='179cm',
        )
    )


def test_hgt_validator():
    assert not hgt_validator('120cm')
    assert hgt_validator('150cm')
    assert hgt_validator('193cm')
    assert not hgt_validator('50in')
    assert hgt_validator('59in')


def test_passport_processing(capsys, mocker):
    mocker.patch(
        'fileinput.input',
        return_value=[
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
            'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
            '\n',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
            'hcl:#cfa07d byr:1929\n',
            '\n',
            'hcl:#ae17e1 iyr:2013\n',
            'eyr:2024\n',
            'ecl:brn pid:760753108 byr:1931\n',
            'hgt:179cm\n',
            '\n',
            'hcl:#cfa07d eyr:2025 pid:166559648\n',
            'iyr:2011 ecl:brn hgt:59in',
        ]
    )

    process_passports()

    captured = capsys.readouterr()
    assert captured.out == '2\n'


def test_passport_processing2(capsys, mocker):
    mocker.patch(
        'fileinput.input',
        return_value=[
            'eyr:1972 cid:100\n',
            'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\n',
            '\n',
            'iyr:2019\n',
            'hcl:#602927 eyr:1967 hgt:170cm\n',
            'ecl:grn pid:012533040 byr:1946\n',
            '\n',
            'hcl:dab227 iyr:2012\n',
            'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\n',
            '\n',
            'hgt:59cm ecl:zzz\n',
            'eyr:2038 hcl:74454a iyr:2023\n',
            'pid:3556412378 byr:2007\n',
            '\n',
            'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\n',
            'hcl:#623a2f\n',
            '\n',
            'eyr:2029 ecl:blu cid:129 byr:1989\n',
            'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\n',
            '\n',
            'hcl:#888785\n',
            'hgt:164cm byr:2001 iyr:2015 cid:88\n',
            'pid:545766238 ecl:hzl\n',
            'eyr:2022\n',
            '\n',
            'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
        ]
    )

    process_passports2()

    captured = capsys.readouterr()
    assert captured.out == '4\n'
