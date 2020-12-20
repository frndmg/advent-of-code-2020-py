from reportrepair import reportrepair, reportrepair2


def test_reportrepair():
    assert reportrepair([
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]) == 514579

    assert reportrepair([
        1010,
        1010,
    ]) == 1010 * 1010

    assert reportrepair([]) == None


def test_reportrepair2():
    assert reportrepair2([
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]) == 241861950
