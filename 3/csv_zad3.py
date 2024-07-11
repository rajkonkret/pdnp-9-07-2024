import pandas

# pip --proxy=wasze_proxy install pandas

data = pandas.read_csv('records_3.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  Radek    Coe     2   9.1
#     name branch  year   cgpa
# 0  Radek    Coe     2  19.10
# 1  Tomek    Cos     3   9.11
# 2  Zenek    Cot     5   9.00
# 3  Marek    Cog     7   7.10
# 4   Ania    Coy     1    NaN
print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'Coe' 2 19.1]
#  ['Tomek' 'Cos' 3 9.11]
#  ['Zenek' 'Cot' 5 9.0]
#  ['Marek' 'Cog' 7 7.1]
#  ['Ania' 'Coy' 1 nan]]
print(data.items)
# <bound method DataFrame.items of     name branch  year   cgpa
# 0  Radek    Coe     2  19.10
# 1  Tomek    Cos     3   9.11
# 2  Zenek    Cot     5   9.00
# 3  Marek    Cog     7   7.10
# 4   Ania    Coy     1    NaN>
