# funkcja obliczająca średnią
def liczby(name=None, *cyfry):  # * worek na dane, dowolna ilosc argumentów pozycyjnych
    print(cyfry)  # (1,) jako tupla
    suma = 0
    count = len(cyfry)  # liczba cyfr
    suma_p = sum(cyfry)  # 21
    print(suma_p)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Kolejny uczeń")


liczby("Adam", 1)
liczby("Zenek", 1, 2, 3)
liczby("Ela", 1, 2, 3, 4, 5, 6)
liczby()  # ()

# ('Adam', 1)
name, *cyfry = ('Adam', 1)
print(name, cyfry)  # Adam [1]
