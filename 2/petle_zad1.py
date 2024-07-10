# petle - możliwosć wykonania wielokrotnie tego samego kodu
# for - petla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ niema zmienna
    print("Test podłogi")
    # print(_)
# Test podłogi
# Test podłogi
# Test podłogi
# Test podłogi
# Test podłogi

for i in range(20):
    print(i * 2, end=" ")
    # 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
print()
print("Radek", "Tadek", "Marek")  # Radek Tadek Marek
print("Radek", "Tadek", "Marek", sep=",")  # Radek,Tadek,Marek

# przerobic lotto na pętle
lista_kule = list(range(1, 50))
lista_wylosowane = []

for i in range(6):  # od 0 do 5, czyli 6 razy
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [16, 11, 26, 34, 8, 48]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:  # dla wszystkich elementów z kolekcji wykona pętlę
    if c > 10:
        print("Wieksze od 10", c)
# Wieksze od 10 30
# Wieksze od 10 34
# Wieksze od 10 31
# Wieksze od 10 37
# Wieksze od 10 48

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # odliczanie w dół
    print(i)

for i in range(-10, 0):
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)
# 0
# 3  nastapiło dodanie 1, c = c + 1 c += 1
# 4
# 6
# 8
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', 'Zenek', 'Ania']
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wyswietlic z indeksem czyli 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) od 0 do 3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca element kolekcji i jego pozycje(numer)
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Arek', 'Tomek', 'Zenek']
wiek = [44, 55, 66, 23]

# Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23

ludzie = ['Radek', 'Arek', 'Tomek', 'Zenek', "Ania"]
wiek = [44, 55, 66, 23]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # IndexError: list index out of range

# zip() - łączy kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Arek', 55)
# ('Tomek', 66)
# ('Zenek', 23)
for i, w in zip(ludzie, wiek):
    print(i, w)
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Arek', 55))
# (2, ('Tomek', 66))
# (3, ('Zenek', 23))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = b
print(c, d)  # Radek 44
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
a, (c, d) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44

# ['Radek', 'Arek', 'Tomek', 'Zenek', "Ania"]
for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)
# 0 Radek 44
# 1 Arek 55
# 2 Tomek 66
# 3 Zenek 23
