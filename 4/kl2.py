class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    # dopisac metody wypisz_wiek, wypisz_wzrost
    def wypisz_wiek(self):
        print("Mam", self.wiek, "lat.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 56, 190, "m")
print(cz1)  # <__main__.Human object at 0x000001F2DF88D7F0>
cz2 = Human(imie="Tomek", wiek=89, wzrost=165)
print(cz2)
cz3 = Human(imie="MArek", wiek=45, wzrost=170)
print(cz3)

cz1.powitanie()
cz2.powitanie()
cz3.powitanie()
# Nazywam się Radek
# Nazywam się Tomek
# Nazywam się MArek
cz3.wypisz_wiek()  # Mam 45 lat.
cz3.ruszaj()
cz1.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
