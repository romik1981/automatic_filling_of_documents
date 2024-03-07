"""
Функции необходимые для записи журналов и чтения данных.
"""

# from Test import result_10_min

# импорт номеров аппаратов
from data_jornal import last_device_input_dek, number_device, number_device_last_in_spo

# импорт номеров и серий ключей
from data_jornal import ser_number_rdt_1_old, number_com_rdt_1_old, fac_number_rdt_1_old, ser_number_rdt_2_old,\
    number_com_rdt_2_old, fac_number_rdt_2_old,\
    number_tape_ckt_old, ser_number_ckt_old, ser_number_ckt_new, number_tape_ckt_new,\
    ser_number_dek_old_1, number_com_dek_old_1, fac_number_dek_old_1, ser_number_dek_old_2, number_com_dek_old_2, \
    fac_number_dek_old_2, \
    ser_number_dek_new_1, number_com_dek_new_1, fac_number_dek_new_1, \
    ser_number_dek_new_2, number_com_dek_new_2, fac_number_dek_new_2, ser_number_comp_spo1, ser_number_comp_spo2, \
    fac_number_spo1, \
    fac_number_spo2, ser_number_nsd, fac_number_nsd, ser_number_nsd_new, fac_number_nsd_new,\
    ser_number_rdt_1, number_com_rdt_1, fac_number_rdt_1, ser_number_rdt_2, number_com_rdt_2, fac_number_rdt_2

# импорт печатей
from data_jornal import stamp_numer_common, stamp_numer_one_r, stamp_numer_two_r, stamp_numer_one_r_ckt_old, \
    stamp_numer_common_old, \
    stamp_numer_one_spo_last, stamp_numer_two_spo_last

# импорт переменных даты и времени
from data_jornal import date_now, time_now, date_time_ckt, extract_date_time_ckt, \
    input_date_time_ckt, date_time_ckt_new, extract_date_time_ckt_new, input_date_time_ckt_new, seal_date_time_ckt_new,\
    seal_date_time_ckt, del_date_time, date_time_op_dek1_old, date_time_op_dek2_old, date_time_del_dek1_old, date_time_del_dek2_old,\
    date_time_cl_dek1_old, date_time_cl_dek2_old, date_time_op_dek1_new, \
    date_time_op_dek2_new, date_time_begin, \
    date_time_in_dek2_new, date_time_in_1_dek1_new, date_time_in_1_dek2_new, date_time_seal_1_dek12_new, date_time_op_2_dek1_new,\
    date_time_op_2_dek2_new, date_time_erase_1_dek12_new,\
    date_time_cl_cap_input, date_time_erase_dek1_new, date_time_op_spo1, date_time_op_spo2, date_time_del_spo12,\
    date_time_in_2_spo1, date_time_in_2_spo2, date_time_cl_2_spo2, date_time_op_1_spo1, date_time_op_1_spo2,\
    date_time_in_1_spo1, date_time_del_1_spo12, date_time_in_1_spo2, date_time_op_nsd_new, date_time_in_nsd_new,\
    date_time_erase_nsd_new, date_time_cl_nsd_new, date_time_del_rdt_old, date_time_op_rdt1, date_time_op_rdt2, \
    date_time_in_rdt2, date_time_erase_rdt1, date_time_erase_rdt2, date_time_cl_rdt1, date_time_cl_rdt2, date_time_op_MUVK,\
    date_time_op_CUV_1, date_time_op_CUV_2, date_time_check_CPO_MUVK_b, date_time_check_CPO_MUVK_e, date_time_erase_CUV_1_b,\
    date_time_erase_CUV_1_e, date_time_cl_CUV_1, date_time_cl_CUV_2, date_time_CPO_INPUT_b, date_time_CPO_INPUT_e,\
    date_time_erase_RDT_b, date_time_erase_RDT_e, date_time_cl_cap_input_b, date_time_cl_cap_input_e, date_time_cl_MUVK,\
    date_time_op_box_CUV_2, date_time_del_CUV_2, date_time_erase_RDT_old_b, date_time_erase_RDT_old_e, date_time_cl_cap_input_dev1


import pprint
import datetime

