class User():
    def __init__(self, username, password, id = None) -> None:
        self.id = id
        self.username = username
        self.password = password
    