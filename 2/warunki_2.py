# match case
# od Pythona 3.10

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam jave")
    case _:  # wartość domyślna, czyli taki else
        print("Nie znam takiego języka programowania")

print(lista)
