import pytest
from custom_customs.__main__ import compute_yes_answers


@pytest.mark.parametrize(('group', 'yes_count'), [
    ('aaa', 1),
    ('bab', 2),
    ('a\na\na', 1),
    ('a\nab\na', 2),
])
def test_compute_yes_answers(group, yes_count):
    assert compute_yes_answers(group) == yes_count
