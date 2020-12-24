import pytest
from binary_boarding.__main__ import compute_seat_id, compute_missing_seat_id


@pytest.mark.parametrize(('seat', 'seat_id'), [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
    ('FFFFFFFLLL', 0),
    ('BBBBBBBRRR', 1023)
])
def test_compute_seat_id(seat, seat_id):
    assert compute_seat_id(seat) == seat_id


@pytest.mark.parametrize(('seats_ids', 'missing_seat_id'), [
    ([1, 2, 3, 5], 4),
    ([99, 100, 102], 101),
])
def test_compute_missing_seat_id(seats_ids, missing_seat_id):
    assert compute_missing_seat_id(seats_ids) == missing_seat_id
