import pytest

from src import coordinates


@pytest.mark.parametrize("country, expected", [(), ()])
def test_get_coordinates(country, expected):
    assert coordinates.get_coordinates(country) == expected
