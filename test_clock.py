from clock import tell_time
import pytest


@pytest.mark.parametrize("minutes, representation",
                         [(15, 'quarter-past'), (30, 'half-past'), (45, 'quarter to')])
def test_tell_time_cardinal(minutes, representation):
    assert tell_time(minutes) == representation


@pytest.mark.parametrize("minutes, representation",
                         [(0, ''), (5, ''), (31, ''), (43, ''), (51, '')])
def test_tell_time_non_cardinal(minutes, representation):
    assert tell_time(minutes) == representation

@pytest.mark.parametrize("minutes, representation",
                         [(-1, ''), (61, '')])
def test_tell_time_improper(minutes, representation):
    with pytest.raises(ValueError):
        assert tell_time(minutes) == representation
