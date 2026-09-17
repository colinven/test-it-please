from problems.p1_sum_digits.solution import sum_digits


def test_example_multi_digit():
    assert sum_digits(1234) == 10


def test_example_single_digit():
    assert sum_digits(7) == 7


def test_zero():
    assert sum_digits(0) == 0


def test_all_same_digits():
    assert sum_digits(1111) == 4


def test_trailing_zeros():
    assert sum_digits(1200) == 3


def test_large_number():
    assert sum_digits(999999999) == 81
