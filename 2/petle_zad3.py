# while - sterowana warunkiem

licznik = 0
while True:
    print("Komunikat!!!")
    licznik += 1  # licznik = licznik + 1
    if licznik > 10:
        break  # wyjscie z pętli

print(licznik)
licznik = 0

while licznik < 10:
    licznik += 1
    print("Komunikat 2 !! !! !!")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło. Podaj ponownie")
#
# print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str()
    if not wej.isnumeric():  # A string is numeric if all characters in the string are numeric
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['5', '6', '7', '1', '2', '34']
# [5, 6, 7, 1, 2, 34]
