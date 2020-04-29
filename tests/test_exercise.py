import pytest
from src.apartment import Apartment

def test_exercise():
    apt_one = Apartment(1, 15, 5200)
    apt_two = Apartment(2, 37, 4000)

    assert not apt_one.larger_than(apt_two)
    assert apt_one.price_difference(apt_two) == 70000
    assert apt_two.more_expensive_than(apt_one)
