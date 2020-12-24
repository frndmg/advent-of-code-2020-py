import pytest
from custom_customs.__main__ import (compute_yes_answers,
                                     how_many_questions_everyone_answered_yes)


@pytest.mark.parametrize(('group', 'yes_count'), [
    ('aaa', 1),
    ('bab', 2),
    ('a\na\na', 1),
    ('a\nab\na', 2),
])
def test_compute_yes_answers(group, yes_count):
    assert compute_yes_answers(group) == yes_count


@pytest.mark.parametrize(('group', 'yes_count'), [
    ('aaa', 1),
    ('a\nab', 1),
    ('ab\nabc\nc', 0),
    ('ab\nabc\nba', 2),
])
def test_how_many_questions_everyone_answered_yes(group, yes_count):
    assert how_many_questions_everyone_answered_yes(group) == yes_count
