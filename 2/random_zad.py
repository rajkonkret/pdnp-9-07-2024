import random

# generowanie liczb pseudolosowych

print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(6))  # int 0 do 5
print(random.random())  # 0.9823664990591615 float od 0 do 0.999999
print(random.random() * 10)  # 1.719426704063598 float od 0 do 9.999999

lista_osoby = ["Radek", "Tomek", "Zenek", "Ania", "Magda", "Ela"]
print(random.choice(lista_osoby))  # Radek

lista_kule = list(range(1, 50))  # range() - dostarcza liczby od 1 do 49
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)

print(random.choices(lista_kule, k=6))  # [49, 36, 40, 15, 45, 15] - losuje z powtórzeniami
print(random.sample(lista_kule, 6))  # losuje  bez powtórzeń
print(random.sample(lista_kule, k=6))  # losuje  bez powtórzeń
# [22, 20, 45, 9, 12, 31]
# [20, 41, 26, 34, 4, 39]
