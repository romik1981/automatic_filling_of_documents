from Test import result_10_min




def write_file_password(data, type_f=None):
    ''' Функция записи паролей в файл'''

    # if type_f == None:
    #     with open('password.xml', 'a+', encoding='utf-8') as fa:
    #         fa.writelines(f'{password}\n')  # Записывает в файл сгенерированный пароль.
    #     return print(f'Пароли сгенерированны в файл password.xml')

    # if type_f == 'sed':
    list_out = []
    with open('jornal_M567M(rdt).csv', 'r', encoding='cp1252') as fr:
        for str_ in fr:
            a = str_.strip().split(";")
            print(a)
            for i, _ in enumerate(a):
                if _ == 'data':
                    a[i] = data
            a.append('\n')
            list_out.append(';'.join(a))
    with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
        for _ in list_out:
            fw.writelines(_)
    return print(f'Данные записаны в файл jornal_out_{type_f}.csv')

write_file_password(result_10_min, 'rdt')
