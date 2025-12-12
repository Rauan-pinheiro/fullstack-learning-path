# import sqlite3
# from pathlib import Path

# ROOT_DIR = Path(__file__).parent
# DB_NAME = 'db.sqlite3'
# DB_FILE = ROOT_DIR / DB_NAME
# TABLE_NAME = 'customers'

# connection = sqlite3.connect(DB_FILE)
# cursor = connection.cursor()

# # CRUD - Create Read   Update Delete
# # SQL -  INSERT SELECT UPDATE DELETE

# # CUIDADO: fazendo delete sem where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# # DELETE mais cuidadoso
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
#     {'nome': 'Joana', 'peso': 5}
# )
# connection.commit()

# cursor.close()
# connection.close()