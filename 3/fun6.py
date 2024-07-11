def connect(**opcje):  # ** argumnety nazwane -> słownikowe
    print(opcje)  # {'a': 1, 'b': 2, 'c': 3}


connect(a=1, b=2, c=3)  # argumenty nazwane


# connect(1,2,c=9)  # TypeError: connect() takes 0 positional arguments but 2 were given

def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()
all_args(1)
all_args(11, 2, 3)
all_args(11, 2, 3, a=9)
all_args(a=0)  # klucz=wartosc
# () {}
# (1,) {}
# (11, 2, 3) {}
# (11, 2, 3) {'a': 9}
# () {'a': 0}
# all_args(a=0, 1, 2, 3)  # SyntaxError: positional argument follows keyword argument
