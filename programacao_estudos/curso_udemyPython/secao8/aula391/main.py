import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
# cursor.execute(
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(id, name, weight) '
#     '(name, weight) '
#     'VALUES '
#     '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'
#     '(?, ?)'
# )
# )
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    '(name, weight) '
    'VALUES '
    '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'
    '(?, ?)'
)
cursor.execute(sql, ['Joana', 4])
connection.commit()
print(sql)

cursor.close()
connection.close()