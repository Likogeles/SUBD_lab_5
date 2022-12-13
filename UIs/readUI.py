from buisness_logics.MasterLogic import MasterLogic
from buisness_logics.ServiceTypeLogic import ServiceTypeLogic


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
                pass
            case 'masters':
                master_logic = MasterLogic(session)
                masters = master_logic.get_all()
                if masters:
                    for master in masters:
                        print(f'{master.master_id}\t{master.master_surname} {master.master_name} {master.master_patronymic} {master.master_date_of_birth}')
                else:
                    print("Записи отсутсвуют")
                pass
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
                pass
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
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/read > ', end='')
        input_command = input()
