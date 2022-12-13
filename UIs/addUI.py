import datetime

from buisness_logics.ComponentLogic import ComponentLogic
from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceLogic import ServiceLogic
from buisness_logics.ServiceTypeLogic import ServiceTypeLogic
from buisness_logics.StorageLogic import StorageLogic


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
                master_logic.add(name, surname, patronymic, datetime.datetime(year, month, day))
                print("База данных успешно обновлена")
            case 'service_type':
                service_type_name = input('Название типа услуги: ')
                service_director_surname = input('Фамилия директора: ')
                service_director_name = input('Имя директора: ')

                master_logic = MasterLogic(session)
                master = master_logic.find(service_director_surname, service_director_name)

                if master is None:
                    print("Мастер не найден")
                else:
                    service_director_premium = int(input('Премия директора: '))
                    service_type_logic = ServiceTypeLogic(session)
                    service_type_logic.add(service_type_name, master.master_id, service_director_premium)
                    print("База данных успешно обновлена")
            case 'component':
                name = input('Название: ')
                number_in_storage = int(input('Кол-во на складе: '))
                component_cost = int(input('Цена: '))
                component_purveyor = input('Производитель: ')

                component_logic = ComponentLogic(session)
                component_logic.add(name, number_in_storage, component_cost, component_purveyor)
                print("База данных успешно обновлена")
            case 'service':
                service_name = input('Название услуги: ')
                service_cost = int(input('Цена услуги: '))
                component_name = input('Название компонента: ')
                service_type_name = input('Тип услуги: ')

                component_logic = ComponentLogic(session)
                component = component_logic.find(component_name)

                service_type_logic = ServiceTypeLogic(session)
                service_type = service_type_logic.find(service_type_name)

                if component is None or service_type is None:
                    print("Компонент или тип услуги не найдены")
                else:
                    service_logic = ServiceLogic(session)
                    service_logic.add(service_name, component.component_id, service_type.service_type_id, service_cost)
                    print("База данных успешно обновлена")
            case 'storage':
                number_of_plates = int(input('Общее количество мест: '))
                number_of_free_plates = int(input('Количество свободных мест: '))
                storage_address = input('Адрес: ')
                storage_logic = StorageLogic(session)
                storage_logic.add(number_of_plates, number_of_free_plates, storage_address)
                print("База данных успешно обновлена")
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/add > ', end='')
        input_command = input()
