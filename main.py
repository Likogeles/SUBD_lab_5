import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from UIs.addUI import add_ui
from UIs.delUI import del_ui
from UIs.readUI import read_ui
from UIs.editUI import edit_ui

from config import host, port, db_name, user, password

engine = db.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

print('Начало работы в ', end='')
for i in session.execute("SELECT version();"):
    print(i, end='')

print('\nroot > ', end='')
input_command = input()
while input_command != 'quit':
    match input_command:
        case 'help':
              print('- help')
              print('- add')
              print('- read')
              print('- edit')
              print('- del')
              print('- quit')
        case 'add':
            add_ui(session)
        case 'read':
            read_ui(session)
        case 'edit':
            edit_ui(session)
        case 'del':
            del_ui(session)
        case 'quit':
            pass
        case _:
            print(f"Команда {input_command} не распознана")

    print('root > ', end='')
    input_command = input()

session.close()
print('Завершено успешно')
