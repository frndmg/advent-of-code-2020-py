import pytest
from binary_boarding.__main__ import compute_seat_id


@pytest.mark.parametrize(('seat', 'seat_id'), [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
    ('FFFFFFFLLL', 0),
    ('BBBBBBBRRR', 1023)
])
def test_compute_seat_id(seat, seat_id):
    assert compute_seat_id(seat) == seat_id
