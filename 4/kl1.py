# klasy - elementy programowania obiektowego
# klasa - szablon, przepis, stempel
# obiekt - zbudowany elemnt wg przepisu (klasy)
# klasa - pola, metody
# obiekty - instancja klasy
# definicja klasy - nic sie nie wykona
# aby korzystać z elementów klasy musimy zbudować z niej obiekt

class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print("Nazywam się", self.imie)


print(Human.__doc__)  # Klasa Human opisująca człowieka w Pythonie
# print(print.__doc__)
#  pydoc -b
#  pydoc -w kl1

# tworzenie obiektu
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001655FFB16A0>
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
#
# None
cz1.wiek = 50
cz1.imie = "Angelika"
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
# Angelika
# 50
cz1.powitanie()  # Nazywam się Angelika

# stworzyc obiekt odmiennej plci, nadac imie, wiek, plec, wypisac stan obiektu
cz2 = Human()
cz2.wiek = 45
cz2.imie = "Tomek"
cz2.plec = "m"
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
# m
# Tomek
# 45
