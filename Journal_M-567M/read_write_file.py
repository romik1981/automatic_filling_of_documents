# from Test import result_10_min
from data_jornal import last_device_input_dek, date_now

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
            # print(str_, type(str_), 'чтение DEK')
            str = str_.strip().split(";")
            # print(str, 'чтение DEK после разделения')
            for _ in str:
                _ = _.encode('utf-8')
            # print(str, type(str), 'промежуточные данные декодирования')
            list_out_dek.append(str)
            # for i, _ in enumerate(a):
            #     if _ == 'data':
            #         a[i] = data
            # a.append('\n')
            # list_out.append(';'.join(a))
        # print(list_out_dek)
    return list_out_dek
    # with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
    #     for _ in list_out:
    #         fw.writelines(_)
    # return print(f'Данные записаны в файл jornal_out_{type_f}.csv')

def write_file_dek(list_data_in, date, type_f=None):

    list_out_new = []
    for row in list_data_in:
        for i, cell in enumerate(row):
            if cell == 'date':
                row[i] = date
        row.append('\n')
        # print(row)

        list_out_new.append(';'.join(row))
    with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1251') as fw:

        for _ in list_out_new:
            fw.writelines(_)
    return print(f'Данные записаны в файл jornal_out_{type_f}.csv')



if __name__ == '__main__':

    # write_file_password(result_10_min, 'rdt')
    read_file_dek()

    # print(list_out_dek[1][2])
    # last_device_input_dek.index(1, 2, last_device_input_dek)
    # list_out_dek[1][2] = last_device_input_dek
    # print(list_out_dek[1][2])
    # print(list_out_dek)

    # Разобрался можно спать, УРА!!!
    # Собираем журнал DEK
    # print(list_out_dek)
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 1 and j == 2:
                list_out_dek[i][j] = last_device_input_dek
            elif i == 1 and j == 8:
                list_out_dek[i][j] = date_now
            elif i == 5 and j == 8:
                list_out_dek[i][j] = date_now
            elif i == 0:
                pass
            elif i != 0 and j != 0:
                list_out_dek[i][j] = ''

    print(list_out_dek)
    write_file_dek(list_out_dek, date_now, 'dek')
