import cards
from tempfile import TemporaryDirectory
import pathlib

def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        count = db.count()
        db.close()
        assert count == 0

def test_one_item():
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        db.add_card(cards.Card("smth"))
        count = db.count()
        db.close()
        assert count == 1