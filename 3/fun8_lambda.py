# funkcja lambda - skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, mozliwosc uzycia w miejscu deklaracji

def odejmij2(a, b):
    return a - b


print(odejmij2(6, 7))  # -1

odejmij = lambda a, b: a - b
print(odejmij(6, 3))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(vat=15, cena=3456))  # 3974.4

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 5, 10, 50, 77, 90, 200]
lista_nowe = []
for i in lista:
    print(i * 2)
    lista_nowe.append(i * 2)
print(lista_nowe)  # [2, 4, 10, 20, 100, 154, 180, 400]

print([i * 2 for i in lista])  # [2, 4, 10, 20, 100, 154, 180, 400]


def zmien(x):
    return x * 2


# robi to samo list(map(lambda x: x * 2, lista))
l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 10, 20, 100, 154, 180, 400]

# funkcje wyzszego rzędu
# map() - bierze lement z listy, wykunej funkcje na tych danych
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 10, 20, 100, 154, 180, 400]
# lambda jako funkcja anonimowa, wykonanie w miejscu deklaracji
# nie jest przypisana do zmiennej
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map(): [2, 4, 10, 20, 100, 154, 180, 400]
# Zastosowanie map(): [2, 4, 10, 20, 100, 154, 180, 400]
# Zastosowanie map(): [4, 8, 20, 40, 200, 308, 360, 800]
# Zastosowanie map(): [12, 24, 60, 120, 600, 924, 1080, 2400]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)

print(l3)  # [1, 2]

# filter() - pobiera element z kolekcji , sprawdza warunek podany funkcją
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter(): [1, 2]
# wyfiltrowac > 3 i < od 30, lista = [1, 2, 5, 10, 50, 77, 90, 200]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 30, lista))}")
# Zastosowanie filter(): [5, 10]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 30, lista))}")
