'''
Создадим классы для работы с журналами
'''

# импорт внешних пакетов
import datetime, pprint

class DataJornal:

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

    def __init__(self, type_dt='', type_work='тест'):
        """ Конструктор класса DataJornal"""
        self.type_dt = type_dt  # аттрибут ввода начала работ
        # self.duration_38_minutes = datetime.timedelta(minutes=38)
        # дата и время начала работ
        date_time_begin = datetime.datetime.now()
        # type_dt = input('Хотите ввести время начала работ(да/нет): ')

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
        date_time_begin = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

        self.date_time_begin = date_time_begin

        # номера аппаратов, печати, ФИО участников
        if type_work == 'ОН':
            self.list_number_device = []
            # через командную строку
            self.number_device = '428M-00' + input('Введите номер аппарата М-567М: ')
            self.list_number_device.append(self.number_device)
            self.str_number_device = str(self.list_number_device)
            self.str_number_device = self.str_number_device[1:len(self.str_number_device) - 1]
            self.number_MUVK = '№' + input('Введите номер МУВК: ')
            self.FIO_1part = input('Введите ФИО 1-й части: ')
            self.FIO_2part = input('Введите ФИО 2-й части: ')
            self.FIO_chief = input('Введите ФИО начальника (ответственного за вскрытие упаковок): ')
            self.FIO_carry_KD = input('Введите ФИО ответственного за обращение с ключами: ')
            self.stamp_numer_one_old_MUVK = input('Введите номер старой печати №1 столбик, которой опечатан МУВК: ')
            self.stamp_numer_two_old_MUVK = input('Введите номер старой печати №2 столбик, которой опечатан МУВК: ')
            self.stamp_numer_one_old = input('Введите номер старой печати №1 столбик: ')
            self.stamp_numer_two_old = input('Введите номер старой печати №2 столбик: ')
            self.stamp_numer_one = input('Введите номер новой печати №1 столбик: ')
            self.stamp_numer_two = input('Введите номер новой печати №2 столбик: ')
            self.stamp_numer_one_r_ckt_old = '№' + input('Введите номер старой печати №1 круглая: ')
            self.stamp_numer_one_r = '№' + input('Введите номер новой печати №1 круглая: ')
            self.stamp_numer_two_r = '№' + input('Введите номер новой печати №2 круглая: ')
            self.number_device_last_in_spo = '№апп.М567М был введён SPO'
            self.stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            self.stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
        elif type_work == 'тест':
            # тестовые данные
            self.last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'
            self.stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            self.stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
            self.number_device = '№апп.М567М'
            self.number_device_last_in_spo = '№апп.М567М был введён SPO'
            self.stamp_numer_one_old = 'п.ст.№1старая'
            self.stamp_numer_two_old = 'п.ст.№2старая'
            self.stamp_numer_one = 'п.ст.№1'
            self.stamp_numer_two = 'п.ст.№2'
            self.stamp_numer_one_r = 'п.кр.№1'
            self.stamp_numer_two_r = 'п.кр.№2'
            self.stamp_numer_one_r_ckt_old = 'п.кр.№1 ckt_old'
            self.stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
            self.stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
            self.stamp_numer_one_old_MUVK = 'п.ст.№1 MUVK'
            self.stamp_numer_two_old_MUVK = 'п.ст.№2 MUVK'
        # объединнённые печати
        self.stamp_numer_common_old = self.stamp_numer_one_old + ', ' + self.stamp_numer_two_old
        self.stamp_numer_common = self.stamp_numer_one + ', ' + self.stamp_numer_two
        self.stamp_numer_common_old_MUVK = self.stamp_numer_one_old_MUVK + ', ' + self.stamp_numer_two_old_MUVK

        print(f'Создан новый объект DataJornal тип работ - {type_work}, с временем начала работ: {self.date_time_begin}')


