import cards
import pytest

@pytest.fixture(scope="session")
def foo():
    return "fooo"

@pytest.fixture(scope="module")
def bar(foo):
    return "bar"

@pytest.fixture
def yahoo(foo, bar):
    return "yahoo"

def test_multi(foo, bar, yahoo):
    print(f"{foo=}")
    print(f"{bar=}")
    print(f"{yahoo=}")