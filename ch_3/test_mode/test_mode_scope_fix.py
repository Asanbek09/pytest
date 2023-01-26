import cards
import pytest
from tempfile import TemporaryDirectory
import pathlib

@pytest.fixture(scope="module")
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

def test_one_item(cards_db):
    cards_db.delete_all()
    cards_db.add_card(cards.Card("smth"))
    count = cards_db.count()
    assert count == 1

def test_empty(cards_db):
    cards_db.delete_all()
    count = cards_db.count()
    assert count == 0
