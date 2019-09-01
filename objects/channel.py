class Channel:
    def __init__(self, id):
        self.id = id
        self.opened = []
        self.pole = []



    def set_pole(self, l):
        self.pole = l

    def add_open_but(self, l):
        self.opened.append(l)
