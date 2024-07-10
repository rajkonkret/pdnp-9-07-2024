# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# w zależnosci od warunku wykonuje jedną lub drugą operacje
# warunek zwraca typ bool
# if
odp = True
print(bool(odp))  # True

if odp:  # warunek musi być True
    # blok do wykonania po if
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"  # bo str niepusty daje True
if odp:
    print("Radek")

if odp == "Radek":
    print("Nadal Radek")  # Nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym wypadku
    print("To nie jest Tomek")

# podatek = 0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# dodac przedział od 10000 do 29999 podatek 0.2
# kolejność ma znaczenie
# pierwszy spełniony warunek wyjscie z całości

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # ternary operator
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienne beda przechowywac dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla console: "Stało się coś strasznego"
# dla email: "System email"
# gdy system email
# poziomy ważnosći: error, medium, inny
# zapisac opis tych błedów w liscie

lista_b = []
alert_system = 'console'
error = 'medium'

if alert_system == 'console':  # == dwa znaki równe, porównanie
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == 'medium':
        lista_b.append("Ostrzeżenie")
    elif error == 'error':
        lista_b.append("Bład krytyczny")
    else:
        print("Błąd typu wielbład;)")
else:
    print("Nie znam tego systemu")

name_len = len("Radek")
if name_len > 3:
    print("Długość prawidłowa")

# walrus operator - operator morsa, przypisanie i porównanie
a = "Radek"
if (n := len(a)) > 3:
    print("Długość prawidłowa", n)  # Długość prawidłowa 5
print("Długość prawidłowa" if (n := len(a)) > 3 else None)  # Długość prawidłowa

# napisac tez z...
# pytanie
# pobrać odpowiedź
# wyswietlić wynik cy odp prawidłowa
odp = input("Podaj datę Chrztu Polski")  # input zwraca str
if odp == '966':
    print("Odpowiedż prawidłowa")
else:
    print("Masz w książce na stronie 18")
