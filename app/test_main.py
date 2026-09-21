import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return 0 when years are 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return 0 when years are 14"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return 1 when years are 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1 when years are 23"),
        pytest.param(
            24, 24, [2, 2],
            id="should return 2 when years are 24"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return 2 when years are 27"
        ),
    ]
)
def test_cat_and_dog_age(
        cat_age: int,
        dog_age: int ,
        result: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_should_return_3_and_2_when_years_equals_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_when_years_equals_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
