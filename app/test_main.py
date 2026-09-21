import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
    ]
)
def test_cat_and_dog_age(cat_age, dog_age, result) -> None:             #1
    assert get_human_age(cat_age, dog_age) == result


def test_should_return_3_and_2_when_years_equals_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_when_years_equals_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
