class cErrorGravedad(Exception):
    def __init__(self, lugar):
        self.txt = lugar

    def print(self):
        print("Error cErrorGravedad en: " + self.txt)
