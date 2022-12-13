from buisness_logics.ComponentLogic import ComponentLogic
from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceLogic import ServiceLogic
from buisness_logics.ServiceTypeLogic import ServiceTypeLogic
from buisness_logics.StorageLogic import StorageLogic


def read_ui(session):
    print('root/read > ', end='')
    input_command = input()
    while input_command != 'quit':
        match input_command:
            case 'help':
                print('- help')

                print('- get_master')
                print('- masters')
                print('- get_service_type')
                print('- service_types')
                print('- component')
                print('- service')
                print('- storage')
                print('- application')

                print('- quit')
            case 'get_master':
                ind = input('Индекс: ')
                master_logic = MasterLogic(session)
                master = master_logic.get(ind)
                if master:
                    print(master.master_id, master.master_surname, master.master_name, master.master_patronymic, master.master_date_of_birth)
                else:
                    print("Запись не найдена")
            case 'masters':
                master_logic = MasterLogic(session)
                masters = master_logic.get_all()
                if masters:
                    for master in masters:
                        print(f'{master.master_id}\t{master.master_surname} {master.master_name} {master.master_patronymic} {master.master_date_of_birth}')
                else:
                    print("Записи отсутсвуют")
            case 'get_service_type':
                ind = input('Индекс: ')
                service_type_logic = ServiceTypeLogic(session)
                service_type = service_type_logic.get(ind)
                if service_type:
                    master_logic = MasterLogic(session)
                    master = master_logic.get(service_type.service_director_id)
                    if master:
                        print(service_type.service_type_id, service_type.service_type_name, master.master_surname, master.master_name, service_type.service_director_premium)
                    else:
                        print("Ошибка чтения")
                else:
                    print("Запись не найдена")
            case 'service_types':
                service_type = ServiceTypeLogic(session)
                service_types = service_type.get_all()
                if service_types:
                    for service_type in service_types:
                        master_logic = MasterLogic(session)
                        master = master_logic.get(service_type.service_director_id)
                        if master:
                            print(f"""{service_type.service_type_id}\t{service_type.service_type_name} - {master.master_surname} {master.master_name} - {service_type.service_director_premium}""")
                        else:
                            print("Ошибка чтения")
                else:
                    print("Записи отсутсвуют")
            case 'get_component':
                ind = input('Индекс: ')
                component_logic = ComponentLogic(session)
                component = component_logic.get(ind)
                if component:
                    print(component.component_id, component.component_name, component.number_in_storage, component.component_cost, component.component_purveyor)
                else:
                    print("Запись не найдена")
            case 'components':
                component_logic = ComponentLogic(session)
                components = component_logic.get_all()
                if components:
                    for component in components:
                        print(f'{component.component_id}\t{component.component_name} {component.number_in_storage} {component.component_cost} {component.component_purveyor}')
                else:
                    print("Записи отсутсвуют")
            case 'get_service':
                ind = input('Индекс: ')
                service_logic = ServiceLogic(session)
                service = service_logic.get(ind)
                if service:
                    component_logic = ComponentLogic(session)
                    component = component_logic.get(service.component_id)
                    service_type_logic = ServiceTypeLogic(session)
                    service_type = service_type_logic.get(service.service_type_id)
                    print(service.service_id, service.service_name, component.component_name, service_type.service_type_name, service.service_cost)
                else:
                    print("Запись не найдена")
            case 'services':
                service_logic = ServiceLogic(session)
                services = service_logic.get_all()
                if services:
                    for service in services:
                        component_logic = ComponentLogic(session)
                        component = component_logic.get(service.component_id)
                        service_type_logic = ServiceTypeLogic(session)
                        service_type = service_type_logic.get(service.service_type_id)
                        print(f"{service.service_id}\t{service.service_name} - {component.component_name} - {service_type.service_type_name} - {service.service_cost}")
                else:
                    print("Записи отсутсвуют")
            case 'get_storage':
                ind = input('Индекс: ')
                storage_logic = StorageLogic(session)
                storage = storage_logic.get(ind)
                if storage:
                    print(storage.storage_id, storage.number_of_plates, storage.number_of_free_plates, storage.storage_address)
                else:
                    print("Запись не найдена")
            case 'storages':
                storage_logic = StorageLogic(session)
                storages = storage_logic.get_all()
                if storages:
                    for storage in storages:
                        print(f'{storage.storage_id}\t{storage.number_of_plates} - {storage.number_of_free_plates} - {storage.storage_address}')
                else:
                    print("Записи отсутсвуют")
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/read > ', end='')
        input_command = input()
