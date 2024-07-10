# wyjątki
# błedy podczas działąnia programu
# print(5 / 0)  # ZeroDivisionError: division by zero
# print("Program nadal działa")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-9-07-2024\2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

number = 90
try:
    # print(number / 0)
    # print(5 / "00")
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Nie ma takiego klucza w słowniku")
    wynik = number / 3
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Błąd", e)
else:  # wykona się tylko gdy nie ma błedu
    print(f"Wynik działania: {wynik}")
finally:  # wykona się zawsze
    print("Biorę kolejny element do obliczeń")
print("Program działa nadal")

# try except [else - finally]
