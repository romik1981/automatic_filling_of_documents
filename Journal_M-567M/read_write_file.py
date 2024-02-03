# from Test import result_10_min

# импорт номеров аппаратов
from data_jornal import last_device_input_dek, number_device

# импорт ноиеров и серий ключей
from data_jornal import number_tape_ckt_old, ser_number_ckt_old
# импорт печатей
from data_jornal import stamp_numer_common, stamp_numer_one_r, stamp_numer_two_r, stamp_numer_one_r_ckt_old
# импорт переменных даты и времени
from data_jornal import date_now, time_now, date_time_ckt, date_ckt, time_ckt, extract_date_time_ckt, input_date_time_ckt,\
    seal_date_time_ckt, del_date_time

import pprint
import datetime

# Глобальные переменные файла
list_out_dek = []
list_out_rdt = []
list_out_ckt = []



# def write_file_password(data, type_f=None):
#     ''' Функция записи паролей в файл'''
#
#     # if type_f == None:
#     #     with open('password.xml', 'a+', encoding='utf-8') as fa:
#     #         fa.writelines(f'{password}\n')  # Записывает в файл сгенерированный пароль.
#     #     return print(f'Пароли сгенерированны в файл password.xml')
#
#     # if type_f == 'sed':
#     list_out = []
#     with open('jornal_M567M(rdt).csv', 'r', encoding='cp1252') as fr:
#         for str_ in fr:
#             a = str_.strip().split(";")
#             print(a)
#             for i, _ in enumerate(a):
#                 if _ == 'data':
#                     a[i] = data
#             a.append('\n')
#             list_out.append(';'.join(a))
#     with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
#         for _ in list_out:
#             fw.writelines(_)
#     return print(f'Данные записаны в файл jornal_out_{type_f}.csv')


def read_file_jornal(type_f=''):
    ''' Функция записи данных в файл журнала DEK '''

    if type_f == 'dek':
        list_out_dek = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                # print(str_, type(str_), 'чтение DEK')
                str = str_.strip().split(";")
                # print(str, 'чтение DEK после разделения')
                for _ in str:
                    _ = _.encode('utf-8')
                # print(str, type(str), 'промежуточные данные декодирования')
                list_out_dek.append(str)
            # print(list_out_dek)
        return list_out_dek

    if type_f == 'rdt':
        list_out_rdt = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:

                str = str_.strip().split(";")

                for _ in str:
                    _ = _.encode('utf-8')
                list_out_rdt.append(str)

        return list_out_rdt

    if type_f == 'ckt':
        list_out_ckt = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:

                str = str_.strip().split(";")

                for _ in str:
                    _ = _.encode('utf-8')
                list_out_ckt.append(str)

        return list_out_ckt

    if type_f == '':
        print('Не указан тип файла жрнала!')

# def read_file_rdt():
#     ''' Функция записи данных в файл журнала RDT '''
#
#     list_out_rdt = []
#
#     with open('jornal_M567M(rdt).csv', 'r', encoding='cp1251') as fr:
#         for str_ in fr:
#             # print(str_, type(str_), 'чтение DEK')
#             str = str_.strip().split(";")
#             # print(str, 'чтение DEK после разделения')
#             for _ in str:
#                 _ = _.encode('utf-8')
#             # print(str, type(str), 'промежуточные данные декодирования')
#             list_out_rdt.append(str)
#             # for i, _ in enumerate(a):
#             #     if _ == 'data':
#             #         a[i] = data
#             # a.append('\n')
#             # list_out.append(';'.join(a))
#         # pprint.pprint(list_out_rdt, depth=12, width=144)
#     return list_out_rdt
#     # with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
#     #     for _ in list_out:
#     #         fw.writelines(_)
#     # return print(f'Данные записаны в файл jornal_out_{type_f}.csv')

def write_file_dek(list_data_in, type_f=None):

    list_out_new = []
    for row in list_data_in:
        # for i, cell in enumerate(row):
        #     if cell == 'date':
        #         row[i] = date
        row.append('\n')
        # print(row)

        list_out_new.append(';'.join(row))
    with open(f'jornal_out_{type_f}.csv', 'a+', encoding='cp1251') as fw:

        for _ in list_out_new:
            fw.writelines(_)
    return print(f'Данные записаны в файл jornal_out_{type_f}.csv')

# Функции для формирования журнала DEK
def create_write_dek_1(list_out_dek):
    # Цикл для формирования записи вскрытия в последний раз опечатанного DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 1 and j == 2:
                list_out_dek[i][j] = last_device_input_dek
            elif i == 1 and j == 8:
                list_out_dek[i][j] = date_now
            elif i == 2 and j == 8:
                list_out_dek[i][j] = time_now
            elif i == 3 and j == 8:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 8:
                list_out_dek[i][j] = date_now
            elif i == 6 and j == 8:
                list_out_dek[i][j] = time_now
            elif i == 7 and j == 8:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i == 0:
                pass
            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]:
                list_out_dek[i][j] = str(i) + ',' + str(j) # ''
            # elif i != 0 and j != 0:
            #     list_out_dek[i][j] = str(i) + ',' + str(j) # ''
            # elif i != 4 and j != 8:
            #     list_out_dek[i][j] = str(i) + ',' + str(j) # ''
            # elif i != 8 and j != 8:
            #     list_out_dek[i][j] = str(i) + ',' + str(j) # ''
    return list_out_dek

