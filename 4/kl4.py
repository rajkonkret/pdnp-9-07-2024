from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dodajemy dekorator dla metody abstrakcyjnej
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # klasa Kura dziedziczy po klasie Ptak
    def __init__(self, gatunek):
        # musimy obowiązkowo wywołąć init z kalsy wyzszej za pomocą super()
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kok ko ko ko ")

    def dziobanie(self):
        print(f"Tu {self.gatunek} idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kier kier kir")

    def polowanie(self):
        print("Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# orz = Ptak("Orzel", 45)
# orz.latam()  # Tu Orzel Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
orz2 = Orzel("Orzel Bielik", 55)
# lista_ptaki = [orz, kur1, kur2, orz2]
lista_ptaki = [kur2, orz2]

# polimorfizm - obiekty maja wspolne cechy, metody
for i in lista_ptaki:
    i.latam()
# Tu Orzel Lecę z szybkością 45
# Tu Kura Lecę z szybkością 0
# Tu Kura domowa Ja nie latam
for i in lista_ptaki:
    i.wydaj_odglos()  # kok ko ko ko
# kok ko ko ko
# Kier kier kir
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa('Sowa', 14)
kur2.dziobanie()
orz2.polowanie()
# Tu Kura domowa idę sobie podziobać
# Rozpoczynam polowanie