class JornalRDT(DataJornal):

    def __init__(self, date_time_begin=datetime.datetime.now(), type_work='тест'):
        """ Конструктор класса JornalDEK"""
        super().__init__()

        # даты и время для RDT
        # набор очередного ключа
        if type_work == 'ОН':
            self.date_time_del_rdt_old = self.date_time_begin + self.duration_30_minutes
            self.date_time_op_rdt1 = self.date_time_begin + self.duration_26_minutes
            self.date_time_op_rdt2 = self.date_time_op_rdt1 + self.duration_1_minutes
            self.date_time_in_rdt2 = self.date_time_op_rdt2 + self.duration_1_minutes
            self.date_time_erase_rdt1 = self.date_time_in_rdt2 + self.duration_6_minutes
            self.date_time_erase_rdt2 = self.date_time_erase_rdt1 + self.duration_5_minutes
            self.date_time_cl_rdt1 = self.date_time_erase_rdt1 + self.duration_1_minutes
            self.date_time_cl_rdt2 = self.date_time_erase_rdt2 + self.duration_1_minutes
            # Опечатывание крышки ввод аппарата
            self.date_time_cl_cap_input = self.date_time_cl_rdt2 + self.duration_2_minutes
        else:
            self.date_time_del_rdt_old = self.date_time_begin + self.duration_50_minutes
            self.date_time_op_rdt1 = self.date_time_del_rdt_old + self.duration_1_h_14_m
            self.date_time_op_rdt2 = self.date_time_op_rdt1 + self.duration_1_minutes
            self.date_time_in_rdt2 = self.date_time_op_rdt2 + self.duration_1_minutes
            self.date_time_erase_rdt1 = self.date_time_in_rdt2 + self.duration_6_minutes
            self.date_time_erase_rdt2 = self.date_time_erase_rdt1 + self.duration_5_minutes
            self.date_time_cl_rdt1 = self.date_time_erase_rdt1 + self.duration_1_minutes
            self.date_time_cl_rdt2 = self.date_time_erase_rdt2 + self.duration_1_minutes
            # Опечатывание крышки ввод аппарата
            self.date_time_cl_cap_input = self.date_time_begin + self.duration_2_h_19_m