def create_write_dek_2(list_out_dek):
    # Цикл для формирования записи стирания старого DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 1 and j == 2:
                list_out_dek[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_dek[i][j] = date_now
            elif i == 2 and j == 3:
                list_out_dek[i][j] = time_now
            elif i == 3 and j == 3:
                list_out_dek[i][j] = stamp_numer_common
            elif i == 5 and j == 6:
                list_out_dek[i][j] = date_now
            elif i == 6 and j == 6:
                list_out_dek[i][j] = time_now
            elif i == 7 and j == 6:
                list_out_dek[i][j] = stamp_numer_common
            elif i == 2 and j == 10:
                list_out_dek[i][j] = date_now
            elif i == 3 and j == 10:
                list_out_dek[i][j] = time_now
            elif i == 6 and j == 10:
                list_out_dek[i][j] = date_now
            elif i == 7 and j == 10:
                list_out_dek[i][j] = time_now
            elif i == 1 and j == 11:
                list_out_dek[i][j] = date_now
            elif i == 2 and j == 11:
                list_out_dek[i][j] = time_now
            elif i == 3 and j == 11:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 11:
                list_out_dek[i][j] = date_now
            elif i == 6 and j == 11:
                list_out_dek[i][j] = time_now
            elif i == 7 and j == 11:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i == 0:
                pass
            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 4, 5, 6, 7, 8, 9]:
                list_out_dek[i][j] = str(i) + ',' + str(j) # ''

    del list_out_dek[0]

    return list_out_dek

# Функции для формирования журнала RDT
def create_write_rdt_1(list_out_rdt):
    # Цикл для формирования записи вскрытия в последний раз опечатанного RDT
    for i, row in enumerate(list_out_rdt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 1 and j == 2:
                list_out_rdt[i][j] = number_device
            elif i == 2 and j == 9:
                list_out_rdt[i][j] = date_now
            elif i == 3 and j == 9:
                list_out_rdt[i][j] = time_now

            elif i == 6 and j == 9:
                list_out_rdt[i][j] = date_now
            elif i == 7 and j == 9:
                list_out_rdt[i][j] = time_now

            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]:
                list_out_rdt[i][j] = str(i) + ',' + str(j) # ''

    return list_out_rdt

# Функции для формирования журнала RDT
def create_write_ckt_old(list_out_ckt):
    # Цикл для формирования записи вскрытия в последний раз опечатанного RDT
    for i, row in enumerate(list_out_ckt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_ckt[i][j] = f'№ {ser_number_ckt_old}, э.ед.'

            elif i == 1 and j == 1:
                list_out_ckt[i][j] = date_ckt
            elif i == 2 and j == 1:
                list_out_ckt[i][j] = time_now
            elif i == 1 and j == 2 or i == 2 and j == 3 or i == 2 and j == 6:
                list_out_ckt[i][j] = number_tape_ckt_old

            elif i == 3 and j == 1:
                list_out_ckt[i][j] = stamp_numer_one_r_ckt_old
            elif i == 2 and j == 2:
                list_out_ckt[i][j] = extract_date_time_ckt

            elif i == 1 and j == 3:
                list_out_ckt[i][j] = number_device
            elif i == 3 and j == 3:
                list_out_ckt[i][j] = input_date_time_ckt

            elif i == 2 and j == 4:
                list_out_ckt[i][j] = input_date_time_ckt

            elif i == 1 and j == 5:
                list_out_ckt[i][j] = stamp_numer_one_r
            elif i == 2 and j == 5:
                list_out_ckt[i][j] = seal_date_time_ckt

            elif i == 1 and j == 6:
                list_out_ckt[i][j] = del_date_time

            elif i in [4] and j in [2, 4, 5, 6, 7]:
                list_out_ckt[i][j] = str(i) + ',' + str(j) # ''

    return list_out_ckt


if __name__ == '__main__':

    # write_file_password(result_10_min, 'rdt')

    # print(list_out_dek[1][2])
    # last_device_input_dek.index(1, 2, last_device_input_dek)
    # list_out_dek[1][2] = last_device_input_dek
    # print(list_out_dek[1][2])

    # Разобрался можно спать, УРА!!!

    # Собираем журнал DEK
    # print(list_out_dek)

    # print(list_out_dek)
    # write_file_dek(list_out_dek, date_now, 'dek')

    # read_file_dek()

    # list_out_dek = create_write_dek_1(read_file_dek())
    # write_file_dek(list_out_dek, 'dek')
    # list_out_dek = create_write_dek_2(read_file_dek())
    #
    # pprint.pprint(list_out_dek, depth=12, width=144)
    #
    # # print(list_out_dek)
    # write_file_dek(list_out_dek, date_now, 'dek')

    # Собираем журнал RDT
    # list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
    # pprint.pprint(list_out_rdt, depth=12, width=144)
    # write_file_dek(list_out_rdt, 'rdt')

    # Собираем журнал CKT
    list_out_ckt = create_write_ckt_old(read_file_jornal('ckt'))
    pprint.pprint(list_out_ckt, depth=12, width=144)
    write_file_dek(list_out_ckt, 'ckt')
