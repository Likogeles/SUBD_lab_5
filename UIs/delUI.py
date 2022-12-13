import datetime

from buisness_logics.ComponentLogic import ComponentLogic
from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceLogic import ServiceLogic
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
            case 'service_type':
                ind = input('Индекс: ')
                service_type_logic = ServiceTypeLogic(session)
                service_type_logic.remove(ind)
                print("База данных успешно обновлена")
            case 'component':
                ind = input('Индекс: ')
                component_logic = ComponentLogic(session)
                component_logic.remove(ind)
                print("База данных успешно обновлена")
            case 'service':
                ind = input('Индекс: ')
                service_logic = ServiceLogic(session)
                service_logic.remove(ind)
                print("База данных успешно обновлена")
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/del > ', end='')
        input_command = input()
