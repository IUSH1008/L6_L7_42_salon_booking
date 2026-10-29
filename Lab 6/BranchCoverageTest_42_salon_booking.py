
import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


def test_unknown_service():
    with pytest.raises(ValueError):
        extra_time_charge("nails", 40, "junior", False)


def test_negative_duration():
    with pytest.raises(ValueError):
        extra_time_charge("haircut", -1, "junior", False)


def test_member_haircut():
    assert extra_time_charge("haircut", 50, "junior", True) == 50


def test_non_member_haircut():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_member_colour():
    assert extra_time_charge("colour", 75, "junior", True) == 0


def test_spa_member():
    assert extra_time_charge("spa", 100, "junior", True) == 100


def test_junior_long_extra_time():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_senior_long_extra_time():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_walk_in_two_people():
    assert can_book(2, 1, True) is True


def test_walk_in_three_people():
    assert can_book(3, 1, True) is False


def test_non_walk_in_large_party():
    assert can_book(5, 1, False) is False


def test_non_walk_in_too_many_services():
    assert can_book(3, 3, False) is False


def test_non_walk_in_valid_booking():
    assert can_book(4, 2, False) is True


def test_colour_weekday_open():
    assert arrival_status(10, True, False) == "open"


def test_colour_weekday_late():
    assert arrival_status(0, True, False) == "late"


def test_colour_weekday_closed():
    assert arrival_status(-6, True, False) == "closed"


def test_non_colour_weekend_open():
    assert arrival_status(15, False, True) == "open"


def test_non_colour_weekday_open():
    assert arrival_status(5, False, False) == "open"
