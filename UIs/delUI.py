import datetime
from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceTypeLogic import ServiceTypeLogic


def del_ui(session):
    print('root/del > ', end='')
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
                ind = input('Индекс: ')
                master_logic = MasterLogic(session)
                master_logic.remove(ind)
                print("База данных успешно обновлена")

                pass
            case 'service_type':
                ind = input('Индекс: ')
                service_type_logic = ServiceTypeLogic(session)
                service_type_logic.remove(ind)
                print("База данных успешно обновлена")

                pass
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/del > ', end='')
        input_command = input()
