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