# Глобальные переменные файла
list_out_dek = []
list_out_rdt = []
list_out_ckt = []
list_out_nsd_spo = []
list_out_technical = []
dict_out_technical = {}

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
        list_out_nsd_spo = []

        with open(f'{type_f}_jornal_M567M.csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                str = str_.strip().split(";")
                for _ in str:
                    _ = _.encode('utf-8')
                list_out_technical.append(str)

        return list_out_technical

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

def create_dict_tech(list_out_technical):

    dict_out_technical = {
        # заголовки технического журнала
        'title': list_out_technical[0],
        # записи о вскрытии контейнера с МУВК
        'date_time_op_MUVK': date_time_op_MUVK,
        'write_open_kontainer': list_out_technical[1][1],
        'catatan_ON_begin': list_out_technical[1][8],
        'FIO_1part': list_out_technical[2][6], # ФИО 1 часть
        'FIO_lukisan_1part': list_out_technical[2][7], # подпись 1 часть
        # записи о вскрытии 1 аппарата
        'date_time_op_cap_input_1_device': date_time_begin,
        'write_open_cap_input_1_device': list_out_technical[3][1],
        'write_open_cap_input_devices': list_out_technical[5][1],
        # записи о проверке ЦПО МУВК
        'date_time_op_CUV_1': date_time_op_CUV_1,
        'write_open_CUV_1': list_out_technical[7][1],
        'date_time_op_CUV_2': date_time_op_CUV_2,
        'FIO_2part': list_out_technical[10][6], # ФИО 2 часть
        'FIO_lukisan_2part': list_out_technical[10][7], # подпись 2 часть
        'date_time_check_open': date_time_op_CUV_2, # дата проверки вскрытия
        'write_check_open': list_out_technical[11][1], # проверка вскрытия
        'FIO_chief': list_out_technical[2][6],  # ФИО начальник
        'FIO_lukisan_chief': list_out_technical[2][7], # подпись начальник
        'date_time_check_CPO_MUVK_b': date_time_check_CPO_MUVK_b, # проверка ЦПО МУВК начало
        'date_time_check_CPO_MUVK_e': date_time_check_CPO_MUVK_e, # проверка ЦПО МУВК конец
        'write_check_CPO_MUVK': list_out_technical[13][1], # проверка ЦПО МУВК
        'date_time_erase_CUV_1_b': date_time_erase_CUV_1_b, # стирание ЦУВ-1 начало
        'date_time_erase_CUV_1_e': date_time_erase_CUV_1_e, # стирание ЦУВ-1 конец
        'write_erase_CUV_1': list_out_technical[16][1], # стирание ЦУВ-1
        'date_time_cl_CUV_1': date_time_cl_CUV_1, # опечатывание ЦУВ-1
        'write_cl_CUV_1': list_out_technical[18][1], # опечатывание ЦУВ-1
        'date_time_cl_CUV_2': date_time_cl_CUV_2, # опечатывание ЦУВ-2
        'write_cl_CUV_2': list_out_technical[20][1], # опечатывание ЦУВ-2
        'date_time_CPO_INPUT_b': date_time_CPO_INPUT_b, # проверка ЦПО аппаратов, ввод ключей
        'date_time_CPO_INPUT_e': date_time_CPO_INPUT_e, # проверка ЦПО аппаратов, ввод ключей
        'write_CPO_INPUT': list_out_technical[22][1], # проверка ЦПО аппаратов, ввод ключей
        'date_time_erase_RDT_b': date_time_erase_RDT_b, # стирание RDT
        'date_time_erase_RDT_e': date_time_erase_RDT_e, # стирание RDT
        'write_erase_RDT': list_out_technical[25][1], # стирание RDT
        'date_time_cl_cap_input_b': date_time_cl_cap_input_b, # опечатывание крышки ввод аппарата №1
        'date_time_cl_cap_input_e': date_time_cl_cap_input_e, # опечатывание крышки ввод последнего аппарата
        'write_cl_cap_input': list_out_technical[28][1], # опечатывание крышки ввод последнего аппарата
        'date_time_cl_MUVK': date_time_cl_MUVK, # опечатывание МУВК
        'write_cl_MUVK': list_out_technical[31][1], # опечатывание МУВК
        'date_time_op_box_CUV_2': date_time_op_box_CUV_2, # вскрытие пенала ЦУВ-2
        'write_op_box_CUV_2': list_out_technical[34][1], # вскрытие пенала ЦУВ-2
        'date_time_del_CUV_2': date_time_del_CUV_2, # уничтожение ЦУВ-2
        'write_del_CUV_2': list_out_technical[36][1], # уничтожение ЦУВ-2
        'date_time_use_KD': date_time_del_CUV_2, # дата проверки правильности обращения с КД
        'write_use_KD': list_out_technical[39][1], # уничтожение ЦУВ-2
        'FIO_carry_KD': list_out_technical[39][6],  # ФИО ответственный за КД
        'lukisan_carry_KD': list_out_technical[39][7],  # подпись ответственный за КД
        'date_time_erase_RDT_old_b': date_time_erase_RDT_old_b, # начало стирания выведенных из обращения RDT
        'date_time_erase_RDT_old_e': date_time_erase_RDT_old_e, # конец стирания выведенных из обращения RDT
        'write_erase_RDT_old': list_out_technical[44][1], # стирание выведенных из обращения RDT
        'date_time_cl_cap_input_dev1': date_time_cl_cap_input_dev1, # опечатывания разъёма ввод аппарата после стирания RDT
        'write_cl_cap_input_dev1': list_out_technical[47][1], # опечатывания разъёма ввод аппарата после стирания RDT
    }

    return dict_out_technical


if __name__ == '__main__':
    # write_file_password(result_10_min, 'rdt')

    # print(list_out_dek[1][2])
    # last_device_input_dek.index(1, 2, last_device_input_dek)
    # list_out_dek[1][2] = last_device_input_dek
    # print(list_out_dek[1][2])

    # Разобрался можно спать, УРА!!!

    '''Собираем журнал DEK'''
    # # Запись о вкрытие старого DEK
    # list_out_dek = create_write_dek_1(read_file_jornal('dek'))
    # print(list_out_dek)
    # write_file_dek(list_out_dek, 'dek', 'Вскрытие старого DEK')
    # # Запись о стирание старого DEK
    # list_out_dek = create_write_dek_2(read_file_jornal('dek'))
    # print(list_out_dek)
    # write_file_dek(list_out_dek, 'dek', 'Стирание старого DEK')
    # # Запись о первом вводе нового DEK
    # list_out_dek = create_write_dek_3_new(read_file_jornal('dek'))
    # pprint.pprint(list_out_dek, depth=12, width=144)
    # write_file_dek(list_out_dek, 'dek')
    # # Запись о втором вводе нового DEK
    # list_out_dek = create_write_dek_4_new(read_file_jornal('dek'))
    # pprint.pprint(list_out_dek, depth=12, width=144)
    # write_file_dek(list_out_dek, 'dek', 'Ввод №2 нового DEK')

    '''Собираем журнал RDT'''
    # # Запись о сбросе RDT
    # list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
    # pprint.pprint(list_out_rdt, depth=12, width=144)
    # write_file_dek(list_out_rdt, 'rdt', 'Сброс старого RDT')
    # # Запись о вводе RDT
    # list_out_rdt = create_write_rdt_2(read_file_jornal('rdt'))
    # pprint.pprint(list_out_rdt, depth=12, width=144)
    # write_file_dek(list_out_rdt, 'rdt', 'Ввод нового RDT')

    '''Собираем журнал CKT'''
    # # Запись о проверке старым CKT
    # list_out_ckt = create_write_ckt_old(read_file_jornal('ckt'))
    # pprint.pprint(list_out_ckt, depth=12, width=144)
    # write_file_dek(list_out_ckt, 'ckt', 'Проверка старым CKT')
    # # Запись о проверке новым CKT
    # list_out_ckt = create_write_ckt_new(read_file_jornal('ckt'))
    # pprint.pprint(list_out_ckt, depth=12, width=144)
    # write_file_dek(list_out_ckt, 'ckt', 'Проверка новым CKT')

    '''Собираем журнал SPO'''
    # # Запись о вскрытие старого SPO
    # list_out_nsd_spo = create_write_spo_1(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Вскрытие СПО')
    # # Запись о сбросе введённого ранее SPO
    # list_out_nsd_spo = create_write_spo_2(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс ранее введённого СПО')
    # # Запись о сбросе введённого ранее NSD
    # list_out_nsd_spo = create_write_nsd_1(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс введённого раннее НСД')
    # # Запись о вводе нового NSD
    # list_out_nsd_spo = create_write_nsd_2(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод нового НСД')
    # # Запись о вводе №1 SPO
    # list_out_nsd_spo = create_write_spo_3(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №1 СПО')
    # # Запись о вводе №2 SPO
    # list_out_nsd_spo = create_write_spo_4(read_file_jornal('nsd_spo'))
    # print(list_out_nsd_spo)
    # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №2 СПО')
    # Записи в технический журнал
    list_out_technical = read_file_jornal('technical')
    pprint.pprint(list_out_technical, depth=12, width=144)
    pprint.pprint(create_dict_tech(list_out_technical), depth=12, width=144)
