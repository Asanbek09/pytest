import cards
import pytest
from tempfile import TemporaryDirectory
import pathlib

@pytest.fixture(scope="session")
def cards_db_session():
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

@pytest.fixture(scope="function")
def cards_db(cards_db_session):
    cards_db_session.delete_all()
    return cards_db_session