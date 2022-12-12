from buisness_logics.MasterLogic import MasterLogic


def read_ui(session):
    print('root/read > ', end='')
    input_command = input()
    while input_command != 'quit':
        match input_command:
            case 'help':
                print('- help')

                print('- get_master')
                print('- masters')
                print('- service_type')
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
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/read > ', end='')
        input_command = input()