
class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros
        #self.hissi_nimi = nimi


    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alinkerros or kohdekerros > self.ylinkerros:
            print(f'Hississä ei ole kerrosta {kohdekerros}.')
            return


        while self.kerros < kohdekerros:
            self.kerros_ylos()

        while self.kerros > kohdekerros:
            self.kerros_alas()

        if self.kerros == kohdekerros:
            print(f'"Pling" hissi on kerroksessa: {kohdekerros} varo sulkeutuvia ovia.')

        return


    def kerros_alas(self):
        print(f'Hissi on kerroksessa: {self.kerros}')
        self.kerros -= 1
        return


    def kerros_ylos(self):
        print(f'Hissi on kerroksessa: {self.kerros}')
        self.kerros += 1
        return



class Talo:
    def __init__(self, alinkerros, ylinkerros, lkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.maara = lkm
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(alinkerros, ylinkerros))


    def aja_hissia(self, numero, kohdekerros):
        print(f'Ajetaan hissiä numero {numero} kerrokseen {kohdekerros}')
        self.hissit[numero - 1].siirry_kerrokseen, {kohdekerros}


    def tarkastaja(self):
        print(f'Tarkastus: {self.ylinkerros}')

    def palohalytys(self):
        self.kohdekerros = self.alinkerros
        print(f'Palohälytys! Hissit siirtyy kerrokseen: {self.kohdekerros}')







t1 = Talo(1, 9, 2)


t1.aja_hissia(1, 3)
t1.aja_hissia(1, 4)
t1.aja_hissia(1, 7)
t1.aja_hissia(1, 2)
t1.aja_hissia(2, 6)

t1.palohalytys()


