class Round:

    def __init__(self, name, matches=None, completed=None):
        self.name = name
        self.matches = matches or []
        self.completed = completed or False
