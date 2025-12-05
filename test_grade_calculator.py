# test_grade_calculator.py

import pytest
from grade_calculator import calculate_average, get_grade, is_pass

def test_calculate_average_normal_case():
    assert calculate_average([80, 90, 100]) == 90

def test_calculate_average_single_mark():
    assert calculate_average([75]) == 75

def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

def test_get_grade_boundaries():
    assert get_grade(95) == "A"
    assert get_grade(80) == "B"
    assert get_grade(65) == "C"
    assert get_grade(55) == "D"
    assert get_grade(40) == "F"

def test_is_pass():
    assert is_pass(75) is True
    assert is_pass(50) is True
    assert is_pass(49) is False
