import pytest

from rrr_1.rrr_1 import hello_world


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("testing", "Hello world!: testing"),
        ("123", "Hello world!: 123"),
    ],
)
def test_hello_world(test_input, expected):
    assert hello_world(test_input) == expected
