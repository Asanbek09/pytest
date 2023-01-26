from cards import Card

def test_equality():
    c1 = Card("something", "King")
    c2 = Card("nothing", "Armor King")
    assert c1 == c2

if __name__ == '__main__':
    test_equality()