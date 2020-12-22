from passport_processing.__main__ import process_passports
from passport_processing.passport import make_passport, is_valid_passport


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
