# импорт внешних пакетов
import datetime, pprint

"""
Функции необходимые для записи журналов и чтения данных.
"""
# Глобальные переменные файла
list_out_dek = []
list_out_rdt = []
list_out_ckt = []
list_out_nsd_spo = []
list_in_technical = []
list_out_technical = []
dict_out_technical = {}
list_number_device = []
list_number_stamp = []

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

    if type_f == 'nsd_spo':
        list_out_nsd_spo = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                str = str_.strip().split(";")
                for _ in str:
                    _ = _.encode('utf-8')
                list_out_nsd_spo.append(str)

        return list_out_nsd_spo

    if type_f == 'technical':
        list_in_technical = []

        with open(f'{type_f}_jornal_M567M.csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                str = str_.strip().split(";")
                for _ in str:
                    _ = _.encode('utf-8')
                list_in_technical.append(str)

        return list_in_technical

    if type_f == '':
        print('Не указан тип файла жрнала!')



def write_file_dek(list_data_in, type_f=None, type_w='Неизвестная'):
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
    return print(f'Сделанна запись "{type_w}", данные записаны в файл jornal_out_{type_f}.csv')


'''Функции для формирования журнала DEK'''
def create_write_dek_1(list_out_dek):
    # Цикл для формирования записи вскрытия в последний раз опечатанного DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_dek[i][j] = ser_number_dek_old_1
            elif i == 3 and j == 0:
                list_out_dek[i][j] = number_com_dek_old_1
            elif i == 4 and j == 0:
                list_out_dek[i][j] = fac_number_dek_old_1
            elif i == 6 and j == 0:
                list_out_dek[i][j] = ser_number_dek_old_2
            elif i == 7 and j == 0:
                list_out_dek[i][j] = number_com_dek_old_2
            elif i == 8 and j == 0:
                list_out_dek[i][j] = fac_number_dek_old_2
            elif i == 1 and j == 2:
                list_out_dek[i][j] = last_device_input_dek
            elif i == 1 and j == 8:
                list_out_dek[i][j] = date_time_op_dek1_old.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 8:
                list_out_dek[i][j] = date_time_op_dek1_old.strftime('T-%H:%M')
            elif i == 3 and j == 8:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 8:
                list_out_dek[i][j] = date_time_op_dek2_old.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 8:
                list_out_dek[i][j] = date_time_op_dek2_old.strftime('T-%H:%M')
            elif i == 7 and j == 8:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                list_out_dek[i][j] = str(i) + ',' + str(j)  # ''

    return list_out_dek


def create_write_dek_2(list_out_dek):
    # Цикл для формирования записи стирания старого DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_dek[i][j] = ser_number_dek_old_1
            elif i == 3 and j == 0:
                list_out_dek[i][j] = number_com_dek_old_1
            elif i == 4 and j == 0:
                list_out_dek[i][j] = fac_number_dek_old_1
            elif i == 6 and j == 0:
                list_out_dek[i][j] = ser_number_dek_old_2
            elif i == 7 and j == 0:
                list_out_dek[i][j] = number_com_dek_old_2
            elif i == 8 and j == 0:
                list_out_dek[i][j] = fac_number_dek_old_2
            elif i == 1 and j == 2:
                list_out_dek[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_dek[i][j] = date_time_begin.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 3:
                list_out_dek[i][j] = date_time_begin.strftime('T-%H:%M')
            elif i == 3 and j == 3:
                list_out_dek[i][j] = stamp_numer_common
            elif i == 5 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('T-%H:%M')
            elif i == 7 and j == 6:
                list_out_dek[i][j] = stamp_numer_common
            elif i == 2 and j == 10:
                list_out_dek[i][j] = date_time_del_dek1_old.strftime('D-%d.%m.%Y')
            elif i == 3 and j == 10:
                list_out_dek[i][j] = date_time_del_dek1_old.strftime('T-%H:%M')
            elif i == 6 and j == 10:
                list_out_dek[i][j] = date_time_del_dek2_old.strftime('D-%d.%m.%Y')
            elif i == 7 and j == 10:
                list_out_dek[i][j] = date_time_del_dek2_old.strftime('T-%H:%M')
            elif i == 1 and j == 11:
                list_out_dek[i][j] = date_time_cl_dek1_old.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 11:
                list_out_dek[i][j] = date_time_cl_dek1_old.strftime('T-%H:%M')
            elif i == 3 and j == 11:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 11:
                list_out_dek[i][j] = date_time_cl_dek2_old.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 11:
                list_out_dek[i][j] = date_time_cl_dek2_old.strftime('T-%H:%M')
            elif i == 7 and j == 11:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 4, 5, 7, 8, 9]:
                list_out_dek[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_dek[i][j] = ''

    list_out_dek[0][0] = 'Запись о стирание старого DEK'

    # del list_out_dek[0]

    return list_out_dek


def create_write_dek_3_new(list_out_dek):
    # Цикл для формирования записи ввода №1 нового DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_dek[i][j] = ser_number_dek_new_1
            elif i == 3 and j == 0:
                list_out_dek[i][j] = number_com_dek_new_1
            elif i == 4 and j == 0:
                list_out_dek[i][j] = fac_number_dek_new_1
            elif i == 6 and j == 0:
                list_out_dek[i][j] = ser_number_dek_new_2
            elif i == 7 and j == 0:
                list_out_dek[i][j] = number_com_dek_new_2
            elif i == 8 and j == 0:
                list_out_dek[i][j] = fac_number_dek_new_2
            elif i == 1 and j == 1:
                list_out_dek[i][j] = date_time_op_dek1_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 1:
                list_out_dek[i][j] = date_time_op_dek1_new.strftime('T-%H:%M')
            elif i == 5 and j == 1:
                list_out_dek[i][j] = date_time_op_dek2_new.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 1:
                list_out_dek[i][j] = date_time_op_dek2_new.strftime('T-%H:%M')
            elif i == 1 and j == 2:
                list_out_dek[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_dek[i][j] = date_time_begin.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 3:
                list_out_dek[i][j] = date_time_begin.strftime('T-%H:%M')
            elif i == 3 and j == 3:
                list_out_dek[i][j] = stamp_numer_common_old
            elif i == 1 and j == 4:
                list_out_dek[i][j] = date_time_op_dek2_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_dek[i][j] = date_time_op_dek2_new.strftime('T-%H:%M')
            elif i == 5 and j == 4:
                list_out_dek[i][j] = date_time_in_dek2_new.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 4:
                list_out_dek[i][j] = date_time_in_dek2_new.strftime('T-%H:%M')
            elif i == 5 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('T-%H:%M')
            elif i == 2 and j == 9:
                list_out_dek[i][j] = date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
            elif i == 3 and j == 9:
                list_out_dek[i][j] = date_time_erase_dek1_new.strftime('T-%H:%M')
            elif i == 6 and j == 9:
                list_out_dek[i][j] = date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
            elif i == 7 and j == 9:
                list_out_dek[i][j] = date_time_erase_dek1_new.strftime('T-%H:%M')

            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [5, 7, 8, 10, 11]:
                list_out_dek[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_dek[i][j] = ''

    list_out_dek[0][0] = 'Запись о вводе №1 DEK в аппарат'

    # del list_out_dek[0]

    return list_out_dek

def create_write_dek_4_new(list_out_dek):
    # Цикл для формирования записи ввода №2 нового DEK
    for i, row in enumerate(list_out_dek):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_dek[i][j] = ser_number_dek_new_1
            elif i == 3 and j == 0:
                list_out_dek[i][j] = number_com_dek_new_1
            elif i == 4 and j == 0:
                list_out_dek[i][j] = fac_number_dek_new_1
            elif i == 6 and j == 0:
                list_out_dek[i][j] = ser_number_dek_new_2
            elif i == 7 and j == 0:
                list_out_dek[i][j] = number_com_dek_new_2
            elif i == 8 and j == 0:
                list_out_dek[i][j] = fac_number_dek_new_2
            elif i == 1 and j == 2:
                list_out_dek[i][j] = number_device
            elif i == 1 and j == 4:
                list_out_dek[i][j] = date_time_in_1_dek1_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_dek[i][j] = date_time_in_1_dek1_new.strftime('T-%H:%M')
            elif i == 5 and j == 4:
                list_out_dek[i][j] = date_time_in_1_dek2_new.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 4:
                list_out_dek[i][j] = date_time_in_1_dek2_new.strftime('T-%H:%M')
            elif i == 5 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 6:
                list_out_dek[i][j] = date_time_cl_cap_input.strftime('T-%H:%M')
            elif i == 1 and j == 7:
                list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 7:
                list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('T-%H:%M')
            elif i == 3 and j == 7:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 7:
                list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
            elif i == 6 and j == 7:
                list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
            elif i == 7 and j == 7:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i == 1 and j == 8:
                list_out_dek[i][j] = date_time_op_2_dek1_new
            elif i == 2 and j == 8:
                list_out_dek[i][j] = date_time_op_2_dek1_new
            elif i == 3 and j == 8:
                list_out_dek[i][j] = stamp_numer_one_r
            elif i == 5 and j == 8:
                list_out_dek[i][j] = date_time_op_2_dek2_new
            elif i == 6 and j == 8:
                list_out_dek[i][j] = date_time_op_2_dek2_new
            elif i == 7 and j == 8:
                list_out_dek[i][j] = stamp_numer_two_r
            elif i == 2 and j == 9:
                list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
            elif i == 3 and j == 9:
                list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('T-%H:%M')
            elif i == 6 and j == 9:
                list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
            elif i == 7 and j == 9:
                list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('T-%H:%M')

            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 5, 10, 11]:
                list_out_dek[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_dek[i][j] = ''

    list_out_dek[0][0] = 'Запись о вводе №2 DEK в аппарат'

    return list_out_dek


'''Функции для формирования журнала RDT'''
def create_write_rdt_1(list_out_rdt):
    # Цикл для формирования записи сброса ранее введённог RDT
    for i, row in enumerate(list_out_rdt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_rdt[i][j] = ser_number_rdt_1_old
            elif i == 3 and j == 0:
                list_out_rdt[i][j] = number_com_rdt_1_old
            elif i == 4 and j == 0:
                list_out_rdt[i][j] = fac_number_rdt_1_old
            elif i == 6 and j == 0:
                list_out_rdt[i][j] = ser_number_rdt_2_old
            elif i == 7 and j == 0:
                list_out_rdt[i][j] = number_com_rdt_2_old
            elif i == 8 and j == 0:
                list_out_rdt[i][j] = fac_number_rdt_2_old
            elif i == 1 and j == 2:
                list_out_rdt[i][j] = number_device
            elif i == 2 and j == 9:
                list_out_rdt[i][j] = date_time_del_rdt_old.strftime('%d.%m.%Y')
            elif i == 3 and j == 9:
                list_out_rdt[i][j] = date_time_del_rdt_old.strftime('%H:%M')
            elif i == 6 and j == 9:
                list_out_rdt[i][j] = date_time_del_rdt_old.strftime('%d.%m.%Y')
            elif i == 7 and j == 9:
                list_out_rdt[i][j] = date_time_del_rdt_old.strftime('%H:%M')

            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 4, 5, 6, 7, 8, 10, 11]:
                list_out_rdt[i][j] = '' # str(i) + ',' + str(j)

    return list_out_rdt

def create_write_rdt_2(list_out_rdt):
    # Цикл для формирования записи ввода RDT
    for i, row in enumerate(list_out_rdt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_rdt[i][j] = ser_number_rdt_1
            elif i == 3 and j == 0:
                list_out_rdt[i][j] = number_com_rdt_1
            elif i == 4 and j == 0:
                list_out_rdt[i][j] = fac_number_rdt_1
            elif i == 6 and j == 0:
                list_out_rdt[i][j] = ser_number_rdt_2
            elif i == 7 and j == 0:
                list_out_rdt[i][j] = number_com_rdt_2
            elif i == 8 and j == 0:
                list_out_rdt[i][j] = fac_number_rdt_2
            elif i == 1 and j == 1:
                list_out_rdt[i][j] = date_time_op_rdt1.strftime('%d.%m.%Y')
            elif i == 2 and j == 1:
                list_out_rdt[i][j] = date_time_op_rdt1.strftime('%H:%M')
            elif i == 5 and j == 1:
                list_out_rdt[i][j] = date_time_op_rdt2.strftime('%d.%m.%Y')
            elif i == 6 and j == 1:
                list_out_rdt[i][j] = date_time_op_rdt2.strftime('%H:%M')
            elif i == 1 and j == 2:
                list_out_rdt[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_rdt[i][j] = date_time_begin.strftime('%d.%m.%Y')
            elif i == 2 and j == 3:
                list_out_rdt[i][j] = date_time_begin.strftime('%H:%M')
            elif i == 3 and j == 3:
                list_out_rdt[i][j] = stamp_numer_common_old
            elif i == 1 and j == 4:
                list_out_rdt[i][j] = date_time_op_rdt2.strftime('%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_rdt[i][j] = date_time_op_rdt2.strftime('%H:%M')
            elif i == 5 and j == 4:
                list_out_rdt[i][j] = date_time_in_rdt2.strftime('%d.%m.%Y')
            elif i == 6 and j == 4:
                list_out_rdt[i][j] = date_time_in_rdt2.strftime('%H:%M')
            elif i == 5 and j == 6:
                list_out_rdt[i][j] = date_time_cl_cap_input.strftime('%d.%m.%Y')
            elif i == 6 and j == 6:
                list_out_rdt[i][j] = date_time_cl_cap_input.strftime('%H:%M')
            elif i == 7 and j == 6:
                list_out_rdt[i][j] = stamp_numer_common
            elif i == 2 and j == 10:
                list_out_rdt[i][j] = date_time_erase_rdt1.strftime('%d.%m.%Y')
            elif i == 3 and j == 10:
                list_out_rdt[i][j] = date_time_erase_rdt1.strftime('%H:%M')
            elif i == 6 and j == 10:
                list_out_rdt[i][j] = date_time_erase_rdt2.strftime('%d.%m.%Y')
            elif i == 7 and j == 10:
                list_out_rdt[i][j] = date_time_erase_rdt2.strftime('%H:%M')
            elif i == 1 and j == 11:
                list_out_rdt[i][j] = date_time_cl_rdt1.strftime('%d.%m.%Y')
            elif i == 2 and j == 11:
                list_out_rdt[i][j] = date_time_cl_rdt1.strftime('%H:%M')
            elif i == 3 and j == 11:
                list_out_rdt[i][j] = stamp_numer_one_r
            elif i == 5 and j == 11:
                list_out_rdt[i][j] = date_time_cl_rdt2.strftime('%d.%m.%Y')
            elif i == 6 and j == 11:
                list_out_rdt[i][j] = date_time_cl_rdt2.strftime('%H:%M')
            elif i == 7 and j == 11:
                list_out_rdt[i][j] = stamp_numer_two_r

            elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [5, 7, 8, 9]:
                list_out_rdt[i][j] = '' # str(i) + ',' + str(j)
            elif i == 0:
                list_out_rdt[i][j] = ''

    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[4]
    # del list_out_nsd_spo[0]
    list_out_rdt[0][0] = 'Запись о вводе RDT в аппарат'

    return list_out_rdt


'''Функции для формирования журнала CKT'''
def create_write_ckt_old(list_out_ckt):
    # Цикл для формирования записи проверке старым CKT
    for i, row in enumerate(list_out_ckt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_ckt[i][j] = f'№ {ser_number_ckt_old}, э.ед.'
            elif i == 1 and j == 1:
                list_out_ckt[i][j] = date_time_ckt.strftime('%d.%m.%Y')
            elif i == 2 and j == 1:
                list_out_ckt[i][j] = date_time_ckt.strftime('%H:%M')
            elif i == 1 and j == 2 or i == 2 and j == 3 or i == 2 and j == 6:
                list_out_ckt[i][j] = number_tape_ckt_old
            elif i == 3 and j == 1:
                list_out_ckt[i][j] = stamp_numer_one_r_ckt_old
            elif i == 2 and j == 2:
                list_out_ckt[i][j] = extract_date_time_ckt.strftime('%d.%m.%Y %H:%M')
            elif i == 1 and j == 3:
                list_out_ckt[i][j] = number_device
            elif i == 3 and j == 3:
                list_out_ckt[i][j] = input_date_time_ckt.strftime('%d.%m.%Y %H:%M')
            elif i == 2 and j == 4:
                list_out_ckt[i][j] = input_date_time_ckt.strftime('%d.%m.%Y')
            elif i == 1 and j == 5:
                list_out_ckt[i][j] = stamp_numer_one_r
            elif i == 2 and j == 5:
                list_out_ckt[i][j] = seal_date_time_ckt.strftime('%d.%m.%Y %H:%M')
            elif i == 1 and j == 6:
                list_out_ckt[i][j] = del_date_time.strftime('%d.%m.%Y %H:%M')

            elif i in [1, 2, 3, 4] and j in [7]:
                list_out_ckt[i][j] = '' # str(i) + ',' + str(j)

    return list_out_ckt

def create_write_ckt_new(list_out_ckt):
    # Цикл для формирования записи проверки новым CKT
    for i, row in enumerate(list_out_ckt):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_ckt[i][j] = f'№ {ser_number_ckt_new}, э.ед.'
            elif i == 1 and j == 1:
                list_out_ckt[i][j] = date_time_ckt_new.strftime('%d.%m.%Y')
            elif i == 2 and j == 1:
                list_out_ckt[i][j] = date_time_ckt_new.strftime('%H:%M')
            elif i == 1 and j == 2 or i == 2 and j == 3 or i == 2 and j == 6:
                list_out_ckt[i][j] = number_tape_ckt_new
            elif i == 3 and j == 1:
                list_out_ckt[i][j] = 'подпись'
            elif i == 4 and j == 1:
                list_out_ckt[i][j] = ''
            elif i == 2 and j == 2:
                list_out_ckt[i][j] = extract_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
            elif i == 1 and j == 3:
                list_out_ckt[i][j] = number_device
            elif i == 3 and j == 3:
                list_out_ckt[i][j] = input_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
            elif i == 2 and j == 4:
                list_out_ckt[i][j] = input_date_time_ckt_new.strftime('%d.%m.%Y')
            elif i == 1 and j == 5:
                list_out_ckt[i][j] = stamp_numer_one_r
            elif i == 2 and j == 5:
                list_out_ckt[i][j] = seal_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
            elif i == 1 and j == 6:
                list_out_ckt[i][j] = del_date_time.strftime('%d.%m.%Y %H:%M')

            elif i in [1, 2, 3, 4] and j in [7]:
                list_out_ckt[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_ckt[i][j] = ''

    list_out_ckt[0][0] = 'Запись о проверке новым CKT'

    return list_out_ckt

'''Функции для формирования журнала SPO'''
def create_write_spo_1(list_out_nsd_spo):
    # Цикл для формирования записи вскрытия SPO
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo1
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo1
            elif i == 5 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo2
            elif i == 6 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo2
            elif i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device_last_in_spo
            elif i == 1 and j == 7:
                list_out_nsd_spo[i][j] = date_time_op_spo1.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 2 and j == 7:
                list_out_nsd_spo[i][j] = stamp_numer_one_spo_last
            elif i == 4 and j == 7:
                list_out_nsd_spo[i][j] = date_time_op_spo2.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 7:
                list_out_nsd_spo[i][j] = stamp_numer_two_spo_last

            elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 8, 9, 10, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''

    return list_out_nsd_spo


def create_write_spo_2(list_out_nsd_spo):
    # Цикл для формирования записи сброса SPO
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo1
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo1
            elif i == 5 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo2
            elif i == 6 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo2
            if i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device
            elif i == 2 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_spo12.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_spo12.strftime('D-%d.%m.%Y T-%H:%M')

            elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_nsd_spo[i][j] = ''

    list_out_nsd_spo[0][0] = 'Запись о  сбросе СПО в аппарате'

    # del list_out_nsd_spo[0]

    return list_out_nsd_spo

def create_write_spo_3(list_out_nsd_spo):
    # Цикл для формирования записи ввода №1 SPO
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo1
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo1
            elif i == 5 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo2
            elif i == 6 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo2
            if i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_nsd_spo[i][j] = date_time_begin.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 2 and j == 3:
                list_out_nsd_spo[i][j] = stamp_numer_common_old
            elif i == 1 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_1_spo1.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_1_spo1.strftime('T-%H:%M')
            elif i == 4 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_1_spo2.strftime('D-%d.%m.%Y')
            elif i == 5 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_1_spo2.strftime('T-%H:%M')
            elif i == 4 and j == 5:
                list_out_nsd_spo[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 5:
                list_out_nsd_spo[i][j] = stamp_numer_common
            elif i == 2 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_1_spo12.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_1_spo12.strftime('D-%d.%m.%Y T-%H:%M')

            elif i in [1, 2, 3, 4, 5, 6] and j in [1, 6, 7, 9, 10, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_nsd_spo[i][j] = ''

    list_out_nsd_spo[0][0] = 'Запись о вводе №1 СПО в аппарат'

    return list_out_nsd_spo

def create_write_spo_4(list_out_nsd_spo):
    # Цикл для формирования записи ввода №2 SPO
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    del list_out_nsd_spo[1]
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo1
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo1
            elif i == 5 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_comp_spo2
            elif i == 6 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_spo2
            if i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device
            elif i == 1 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_2_spo1.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_2_spo1.strftime('T-%H:%M')
            elif i == 4 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_2_spo2.strftime('D-%d.%m.%Y')
            elif i == 5 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_2_spo2.strftime('T-%H:%M')
            elif i == 4 and j == 5:
                list_out_nsd_spo[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 5:
                list_out_nsd_spo[i][j] = stamp_numer_common
            elif i == 1 and j == 6:
                list_out_nsd_spo[i][j] = date_time_in_2_spo2.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 2 and j == 6:
                list_out_nsd_spo[i][j] = stamp_numer_one_r
            elif i == 4 and j == 6:
                list_out_nsd_spo[i][j] = date_time_cl_2_spo2.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 6:
                list_out_nsd_spo[i][j] = stamp_numer_two_r
            elif i == 1 and j == 7:
                list_out_nsd_spo[i][j] = date_time_op_1_spo1
            elif i == 2 and j == 7:
                list_out_nsd_spo[i][j] = stamp_numer_one_r
            elif i == 4 and j == 7:
                list_out_nsd_spo[i][j] = date_time_op_1_spo2
            elif i == 5 and j == 7:
                list_out_nsd_spo[i][j] = stamp_numer_two_r

            elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 6, 7, 8, 9, 10, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_nsd_spo[i][j] = ''

    list_out_nsd_spo[0][0] = 'Запись о вводе №2 СПО в аппарат'

    return list_out_nsd_spo


def create_write_nsd_1(list_out_nsd_spo):
    # Цикл для формирования записи сброса NSD
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_nsd
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_nsd
            if i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device
            elif i == 2 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_spo12.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 5 and j == 8:
                list_out_nsd_spo[i][j] = date_time_del_spo12.strftime('D-%d.%m.%Y T-%H:%M')

            elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_nsd_spo[i][j] = ''

    list_out_nsd_spo[0][0] = 'Запись о сбросе НСД в аппарате'

    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    # del list_out_nsd_spo[0]

    return list_out_nsd_spo


def create_write_nsd_2(list_out_nsd_spo):
    # Цикл для формирования записи ввода NSD
    for i, row in enumerate(list_out_nsd_spo):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            if i == 2 and j == 0:
                list_out_nsd_spo[i][j] = ser_number_nsd_new
            elif i == 3 and j == 0:
                list_out_nsd_spo[i][j] = fac_number_nsd_new
            elif i == 1 and j == 1:
                list_out_nsd_spo[i][j] = date_time_op_nsd_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 1:
                list_out_nsd_spo[i][j] = date_time_op_nsd_new.strftime('T-%H:%M')
            if i == 1 and j == 2:
                list_out_nsd_spo[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_nsd_spo[i][j] = date_time_begin.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 2 and j == 3:
                list_out_nsd_spo[i][j] = stamp_numer_common_old
            elif i == 1 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_nsd_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 4:
                list_out_nsd_spo[i][j] = date_time_in_nsd_new.strftime('T-%H:%M')
            elif i == 1 and j == 5:
                list_out_nsd_spo[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 2 and j == 5:
                list_out_nsd_spo[i][j] = stamp_numer_common
            elif i == 2 and j == 9:
                list_out_nsd_spo[i][j] = date_time_erase_nsd_new.strftime('D-%d.%m.%Y T-%H:%M')
            elif i == 1 and j == 10:
                list_out_nsd_spo[i][j] = date_time_cl_nsd_new.strftime('D-%d.%m.%Y')
            elif i == 2 and j == 10:
                list_out_nsd_spo[i][j] = date_time_cl_nsd_new.strftime('T-%H:%M')
            elif i == 3 and j == 10:
                list_out_nsd_spo[i][j] = stamp_numer_one_r

            elif i in [1, 2, 3, 4, 5, 6] and j in [6, 7, 8, 11]:
                list_out_nsd_spo[i][j] = str(i) + ',' + str(j)  # ''
            elif i == 0:
                list_out_nsd_spo[i][j] = ''

    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    del list_out_nsd_spo[4]
    # del list_out_nsd_spo[0]
    list_out_nsd_spo[0][0] = 'Запись о вводе НСД в аппарат'

    return list_out_nsd_spo

'''Функции для формирования технического журнала'''
def create_dict_tech(list_in_technical):

    dict_out_technical = {
        # заголовки технического журнала
        'title': list_in_technical[0],
        # записи о вскрытии контейнера с МУВК
        'date_time_op_MUVK': date_time_op_MUVK,
        'write_open_kontainer': list_in_technical[1][1],
        'catatan_ON_begin': list_in_technical[1][8],
        'FIO_1part': list_in_technical[2][6], # ФИО 1 часть
        'FIO_lukisan_1part': list_in_technical[2][7], # подпись 1 часть
        # записи о вскрытии 1 аппарата
        'date_time_op_cap_input_1_device': date_time_op_cap_input_1_device,
        'date_time_op_cap_input_2_device': date_time_op_cap_input_2_device,
        'date_time_op_cap_input_n_device': date_time_op_cap_input_n_device,
        'write_open_cap_input_1_device': list_in_technical[3][1],
        'write_open_cap_input_devices': list_in_technical[5][1],
        # записи о проверке ЦПО МУВК
        'date_time_op_CUV_1': date_time_op_CUV_1,
        'write_open_CUV_1': list_in_technical[7][1],
        'date_time_op_CUV_2': date_time_op_CUV_2,
        'write_open_CUV_2': list_in_technical[9][1],
        'FIO_2part': list_in_technical[10][6], # ФИО 2 часть
        'FIO_lukisan_2part': list_in_technical[10][7], # подпись 2 часть
        'date_time_check_open': date_time_op_CUV_2, # дата проверки вскрытия
        'write_check_open': list_in_technical[11][1], # проверка вскрытия
        'FIO_chief': list_in_technical[2][6],  # ФИО начальник
        'FIO_lukisan_chief': list_in_technical[2][7], # подпись начальник
        'date_time_check_CPO_MUVK_b': date_time_check_CPO_MUVK_b, # проверка ЦПО МУВК начало
        'date_time_check_CPO_MUVK_e': date_time_check_CPO_MUVK_e, # проверка ЦПО МУВК конец
        'write_check_CPO_MUVK': list_in_technical[13][1], # проверка ЦПО МУВК
        'date_time_erase_CUV_1_b': date_time_erase_CUV_1_b, # стирание ЦУВ-1 начало
        'date_time_erase_CUV_1_e': date_time_erase_CUV_1_e, # стирание ЦУВ-1 конец
        'write_erase_CUV_1': list_in_technical[16][1], # стирание ЦУВ-1
        'date_time_cl_CUV_1': date_time_cl_CUV_1, # опечатывание ЦУВ-1
        'write_cl_CUV_1': list_in_technical[18][1], # опечатывание ЦУВ-1
        'date_time_cl_CUV_2': date_time_cl_CUV_2, # опечатывание ЦУВ-2
        'write_cl_CUV_2': list_in_technical[20][1], # опечатывание ЦУВ-2
        'date_time_CPO_INPUT_b': date_time_CPO_INPUT_b, # проверка ЦПО аппаратов, ввод ключей
        'date_time_CPO_INPUT_e': date_time_CPO_INPUT_e, # проверка ЦПО аппаратов, ввод ключей
        'write_CPO_INPUT': list_in_technical[22][1], # проверка ЦПО аппаратов, ввод ключей
        'date_time_erase_RDT_b': date_time_erase_RDT_b, # стирание RDT
        'date_time_erase_RDT_e': date_time_erase_RDT_e, # стирание RDT
        'write_erase_RDT': list_in_technical[25][1], # стирание RDT
        'date_time_cl_cap_input_b': date_time_cl_cap_input_b, # опечатывание крышки ввод аппарата №1
        'date_time_cl_cap_input_e': date_time_cl_cap_input_e, # опечатывание крышки ввод последнего аппарата
        'write_cl_cap_input': list_in_technical[28][1], # опечатывание крышек ввод  аппаратов
        'date_time_cl_MUVK': date_time_cl_MUVK, # опечатывание МУВК
        'write_cl_MUVK': list_in_technical[31][1], # опечатывание МУВК
        'date_time_op_box_CUV_2': date_time_op_box_CUV_2, # вскрытие пенала ЦУВ-2
        'write_op_box_CUV_2': list_in_technical[34][1], # вскрытие пенала ЦУВ-2
        'date_time_del_CUV_2': date_time_del_CUV_2, # уничтожение ЦУВ-2
        'write_del_CUV_2': list_in_technical[36][1], # уничтожение ЦУВ-2
        'date_time_use_KD': date_time_del_CUV_2, # дата проверки правильности обращения с КД
        'write_use_KD': list_in_technical[39][1], # проверка правильности обращения с КД
        'FIO_carry_KD': list_in_technical[39][6],  # ФИО ответственный за КД
        'lukisan_carry_KD': list_in_technical[39][7],  # подпись ответственный за КД
        'date_time_erase_RDT_old_b': date_time_erase_RDT_old_b, # начало стирания выведенных из обращения RDT
        'date_time_erase_RDT_old_e': date_time_erase_RDT_old_e, # конец стирания выведенных из обращения RDT
        'write_erase_RDT_old': list_in_technical[44][1], # стирание выведенных из обращения RDT
        'date_time_cl_cap_input_dev1': date_time_cl_cap_input_dev1, # опечатывания разъёма ввод аппарата после стирания RDT
        'write_cl_cap_input_dev1': list_in_technical[47][1], # опечатывания разъёма ввод аппарата после стирания RDT
    }

    return dict_out_technical

def create_write_technical(list_in_technical, dict_out_technical, type_work=None):

    list_out_technical = []
    # Условие для формирования технического журнала при очередном наборе
    if type_work == 'ОН':

        list_out_technical.append(list_in_technical[0])
        # запись о вскрытии МУВК
        list_out_technical.append(list_in_technical[1])
        list_out_technical.append(list_in_technical[2])
        list_out_technical[1][0] = dict_out_technical['date_time_op_MUVK'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_kontainer'] = f'Вскрыт контейнер с МУВК ПА655М {number_MUVK}, опечатанный печатями {stamp_numer_common_old_MUVK}'
        list_out_technical[1][1] = dict_out_technical['write_open_kontainer']
        del list_out_technical[1][8] # удаляем примечание
        # print(list_out_technical[1][1])
        list_out_technical[2][0] = dict_out_technical['date_time_op_MUVK'].strftime('%H:%M')
        dict_out_technical['FIO_1part'] = FIO_1part
        list_out_technical[2][6] = dict_out_technical['FIO_1part']
        # запись о вскрытии крышки "Ввод" первого аппарата
        list_out_technical.append(list_in_technical[3])
        list_out_technical.append(list_in_technical[4])
        list_out_technical[3][0] = dict_out_technical['date_time_op_cap_input_1_device'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_cap_input_1_device'] = f'Вскрыта крышка разъёма "Ввод" аппаратуры М-567М №{number_device_first},' \
            f'опечатанный печатями {stamp_numer_common_old_first}'
        list_out_technical[3][1] = dict_out_technical['write_open_cap_input_1_device']
        list_out_technical[4][0] = dict_out_technical['date_time_op_cap_input_1_device'].strftime('%H:%M')
        list_out_technical[4][6] = dict_out_technical['FIO_1part']
        # запись о вскрытии крышек "Ввод" остальных аппаратов
        list_out_technical.append(list_in_technical[5])
        list_out_technical.append(list_in_technical[6])
        list_out_technical[5][0] = dict_out_technical['date_time_op_cap_input_2_device'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_cap_input_devices'] = f'Вскрыты крышки разъёма "Ввод" аппаратуры М-567М №{str_number_device}, опечатанные печатями {str_number_stamp}'
        list_out_technical[5][1] = dict_out_technical['write_open_cap_input_devices']
        list_out_technical[6][0] = dict_out_technical['date_time_op_cap_input_2_device'].strftime('%H:%M') + '-' +\
                                   dict_out_technical['date_time_op_cap_input_n_device'].strftime('%H:%M')
        list_out_technical[6][6] = dict_out_technical['FIO_1part']
        # запись о вскрытии ЦУВ-1
        list_out_technical.append(list_in_technical[7])
        list_out_technical.append(list_in_technical[8])
        list_out_technical[7][0] = dict_out_technical['date_time_op_CUV_1'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_CUV_1'] = f'Вскрыта упаковка шифрблокнота ЦУВ-1-1012 серия №{ser_number_CUV_1_2}, э.ед., {fac_number_CUV_1}'
        list_out_technical[7][1] = dict_out_technical['write_open_CUV_1']
        list_out_technical[8][0] = dict_out_technical['date_time_op_CUV_1'].strftime('%H:%M')
        list_out_technical[8][6] = dict_out_technical['FIO_1part']
        # запись о вскрытии ЦУВ-2
        list_out_technical.append(list_in_technical[9])
        list_out_technical.append(list_in_technical[10])
        list_out_technical[9][0] = dict_out_technical['date_time_op_CUV_2'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_CUV_2'] = f'Вскрыта упаковка шифрблокнота ЦУВ-2-1012 серия №{ser_number_CUV_1_2}, э.ед.'
        list_out_technical[9][1] = dict_out_technical['write_open_CUV_2']
        list_out_technical[10][0] = dict_out_technical['date_time_op_CUV_2'].strftime('%H:%M')
        dict_out_technical['FIO_2part'] = FIO_2part
        list_out_technical[10][6] = dict_out_technical['FIO_2part']
        # запись о проверки правильности вскрытия
        list_out_technical.append(list_in_technical[11])
        list_out_technical.append(list_in_technical[12])
        list_out_technical[11][0] = dict_out_technical['date_time_check_open'].strftime('%d.%m.%Y')
        dict_out_technical['write_open_CUV_1'] = f'Вскрыта упаковка шифрблокнота ЦУВ-1-1012 серия №{ser_number_CUV_1_2}, э.ед., {fac_number_CUV_1}'
        list_out_technical[11][1] = dict_out_technical['write_check_open']
        dict_out_technical['FIO_chief'] = FIO_chief
        list_out_technical[12][6] = dict_out_technical['FIO_chief']
        # проверка ЦПО МУВК
        list_out_technical.append(list_in_technical[13])
        list_out_technical.append(list_in_technical[14])
        list_out_technical.append(list_in_technical[15])
        list_out_technical[13][0] = dict_out_technical['date_time_check_CPO_MUVK_b'].strftime('%d.%m.%Y')
        dict_out_technical['write_check_CPO_MUVK'] = f'Проведена проверка ЦПО МУВК ПА655М(V1012) {number_MUVK}, подключенного к аппаратуре ' \
            f'М-567М(V1054)№{number_device_first} с использованием КД ЦУВ-1,2-1012 серия №{ser_number_CUV_1_2}, э.ед. Результат проверки - "норма"'
        list_out_technical[13][1] = dict_out_technical['write_check_CPO_MUVK']
        list_out_technical[14][0] = dict_out_technical['date_time_check_CPO_MUVK_b'].strftime('%H:%M') + '-' + \
                                   dict_out_technical['date_time_check_CPO_MUVK_e'].strftime('%H:%M')
        list_out_technical[14][6] = dict_out_technical['FIO_1part']
        list_out_technical[15][6] = dict_out_technical['FIO_2part']
        # стирание ЦУВ-1
        list_out_technical.append(list_in_technical[16])
        list_out_technical.append(list_in_technical[17])
        list_out_technical[16][0] = dict_out_technical['date_time_erase_CUV_1_b'].strftime('%d.%m.%Y')
        dict_out_technical['write_erase_CUV_1'] = f'Произведено стирание КИ с КД ЦУВ-1-1012 серия №{ser_number_CUV_1_2}, э.ед.,' \
            f'{fac_number_CUV_1} с использованием МУВК ПА655М {number_MUVK}, подключенного к аппаратуре М-567М №{number_device_first}'
        list_out_technical[16][1] = dict_out_technical['write_erase_CUV_1']
        list_out_technical[17][0] = dict_out_technical['date_time_erase_CUV_1_b'].strftime('%H:%M') + '-' + \
                                    dict_out_technical['date_time_erase_CUV_1_e'].strftime('%H:%M')
        list_out_technical[17][6] = dict_out_technical['FIO_1part']
        # опечатывание стёртого ЦУВ-1
        list_out_technical.append(list_in_technical[18])
        list_out_technical.append(list_in_technical[19])
        list_out_technical[18][0] = dict_out_technical['date_time_cl_CUV_1'].strftime('%d.%m.%Y')
        dict_out_technical['write_cl_CUV_1'] = f'Конверт с ключевым носителем К1634ДК6 {fac_number_CUV_1} закрыт и опечатан печатью {stamp_numer_one_r}'
        list_out_technical[18][1] = dict_out_technical['write_cl_CUV_1']
        list_out_technical[19][0] = dict_out_technical['date_time_cl_CUV_1'].strftime('%H:%M')
        list_out_technical[19][6] = dict_out_technical['FIO_1part']
        # опечатывание ЦУВ-2
        list_out_technical.append(list_in_technical[20])
        list_out_technical.append(list_in_technical[21])
        list_out_technical[20][0] = dict_out_technical['date_time_cl_CUV_2'].strftime('%d.%m.%Y')
        dict_out_technical['write_cl_CUV_2'] = f'Пенал с КД ЦУВ-2-1012 серия {ser_number_CUV_1_2}, э.ед. закрыт и опечатан печатью {stamp_numer_two_r}'
        list_out_technical[20][1] = dict_out_technical['write_cl_CUV_2']
        list_out_technical[21][0] = dict_out_technical['date_time_cl_CUV_2'].strftime('%H:%M')
        list_out_technical[21][6] = dict_out_technical['FIO_2part']
        # проверка ЦПО аппаратов, ввод КИ, переход на очередную КИ в аппратах
        list_out_technical.append(list_in_technical[22])
        list_out_technical.append(list_in_technical[23])
        list_out_technical.append(list_in_technical[24])
        list_out_technical[22][0] = dict_out_technical['date_time_CPO_INPUT_b'].strftime('%d.%m.%Y')
        dict_out_technical['write_CPO_INPUT'] = f'В аппаратуре М-567М №{str_number_device} проведена проверка ЦПО,' \
            f'произведён ввод очередного ключа и произведён переход на очередной ключ'
        list_out_technical[22][1] = dict_out_technical['write_CPO_INPUT']
        list_out_technical[23][0] = dict_out_technical['date_time_CPO_INPUT_b'].strftime('%H:%M') + '-' + \
                                    dict_out_technical['date_time_CPO_INPUT_e'].strftime('%H:%M')
        list_out_technical[23][6] = dict_out_technical['FIO_1part']
        list_out_technical[24][6] = dict_out_technical['FIO_2part']
        # стирание КИ с введённых КД
        list_out_technical.append(list_in_technical[25])
        list_out_technical.append(list_in_technical[26])
        list_out_technical.append(list_in_technical[27])
        list_out_technical[25][0] = dict_out_technical['date_time_erase_RDT_b'].strftime('%d.%m.%Y')
        dict_out_technical['write_erase_RDT'] = f'Стирание КИ с введённых КД с использованием МУВК ПА655М {number_MUVK}'
        list_out_technical[25][1] = dict_out_technical['write_erase_RDT']
        list_out_technical[26][0] = dict_out_technical['date_time_erase_RDT_b'].strftime('%H:%M') + '-' + \
                                    dict_out_technical['date_time_erase_RDT_e'].strftime('%H:%M')
        list_out_technical[26][6] = dict_out_technical['FIO_1part']
        list_out_technical[27][6] = dict_out_technical['FIO_2part']
        # опечатывание крышек разъёма "Ввод" аппаратуры
        list_out_technical.append(list_in_technical[28])
        list_out_technical.append(list_in_technical[29])
        list_out_technical.append(list_in_technical[30])
        list_out_technical[28][0] = dict_out_technical['date_time_cl_cap_input_b'].strftime('%d.%m.%Y')
        dict_out_technical['write_cl_cap_input'] = f'Крышки рзаъёмов "Ввод" аппаратуры М567М №{str_number_device} закрыты' \
            f' и опечатаны печатями {stamp_numer_common}'
        list_out_technical[28][1] = dict_out_technical['write_cl_cap_input']
        list_out_technical[29][0] = dict_out_technical['date_time_cl_cap_input_b'].strftime('%H:%M') + '-' + \
                                    dict_out_technical['date_time_cl_cap_input_e'].strftime('%H:%M')
        list_out_technical[29][6] = dict_out_technical['FIO_1part']
        list_out_technical[30][6] = dict_out_technical['FIO_2part']
        # запись об оепчатывании МУВК
        list_out_technical.append(list_in_technical[31])
        list_out_technical.append(list_in_technical[32])
        list_out_technical.append(list_in_technical[33])
        list_out_technical[31][0] = dict_out_technical['date_time_cl_MUVK'].strftime('%d.%m.%Y')
        dict_out_technical['write_cl_MUVK'] = f'Контейнер с МУВК ПА655М {number_MUVK} закрыт и опечатан печатями {stamp_numer_common}'
        list_out_technical[31][1] = dict_out_technical['write_cl_MUVK']
        list_out_technical[32][0] = dict_out_technical['date_time_cl_MUVK'].strftime('%H:%M')
        list_out_technical[32][6] = dict_out_technical['FIO_1part']
        list_out_technical[33][6] = dict_out_technical['FIO_2part']
        # запись о вскрытии ЦУВ-1 для стирания
        list_out_technical.append(list_in_technical[34])
        list_out_technical.append(list_in_technical[35])
        list_out_technical[34][0] = dict_out_technical[ 'date_time_op_box_CUV_2'].strftime('%d.%m.%Y')
        dict_out_technical['write_op_box_CUV_2'] = f'Вскрыт пенал с КД ЦУВ-2-1012 серия №{ser_number_CUV_1_2}, э.ед., ' \
            f'опечатанный печатью {stamp_numer_two_r}'
        list_out_technical[34][1] = dict_out_technical['write_op_box_CUV_2']
        list_out_technical[35][0] = dict_out_technical[ 'date_time_op_box_CUV_2'].strftime('%H:%M')
        list_out_technical[35][6] = dict_out_technical['FIO_2part']
        # запись об уничтожении ЦУВ-2
        list_out_technical.append(list_in_technical[36])
        list_out_technical.append(list_in_technical[37])
        list_out_technical.append(list_in_technical[38])
        list_out_technical[36][0] = dict_out_technical['date_time_del_CUV_2'].strftime('%d.%m.%Y')
        dict_out_technical['write_del_CUV_2'] = f'Произведено уничтожение ЦУВ-2-1012 серия №{ser_number_CUV_1_2}, э.ед.'
        list_out_technical[36][1] = dict_out_technical['write_del_CUV_2']
        list_out_technical[37][0] = dict_out_technical['date_time_del_CUV_2'].strftime('%H:%M')
        list_out_technical[37][6] = dict_out_technical['FIO_1part']
        list_out_technical[38][6] = dict_out_technical['FIO_2part']
        # запись о проверки правильности обращения с КД
        list_out_technical.append(list_in_technical[39])
        list_out_technical[39][0] = dict_out_technical['date_time_use_KD'].strftime('%d.%m.%Y')
        dict_out_technical['write_use_KD'] = f'Правильность обращения с КД проверил'
        list_out_technical[39][1] = dict_out_technical['write_use_KD']
        dict_out_technical['FIO_carry_KD'] = FIO_carry_KD
        list_out_technical[39][6] = dict_out_technical['FIO_carry_KD']

    return list_out_technical


"""
Образцы записей в журналы.
Данные используемые в журналах.
Формирование данных для передачи в функции записи журналов.
"""

type_work = input('Введите вид работ ("ТО", "ОН", "Сб"): ') # выбор типа работ с аппаратурой
quantity_device = int(input('Сколько аппаратов вы используете: ')) # количество вводимых аппаратов

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'

# Приращения времени
duration_1_minutes = datetime.timedelta(minutes=1)
duration_2_minutes = datetime.timedelta(minutes=2)
duration_3_minutes = datetime.timedelta(minutes=3)
duration_4_minutes = datetime.timedelta(minutes=4)
duration_5_minutes = datetime.timedelta(minutes=5)
duration_6_minutes = datetime.timedelta(minutes=6)
duration_7_minutes = datetime.timedelta(minutes=7)
duration_11_minutes = datetime.timedelta(minutes=11)
duration_14_minutes = datetime.timedelta(minutes=14)
duration_20_minutes = datetime.timedelta(minutes=20)
duration_23_minutes = datetime.timedelta(minutes=23)
duration_25_minutes = datetime.timedelta(minutes=25)
duration_26_minutes = datetime.timedelta(minutes=26)
duration_27_minutes = datetime.timedelta(minutes=27)
duration_30_minutes = datetime.timedelta(minutes=30)
duration_38_minutes = datetime.timedelta(minutes=38)
duration_50_minutes = datetime.timedelta(minutes=50)
duration_52_minutes = datetime.timedelta(minutes=52)
duration_58_minutes = datetime.timedelta(minutes=58)
duration_1_h_25_m = datetime.timedelta(hours=1, minutes=25)
duration_1_h_14_m = datetime.timedelta(hours=1, minutes=14)
duration_1_h_02_m = datetime.timedelta(hours=1, minutes=2)
duration_2_h_19_m = datetime.timedelta(hours=2, minutes=19)
duration_10_hours = datetime.timedelta(hours=10)
duration_4_hours = datetime.timedelta(hours=4)
duration_10_h_19_m = datetime.timedelta(hours=10, minutes=19)
duration_14_hours = datetime.timedelta(hours=14)
duration_14_h_30_m = datetime.timedelta(hours=14, minutes=30)

"""
Код запуска процессов формирования записей производимых при данных работах.
"""

point_exit = 'да'
n = 1 # счётчик циклов набора аппаратов
date_time_cl_cap_input = datetime.datetime.now()
while n <= quantity_device:
    if point_exit == 'нет':
        break
    else:
        if n > 1:
            date_time_begin = date_time_cl_cap_input + duration_3_minutes
        else:
            date_time_begin = datetime.datetime.now()
        # получаем значения года, месяца, дня, часа, минут, секунд

        if n == 1:
            type_dt = input('Хотите ввести время начала работ(да/нет): ')
            if type_dt == 'да':
                year = date_time_begin.year
                # print(year, type(year))
                month = date_time_begin.month
                # print(month, type(month))
                day = date_time_begin.day
                # print(day, type(day))
                # hour = date_time_begin.strftime('%H')
                # print(hour, type(hour))
                # minute = date_time_begin.strftime('%M')
                # print(minute, type(minute))
                second = date_time_begin.second
                # print(second, type(second))
                hour = int(input('Введите время начала работ- часы: '))
                minute = int(input('-минуты: '))
                # print(hour, type(hour))
                date_time_begin = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=00)

        print(date_time_begin)

        # даты и время для DEK
        date_time_op_dek1_old = date_time_begin + duration_38_minutes
        date_time_op_dek2_old = date_time_op_dek1_old + duration_2_minutes
        date_time_del_dek1_old = date_time_op_dek2_old + duration_3_minutes
        date_time_del_dek2_old = date_time_del_dek1_old + duration_5_minutes
        date_time_cl_dek1_old = date_time_del_dek1_old + duration_1_minutes
        date_time_cl_dek2_old = date_time_del_dek2_old + duration_1_minutes
        date_time_op_dek1_new = date_time_begin + duration_58_minutes
        date_time_op_dek2_new = date_time_op_dek1_new + duration_1_minutes
        date_time_in_dek2_new = date_time_op_dek2_new + duration_1_minutes
        date_time_erase_dek1_new = date_time_in_dek2_new + duration_2_minutes

        # даты и время для SPO
        date_time_op_spo1 = date_time_begin + duration_1_h_25_m
        date_time_op_spo2 = date_time_op_spo1 + duration_1_minutes
        date_time_del_spo12 = date_time_begin + duration_1_h_02_m
        date_time_in_1_spo1 = date_time_op_spo2 + duration_2_minutes
        date_time_in_1_spo2 = date_time_in_1_spo1 + duration_2_minutes
        date_time_del_1_spo12 = date_time_in_1_spo2 + duration_27_minutes
        date_time_in_2_spo1 = date_time_del_1_spo12 + duration_3_minutes
        date_time_in_2_spo2 = date_time_in_2_spo1 + duration_2_minutes
        date_time_cl_2_spo2 = date_time_in_2_spo2 + duration_1_minutes
        date_time_op_1_spo1 = 'вр вск spo для апп №2'
        date_time_op_1_spo2 = 'вр вск spo для апп №2'

        # даты и время для DEK продолжение
        date_time_in_1_dek1_new = date_time_in_1_spo1 + duration_2_minutes
        date_time_in_1_dek2_new = date_time_in_1_dek1_new + duration_1_minutes
        date_time_seal_1_dek12_new = date_time_in_1_dek2_new + duration_23_minutes
        date_time_op_2_dek1_new = 'вр вск dek для апп №2'
        date_time_op_2_dek2_new = 'вр вск dek для апп №2'
        date_time_erase_1_dek12_new = date_time_seal_1_dek12_new + duration_1_minutes

        # даты и время для NSD
        date_time_op_nsd_new = date_time_del_spo12 + duration_6_minutes
        date_time_in_nsd_new = date_time_op_nsd_new + duration_1_minutes
        date_time_erase_nsd_new = date_time_in_nsd_new + duration_14_minutes
        date_time_cl_nsd_new = date_time_erase_nsd_new + duration_1_minutes

        # даты и время для CKT
        # набор очередного ключа
        if type_work == 'ОН':
            if n == 1:
                date_time_ckt = date_time_begin + duration_20_minutes # вскрытие футляра ckt
            # if n == 2:
            #     dict_out_technical['date_time_op_cap_input_2_device'] = date_time_begin # вскрытие крышки ввод 2-го аппарата
            # if n == quantity_device:
            #     dict_out_technical['date_time_op_cap_input_n_device'] = date_time_begin # вскрытие крышки ввод n-го аппарата
            else:
                date_time_ckt = date_time_begin + duration_1_minutes
            extract_date_time_ckt = date_time_ckt + duration_1_minutes
            input_date_time_ckt = date_time_ckt + duration_2_minutes
            seal_date_time_ckt = date_time_ckt + duration_4_minutes
            # Время уничтожения ключей, блокнотов и упаковок
            if n == 1:
                del_date_time = date_time_begin + duration_25_minutes + datetime.timedelta(minutes=quantity_device*25) # уничтожение ключей и таблиц блокнотов
            date_time_ckt_new = date_time_begin + duration_1_h_14_m
            extract_date_time_ckt_new = date_time_ckt_new + duration_1_minutes
            input_date_time_ckt_new = date_time_ckt_new + duration_2_minutes
            seal_date_time_ckt_new = date_time_ckt_new + duration_4_minutes
        else:
            date_time_ckt = date_time_begin + duration_52_minutes
            extract_date_time_ckt = date_time_ckt + duration_1_minutes
            input_date_time_ckt = date_time_ckt + duration_2_minutes
            seal_date_time_ckt = date_time_ckt + duration_4_minutes
            date_time_ckt_new = date_time_begin + duration_1_h_14_m
            extract_date_time_ckt_new = date_time_ckt_new + duration_1_minutes
            input_date_time_ckt_new = date_time_ckt_new + duration_2_minutes
            seal_date_time_ckt_new = date_time_ckt_new + duration_4_minutes
            # Время уничтожения ключей, блокнотов и упаковок
            del_date_time = date_time_begin + duration_14_h_30_m

        # даты и время для RDT
        # набор очередного ключа
        if type_work == 'ОН':
            if n == 1:
                date_time_del_rdt_old = date_time_begin + duration_30_minutes # сброс старого rdt
                date_time_op_rdt1 = date_time_begin + duration_26_minutes     # вскрытие нового rdt
            else:
                date_time_del_rdt_old = date_time_begin + duration_11_minutes
                date_time_op_rdt1 = date_time_begin + duration_7_minutes

            date_time_op_rdt2 = date_time_op_rdt1 + duration_1_minutes
            date_time_in_rdt2 = date_time_op_rdt2 + duration_1_minutes
            date_time_erase_rdt1 = date_time_in_rdt2 + duration_6_minutes
            date_time_erase_rdt2 = date_time_erase_rdt1 + duration_5_minutes
            date_time_cl_rdt1 = date_time_erase_rdt1 + duration_1_minutes
            date_time_cl_rdt2 = date_time_erase_rdt2 + duration_1_minutes
            # Опечатывание крышки ввод аппарата
            date_time_cl_cap_input = date_time_cl_rdt2 + duration_2_minutes
        else:
            date_time_del_rdt_old = date_time_begin + duration_50_minutes
            date_time_op_rdt1 = date_time_del_rdt_old + duration_1_h_14_m
            date_time_op_rdt2 = date_time_op_rdt1 + duration_1_minutes
            date_time_in_rdt2 = date_time_op_rdt2 + duration_1_minutes
            date_time_erase_rdt1 = date_time_in_rdt2 + duration_6_minutes
            date_time_erase_rdt2 = date_time_erase_rdt1 + duration_5_minutes
            date_time_cl_rdt1 = date_time_erase_rdt1 + duration_1_minutes
            date_time_cl_rdt2 = date_time_erase_rdt2 + duration_1_minutes
            # Опечатывание крышки ввод аппарата
            date_time_cl_cap_input = date_time_begin + duration_2_h_19_m

        # даты и время для technical_jornal
        if n == 1:
            date_time_op_MUVK = date_time_begin - duration_2_minutes  # вскрытие фуляра МУВК
            date_time_op_cap_input_1_device = date_time_begin # вскрытие крышки ввод 1-го аппарата
            date_time_op_CUV_1 = date_time_begin + duration_2_minutes  # вскрытие упаковки ЦУВ-1
            date_time_op_CUV_2 = date_time_op_CUV_1 + duration_2_minutes  # вскрытие упаковки ЦУВ-2
            date_time_check_CPO_MUVK_b = date_time_op_CUV_2 + duration_2_minutes  # проверка ЦПО МУВК начало
            date_time_check_CPO_MUVK_e = date_time_check_CPO_MUVK_b + duration_4_minutes  # проверка ЦПО МУВК конец
            date_time_erase_CUV_1_b = date_time_check_CPO_MUVK_e + duration_1_minutes  # стирание ЦУВ-1 начало
            date_time_erase_CUV_1_e = date_time_erase_CUV_1_b + duration_5_minutes  # стирание ЦУВ-1 конец
            date_time_cl_CUV_1 = date_time_erase_CUV_1_e + duration_2_minutes  # опечатывание ЦУВ-1
            date_time_cl_CUV_2 = date_time_cl_CUV_1 + duration_1_minutes  # опечатывание ЦУВ-2
            date_time_CPO_INPUT_b = input_date_time_ckt  # проверка ЦПО аппаратов, ввод ключей
            date_time_CPO_INPUT_e = date_time_in_rdt2  # проверка ЦПО аппаратов, ввод ключей
            date_time_erase_RDT_b = date_time_erase_rdt1  # стирание RDT1 начало
            date_time_erase_RDT_e = date_time_erase_rdt2  # стирание RDT2 конец
            date_time_cl_cap_input_b = date_time_cl_cap_input  # опечатывание крышки ввод аппарата №1
            date_time_cl_cap_input_e = date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
            date_time_cl_MUVK = date_time_cl_cap_input + duration_3_minutes  # опечатывание МУВК
            # если аппарат только один
            date_time_op_cap_input_2_device = date_time_begin # вскрытие крышки ввод 2-го аппарата
        if n == 2:
            date_time_op_cap_input_2_device = date_time_begin # вскрытие крышки ввод 2-го аппарата
        if n == quantity_device:
            date_time_op_cap_input_n_device = date_time_begin  # вскрытие крышки ввод n-го аппарата
            date_time_CPO_INPUT_e = date_time_in_rdt2  # проверка ЦПО аппаратов, ввод ключей
            date_time_erase_RDT_e = date_time_erase_rdt2  # стирание RDT2 конец
            date_time_cl_cap_input_e = date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
            date_time_cl_MUVK = date_time_cl_cap_input + duration_3_minutes  # опечатывание МУВК
        # if n == 1:
        #     date_time_erase_RDT_b = date_time_erase_rdt1  # стирание RDT1 начало
        # if n == 1:
        #     date_time_erase_RDT_e = date_time_erase_rdt2  # стирание RDT2 конец
        # elif n == quantity_device:
        #     date_time_erase_RDT_e = date_time_erase_rdt2  # стирание RDT2 конец
        # if n == 1:
        #     date_time_cl_cap_input_b = date_time_cl_cap_input  # опечатывание крышки ввод аппарата №1
        # if n == 1:
        #     date_time_cl_cap_input_e = date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
        #     date_time_cl_MUVK = date_time_cl_cap_input + duration_3_minutes  # опечатывание МУВК
        # elif n == quantity_device:
        #     date_time_cl_cap_input_e = date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
        #     date_time_cl_MUVK = date_time_cl_cap_input + duration_3_minutes  # опечатывание МУВК
        date_time_op_box_CUV_2 = del_date_time - duration_2_minutes  # вскрытие пенала ЦУВ-2
        date_time_del_CUV_2 = del_date_time  # уничтожение ЦУВ-2
        date_time_erase_RDT_old_b = 'дата время начала стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        date_time_erase_RDT_old_e = 'дата время окончания стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        date_time_cl_cap_input_dev1 = date_time_cl_cap_input  # опечатывания разъёма ввод аппарата после стирания RDT

        # номера аппаратов и печати
        # через командную строку

        number_device = '428M-00' + input('Введите номер аппарата М-567М: ')
        list_number_device.append(number_device)
        str_number_device = str(list_number_device)
        str_number_device = str_number_device[1:len(str_number_device) - 1]
        if n == 1:
            number_device_first = number_device
            number_MUVK = '№' + input('Введите номер МУВК: ')
            FIO_1part = input('Введите ФИО 1-й части: ')
            FIO_2part = input('Введите ФИО 2-й части: ')
            FIO_chief = input('Введите ФИО начальника (ответственного за вскрытие упаковок): ')
            FIO_carry_KD = input('Введите ФИО ответственного за обращение с ключами: ')
            stamp_numer_one_old_MUVK = input('Введите номер старой печати №1 столбик, которой опечатан МУВК: ')
            stamp_numer_two_old_MUVK = input('Введите номер старой печати №2 столбик, которой опечатан МУВК: ')
        print('Крышка "Ввод" аппаратуры опечатана печатями')
        stamp_numer_one_old = input('Введите номер старой печати №1 столбик: ')
        stamp_numer_two_old = input('Введите номер старой печати №2 столбик: ')
        print('Пенал с КД ЦК-Т-1054 опеатан печатью')
        stamp_numer_one_r_ckt_old = '№' + input('Введите номер старой печати №1 круглая: ')
        if n == 1:
            stamp_numer_one = input('Введите номер новой печати №1 столбик: ')
            stamp_numer_two = input('Введите номер новой печати №2 столбик: ')
            stamp_numer_one_r = '№' + input('Введите номер новой печати №1 круглая: ')
            stamp_numer_two_r = '№' + input('Введите номер новой печати №2 круглая: ')
        # number_device_last_in_spo = '№апп.М567М был введён SPO'
        # stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
        # stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
        # тестовые данные
        # number_device = '№апп.М567М'1676
        number_device_last_in_spo = '№апп.М567М был введён SPO'
        # stamp_numer_one_old = 'п.ст.№1старая'
        # stamp_numer_two_old = 'п.ст.№2старая'
        # stamp_numer_one = 'п.ст.№1'
        # stamp_numer_two = 'п.ст.№2'
        # stamp_numer_one_r = 'п.кр.№1'
        # stamp_numer_two_r = 'п.кр.№2'
        # stamp_numer_one_r_ckt_old = 'п.кр.№1 ckt_old'
        stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
        stamp_numer_two_spo_last = 'п.кр.№2 spo_last'

        # номера и серии ключей
        # CUV
        if n == 1:
            ser_number_CUV_1_2 = input('Введите номер серии ЦУВ-1,2: ')
            fac_number_CUV_1 = 'зав. №' + input('Введите заводской номер ЦУВ-1: ')
        # CKT
        # cmd
        ser_number_ckt_old = input('Введите номер ckt старый: ')
        number_tape_ckt_old = input('Введите номер ленты ckt старый: ')
        # ser_number_ckt_new = '№' + input('Введите номер ckt новый: ') + ', э.ед.'
        # number_tape_ckt_new = input('Введите номер ленты ckt новый: ')
        # test
        # ser_number_ckt_old = 'номер ckt старый'
        # number_tape_ckt_old = 'номер ленты ckt старый'
        ser_number_ckt_new = 'номер ckt новый'
        number_tape_ckt_new = 'номер ленты ckt новый'

        # DEK
        ser_number_dek_old_1 = '1-номер dek старый'
        number_com_dek_old_1 = '1-номер компл dek старый'
        fac_number_dek_old_1 = '1-зав. № dek старый'
        ser_number_dek_old_2 = '2-номер dek старый'
        number_com_dek_old_2 = '2-номер компл dek старый'
        fac_number_dek_old_2 = '2-зав. № dek старый'
        ser_number_dek_new_1 = '1-номер dek новый'
        number_com_dek_new_1 = '1-номер компл dek новый'
        fac_number_dek_new_1 = '1-зав. № dek новый'
        ser_number_dek_new_2 = '2-номер dek новый'
        number_com_dek_new_2 = '2-номер компл dek новый'
        fac_number_dek_new_2 = '2-зав. № dek новый'
        # SPO
        ser_number_comp_spo1 = '1-номер и комп spo1'
        fac_number_spo1 = '1-зав. № spo1'
        ser_number_comp_spo2 = '2-номер и комп spo2'
        fac_number_spo2 = '2-зав. № spo2'
        # NSD
        ser_number_nsd = 'номер серии nsd'
        fac_number_nsd = 'зав. № nsd'
        ser_number_nsd_new = 'номер серии nsd_new'
        fac_number_nsd_new = 'зав. № nsd_new'
        # RDT
        # старые
        # cmd
        if n == 1:
            ser_number_rdt_1_old = '№' + input('Введите номер старой серии rdt: ') + ', з.017'
            number_key_rdt_old = input('Введите номер ключа старой серии rdt: ')
        number_com_rdt_1_old = "№" + input(f"Введите номер старого комплекта rdt для аппарата №"
                                           f"{number_device}: ") + ", кл." + number_key_rdt_old + ", э.ед."
        fac_number_rdt_1_old = 'зав. №' + input(f'Введите заводской номер старого rdt1 для аппарата {number_device}: ')
        ser_number_rdt_2_old = ser_number_rdt_1_old
        number_com_rdt_2_old = number_com_rdt_1_old
        fac_number_rdt_2_old = 'зав. №' + input(f'Введите заводской номер старого rdt2 для аппарата {number_device}: ')
        if n == 1:
            ser_number_rdt_1 = '№' + input('Введите номер новой серии rdt: ') + ', з.0' +\
                               input('Введите номер зоны новой серии rdt: ')
            number_key_rdt = input('Введите номер ключа новой серии rdt: ')
        number_com_rdt_1 = "№" + input(f"Введите номер нового комплекта rdt для аппарата №"
                                       f"{number_device}: ") + ", кл." + number_key_rdt + ", э.ед."
        fac_number_rdt_1 = 'зав. №' + input(f'Введите заводской номер нового rdt1 для аппарата {number_device}: ')
        ser_number_rdt_2 = ser_number_rdt_1
        number_com_rdt_2 = number_com_rdt_1
        fac_number_rdt_2 = 'зав. №' + input(f'Введите заводской номер нового rdt2 для аппарата {number_device}: ')
        # test
        # ser_number_rdt_1_old = '1- сер номер rdt, з.№ старая'
        # number_com_rdt_1_old = '1-номер компл rdt старая'
        # fac_number_rdt_1_old = '1-зав. № rdt старая'
        # ser_number_rdt_2_old = '2- сер номер rdt, з.№ старая'
        # number_com_rdt_2_old = '2-номер компл rdt старая'
        # fac_number_rdt_2_old = '2-зав. № rdt старая'
        # новые
        # ser_number_rdt_1 = '1- сер номер rdt, з.№'
        # number_com_rdt_1 = '1-номер компл rdt'
        # fac_number_rdt_1 = '1-зав. № rdt'
        # ser_number_rdt_2 = '2- сер номер rdt, з.№'
        # number_com_rdt_2 = '2-номер компл rdt'
        # fac_number_rdt_2 = '2-зав. № rdt'

        # объединнённые печати
        stamp_numer_common_old = stamp_numer_one_old + ', ' + stamp_numer_two_old
        if n == 1:
            stamp_numer_common_old_first = stamp_numer_common_old
        list_number_stamp.append(stamp_numer_common_old)
        str_number_stamp = str(list_number_stamp)
        str_number_stamp = str_number_stamp[1:len(str_number_stamp) - 1]
        stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two
        stamp_numer_common_old_MUVK = stamp_numer_one_old_MUVK + ', ' + stamp_numer_two_old_MUVK

        ''' Формирование журнала DEK '''
        # # Запись о вкрытие старого DEK
        # list_out_dek = create_write_dek_1(read_file_jornal('dek'))1676
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Вскрытие старого DEK')
        # # Запись о стирание старого DEK
        # list_out_dek = create_write_dek_2(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Стирание старого DEK')
        # # Запись о первом вводе нового DEK
        # list_out_dek = create_write_dek_3_new(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Ввод №1 нового DEK')
        # # Запись о втором вводе нового DEK
        # list_out_dek = create_write_dek_4_new(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Ввод №2 нового DEK')

        ''' Формирование журнала RDT '''
        # Запись о сбросе старого RDT
        list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_rdt, 'rdt', 'Сброс старого RDT')
        # Запись о вводе RDT
        list_out_rdt = create_write_rdt_2(read_file_jornal('rdt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_rdt, 'rdt', 'Ввод нового RDT')

        ''' Формирование журнала CKT '''
        # Запись о проверке старым CKT
        list_out_ckt = create_write_ckt_old(read_file_jornal('ckt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_ckt, 'ckt', 'Проверка старым CKT')
        # Запись о проверке новым CKT
        # list_out_ckt = create_write_ckt_new(read_file_jornal('ckt'))
        # pprint.pprint(list_out_rdt, depth=12, width=144)
        # write_file_dek(list_out_ckt, 'ckt', 'Проверка новым CKT')

        '''Форимрование журнала SPO'''
        # # Запись о вскрытие старого SPO
        # list_out_nsd_spo = create_write_spo_1(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Вскрытие старого СПО')
        # # Запись о сбросе введённого ранее SPO
        # list_out_nsd_spo = create_write_spo_2(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс введённого ранее СПО')
        # # Запись о сбросе введённого ранее NSD
        # list_out_nsd_spo = create_write_nsd_1(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс введённого ранее НСД')
        # # Запись о вводе нового NSD
        # list_out_nsd_spo = create_write_nsd_2(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод нового НСД')
        # # Запись о вводе №1 SPO
        # list_out_nsd_spo = create_write_spo_3(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №1 СПО')
        # # Запись о вводе №1 SPO
        # list_out_nsd_spo = create_write_spo_4(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №2 СПО')

        '''Форимрование технического журнала'''
        # Записи в технический журнал
        if n == quantity_device:
            list_in_technical = read_file_jornal('technical')
            # print(list_in_technical)
            dict_out_technical = create_dict_tech(list_in_technical)
        # if n == quantity_device:
        #     dict_out_technical = create_dict_tech(list_in_technical)
            list_out_technical = create_write_technical(list_in_technical, dict_out_technical, 'ОН')
            pprint.pprint(list_out_technical, depth=12, width=144)
            write_file_dek(list_out_technical, 'technical', 'Технический журнал')

        print(f'Вы набрали {n} аппарат.')
        n += 1
        if n <= quantity_device:
            point_exit = input('Продолжить набор аппаратов (да/нет): ')
