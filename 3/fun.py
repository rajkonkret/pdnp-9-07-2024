# funkcja - wydzielony fragment kodu, możliwosć wykonania w dowolnym momencie
# moze posiadać argumenty
# może zwracac wartości
# deklaracja funkcji musi być przed miejscem użycia funkcji
# w miejscu deklaracji funkcja się nie wykonuje
# żeby funkcję wykonać trzeba ją wywołąć


a = 6
b = 8


# deklaracja funkcji - tu się nie wykona
# def nazwa_funkcji i nawiasy ()
# PEP8 wymaga by były dwie puste linie
def dodaj():  # nia ma argumentów
    print(a + b)  # zmienne globalnego z zewnętrznego scopu programu


def dodaj2(a, b):  # funkcja przyjmuje dwa argumenty a i b, obowiazkowe do przekazania
    print(a + b)


def odejmij(a, b, c=0):  # a  i b obowiązkowe, c ma wartość domyślną
    print(a - b - c)


# wywołanie funkcji
# nazwa_funkcji i nawiasy ()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty przekazane po pozycji
dodaj2(15, 9)  # 24
odejmij(5, 6)  # -1 c=0
odejmij(5, 6, 7)  # -8 c=7

# przekazanie argumntów po nazwie
odejmij(c=9, b=9, a=2)
odejmij(a=9, b=9, c=2)

# przekazac mieszane
odejmij(1, c=9, b=5)
# odejmij(1, c=9, a=1)  # TypeError: odejmij() got multiple values for argument 'a'
# odejmij(b=7, 1, 2)  # SyntaxError: positional argument follows keyword argument

print(dodaj())  # None
# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
