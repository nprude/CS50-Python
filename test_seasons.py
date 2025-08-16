from seasons import calculate_minutes
from datetime import date, timedelta
import pytest

def test_exact_minute_count():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    assert calculate_minutes(yesterday) == "One thousand, four hundred forty minutes"

def test_zero_minutes():
    today = date.today().isoformat()
    assert calculate_minutes(today) == "Zero minutes"

def test_known_value():
    fixed_today = date(2000, 1, 1)
    result = calculate_minutes("1999-01-01", today=fixed_today)
    assert result == "Five hundred twenty-five thousand, six hundred minutes"
def test_invalid_date_format():
    with pytest.raises(ValueError):
        calculate_minutes("February 6th, 1998")

