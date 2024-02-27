"""
Образцы записей в журналы.
Данные используемые в журналах.
Формирование данных для передачи в функции записи журналов.
"""
# импорт внешних пакетов
import datetime, pprint
# импорт встроенных модулей
# from read_write_file import read_file_jornal


'''Функции считывания и ввода данных'''
def read_file_date_input(type_f=''):
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

    if type_f == 'rdt_old':
        list_in_rdt_old_rdt = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                str = str_.strip().split(";")
                for _ in str:
                    _ = _.encode('utf-8')
                list_in_rdt_old_rdt.append(str)

        return list_in_rdt_old_rdt

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

def create_date_rdt_old(list_in_rdt_old):
    # Цикл для формирования данных старого rdt
    for i, row in enumerate(list_in_rdt_old):
        # print(row)
        for j, cell in enumerate(row):
            # print(cell)
            # серии и номера rdt
            if i == 2 and j == 0:
                ser_number_rdt_1_old = list_in_rdt_old[i][j]
            elif i == 3 and j == 0:
                number_com_rdt_1_old = list_in_rdt_old[i][j]
            elif i == 4 and j == 0:
                fac_number_rdt_1_old = list_in_rdt_old[i][j]
            elif i == 6 and j == 0:
                ser_number_rdt_2_old = list_in_rdt_old[i][j]
            elif i == 7 and j == 0:
                number_com_rdt_2_old = list_in_rdt_old[i][j]
            elif i == 8 and j == 0:
                fac_number_rdt_2_old = list_in_rdt_old[i][j]
            # номер аппарата
            elif i == 1 and j == 2:
                number_device = list_in_rdt_old[i][j]
            # крышка ввод опечатана (столбик)
            elif i == 7 and j == 6:
                stamp_numer_common_old = list_in_rdt_old[i][j]

    return ser_number_rdt_1_old, number_com_rdt_1_old, fac_number_rdt_1_old, ser_number_rdt_2_old, number_com_rdt_2_old,\
           fac_number_rdt_2_old, number_device, stamp_numer_common_old

type_work = input('Введите вид работ ("ТО", "ОН", "Сб"): ')

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'

# Переменные даты и времени
date_time_now = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
# время начала работ (вскрытие крышки ввод)
date_time_begin = datetime.datetime.now()
date_now = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_now = datetime.datetime.now().strftime('Time - %H:%M')
# получаем значения года, месяца, дня, часа, минут, секунд
print(date_time_begin)
year = date_time_begin.strftime('%Y')
# print(year, type(year))
month = date_time_begin.strftime('%m')
# print(month, type(month))
day = date_time_begin.strftime('%d')
# print(day, type(day))
hour = date_time_begin.strftime('%H')
# print(hour, type(hour))
minute = date_time_begin.strftime('%M')
# print(minute, type(minute))
second = date_time_begin.strftime('%S')
# print(second, type(second))

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

# получаем данные необходимые для выполнения работ
# ввод ключей в аппарат
# list_in_rdt_old = read_file_date_input('rdt_old') # список данных по старым ключам rdt
# pprint.pprint(list_in_rdt_old, depth=12, width=144)
# print(create_date_rdt_old(list_in_rdt_old))
# print(create_date_rdt_old(list_in_rdt_old)[6])
# print(create_date_rdt_old(list_in_rdt_old)[7].split(' ')[0])

if __name__ == '__main__':
    '''Функции считывания и ввода данных'''
    # print(date_time_begin)
    # date_time_24_02_23_10_00 = datetime.datetime(year=2024, month=2, day=23, hour=10, minute=00, second=00)
    # # print(date_time_24_02_23_10_00, type(date_time_24_02_23_10_00))
    # date_time_begin = date_time_24_02_23_10_00
    # print(date_time_begin)
    # hour = int(input('Введите время начала работ: '))
    # date_time_24_02_23_hour_00 = datetime.datetime(year=2024, month=2, day=23, hour=hour, minute=00, second=00)
    # print(date_time_24_02_23_hour_00)
    # получаем значения года, месяца, дня, часа, минут, секунд
    # print(date_time_begin)
    # year = date_time_begin.strftime('%Y')
    # print(year, type(year))
    # month = date_time_begin.strftime('%m')
    # print(month, type(month))
    # day = date_time_begin.strftime('%d')
    # print(day, type(day))
    # hour = date_time_begin.strftime('%H')
    # print(hour, type(hour))
    # minute = date_time_begin.strftime('%M')
    # print(minute, type(minute))
    # second = date_time_begin.strftime('%S')
    # print(second, type(second))
