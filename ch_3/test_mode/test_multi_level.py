import cards
import pytest
from tempfile import TemporaryDirectory
import pathlib

@pytest.fixture(scope="module")
def cards_db_module():
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

@pytest.fixture(scope="function")
def empty_cards_db(cards_db_module):
    cards_db_module.delete_all()
    return cards_db_module

def test_one_item(cards_db_module):
    cards_db_module.add_card(cards.Card("smth"))
    count = cards_db_module.count()
    

def test_empty(cards_db_module):
    count = cards_db_module.count()
