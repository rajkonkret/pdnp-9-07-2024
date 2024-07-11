from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-07-10

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-07-10 15:30:14.534145
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-07-11

print(time.time())
print(time.today())
# 15:35:55.532709
# 2024-07-10 15:35:55.532709

formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data", formatted_date)  # Sformatowana data 10/07/2024

formatted_time = datetime.now().strftime('%H:%M')
print("Sformatowany czas", formatted_time)  # Sformatowany czas 15:38

# zamiana daty na obiekt typu datatime
data_object = datetime.strptime("10/07/2024", '%d/%m/%Y')
print(data_object)  # 2024-07-10 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

