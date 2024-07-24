'''Файл для создания журналов при работе с аппаратурой М567М'''


# импорт внешних пакетов
import datetime, pprint

# импорт собственных классов
from classes_for_jornal import DataJornal, JornalDEK, JornalRDT, JornalNSD_SPO, JornalCKT, TechnicalJornal

# рабочий сценарий
"""
Образцы записей в журналы.
Данные используемые в журналах.
Формирование данных для передачи в функции записи журналов.
"""

type_work = input('Введите вид работ ("ТО", "ОН", "Сб"): ') # выбор типа работ с аппаратурой
quantity_device = int(input('Сколько аппаратов вы используете: ')) # количество вводимых аппаратов
type_dt = input('Хотите ввести время начала работ(да/нет): ')


"""
Код запуска процессов формирования записей производимых при данных работах.
"""

point_exit = 'да'
n = 1 # счётчик циклов набора аппаратов

while n <= quantity_device:
    if point_exit == 'нет':
        break
    else:
        # дата и время начала работ
        date_time_begin = datetime.datetime.now()

        year = date_time_begin.year
        # print(year, type(year))
        month = date_time_begin.month
        # print(month, type(month))
        day = date_time_begin.day
        # print(day, type(day))
        hour = date_time_begin.hour
        # print(hour, type(hour))
        minute = date_time_begin.minute
        # print(minute, type(minute))
        second = date_time_begin.second
        # print(second, type(second))

        if type_dt == 'да':
            hour = int(input('Введите время начала работ- часы: '))
            minute = int(input('-минуты: '))
            # print(hour, type(hour))
            # print(minute, type(minute))
        date_time_begin = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute,
                                                 second=second)  # время начала работ
        # номера аппаратов, печати, ФИО участников
        if type_work == 'ОН':
            list_number_device = []
            # через командную строку
            number_device = '428M-00' + input('Введите номер аппарата М-567М: ')
            list_number_device.append(number_device)
            str_number_device = str(list_number_device)
            str_number_device = str_number_device[1:len(str_number_device) - 1]
            number_MUVK = input('Введите номер МУВК: ')
            FIO_1part = input('Введите ФИО 1-й части: ')
            FIO_2part = input('Введите ФИО 2-й части: ')
            FIO_chief = input('Введите ФИО начальника (ответственного за вскрытие упаковок): ')
            FIO_carry_KD = input('Введите ФИО ответственного за обращение с ключами: ')
            stamp_numer_one_old_MUVK = input('Введите номер старой печати №1 столбик, которой опечатан МУВК: ')
            stamp_numer_two_old_MUVK = input('Введите номер старой печати №2 столбик, которой опечатан МУВК: ')
            stamp_numer_one_old = input('Введите номер старой печати №1 столбик: ')
            stamp_numer_two_old = input('Введите номер старой печати №2 столбик: ')
            stamp_numer_one = input('Введите номер новой печати №1 столбик: ')
            stamp_numer_two = input('Введите номер новой печати №2 столбик: ')
            stamp_numer_one_r_ckt_old = '№' + input('Введите номер старой печати №1 круглая: ')
            stamp_numer_one_r = '№' + input('Введите номер новой печати №1 круглая: ')
            stamp_numer_two_r = '№' + input('Введите номер новой печати №2 круглая: ')
            number_device_last_in_spo = '№апп.М567М был введён SPO'
            stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
        # elif self.type_work == 'тест':
        else:
            # тестовые данные
            list_number_device = []
            last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'
            stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
            number_device = '№апп.М567М'
            list_number_device.append(number_device)
            str_number_device = str(list_number_device)
            str_number_device = str_number_device[1:len(str_number_device) - 1]
            number_MUVK = 'номер МУВК'
            FIO_1part = 'ФИО 1-й части'
            FIO_2part = 'ФИО 2-й части'
            FIO_chief = 'ФИО начальника (ответственного за вскрытие упаковок)'
            FIO_carry_KD = 'ФИО ответственного за обращение с ключами'
            stamp_numer_one_old_MUVK = 'номер ст. печати №1 столбик МУВК'
            stamp_numer_two_old_MUVK = 'номер ст. печати №2 столбик МУВК'
            number_device_last_in_spo = '№апп.М567М был введён SPO'
            stamp_numer_one_old = 'п.ст.№1старая'
            stamp_numer_two_old = 'п.ст.№2старая'
            stamp_numer_one = 'п.ст.№1'
            stamp_numer_two = 'п.ст.№2'
            stamp_numer_one_r = 'п.кр.№1'
            stamp_numer_two_r = 'п.кр.№2'
            stamp_numer_one_r_ckt_old = 'п.кр.№1 ckt_old'
            stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
            stamp_numer_one_old_MUVK = 'п.ст.№1 MUVK'
            stamp_numer_two_old_MUVK = 'п.ст.№2 MUVK'
        # data_1 = DataJornal(type_dt=type_dt, type_work=type_work)  # создание объекта данных для журналов М567М
        # print(data_1.type_work)
        # print(data_1.type_dt)
        # print(data_1.date_time_begin)
        ''' Формирование журнала RDT '''
        # Журнал RDT сброс
        data_2 = JornalRDT(type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r) # создание объекта данных для журнала RDT М567М
        print(data_2.read_file_jornal('rdt'))
        list_out_rdt = data_2.create_write_rdt_1()
        pprint.pprint(list_out_rdt, depth=12, width=144)
        data_2.write_file_dek(list_out_rdt, 'rdt', 'Запись о сбросе ранее введённого RDT')
        # Журнал RDT ввод
        list_out_rdt = data_2.create_write_rdt_2()
        pprint.pprint(list_out_rdt, depth=12, width=144)
        data_2.write_file_dek(list_out_rdt, 'rdt', 'Запись о вводе RDT в аппарат')
        ''' Формирование журнала CKT '''
        # Журнал CKT проверка перед вводом
        data_3 = JornalCKT(type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r)
        print(data_3.read_file_jornal('ckt'))
        list_out_ckt = data_3.create_write_ckt_old()
        pprint.pprint(list_out_ckt, depth=12, width=144)
        data_3.write_file_dek(list_out_ckt, 'ckt', 'Запись о проверке старым CKT')
        ''' Формирование технического журнала '''
        # Технический журнал для очередного набора ключей
        data_4 = TechnicalJornal(type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r)
        print(data_4.read_file_jornal('technical'))
        list_out_technical = data_4.create_write_technical()
        pprint.pprint(list_out_technical, depth=12, width=144)
        data_4.write_file_dek(list_out_technical, 'technical', 'Запись техническом журнале')

    print(f'Вы набрали {n} аппарат.')
    n += 1
    if n <= quantity_device:
        point_exit = input('Продолжить набор аппаратов (да/нет): ')