class JornalDEK(JornalRDT):

    # печати и номера ключей
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

    def __init__(self, date_time_begin=datetime.datetime.now(), type_work='тест'):
        """ Конструктор класса JornalDEK"""
        super().__init__()
        self.date_time_begin = date_time_begin
        # переменные журнала DEK
        # даты и время для DEK
        self.date_time_op_dek1_old = self.date_time_begin + self.duration_38_minutes
        self.date_time_op_dek2_old = self.date_time_op_dek1_old + self.duration_2_minutes
        self.date_time_del_dek1_old = self.date_time_op_dek2_old + self.duration_3_minutes
        self.date_time_del_dek2_old = self.date_time_del_dek1_old + self.duration_5_minutes
        self.date_time_cl_dek1_old = self.date_time_del_dek1_old + self.duration_1_minutes
        self.date_time_cl_dek2_old = self.date_time_del_dek2_old + self.duration_1_minutes
        self.date_time_op_dek1_new = self.date_time_begin + self.duration_58_minutes
        self.date_time_op_dek2_new = self.date_time_op_dek1_new + self.duration_1_minutes
        self.date_time_in_dek2_new = self.date_time_op_dek2_new + self.duration_1_minutes
        self.date_time_erase_dek1_new = self.date_time_in_dek2_new + self.duration_2_minutes


    def read_file_jornal(self, type_f=''):
        ''' Функция чтения данных из файла журнала DEK '''

        # if type_f == 'dek':
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

    def write_file_dek(self, list_out_dek, type_f=None, type_w='Неизвестная'):
        '''Функция записи журнала DEK в файл'''

        list_out_new = []

        for row in list_out_dek:
            row.append('\n')
            # print(row)
            list_out_new.append(';'.join(row))

        with open(f'jornal_out_{type_f}.csv', 'a+', encoding='cp1251') as fw:
            for _ in list_out_new:
                fw.writelines(_)

        return print(f'Сделанна запись "{type_w}", данные записаны в файл jornal_out_{type_f}.csv')


    '''Функции для формирования журнала DEK'''
    def create_write_dek_1(self):
        '''Функция формирования записи вскрытия в последний раз опечатанного DEK'''

        list_out_dek = self.read_file_jornal('dek')

        for i, row in enumerate(list_out_dek):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_old_1
                elif i == 3 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_old_1
                elif i == 4 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_old_1
                elif i == 6 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_old_2
                elif i == 7 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_old_2
                elif i == 8 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_old_2
                elif i == 1 and j == 2:
                    list_out_dek[i][j] = self.last_device_input_dek
                elif i == 1 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_dek1_old.strftime('%d.%m.%Y')
                elif i == 2 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_dek1_old.strftime('%H:%M')
                elif i == 3 and j == 8:
                    list_out_dek[i][j] = self.stamp_numer_one_r
                elif i == 5 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_dek2_old.strftime('%d.%m.%Y')
                elif i == 6 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_dek2_old.strftime('%H:%M')
                elif i == 7 and j == 8:
                    list_out_dek[i][j] = self.stamp_numer_two_r
                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                    list_out_dek[i][j] = ''  # str(i) + ',' + str(j)

        return list_out_dek

    def create_write_dek_2(self):
        # Цикл для формирования записи стирания старого DEK

        list_out_dek = self.read_file_jornal('dek')

        for i, row in enumerate(list_out_dek):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_old_1
                elif i == 3 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_old_1
                elif i == 4 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_old_1
                elif i == 6 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_old_2
                elif i == 7 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_old_2
                elif i == 8 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_old_2
                elif i == 1 and j == 2:
                    list_out_dek[i][j] = self.number_device
                elif i == 1 and j == 3:
                    list_out_dek[i][j] = self.date_time_begin.strftime('%d.%m.%Y')
                elif i == 2 and j == 3:
                    list_out_dek[i][j] = self.date_time_begin.strftime('%H:%M')
                elif i == 3 and j == 3:
                    list_out_dek[i][j] = self.stamp_numer_common
                elif i == 5 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('%d.%m.%Y')
                elif i == 6 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('%H:%M')
                elif i == 7 and j == 6:
                    list_out_dek[i][j] = self.stamp_numer_common
                elif i == 2 and j == 10:
                    list_out_dek[i][j] = self.date_time_del_dek1_old.strftime('%d.%m.%Y')
                elif i == 3 and j == 10:
                    list_out_dek[i][j] = self.date_time_del_dek1_old.strftime('%H:%M')
                elif i == 6 and j == 10:
                    list_out_dek[i][j] = self.date_time_del_dek2_old.strftime('%d.%m.%Y')
                elif i == 7 and j == 10:
                    list_out_dek[i][j] = self.date_time_del_dek2_old.strftime('%H:%M')
                elif i == 1 and j == 11:
                    list_out_dek[i][j] = self.date_time_cl_dek1_old.strftime('%d.%m.%Y')
                elif i == 2 and j == 11:
                    list_out_dek[i][j] = self.date_time_cl_dek1_old.strftime('%H:%M')
                elif i == 3 and j == 11:
                    list_out_dek[i][j] = self.stamp_numer_one_r
                elif i == 5 and j == 11:
                    list_out_dek[i][j] = self.date_time_cl_dek2_old.strftime('%d.%m.%Y')
                elif i == 6 and j == 11:
                    list_out_dek[i][j] = self.date_time_cl_dek2_old.strftime('%H:%M')
                elif i == 7 and j == 11:
                    list_out_dek[i][j] = self.stamp_numer_two_r
                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 4, 5, 7, 8, 9]:
                    list_out_dek[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_dek[i][j] = ''

        list_out_dek[0][0] = 'Запись о стирание старого DEK'

        # del list_out_dek[0]

        return list_out_dek
    #
    # def create_write_dek_3_new(list_out_dek):
    #     # Цикл для формирования записи ввода №1 нового DEK
    #     for i, row in enumerate(list_out_dek):
    #         # print(row)
    #         for j, cell in enumerate(row):
    #             # print(cell)
    #             if i == 2 and j == 0:
    #                 list_out_dek[i][j] = ser_number_dek_new_1
    #             elif i == 3 and j == 0:
    #                 list_out_dek[i][j] = number_com_dek_new_1
    #             elif i == 4 and j == 0:
    #                 list_out_dek[i][j] = fac_number_dek_new_1
    #             elif i == 6 and j == 0:
    #                 list_out_dek[i][j] = ser_number_dek_new_2
    #             elif i == 7 and j == 0:
    #                 list_out_dek[i][j] = number_com_dek_new_2
    #             elif i == 8 and j == 0:
    #                 list_out_dek[i][j] = fac_number_dek_new_2
    #             elif i == 1 and j == 1:
    #                 list_out_dek[i][j] = date_time_op_dek1_new.strftime('D-%d.%m.%Y')
    #             elif i == 2 and j == 1:
    #                 list_out_dek[i][j] = date_time_op_dek1_new.strftime('T-%H:%M')
    #             elif i == 5 and j == 1:
    #                 list_out_dek[i][j] = date_time_op_dek2_new.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 1:
    #                 list_out_dek[i][j] = date_time_op_dek2_new.strftime('T-%H:%M')
    #             elif i == 1 and j == 2:
    #                 list_out_dek[i][j] = number_device
    #             elif i == 1 and j == 3:
    #                 list_out_dek[i][j] = date_time_begin.strftime('D-%d.%m.%Y')
    #             elif i == 2 and j == 3:
    #                 list_out_dek[i][j] = date_time_begin.strftime('T-%H:%M')
    #             elif i == 3 and j == 3:
    #                 list_out_dek[i][j] = stamp_numer_common_old
    #             elif i == 1 and j == 4:
    #                 list_out_dek[i][j] = date_time_op_dek2_new.strftime('D-%d.%m.%Y')
    #             elif i == 2 and j == 4:
    #                 list_out_dek[i][j] = date_time_op_dek2_new.strftime('T-%H:%M')
    #             elif i == 5 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_dek2_new.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_dek2_new.strftime('T-%H:%M')
    #             elif i == 5 and j == 6:
    #                 list_out_dek[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 6:
    #                 list_out_dek[i][j] = date_time_cl_cap_input.strftime('T-%H:%M')
    #             elif i == 2 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
    #             elif i == 3 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_dek1_new.strftime('T-%H:%M')
    #             elif i == 6 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
    #             elif i == 7 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_dek1_new.strftime('T-%H:%M')
    #
    #             elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [5, 7, 8, 10, 11]:
    #                 list_out_dek[i][j] = str(i) + ',' + str(j)  # ''
    #             elif i == 0:
    #                 list_out_dek[i][j] = ''
    #
    #     list_out_dek[0][0] = 'Запись о вводе №1 DEK в аппарат'
    #
    #     # del list_out_dek[0]
    #
    #     return list_out_dek
    #
    # def create_write_dek_4_new(list_out_dek):
    #     # Цикл для формирования записи ввода №2 нового DEK
    #     for i, row in enumerate(list_out_dek):
    #         # print(row)
    #         for j, cell in enumerate(row):
    #             # print(cell)
    #             if i == 2 and j == 0:
    #                 list_out_dek[i][j] = ser_number_dek_new_1
    #             elif i == 3 and j == 0:
    #                 list_out_dek[i][j] = number_com_dek_new_1
    #             elif i == 4 and j == 0:
    #                 list_out_dek[i][j] = fac_number_dek_new_1
    #             elif i == 6 and j == 0:
    #                 list_out_dek[i][j] = ser_number_dek_new_2
    #             elif i == 7 and j == 0:
    #                 list_out_dek[i][j] = number_com_dek_new_2
    #             elif i == 8 and j == 0:
    #                 list_out_dek[i][j] = fac_number_dek_new_2
    #             elif i == 1 and j == 2:
    #                 list_out_dek[i][j] = number_device
    #             elif i == 1 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_1_dek1_new.strftime('D-%d.%m.%Y')
    #             elif i == 2 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_1_dek1_new.strftime('T-%H:%M')
    #             elif i == 5 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_1_dek2_new.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 4:
    #                 list_out_dek[i][j] = date_time_in_1_dek2_new.strftime('T-%H:%M')
    #             elif i == 5 and j == 6:
    #                 list_out_dek[i][j] = date_time_cl_cap_input.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 6:
    #                 list_out_dek[i][j] = date_time_cl_cap_input.strftime('T-%H:%M')
    #             elif i == 1 and j == 7:
    #                 list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
    #             elif i == 2 and j == 7:
    #                 list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('T-%H:%M')
    #             elif i == 3 and j == 7:
    #                 list_out_dek[i][j] = stamp_numer_one_r
    #             elif i == 5 and j == 7:
    #                 list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
    #             elif i == 6 and j == 7:
    #                 list_out_dek[i][j] = date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
    #             elif i == 7 and j == 7:
    #                 list_out_dek[i][j] = stamp_numer_two_r
    #             elif i == 1 and j == 8:
    #                 list_out_dek[i][j] = date_time_op_2_dek1_new
    #             elif i == 2 and j == 8:
    #                 list_out_dek[i][j] = date_time_op_2_dek1_new
    #             elif i == 3 and j == 8:
    #                 list_out_dek[i][j] = stamp_numer_one_r
    #             elif i == 5 and j == 8:
    #                 list_out_dek[i][j] = date_time_op_2_dek2_new
    #             elif i == 6 and j == 8:
    #                 list_out_dek[i][j] = date_time_op_2_dek2_new
    #             elif i == 7 and j == 8:
    #                 list_out_dek[i][j] = stamp_numer_two_r
    #             elif i == 2 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
    #             elif i == 3 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('T-%H:%M')
    #             elif i == 6 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
    #             elif i == 7 and j == 9:
    #                 list_out_dek[i][j] = date_time_erase_1_dek12_new.strftime('T-%H:%M')
    #
    #             elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 5, 10, 11]:
    #                 list_out_dek[i][j] = str(i) + ',' + str(j)  # ''
    #             elif i == 0:
    #                 list_out_dek[i][j] = ''
    #
    #     list_out_dek[0][0] = 'Запись о вводе №2 DEK в аппарат'
    #
    #     return list_out_dek



if __name__ == '__main__':

    # data_1 = DataJornal('да')
    # data_2 = DataJornal()
    # print(data_2.duration_1_h_02_m)
    # print(type(data_2.duration_1_h_02_m))
    # data_3 = JornalDEK(DataJornal('да').date_time_begin)
    data_4 = JornalDEK()
    # print(data_3.date_time_begin.strftime('%H:%M'))
    # print(data_3.date_time_op_dek1_old)
    # print(data_3.date_time_op_dek2_old)
    # print(data_4.date_time_erase_dek1_new)
    print(data_4.read_file_jornal('dek'))
    list_out_dek = data_4.create_write_dek_1()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Вскрытие DEK')
    list_out_dek = data_4.create_write_dek_2()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Стирание DEK')