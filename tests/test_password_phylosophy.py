from password_philosophy.password_philosophy import valid_password, valid_password2


def test_valid_password():
    assert valid_password('1-3 a: abcde')
    assert not valid_password('1-3 b: cdefg')
    assert valid_password('1-9 c: ccccccccc')


def test_valid_password2():
    assert valid_password2('1-3 a: abcde')
    assert not valid_password2('1-3 b: cdefg')
    assert not valid_password2('1-9 c: ccccccccc')
