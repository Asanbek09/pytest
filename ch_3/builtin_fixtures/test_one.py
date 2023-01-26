import cards

def test_one_item(cards_db):
    cards_db.add_card(cards.Card("smth"))
    count = cards_db.count()
    assert count == 1
