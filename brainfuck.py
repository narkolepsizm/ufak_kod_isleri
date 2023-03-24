class bf:
    def __init__(self, kod):
        self.alfabe = ['>', '<', '+', '-', '.', ',', '[', ']']
        kod = "".join(list(filter(self.filtrele, kod)))
        self.kod_oku(kod)

    def filtrele(self,kod):
        if kod in self.alfabe:
            return True
        else:
            return False

    def getir(self):
        return self.sonuc

    def kod_oku(self,kod):
        hafiza = [0 for i in range(32768)]
        isaret = 0
        kod_isaret = 0
        dongu_index = []
        self.sonuc = ""
        while kod_isaret < len(kod):
            if kod[kod_isaret] == '>':
                isaret += 1
            elif kod[kod_isaret] == '<':
                isaret -= 1
            elif kod[kod_isaret] == '+':
                hafiza[isaret] += 1
            elif kod[kod_isaret] == '-':
                hafiza[isaret] -= 1
            elif kod[kod_isaret] == '.':
                self.sonuc += chr(hafiza[isaret])
            elif kod[kod_isaret] == ',':
                hafiza[isaret] = ord(str(input())[0])
            elif kod[kod_isaret] == '[':
                dongu_index.append(kod_isaret)
            elif kod[kod_isaret] == ']':
                if hafiza[isaret] == 0:
                    dongu_index.pop()
                else:
                    kod_isaret = dongu_index[-1] - 1
            kod_isaret += 1