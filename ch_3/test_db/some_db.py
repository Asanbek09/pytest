class DB():
    def __init__(self):
        print("-- connect to database --")

    def close(self):
        print("-- disconnect from database --")

    def some_action(self):
        print("-- DB: some_action() --")
        return 42