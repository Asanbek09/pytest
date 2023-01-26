from cards import Card

def test_to_dict():
    c1 = Card("smth", "King", "todo", 222)
    c2 = c1.to_dict()

    c2_expected = {
        "summary": "smth", "owner": "King", "state": "todo", "id": 222
    }
    assert c2 == c2_expected