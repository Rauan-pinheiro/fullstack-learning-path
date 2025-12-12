import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    '(name, weight) '
    'VALUES '
    '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'
    '(?, ?)'
)

# cursor.execute(sql, ['Joana', 4])
cursor.executemany(
    sql,
    (
        ('Joana', 4), ('Luiz', 5)
    )
)
connection.commit()
print(sql)

cursor.close()
connection.close()