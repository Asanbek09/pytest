from cards import Card
import pytest

def test_equality():
    c1 = Card("something", "King")
    c2 = Card("nothing", "Armor King")
    if c1 != c2:
        pytest.fail("they are not equal")
