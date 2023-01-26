from cards import Card

class TestEquality:
    def test_equality(self):
        c1 = Card("smth", "King", "todo", 111)
        c2 = Card("smth", "King", "todo", 111)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card("smth", "King", "todo", 111)
        c2 = Card("smth", "King", "todo", 2222)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("smth", "King", "todo", 111)
        c2 = Card("smth", "King", "done", 111)
        assert c1 != c2