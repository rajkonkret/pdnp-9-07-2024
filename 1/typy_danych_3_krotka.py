# krotka - kolekcja przechowujaca dowolna liczbę danych, dowolnego typu
# niemutowalna
# pozwala efektywniej zarządzać pamięcią
# jedoelementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # str

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

# wyznacznikiem tupli jest przecinek
tupla_3 = "Radek",
tupla_4 = ("Radek",)  # PEP* prosi by przy tuplach jednoelementowych tworzyć je z użyciem nawiasu ()
print(type(tupla_3))  # <class 'tuple'>
print(type(tupla_4))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla_names = "Radek", "Tomek", "Zenek", "Marcin", "Kasia", "Marek"
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Kasia', 'Marek')
print(type(tupla_names))  # <class 'tuple'>

print(tupla_liczby[2])  # 22.34
print(tupla_liczby[3])  # 11

# del tupla_liczby[0]  # TypeError: 'tuple' object doesn't support item deletion
del tupla_liczby  # usunięcie tupli
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

print(tupla_names.index("Radek"))  # 0
print(tupla_names.count("Tomek"))  # 1

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2  # automatycznie podstawił pod z mienne według kolejnosci
print(a, b)  # 1 2
a, b = tup
print(a, b)  # 1 2

tup_1 = 1, 2, 3
# a,b = tup_1  # ValueError: too many values to unpack (expected 2)

a, *b = tup_1  # * - worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_names)
*name1, name2, name3 = tupla_names
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Marcin'] Kasia Marek

name1, *name2, name3 = tupla_names
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Marcin', 'Kasia'] Marek

name1, name2, *name3 = tupla_names
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marcin', 'Kasia', 'Marek']
print(name3[2])  # Kasia

name1, name2, *name3 = "Ela", "Tomek"
print(name1, name2, name3)  # Ela Tomek []

# sortowanie tupli zwraca listę
print(sorted(tupla_names))  # ['Kasia', 'Marcin', 'Marek', 'Radek', 'Tomek', 'Zenek']

lista = list(tupla_names)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marcin', 'Kasia', 'Marek']
print(type(lista))  # <class 'list'>
