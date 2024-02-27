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
            if i == 1 and j == 2:
                list_out_rdt[i][j] = number_device
            elif i == 1 and j == 3:
                list_out_rdt[i][j] = date_time_begin.strftime('%d.%m.%Y')
            elif i == 2 and j == 3:
                list_out_rdt[i][j] = date_time_begin.strftime('%H:%M')
            elif i == 2 and j == 3:
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

"""
Образцы записей в журналы.
Данные используемые в журналах.
Формирование данных для передачи в функции записи журналов.
"""

type_work = input('Введите вид работ ("ТО", "ОН", "Сб"): ')

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'

# Приращения времени
duration_1_minutes = datetime.timedelta(minutes=1)
duration_2_minutes = datetime.timedelta(minutes=2)
duration_3_minutes = datetime.timedelta(minutes=3)
duration_4_minutes = datetime.timedelta(minutes=4)
duration_5_minutes = datetime.timedelta(minutes=5)
duration_6_minutes = datetime.timedelta(minutes=6)
duration_14_minutes = datetime.timedelta(minutes=14)
duration_20_minutes = datetime.timedelta(minutes=20)
duration_23_minutes = datetime.timedelta(minutes=23)
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

point_exit = 'y'
n = 1
date_time_cl_cap_input = datetime.datetime.now()
while True:
    if point_exit == 'n':
        break
    else:
        if n > 1:
            date_time_begin = date_time_cl_cap_input + duration_3_minutes
        else:
            date_time_begin = datetime.datetime.now()
        # получаем значения года, месяца, дня, часа, минут, секунд
        print(date_time_begin)
        if n == 1:
            type_dt = input('Хотите ввести время начала работ(y/n): ')
            if type_dt == 'y':
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
                hour = int(input('Введите время начала работ: '))
                minute = int(input('-'))
                # print(hour, type(hour))
                date_time_begin = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
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
            date_time_ckt = date_time_begin + duration_20_minutes
            extract_date_time_ckt = date_time_ckt + duration_1_minutes
            input_date_time_ckt = date_time_ckt + duration_2_minutes
            seal_date_time_ckt = date_time_ckt + duration_4_minutes
            # Время уничтожения ключей, блокнотов и упаковок
            if n == 1:
                del_date_time = date_time_begin + duration_4_hours
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
            date_time_del_rdt_old = date_time_begin + duration_30_minutes
            date_time_op_rdt1 = date_time_begin + duration_26_minutes
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

        # номера аппаратов и печати
        # через командную строку

        number_device = '428M-00' + input('Введите номер аппарата М-567М: ')
        # number_device_last_in_spo = '№апп.М567М был введён SPO'
        stamp_numer_one_old = input('Введите номер старой печати №1 столбик: ')
        stamp_numer_two_old = input('Введите номер старой печати №2 столбик: ')
        stamp_numer_one = input('Введите номер новой печати №1 столбик: ')
        stamp_numer_two = input('Введите номер новой печати №2 столбик: ')
        stamp_numer_one_r_ckt_old = '№' + input('Введите номер старой печати №1 круглая: ')
        stamp_numer_one_r = '№' + input('Введите номер новой печати №1 круглая: ')
        stamp_numer_two_r = '№' + input('Введите номер новой печати №2 круглая: ')
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
        ser_number_rdt_1_old = '№' + input('Введите номер старой серии rdt: ') + ', з.017'
        number_com_rdt_1_old = '№' + input('Введите номер старого комплекта rdt: ') + ', кл.3, э.ед.'
        fac_number_rdt_1_old = 'зав. №' + input('Введите заводской номер старого rdt1: ')
        ser_number_rdt_2_old = ser_number_rdt_1_old
        number_com_rdt_2_old = number_com_rdt_1_old
        fac_number_rdt_2_old = 'зав. №' + input('Введите заводской номер старого rdt2: ')
        ser_number_rdt_1 = '№' + input('Введите номер новой серии rdt: ') + ', з.017'
        number_com_rdt_1 = '№' + input('Введите номер нового комплекта rdt: ') + ', кл.3, э.ед.'
        fac_number_rdt_1 = 'зав. №' + input('Введите заводской номер нового rdt1: ')
        ser_number_rdt_2 = ser_number_rdt_1
        number_com_rdt_2 = number_com_rdt_1
        fac_number_rdt_2 = 'зав. №' + input('Введите заводской номер нового rdt2: ')
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
        stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two

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

        print(f'Вы набрали {n} аппарат.')
        n += 1

        point_exit = input('Продолжить ввод (y/n): ')
