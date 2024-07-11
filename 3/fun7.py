def all_params(a, b, /, c=42, d=256):
    print(f"{a=} {b=}")
    print(f"{c=} {d=}")


# minimum 2, a i b, bo nie maja wartości domyslnej
all_params(1, 2)
# a=1 b=2
# c=42 d=256
# Po dodaniu / w argumentach
# / oddziela argumenty, które muszą być przekazane po pozycji od argumentów które mogą byc po pozycji lub jako nazwane
all_params(1, 2, c=9)


# a=1 b=2
# c=9 d=256

# all_params(a=6, b=8)
# all_params(a=7, b=9, c=45)
# a=6 b=8
# c=42 d=256
# a=7 b=9
# c=45 d=256
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-9-07-2024\3\fun7.py", line 10, in <module>
#     all_params(a=6, b=8)
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'

def all_params_2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{kwargs=}")
    print(f"{args=}")
    print(f"{c=} {d=}")
    print(f"{a=} {b=}")


# ile minimum argumentow?
all_params_2(1, 2)
# czy c moze byc po nazwie?
all_params_2(1, 2, c=8)
all_params_2(1, 2, 8)
# czy a moze byc po nazwie?
all_params_2(1, 2, a=1)  # kwargs={'a': 1}
# gdzie trafi 4 argument
all_params_2(1, 2, 3, 4)  # args=(4,)
# jak przekazac do d
all_params_2(1, 2, 3, d=6)
all_params_2(1, 2, c=3, d=6)
# gdzie trafi d = 10
all_params_2(1, 2, d=10, a=8, b=9, name='Radek')
# kwargs={'a': 8, 'b': 9, 'name': 'Radek'}
# args=()
# c=42 d=10
# a=1 b=2
