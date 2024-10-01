import pytest
from datetime import datetime, timedelta

data = [
    (datetime(2024, 10, 1), datetime(2024, 9, 30), timedelta(1)),
    (datetime(2024, 10, 1), datetime(2024, 10, 2), timedelta(1)),
]

@pytest.mark.parametrize("a,b,expected", data)
def test_delta(a, b, expected):
    diff = a - b
    assert diff == expected