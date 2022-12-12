import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from UIs import add_ui
from config import host, port, db_name, user, password
from models.models import Master, ServiceType, Component, Service, Storage, Application

engine = db.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

print('Начало работы')
print('root > ', end='')
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
            add_ui()
        case 'quit':
            pass
        case _:
            print(f"Команда {input_command} не распознана")

    print('root > ', end='')
    input_command = input()

session.close()
print('Завершено успешно')

# service_types = session.query(Application)
# for service_type in service_types:
#     print(service_type.application_id, service_type.application_date, service_type.service.service_name, service_type.master.master_name, service_type.storage.storage_address)

