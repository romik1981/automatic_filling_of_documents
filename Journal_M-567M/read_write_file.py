# from Test import result_10_min
from data_jornal import last_device_input_dek

# Глобальные переменные файла
list_out_dek = []



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


def read_file_dek():
    ''' Функция записи данных в файл журнала DEK'''

    n = 1

    with open('jornal_M567M(dek).csv', 'r', encoding='cp1251') as fr:
        for str_ in fr:
            str = str_.strip().split(";")
            for _ in  str:
                _ = _.encode('utf-8')
            print(str, type(str), 'промежуточные данные')
            list_out_dek.append(str)
            # for i, _ in enumerate(a):
            #     if _ == 'data':
            #         a[i] = data
            # a.append('\n')
            # list_out.append(';'.join(a))
        print(list_out_dek)
    return list_out_dek
    # with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
    #     for _ in list_out:
    #         fw.writelines(_)
    # return print(f'Данные записаны в файл jornal_out_{type_f}.csv')

def write_file_dek(list_out_dek, type_f=None):

    with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1251') as fw:
        for _ in list_out_dek:
            fw.writelines(_)
    return print(f'Данные записаны в файл jornal_out_{type_f}.csv')



if __name__ == '__main__':

    # write_file_password(result_10_min, 'rdt')
    read_file_dek()

    print(list_out_dek[1][2])
    # last_device_input_dek.index(1, 2, last_device_input_dek)
    list_out_dek[1][2] = last_device_input_dek
    print(list_out_dek[1][2])
    print(list_out_dek)

    write_file_dek(list_out_dek, 'dek')
