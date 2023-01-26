def test_empty(cards_db):
    count = cards_db.count()
    assert count == 0