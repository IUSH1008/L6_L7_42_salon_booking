import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


def test_unknown_service():
    with pytest.raises(ValueError):
        extra_time_charge("nails", 40, "junior", False)


def test_negative_duration():
    with pytest.raises(ValueError):
        extra_time_charge("haircut", -1, "junior", False)


def test_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0


def test_member_extra_time():
    assert extra_time_charge("haircut", 50, "junior", True) == 50


def test_junior_rate():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_senior_rate():
    assert extra_time_charge("haircut", 40, "senior", False) == 180


def test_extra_over_60_junior():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_extra_over_60_senior():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_spa_member():
    assert extra_time_charge("spa", 90, "junior", True) == 0


def test_walk_in_allowed():
    assert can_book(2, 1, True) is True


def test_walk_in_too_large():
    assert can_book(3, 1, True) is False


def test_party_too_large():
    assert can_book(5, 1, False) is False


def test_too_many_services():
    assert can_book(3, 3, False) is False


def test_regular_booking_allowed():
    assert can_book(4, 2, False) is True


def test_arrival_open():
    assert arrival_status(10, True, False) == "open"


def test_arrival_late():
    assert arrival_status(0, True, False) == "late"


def test_arrival_closed():
    assert arrival_status(-6, True, False) == "closed"


def test_weekend_cutoff():
    assert arrival_status(15, False, True) == "open"