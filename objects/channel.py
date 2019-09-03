from loguru import logger

class Channel:
    def __init__(self, id):
        self.id = id
        self.opened = []
        self.pole = []



    def set_pole(self, l):
        self.pole = l

    def add_open_but(self, l):
        self.opened.append(l)
        logger.info(l)
        if self.pole[l[0]][l[1]]=='0':
            i = l[0]
            j = l[1]
            if i>0:
                self.add_open_but([i-1, j])
                if j>0:
                    self.add_open_but([i-1, j-1])
                if j<len(self.pole[0]):
                    self.add_open_but([i-1, j+1])
            if i<len(self.pole):
                self.add_open_but([i+1, j])
                if j>0:
                    self.add_open_but([i+1, j-1])
                if j<len(self.pole[0]):
                    self.add_open_but([i+1, j+1])
            if j>0:
                self.add_open_but([i, j-1])
            if j<len(self.pole[0]):
                self.add_open_but([i, j+1])
