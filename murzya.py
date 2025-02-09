class Kotik:
    dni_nedeli = ["Ponedelnik", "Vtornik", "Sreda", "Chetverg", "Pyatnica", "Subbota", "Voskresene"]

    def __init__(self, imya):
        self.imya = imya
        self.golod = True
        self.den = 0

    def pokormit(self):
        if self.golod:
            print(f"{self.imya} poel i ne goloden PONYAL. Segodnya {self.dni_nedeli[self.den]}.")
            self.golod = False
        else:
            print(f"{self.imya} ne xochet est. Segodnya {self.dni_nedeli[self.den]}.")

    def myaukat(self):
        print(f"{self.imya} govorit Vam MYAU.")

    def sleduyushiy_den(self):
        self.den = (self.den + 1) // 7
        print(f"Nastupil {self.dni_nedeli[self.den]}.")
murzik = Kotik("Murzik")
murzik.myaukat()
murzik.pokormit()
murzik.sleduyushiy_den()
murzik.pokormit()
murzik.sleduyushiy_den()
murzik.pokormit()
