# funkcja zagnieżdzona, wewnetrzna
# wykorzystują zasadę funkcji wewnętrznej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funkcjii!!!, bez nawiasów


fun1()
xFun = fun1()  #
print(xFun)  # <function fun1.<locals>.fun2 at 0x000002F60DC28C20>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
