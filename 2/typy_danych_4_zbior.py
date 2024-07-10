# zbiór - set - przechowuje unikalne elementy
# nie zachowuje kolejsności przy dodawaniu elementów
# nie posiadu indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - rzutowanie na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# tworzenie pustego seta, musi byc komendą set()
zb2 = set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))
zb2.add(22)
print(zb2)

zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(33 in zbior)  # True

# usunięcie elementów w zbiorze
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# pop() - usunięcie pierwszego elemntu ze zbioru
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()
print(id(zbior))  # 2578361274368
print(id(zbior_copy))  # 2578361274144

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>

# suma zbiorów
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(zbior)
print(zbior_2)
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

# cześć wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {777, 66, 22}
print(zbior.difference(zbior_2))  # {777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

# łaczy zbiory, zmmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

lista = list(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(lista)  # (66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62)

krotka = tuple(zbior)
print(krotka)  # (66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62)
