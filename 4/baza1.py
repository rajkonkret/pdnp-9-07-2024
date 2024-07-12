import sqlite3

# baza sql

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych zostałą podłączona")

    query = '''
    CREATE TABLE IF NOT EXISTS hardware (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL);
    '''

    # c.execute(query)
    # conn.commit()
    insert = """
    INSERT INTO hardware (id,name,price) VALUES (1,'Apple', 6999);
    """

    # c.execute(insert)
    # conn.commit()

    update = """
    UPDATE hardware SET price=8999 WHERE id=1;
    """

    c.execute(update)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd podłąćzania do bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
