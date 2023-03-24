class bf_gen:
    def __init__(self, param, ascii_liste = False):
        self.sonuc = ""
        if ascii_liste:
            for c in param:
                for i in range(0, c):
                    self.sonuc += "+"
                self.sonuc += ".>"
        else:
            for c in param:
                for i in range(0, ord(c)):
                    self.sonuc += "+"
                self.sonuc += ".>"
    def getir(self):
        return self.sonuc