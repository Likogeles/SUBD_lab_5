import datetime

from buisness_logics.ComponentLogic import ComponentLogic
from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceLogic import ServiceLogic
from buisness_logics.ServiceTypeLogic import ServiceTypeLogic
from buisness_logics.StorageLogic import StorageLogic


def edit_ui(session):
    print('root/edit > ', end='')
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
                master = master_logic.get(ind)
                if master:
                    print(master.master_id, master.master_surname, master.master_name, master.master_patronymic, master.master_date_of_birth)
                    surname = input('Фамилия: ')
                    name = input('Имя: ')
                    patronymic = input('Отчество: ')
                    year = int(input('Год рождения: '))
                    month = int(input('Месяц рождения: '))
                    day = int(input('День рождения: '))

                    master_logic = MasterLogic(session)
                    master_logic.edit(ind, name, surname, patronymic, datetime.datetime(year, month, day))
                    print("База данных успешно обновлена")
                else:
                    print("Запись не найдена")
            case 'service_type':
                ind = input('Индекс: ')
                service_type_logic = ServiceTypeLogic(session)
                service_type = service_type_logic.get(ind)
                if service_type:
                    master_logic = MasterLogic(session)
                    master = master_logic.get(service_type.service_director_id)
                    if master:
                        print(service_type.service_type_id, service_type.service_type_name, master.master_surname,
                              master.master_name, service_type.service_director_premium)
                        service_type_name = input('Название сервиса: ')
                        service_director_surname = input('Фамилия директора: ')
                        service_director_name = input('Имя директора: ')

                        master_logic = MasterLogic(session)
                        master = master_logic.find(service_director_surname, service_director_name)

                        if master is None:
                            print("Мастер не найден")
                        else:
                            service_director_premium = int(input('Премия директора: '))
                            service_type_logic = ServiceTypeLogic(session)
                            service_type_logic.edit(ind, service_type_name, master.master_id, service_director_premium)
                            print("База данных успешно обновлена")
                    else:
                        print("Ошибка чтения")
                else:
                    print("Запись не найдена")
            case 'component':
                ind = input('Индекс: ')
                component_logic = ComponentLogic(session)
                component = component_logic.get(ind)
                if component:
                    print(component.component_id, component.component_name, component.number_in_storage, component.component_cost, component.component_purveyor)
                    name = input('Название: ')
                    number_in_storage = int(input('Кол-во на складе: '))
                    component_cost = int(input('Цена: '))
                    component_purveyor = input('Производитель: ')

                    component_logic.edit(ind, name, number_in_storage, component_cost, component_purveyor)
                    print("База данных успешно обновлена")
                else:
                    print("Запись не найдена")
            case 'service':
                ind = input('Индекс: ')
                service_logic = ServiceLogic(session)
                service = service_logic.get(ind)
                if service:
                    component_logic = ComponentLogic(session)
                    component = component_logic.get(service.component_id)
                    service_type_logic = ServiceTypeLogic(session)
                    service_type = service_type_logic.get(service.service_type_id)
                    if component and service_type:
                        print(service.service_id, service.service_name, component.component_name,
                              service_type.service_type_name, service.service_cost)

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
                            service_logic.edit(ind, service_name, component.component_id, service_type.service_type_id, service_cost)
                            print("База данных успешно обновлена")
                    else:
                        print("Ошибка чтения")
                else:
                    print("Запись не найдена")
            case 'storage':
                ind = input('Индекс: ')
                storage_logic = StorageLogic(session)
                storage = storage_logic.get(ind)
                if storage:
                    print(storage.storage_id, storage.number_of_plates, storage.number_of_free_plates,
                          storage.storage_address)
                    number_of_plates = int(input('Общее количество мест: '))
                    number_of_free_plates = int(input('Количество свободных мест: '))
                    storage_address = input('Адрес: ')

                    storage_logic.edit(ind, number_of_plates, number_of_free_plates, storage_address)
                    print("База данных успешно обновлена")
                else:
                    print("Запись не найдена")
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/edit > ', end='')
        input_command = input()
