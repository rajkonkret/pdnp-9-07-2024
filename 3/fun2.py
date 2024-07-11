# funkcje zwracające wynik
# kończą się słówkiem return
# gdy napotka return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 9))  # 15
print(odejmij(5, 1, 2))  # 2
print(odejmij())  # 0
print(odejmij(5, 1))  # 4
print(odejmij(1, c=9))
# print(odejmij(a := int(input("Podaj")), c=9))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=17000))

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Ok")  # Ok

# wynik tych funkcji można użyc dalej w programie
print(dodaj(5, 6) + oblicz_vat(500))  # 626.0
