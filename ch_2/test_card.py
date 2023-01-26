from cards import Card

def test_field_access():
    c = Card("something", "King", "todo", 321)
    assert c.summary == "something"
    assert c.owner == "King"
    assert c.state == "todo"
    assert c.id == 321

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "King", "todo", 321)
    c2 = Card("something", "King", "todo", 321)
    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card("something", "King", "todo", 321)
    c2 = Card("something", "King", "todo", 456231)
    assert c1 == c2


def test_inequality():
    c1 = Card("something", "King", "todo", 321)
    c2 = Card("completely different", "okken", "done", 321)
    assert c1 != c2


def test_from_dict():
    c1 = Card("something", "King", "todo", 321)
    c2_dict = {"summary": "something", "owner": "King", "state": "todo", "id": 321}
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c1 = Card("something", "King", "todo", 321)
    c2 = c1.to_dict()
    c2_expected = {"summary": "something", "owner": "King", "state": "todo", "id": 321}
    assert c2 == c2_expected
