import datetime
from buisness_logics.MasterLogic import MasterLogic


def add_ui(session):
    print('root/add > ', end='')
    input_command = input()
    while input_command != 'quit':
        match input_command:
            case 'help':
                print('- help')

                print('- master')
                print('- service_type')
                print('- component')
                print('- service')
                print('- storage')
                print('- application')

                print('- quit')
            case 'master':
                surname = input('Фамилия: ')
                name = input('Имя: ')
                patronymic = input('Отчество: ')
                year = int(input('Год рождения: '))
                month = int(input('Месяц рождения: '))
                day = int(input('День рождения: '))

                master_logic = MasterLogic(session)
                master_logic.add_master(name, surname, patronymic, datetime.datetime(year, month, day))
                pass
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/add > ', end='')
        input_command = input()
