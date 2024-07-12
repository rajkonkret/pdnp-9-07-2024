class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor (metoda inicjalizująca)
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja - ustawiamy pole jako prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"prędkość wynosi {self.__predkosc} km/h")

    def hamulec(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    # metoda prywatna
    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Opel", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# pooznaczeniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # prędkość wynosi 50 km/h
car.__predkosc = 0  # dodalismy pole o tej samej nazwie ale globalne
car.licznik()  # prędkość wynosi 50 km/h
print(car.__predkosc)  # 0 tu juz odczytujemy globalne
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.licznik()  # prędkość wynosi 0 km/h
# enkapsulacja - zabezpieczenie pol przed dostepem z zewnątrz(hermetyzacja)
# i wystawienie metod do zmmiany tych pól i odczytu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# prędkość wynosi 0 km/h
