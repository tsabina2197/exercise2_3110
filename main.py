class Vaqt:
    def __init__(self, soat, minut, sekund):
        self.soat = soat
        self.minut = minut
        self.sekund = sekund

    def vaqt_korsat(self):
        return f"{self.soat:02d}:{self.minut:02d}:{self.sekund:02d}"

    def sekund_qosh(self, s):
        self.sekund += s
        self.minut += self.sekund // 60
        self.soat += self.minut // 60
        self.sekund %= 60
        self.minut %= 60
        self.soat %= 24


v = Vaqt(23, 59, 50)
print(v.vaqt_korsat())
v.sekund_qosh(15)
print(v.vaqt_korsat())
