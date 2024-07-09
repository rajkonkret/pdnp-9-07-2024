# kolekcje
# lista - przechowuje wiele danych, róznego typu w jednej liscie

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementu na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Kasia")
print(f"Lista osób zdających egzamin: {lista}")
# Lista osób zdających egzamin: ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kasia']
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kasia']
#    0          1       2         3       4
#    -5        -4       -3       -2       -1
# wypisanie lementu z listy po indeksie
print(lista[0])  # indeks 0 - pierwszy element z listy, Radek
print(lista[2])  # Zenek
print(lista[3])  # Marek
print(lista[4])  # Kasia
# print(lista[5])  # IndexError: list index out of range
print(len(lista))  # 5
# ostatni indeks 5 - 4 = -1 ostatni element
print(lista[-1])  # Kasia

# wypisać fragment listy, slicowanie
print(lista[0:3])  # start: stop(niewłącznie) ['Radek', 'Tomek', 'Zenek'] 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:4])  # ['Zenek', 'Marek'] 2,3
print(lista[2:])  # ['Zenek', 'Marek', 'Kasia'] wypisze do końća
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kasia']
print(lista[6:10])  # []
print(lista[2:10])  # ['Zenek', 'Marek', 'Kasia']
print(lista[2:3])  # ['Zenek'] o indeksie 2
print(lista[2:2])  # []
print(lista[-2:0])  # [3:0] -> []
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek'] [0:3]
print(lista[0:4:2])  # start:stop:krok  # ['Radek', 'Zenek']

lista_15 = list(range(15))  # 0 .. 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(type(lista_15))  # <class 'list'>
print(lista_15[-10])  # 5
print(lista_15[0:10:3])  # [0, 3, 6, 9]

# nadpisanie elementu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Mikołaj', 'Marek', 'Kasia']  na indeksie 2 zmienione

# rozszerzenie listy, wstawienie we wskazany indeks
lista.insert(1, "Ela")
print(lista)  # ['Radek', 'Ela', 'Tomek', 'Mikołaj', 'Marek', 'Kasia'] dodoane na indeks 1
print(len(lista))  # 6
lista.insert(11, "Bożena")
print(lista)  # ['Radek', 'Ela', 'Tomek', 'Mikołaj', 'Marek', 'Kasia', 'Bożena']

# sprawdzenie indeksu elementu
print(lista.index("Bożena"))  # 6

# usunięcie elementu
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Ela', 'Tomek', 'Marek', 'Kasia', 'Bożena']

# usunięcie elementu po indeksie, zwraca usunięty element
print(lista.pop(5))  # Bożena
print(lista)  # ['Radek', 'Ela', 'Tomek', 'Marek', 'Kasia']
print(lista.pop())  # Kasia, ostatni
print(lista.pop(-2))  # Tomek
print(lista)  # ['Radek', 'Ela', 'Marek']

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b jak linia 80? skopiowanie referencji (adres w pamieci)
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)  # ['Radek', 'Ela', 'Marek'] ['Radek', 'Ela', 'Marek']
lista.clear()  # czyszczenie listy, podobna operacja jak 82?
print(lista_2, lista)  # [] [][] []
print(lista_copy)  # ['Radek', 'Ela', 'Marek']
print(id(lista))  # 2632492896640
print(id(lista_2))  # 2632492896640
print(id(lista_copy))  # 2632493217088

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'agata', 'lena']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']
lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']
lista_osob.reverse()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek'] tylko odwraca

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

print(liczby.pop(2))  # usunięcie po indeksie, indeks 2, element 34
print(liczby)  # [54, 999, 666, 12.34, 687, 'A']

tekst = "Pyt hon."
lista1 = list(tekst)  # list() rzutowanie na listę, rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', ' ', 'h', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyt hon.']

krotka = tuple(liczby)  # tuple() - rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (54, 999, 666, 12.34, 687, 'A')
