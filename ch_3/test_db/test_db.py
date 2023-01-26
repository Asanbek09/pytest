from some_db import DB

def test_db():
    db = DB()

    result = db.some_action()

    db.close()
    assert result == 42