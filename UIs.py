def add_ui():
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

                pass
            case 'quit':
                pass
            case _:
                print(f"Команда {input_command} не распознана")

        print('root/add > ', end='')
        input_command = input()