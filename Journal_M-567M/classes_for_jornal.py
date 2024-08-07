'''Создадим классы для работы с журналами'''

# импорт внешних пакетов
import datetime, pprint

class DataJornal():

    def __init__(self, n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, del_date_time):
        """ Конструктор класса DataJornal"""

        self.type_dt = type_dt  # аттрибут ввода начала работ
        self.type_work = type_work
        self.date_time_begin = date_time_begin # время начала работ
        self.n = n # счётчик циклов набора
        self.quantity_device = quantity_device # количество аппаратов

        # Приращения времени
        self.duration_1_minutes = datetime.timedelta(minutes=1)
        self.duration_2_minutes = datetime.timedelta(minutes=2)
        self.duration_3_minutes = datetime.timedelta(minutes=3)
        self.duration_4_minutes = datetime.timedelta(minutes=4)
        self.duration_5_minutes = datetime.timedelta(minutes=5)
        self.duration_6_minutes = datetime.timedelta(minutes=6)
        self.duration_7_minutes = datetime.timedelta(minutes=7)
        self.duration_11_minutes = datetime.timedelta(minutes=11)
        self.duration_14_minutes = datetime.timedelta(minutes=14)
        self.duration_20_minutes = datetime.timedelta(minutes=20)
        self.duration_23_minutes = datetime.timedelta(minutes=23)
        self.duration_25_minutes = datetime.timedelta(minutes=25)
        self.duration_26_minutes = datetime.timedelta(minutes=26)
        self.duration_27_minutes = datetime.timedelta(minutes=27)
        self.duration_30_minutes = datetime.timedelta(minutes=30)
        self.duration_38_minutes = datetime.timedelta(minutes=38)
        self.duration_50_minutes = datetime.timedelta(minutes=50)
        self.duration_52_minutes = datetime.timedelta(minutes=52)
        self.duration_58_minutes = datetime.timedelta(minutes=58)
        self.duration_1_h_25_m = datetime.timedelta(hours=1, minutes=25)
        self.duration_1_h_14_m = datetime.timedelta(hours=1, minutes=14)
        self.duration_1_h_02_m = datetime.timedelta(hours=1, minutes=2)
        self.duration_2_h_19_m = datetime.timedelta(hours=2, minutes=19)
        self.duration_10_hours = datetime.timedelta(hours=10)
        self.duration_4_hours = datetime.timedelta(hours=4)
        self.duration_10_h_19_m = datetime.timedelta(hours=10, minutes=19)
        self.duration_14_hours = datetime.timedelta(hours=14)
        self.duration_14_h_30_m = datetime.timedelta(hours=14, minutes=30)

        # даты и время для SPO
        self.date_time_op_spo1 = self.date_time_begin + self.duration_1_h_25_m
        self.date_time_op_spo2 = self.date_time_op_spo1 + self.duration_1_minutes
        self.date_time_del_spo12 = self.date_time_begin + self.duration_1_h_02_m
        self.date_time_in_1_spo1 = self.date_time_op_spo2 + self.duration_2_minutes
        self.date_time_in_1_spo2 = self.date_time_in_1_spo1 + self.duration_2_minutes
        self.date_time_del_1_spo12 = self.date_time_in_1_spo2 + self.duration_27_minutes
        self.date_time_in_2_spo1 = self.date_time_del_1_spo12 + self.duration_3_minutes
        self.date_time_in_2_spo2 = self.date_time_in_2_spo1 + self.duration_2_minutes
        self.date_time_cl_2_spo2 = self.date_time_in_2_spo2 + self.duration_1_minutes
        self.date_time_op_1_spo1 = 'вр вск spo для апп №2'
        self.date_time_op_1_spo2 = 'вр вск spo для апп №2'
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
        # даты и время для DEK продолжение
        self.date_time_in_1_dek1_new = self.date_time_in_1_spo1 + self.duration_2_minutes
        self.date_time_in_1_dek2_new = self.date_time_in_1_dek1_new + self.duration_1_minutes
        self.date_time_seal_1_dek12_new = self.date_time_in_1_dek2_new + self.duration_23_minutes
        self.date_time_op_2_dek1_new = 'вр вск dek для апп №2'
        self.date_time_op_2_dek2_new = 'вр вск dek для апп №2'
        self.date_time_erase_1_dek12_new = self.date_time_seal_1_dek12_new + self.duration_1_minutes
        # даты и время для CKT
        # набор очередного ключа
        if self.type_work == 'ОН':
            if self.n == 1:
                self.date_time_ckt = date_time_begin + self.duration_20_minutes  # вскрытие футляра ckt
            else:
                self.date_time_ckt = date_time_begin + self.duration_1_minutes
            self.extract_date_time_ckt = self.date_time_ckt + self.duration_1_minutes
            self.input_date_time_ckt = self.date_time_ckt + self.duration_2_minutes
            self.seal_date_time_ckt = self.date_time_ckt + self.duration_4_minutes
            # Время уничтожения ключей, блокнотов и упаковок
            # if self.n == 1:
            #     self.del_date_time = self.date_time_begin + self.duration_25_minutes + datetime.timedelta(
            #         minutes=self.quantity_device * 25)  # уничтожение ключей и таблиц блокнотов
            self.del_date_time = del_date_time
            self.date_time_ckt_new = self.date_time_begin + self.duration_1_h_14_m
            self.extract_date_time_ckt_new = self.date_time_ckt_new + self.duration_1_minutes
            self.input_date_time_ckt_new = self.date_time_ckt_new + self.duration_2_minutes
            self.seal_date_time_ckt_new = self.date_time_ckt_new + self.duration_4_minutes
        else:
            self.date_time_ckt = self.date_time_begin + self.duration_52_minutes
            self.extract_date_time_ckt = self.date_time_ckt + self.duration_1_minutes
            self.input_date_time_ckt = self.date_time_ckt + self.duration_2_minutes
            self.seal_date_time_ckt = self.date_time_ckt + self.duration_4_minutes
            self.date_time_ckt_new = self.date_time_begin + self.duration_1_h_14_m
            self.extract_date_time_ckt_new = self.date_time_ckt_new + self.duration_1_minutes
            self.input_date_time_ckt_new = self.date_time_ckt_new + self.duration_2_minutes
            self.seal_date_time_ckt_new = self.date_time_ckt_new + self.duration_4_minutes
            # Время уничтожения ключей, блокнотов и упаковок
            self.del_date_time = self.date_time_begin + self.duration_14_h_30_m
        # даты и время для NSD
        self.date_time_op_nsd_new = self.date_time_del_spo12 + self.duration_6_minutes
        self.date_time_in_nsd_new = self.date_time_op_nsd_new + self.duration_1_minutes
        self.date_time_erase_nsd_new = self.date_time_in_nsd_new + self.duration_14_minutes
        self.date_time_cl_nsd_new = self.date_time_erase_nsd_new + self.duration_1_minutes
        # даты и время для RDT
        # набор очередного ключа
        if self.type_work == 'ОН':
            # работает для одного аппарата, разобраться с переменными для случая когда n > 1
            if n == 1:
                self.date_time_del_rdt_old = self.date_time_begin + self.duration_30_minutes  # сброс старого rdt
                self.date_time_op_rdt1 = self.date_time_begin + self.duration_26_minutes  # вскрытие нового rdt
            else:
                self.date_time_del_rdt_old = self.date_time_begin + self.duration_11_minutes
                self.date_time_op_rdt1 = self.date_time_begin + self.duration_7_minutes
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

        # даты и время для technical_jornal

        # self.date_time_op_MUVK = self.date_time_begin - self.duration_2_minutes  # вскрытие фуляра МУВК
        # self.date_time_op_CUV_1 = self.date_time_begin + self.duration_2_minutes  # вскрытие упаковки ЦУВ-1
        # self.date_time_op_CUV_2 = self.date_time_op_CUV_1 + self.duration_2_minutes  # вскрытие упаковки ЦУВ-2
        # self.date_time_check_CPO_MUVK_b = self.date_time_op_CUV_2 + self.duration_2_minutes  # проверка ЦПО МУВК начало
        # self.date_time_check_CPO_MUVK_e = self.date_time_op_CUV_2 + self.duration_4_minutes  # проверка ЦПО МУВК конец
        # self.date_time_erase_CUV_1_b = self.date_time_check_CPO_MUVK_e + self.duration_1_minutes  # стирание ЦУВ-1 начало
        # self.date_time_erase_CUV_1_e = self.date_time_check_CPO_MUVK_e + self.duration_1_minutes  # стирание ЦУВ-1 конец
        # self.date_time_cl_CUV_1 = self.date_time_erase_CUV_1_e + self.duration_2_minutes  # опечатывание ЦУВ-1
        # self.date_time_cl_CUV_2 = self.date_time_cl_CUV_1 + self.duration_1_minutes  # опечатывание ЦУВ-2
        # self.date_time_CPO_INPUT_b = self.input_date_time_ckt  # проверка ЦПО аппаратов, ввод ключей
        # self.date_time_CPO_INPUT_e = self.date_time_in_rdt2  # проверка ЦПО аппаратов, ввод ключей
        # self.date_time_erase_RDT_b = self.date_time_erase_rdt1  # стирание RDT
        # self.date_time_erase_RDT_e = self.date_time_erase_rdt2  # стирание RDT
        # self.date_time_cl_cap_input_b = self.date_time_cl_cap_input  # опечатывание крышки ввод аппарата №1
        # self.date_time_cl_cap_input_e = self.date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
        # self.date_time_cl_MUVK = self.date_time_cl_cap_input + self.duration_3_minutes  # опечатывание МУВК
        # self.date_time_op_box_CUV_2 = self.date_time_cl_MUVK + self.duration_2_minutes  # вскрытие пенала ЦУВ-2
        # self.date_time_del_CUV_2 = self.date_time_cl_CUV_2 + self.duration_3_minutes  # уничтожение ЦУВ-2
        # self.date_time_erase_RDT_old_b = 'дата время начала стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        # self.date_time_erase_RDT_old_e = 'дата время окончания стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        # self.date_time_cl_cap_input_dev1 = self.date_time_cl_cap_input  # опечатывания разъёма ввод аппарата после стирания RDT
        # доделать переменные и функции класса technical_jornal для набора нескольких аппаратов!!!
        if n == 1:
            self.date_time_op_MUVK = self.date_time_begin - self.duration_2_minutes  # вскрытие фуляра МУВК
            self.date_time_op_cap_input_1_device = self.date_time_begin # вскрытие крышки ввод 1-го аппарата
            self.date_time_op_CUV_1 = self.date_time_begin + self.duration_2_minutes  # вскрытие упаковки ЦУВ-1
            self.date_time_op_CUV_2 = self.date_time_op_CUV_1 + self.duration_2_minutes  # вскрытие упаковки ЦУВ-2
            self.date_time_check_CPO_MUVK_b = self.date_time_op_CUV_2 + self.duration_2_minutes  # проверка ЦПО МУВК начало
            self.date_time_check_CPO_MUVK_e = self.date_time_check_CPO_MUVK_b + self.duration_4_minutes  # проверка ЦПО МУВК конец
            self.date_time_erase_CUV_1_b = self.date_time_check_CPO_MUVK_e + self.duration_1_minutes  # стирание ЦУВ-1 начало
            self.date_time_erase_CUV_1_e = self.date_time_erase_CUV_1_b + self.duration_5_minutes  # стирание ЦУВ-1 конец
            self.date_time_cl_CUV_1 = self.date_time_erase_CUV_1_e + self.duration_2_minutes  # опечатывание ЦУВ-1
            self.date_time_cl_CUV_2 = self.date_time_cl_CUV_1 + self.duration_1_minutes  # опечатывание ЦУВ-2
            self.date_time_CPO_INPUT_b = self.input_date_time_ckt  # проверка ЦПО аппаратов, ввод ключей
            self.date_time_CPO_INPUT_e = self.date_time_in_rdt2  # проверка ЦПО аппаратов, ввод ключей
            self.date_time_erase_RDT_b = self.date_time_erase_rdt1  # стирание RDT1 начало
            self.date_time_erase_RDT_e = self.date_time_erase_rdt2  # стирание RDT2 конец
            self.date_time_cl_cap_input_b = self.date_time_cl_cap_input  # опечатывание крышки ввод аппарата №1
            self.date_time_cl_cap_input_e = self.date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
            self.date_time_cl_MUVK = self.date_time_cl_cap_input + self.duration_3_minutes  # опечатывание МУВК
            # если аппарат только один
            self.date_time_op_cap_input_2_device = self.date_time_begin # вскрытие крышки ввод 1-го аппарата
        if n == 2:
            self.date_time_op_cap_input_2_device = self.date_time_begin # вскрытие крышки ввод 2-го аппарата
        if n == quantity_device:
            self.date_time_op_cap_input_n_device = self.date_time_begin  # вскрытие крышки ввод n-го аппарата
            self.date_time_CPO_INPUT_e = self.date_time_in_rdt2  # проверка ЦПО аппаратов, ввод ключей
            self.date_time_erase_RDT_e = self.date_time_erase_rdt2  # стирание RDT2 конец
            self.date_time_cl_cap_input_e = self.date_time_cl_cap_input  # опечатывание крышки ввод последнего аппарата
            self.date_time_cl_MUVK = self.date_time_cl_cap_input + self.duration_3_minutes  # опечатывание МУВК
        self.date_time_op_box_CUV_2 = self.del_date_time - self.duration_2_minutes  # вскрытие пенала ЦУВ-2
        self.date_time_del_CUV_2 = self.del_date_time  # уничтожение ЦУВ-2
        self.date_time_erase_RDT_old_b = 'дата время начала стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        self.date_time_erase_RDT_old_e = 'дата время окончания стирания выведенных из обращения RDT'  # начало стирания выведенных из обращения RDT
        self.date_time_cl_cap_input_dev1 = self.date_time_cl_cap_input  # опечатывания разъёма ввод аппарата после стирания RDT

        # номера аппаратов
        self.number_device = number_device
        self.str_number_device = str_number_device
        # номер МУВК
        self.number_MUVK = number_MUVK
        # участники работ
        self.FIO_1part = FIO_1part
        self.FIO_2part = FIO_2part
        self.FIO_chief = FIO_chief
        self.FIO_carry_KD = FIO_carry_KD
        # печати
        self.stamp_numer_one_old = stamp_numer_one_old
        self.stamp_numer_two_old = stamp_numer_two_old
        self.stamp_numer_one = stamp_numer_one
        self.stamp_numer_two = stamp_numer_two
        self.stamp_numer_one_old_MUVK = stamp_numer_one_old_MUVK
        self.stamp_numer_two_old_MUVK = stamp_numer_two_old_MUVK
        self.stamp_numer_one_r_ckt_old = stamp_numer_one_r_ckt_old
        self.stamp_numer_one_r = stamp_numer_one_r
        self.stamp_numer_two_r = stamp_numer_two_r
        self.number_device_last_in_spo = '№апп.М567М был введён SPO'
        self.stamp_numer_one_spo_last = 'п.кр.№1 spo_last'
        self.stamp_numer_two_spo_last = 'п.кр.№2 spo_last'
        # объединнённые печати
        self.stamp_numer_common_old = self.stamp_numer_one_old + ', ' + self.stamp_numer_two_old
        self.stamp_numer_common = self.stamp_numer_one + ', ' + self.stamp_numer_two
        self.stamp_numer_common_old_MUVK = self.stamp_numer_one_old_MUVK + ', ' + self.stamp_numer_two_old_MUVK

        print(f'Создан новый объект DataJornal тип работ - {type_work}, с временем начала работ: {self.date_time_begin}')

    '''Функции чтения и записи данных в журналы'''
    def read_file_jornal(self, type_f=''):
        '''Функция чтения данных из файла журнала DEK'''

        # if type_f == 'dek':
        list_out_data = []

        with open(f'jornal_M567M({type_f}).csv', 'r', encoding='cp1251') as fr:
            for str_ in fr:
                # print(str_, type(str_), 'чтение DEK')
                str = str_.strip().split(";")
                # print(str, 'чтение DEK после разделения')
                for _ in str:
                    _ = _.encode('utf-8')
                # print(str, type(str), 'промежуточные данные декодирования')
                list_out_data.append(str)
            # print(list_out_dek)
        return list_out_data

    def write_file_dek(self, list_out_data, type_f=None, type_w='Неизвестная'):
        '''Функция записи журнала DEK в файл'''

        list_out_new = []

        for row in list_out_data:
            row.append('\n')
            # print(row)
            list_out_new.append(';'.join(row))

        with open(f'jornal_out_{type_f}.csv', 'a+', encoding='cp1251') as fw:
            for _ in list_out_new:
                fw.writelines(_)

        return print(f'Сделанна запись "{type_w}", данные записаны в файл jornal_out_{type_f}.csv')


class JornalRDT(DataJornal):

    def __init__(self, n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, ser_number_rdt_1_old, number_com_rdt_1_old, fac_number_rdt_1_old,
                           fac_number_rdt_2_old, ser_number_rdt_1, number_com_rdt_1, fac_number_rdt_1, fac_number_rdt_2, del_date_time):

        """ Конструктор класса JornalDEK"""

        super().__init__(n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, del_date_time)

        # RDT
        if self.type_work == 'ОН':
            # cmd
            # старые
            self.ser_number_rdt_1_old = ser_number_rdt_1_old
            self.number_com_rdt_1_old = number_com_rdt_1_old
            self.fac_number_rdt_1_old = fac_number_rdt_1_old
            self.ser_number_rdt_2_old = ser_number_rdt_1_old
            self.number_com_rdt_2_old = number_com_rdt_1_old
            self.fac_number_rdt_2_old = fac_number_rdt_2_old
            # новые
            self.ser_number_rdt_1 = ser_number_rdt_1
            self.number_com_rdt_1 = number_com_rdt_1
            self.fac_number_rdt_1 = fac_number_rdt_1
            self.ser_number_rdt_2 = ser_number_rdt_1
            self.number_com_rdt_2 = number_com_rdt_1
            self.fac_number_rdt_2 = fac_number_rdt_2
        else:
            # test
            # старые
            self.ser_number_rdt_1_old = '1- сер номер rdt, з.№ старая'
            self.number_com_rdt_1_old = '1-номер компл rdt старая'
            self.fac_number_rdt_1_old = '1-зав. № rdt старая'
            self.ser_number_rdt_2_old = '2- сер номер rdt, з.№ старая'
            self.number_com_rdt_2_old = '2-номер компл rdt старая'
            self.fac_number_rdt_2_old = '2-зав. № rdt старая'
            # новые
            self.ser_number_rdt_1 = '1- сер номер rdt, з.№'
            self.number_com_rdt_1 = '1-номер компл rdt'
            self.fac_number_rdt_1 = '1-зав. № rdt'
            self.ser_number_rdt_2 = '2- сер номер rdt, з.№'
            self.number_com_rdt_2 = '2-номер компл rdt'
            self.fac_number_rdt_2 = '2-зав. № rdt'

    '''Функции для формирования журнала RDT'''
    def create_write_rdt_1(self):
        """Цикл для формирования записи сброса ранее введённог RDT"""

        list_out_rdt = self.read_file_jornal('rdt')

        for i, row in enumerate(list_out_rdt):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_rdt[i][j] = self.ser_number_rdt_1_old
                elif i == 3 and j == 0:
                    list_out_rdt[i][j] = self.number_com_rdt_1_old
                elif i == 4 and j == 0:
                    list_out_rdt[i][j] = self.fac_number_rdt_1_old
                elif i == 6 and j == 0:
                    list_out_rdt[i][j] = self.ser_number_rdt_2_old
                elif i == 7 and j == 0:
                    list_out_rdt[i][j] = self.number_com_rdt_2_old
                elif i == 8 and j == 0:
                    list_out_rdt[i][j] = self.fac_number_rdt_2_old
                elif i == 1 and j == 2:
                    list_out_rdt[i][j] = self.number_device
                elif i == 3 and j == 2:
                    list_out_rdt[i][j] = self.number_MUVK
                elif i == 1 and j == 9:
                    list_out_rdt[i][j] = self.number_MUVK + ' v1012'
                elif i == 2 and j == 9:
                    list_out_rdt[i][j] = self.date_time_del_rdt_old.strftime('%d.%m.%Y')
                elif i == 3 and j == 9:
                    list_out_rdt[i][j] = self.date_time_del_rdt_old.strftime('%H:%M')
                elif i == 5 and j == 9:
                    list_out_rdt[i][j] = self.number_MUVK + ' v1012'
                elif i == 6 and j == 9:
                    list_out_rdt[i][j] = self.date_time_del_rdt_old.strftime('%d.%m.%Y')
                elif i == 7 and j == 9:
                    list_out_rdt[i][j] = self.date_time_del_rdt_old.strftime('%H:%M')

                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 4, 5, 6, 7, 8, 10, 11]:
                    list_out_rdt[i][j] = ''  # str(i) + ',' + str(j)

        return list_out_rdt

    def create_write_rdt_2(self):
        """Цикл для формирования записи ввода RDT"""

        list_out_rdt = self.read_file_jornal('rdt')

        for i, row in enumerate(list_out_rdt):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_rdt[i][j] = self.ser_number_rdt_1
                elif i == 3 and j == 0:
                    list_out_rdt[i][j] = self.number_com_rdt_1
                elif i == 4 and j == 0:
                    list_out_rdt[i][j] = self.fac_number_rdt_1
                elif i == 6 and j == 0:
                    list_out_rdt[i][j] = self.ser_number_rdt_2
                elif i == 7 and j == 0:
                    list_out_rdt[i][j] = self.number_com_rdt_2
                elif i == 8 and j == 0:
                    list_out_rdt[i][j] = self.fac_number_rdt_2
                elif i == 1 and j == 1:
                    list_out_rdt[i][j] = self.date_time_op_rdt1.strftime('%d.%m.%Y')
                elif i == 2 and j == 1:
                    list_out_rdt[i][j] = self.date_time_op_rdt1.strftime('%H:%M')
                elif i == 5 and j == 1:
                    list_out_rdt[i][j] = self.date_time_op_rdt2.strftime('%d.%m.%Y')
                elif i == 6 and j == 1:
                    list_out_rdt[i][j] = self.date_time_op_rdt2.strftime('%H:%M')
                elif i == 1 and j == 2:
                    list_out_rdt[i][j] = self.number_device
                elif i == 3 and j == 2:
                    list_out_rdt[i][j] = self.number_MUVK
                elif i == 1 and j == 3:
                    list_out_rdt[i][j] = self.date_time_begin.strftime('%d.%m.%Y')
                elif i == 2 and j == 3:
                    list_out_rdt[i][j] = self.date_time_begin.strftime('%H:%M')
                elif i == 3 and j == 3:
                    list_out_rdt[i][j] = self.stamp_numer_common_old
                elif i == 1 and j == 4:
                    list_out_rdt[i][j] = self.date_time_op_rdt2.strftime('%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_rdt[i][j] = self.date_time_op_rdt2.strftime('%H:%M')
                elif i == 5 and j == 4:
                    list_out_rdt[i][j] = self.date_time_in_rdt2.strftime('%d.%m.%Y')
                elif i == 6 and j == 4:
                    list_out_rdt[i][j] = self.date_time_in_rdt2.strftime('%H:%M')
                elif i == 5 and j == 6:
                    list_out_rdt[i][j] = self.date_time_cl_cap_input.strftime('%d.%m.%Y')
                elif i == 6 and j == 6:
                    list_out_rdt[i][j] = self.date_time_cl_cap_input.strftime('%H:%M')
                elif i == 7 and j == 6:
                    list_out_rdt[i][j] = self.stamp_numer_common
                elif i == 1 and j == 10:
                    list_out_rdt[i][j] = self.number_MUVK
                elif i == 2 and j == 10:
                    list_out_rdt[i][j] = self.date_time_erase_rdt1.strftime('%d.%m.%Y')
                elif i == 3 and j == 10:
                    list_out_rdt[i][j] = self.date_time_erase_rdt1.strftime('%H:%M')
                elif i == 5 and j == 10:
                    list_out_rdt[i][j] = self.number_MUVK
                elif i == 6 and j == 10:
                    list_out_rdt[i][j] = self.date_time_erase_rdt2.strftime('%d.%m.%Y')
                elif i == 7 and j == 10:
                    list_out_rdt[i][j] = self.date_time_erase_rdt2.strftime('%H:%M')
                elif i == 1 and j == 11:
                    list_out_rdt[i][j] = self.date_time_cl_rdt1.strftime('%d.%m.%Y')
                elif i == 2 and j == 11:
                    list_out_rdt[i][j] = self.date_time_cl_rdt1.strftime('%H:%M')
                elif i == 3 and j == 11:
                    list_out_rdt[i][j] = self.stamp_numer_one_r
                elif i == 5 and j == 11:
                    list_out_rdt[i][j] = self.date_time_cl_rdt2.strftime('%d.%m.%Y')
                elif i == 6 and j == 11:
                    list_out_rdt[i][j] = self.date_time_cl_rdt2.strftime('%H:%M')
                elif i == 7 and j == 11:
                    list_out_rdt[i][j] = self.stamp_numer_two_r

                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [5, 7, 8, 9]:
                    list_out_rdt[i][j] = ''  # str(i) + ',' + str(j)
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


class JornalNSD_SPO(DataJornal):

    def __init__(self):
        """Конструктор класса JornalSPO"""
        super().__init__()

        # номера ключей
        if self.type_work == 'ОН':
            # SPO
            self.ser_number_comp_spo1 = '1-номер и комп spo1'
            self.fac_number_spo1 = '1-зав. № spo1'
            self.ser_number_comp_spo2 = '2-номер и комп spo2'
            self.fac_number_spo2 = '2-зав. № spo2'
            # NSD
            self.ser_number_nsd = 'номер серии nsd'
            self.fac_number_nsd = 'зав. № nsd'
            self.ser_number_nsd_new = 'номер серии nsd_new'
            self.fac_number_nsd_new = 'зав. № nsd_new'
        else:
            # SPO
            self.ser_number_comp_spo1 = '1-номер и комп spo1'
            self.fac_number_spo1 = '1-зав. № spo1'
            self.ser_number_comp_spo2 = '2-номер и комп spo2'
            self.fac_number_spo2 = '2-зав. № spo2'
            # NSD
            self.ser_number_nsd = 'номер серии nsd'
            self.fac_number_nsd = 'зав. № nsd'
            self.ser_number_nsd_new = 'номер серии nsd_new'
            self.fac_number_nsd_new = 'зав. № nsd_new'

    '''Функции для формирования журнала NSD_SPO'''
    def create_write_spo_1(self):
        """Цикл для формирования записи вскрытия SPO"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]
        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo1
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo1
                elif i == 5 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo2
                elif i == 6 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo2
                elif i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device_last_in_spo
                elif i == 1 and j == 7:
                    list_out_nsd_spo[i][j] = self.date_time_op_spo1.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 7:
                    list_out_nsd_spo[i][j] = self.stamp_numer_one_spo_last
                elif i == 4 and j == 7:
                    list_out_nsd_spo[i][j] = self.date_time_op_spo2.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 7:
                    list_out_nsd_spo[i][j] = self.stamp_numer_two_spo_last

                elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 8, 9, 10, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)

        return list_out_nsd_spo

    def create_write_spo_2(self):
        """Цикл для формирования записи сброса SPO"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]

        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo1
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo1
                elif i == 5 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo2
                elif i == 6 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo2
                if i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device
                elif i == 2 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_spo12.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_spo12.strftime('%d.%m.%Y %H:%M')

                elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_nsd_spo[i][j] = ''

        list_out_nsd_spo[0][0] = 'Запись о  сбросе СПО в аппарате'

        # del list_out_nsd_spo[0]

        return list_out_nsd_spo

    def create_write_spo_3(self):
        """Цикл для формирования записи ввода №1 SPO"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]

        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo1
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo1
                elif i == 5 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo2
                elif i == 6 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo2
                if i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device
                elif i == 1 and j == 3:
                    list_out_nsd_spo[i][j] = self.date_time_begin.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 3:
                    list_out_nsd_spo[i][j] = self.stamp_numer_common_old
                elif i == 1 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_1_spo1.strftime('%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_1_spo1.strftime('%H:%M')
                elif i == 4 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_1_spo2.strftime('%d.%m.%Y')
                elif i == 5 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_1_spo2.strftime('%H:%M')
                elif i == 4 and j == 5:
                    list_out_nsd_spo[i][j] = self.date_time_cl_cap_input.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 5:
                    list_out_nsd_spo[i][j] = self.stamp_numer_common
                elif i == 2 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_1_spo12.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_1_spo12.strftime('%d.%m.%Y %H:%M')

                elif i in [1, 2, 3, 4, 5, 6] and j in [1, 6, 7, 9, 10, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_nsd_spo[i][j] = ''

        list_out_nsd_spo[0][0] = 'Запись о вводе №1 СПО в аппарат'

        return list_out_nsd_spo

    def create_write_spo_4(self):
        """Цикл для формирования записи ввода №2 SPO"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]
        del list_out_nsd_spo[1]

        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo1
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo1
                elif i == 5 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_comp_spo2
                elif i == 6 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_spo2
                if i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device
                elif i == 1 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_2_spo1.strftime('%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_2_spo1.strftime('%H:%M')
                elif i == 4 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_2_spo2.strftime('%d.%m.%Y')
                elif i == 5 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_2_spo2.strftime('%H:%M')
                elif i == 4 and j == 5:
                    list_out_nsd_spo[i][j] = self.date_time_cl_cap_input.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 5:
                    list_out_nsd_spo[i][j] = self.stamp_numer_common
                elif i == 1 and j == 6:
                    list_out_nsd_spo[i][j] = self.date_time_in_2_spo2.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 6:
                    list_out_nsd_spo[i][j] = self.stamp_numer_one_r
                elif i == 4 and j == 6:
                    list_out_nsd_spo[i][j] = self.date_time_cl_2_spo2.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 6:
                    list_out_nsd_spo[i][j] = self.stamp_numer_two_r
                elif i == 1 and j == 7:
                    list_out_nsd_spo[i][j] = self.date_time_op_1_spo1
                elif i == 2 and j == 7:
                    list_out_nsd_spo[i][j] = self.stamp_numer_one_r
                elif i == 4 and j == 7:
                    list_out_nsd_spo[i][j] = self.date_time_op_1_spo2
                elif i == 5 and j == 7:
                    list_out_nsd_spo[i][j] = self.stamp_numer_two_r

                elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 6, 7, 8, 9, 10, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_nsd_spo[i][j] = ''

        list_out_nsd_spo[0][0] = 'Запись о вводе №2 СПО в аппарат'

        return list_out_nsd_spo

    def create_write_nsd_1(self):
        """Цикл для формирования записи сброса NSD"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_nsd
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_nsd
                if i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device
                elif i == 2 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_spo12.strftime('%d.%m.%Y %H:%M')
                elif i == 5 and j == 8:
                    list_out_nsd_spo[i][j] = self.date_time_del_spo12.strftime('%d.%m.%Y %H:%M')

                elif i in [1, 2, 3, 4, 5, 6] and j in [1, 3, 4, 5, 6, 7, 9, 10, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)
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

    def create_write_nsd_2(self):
        """Цикл для формирования записи ввода NSD"""

        list_out_nsd_spo = self.read_file_jornal('nsd_spo')

        for i, row in enumerate(list_out_nsd_spo):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_nsd_spo[i][j] = self.ser_number_nsd_new
                elif i == 3 and j == 0:
                    list_out_nsd_spo[i][j] = self.fac_number_nsd_new
                elif i == 1 and j == 1:
                    list_out_nsd_spo[i][j] = self.date_time_op_nsd_new.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 1:
                    list_out_nsd_spo[i][j] = self.date_time_op_nsd_new.strftime('T-%H:%M')
                if i == 1 and j == 2:
                    list_out_nsd_spo[i][j] = self.number_device
                elif i == 1 and j == 3:
                    list_out_nsd_spo[i][j] = self.date_time_begin.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 3:
                    list_out_nsd_spo[i][j] = self.stamp_numer_common_old
                elif i == 1 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_nsd_new.strftime('%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_nsd_spo[i][j] = self.date_time_in_nsd_new.strftime('%H:%M')
                elif i == 1 and j == 5:
                    list_out_nsd_spo[i][j] = self.date_time_cl_cap_input.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 5:
                    list_out_nsd_spo[i][j] = self.stamp_numer_common
                elif i == 2 and j == 9:
                    list_out_nsd_spo[i][j] = self.date_time_erase_nsd_new.strftime('%d.%m.%Y %H:%M')
                elif i == 1 and j == 10:
                    list_out_nsd_spo[i][j] = self.date_time_cl_nsd_new.strftime('%d.%m.%Y')
                elif i == 2 and j == 10:
                    list_out_nsd_spo[i][j] = self.date_time_cl_nsd_new.strftime('%H:%M')
                elif i == 3 and j == 10:
                    list_out_nsd_spo[i][j] = self.stamp_numer_one_r

                elif i in [1, 2, 3, 4, 5, 6] and j in [6, 7, 8, 11]:
                    list_out_nsd_spo[i][j] = '' # str(i) + ',' + str(j)
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


class JornalDEK(DataJornal):

    def __init__(self):
        """Конструктор класса JornalDEK"""
        super().__init__()

        # self.date_time_begin = date_time_begin
        # переменные журнала DEK
        # DEK номера ключей
        self.ser_number_dek_old_1 = '1-номер dek старый'
        self.number_com_dek_old_1 = '1-номер компл dek старый'
        self.fac_number_dek_old_1 = '1-зав. № dek старый'
        self.ser_number_dek_old_2 = '2-номер dek старый'
        self.number_com_dek_old_2 = '2-номер компл dek старый'
        self.fac_number_dek_old_2 = '2-зав. № dek старый'
        self.ser_number_dek_new_1 = '1-номер dek новый'
        self.number_com_dek_new_1 = '1-номер компл dek новый'
        self.fac_number_dek_new_1 = '1-зав. № dek новый'
        self.ser_number_dek_new_2 = '2-номер dek новый'
        self.number_com_dek_new_2 = '2-номер компл dek новый'
        self.fac_number_dek_new_2 = '2-зав. № dek новый'

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
        ''' Цикл для формирования записи стирания старого DEK '''

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

    def create_write_dek_3(self):
        '''Цикл для формирования записи ввода №1 нового DEK'''

        list_out_dek = self.read_file_jornal('dek')

        for i, row in enumerate(list_out_dek):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_new_1
                elif i == 3 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_new_1
                elif i == 4 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_new_1
                elif i == 6 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_new_2
                elif i == 7 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_new_2
                elif i == 8 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_new_2
                elif i == 1 and j == 1:
                    list_out_dek[i][j] = self.date_time_op_dek1_new.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 1:
                    list_out_dek[i][j] = self.date_time_op_dek1_new.strftime('T-%H:%M')
                elif i == 5 and j == 1:
                    list_out_dek[i][j] = self.date_time_op_dek2_new.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 1:
                    list_out_dek[i][j] = self.date_time_op_dek2_new.strftime('T-%H:%M')
                elif i == 1 and j == 2:
                    list_out_dek[i][j] = self.number_device
                elif i == 1 and j == 3:
                    list_out_dek[i][j] = self.date_time_begin.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 3:
                    list_out_dek[i][j] = self.date_time_begin.strftime('T-%H:%M')
                elif i == 3 and j == 3:
                    list_out_dek[i][j] = self.stamp_numer_common_old
                elif i == 1 and j == 4:
                    list_out_dek[i][j] = self.date_time_op_dek2_new.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_dek[i][j] = self.date_time_op_dek2_new.strftime('T-%H:%M')
                elif i == 5 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_dek2_new.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_dek2_new.strftime('T-%H:%M')
                elif i == 5 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('T-%H:%M')
                elif i == 2 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
                elif i == 3 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_dek1_new.strftime('T-%H:%M')
                elif i == 6 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_dek1_new.strftime('D-%d.%m.%Y')
                elif i == 7 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_dek1_new.strftime('T-%H:%M')

                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [5, 7, 8, 10, 11]:
                    list_out_dek[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_dek[i][j] = ''

        list_out_dek[0][0] = 'Запись о вводе №1 DEK в аппарат'

        # del list_out_dek[0]

        return list_out_dek

    def create_write_dek_4(self):
        '''Цикл для формирования записи ввода №2 нового DEK'''

        list_out_dek = self.read_file_jornal('dek')

        for i, row in enumerate(list_out_dek):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_new_1
                elif i == 3 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_new_1
                elif i == 4 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_new_1
                elif i == 6 and j == 0:
                    list_out_dek[i][j] = self.ser_number_dek_new_2
                elif i == 7 and j == 0:
                    list_out_dek[i][j] = self.number_com_dek_new_2
                elif i == 8 and j == 0:
                    list_out_dek[i][j] = self.fac_number_dek_new_2
                elif i == 1 and j == 2:
                    list_out_dek[i][j] = self.number_device
                elif i == 1 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_1_dek1_new.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_1_dek1_new.strftime('T-%H:%M')
                elif i == 5 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_1_dek2_new.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 4:
                    list_out_dek[i][j] = self.date_time_in_1_dek2_new.strftime('T-%H:%M')
                elif i == 5 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 6:
                    list_out_dek[i][j] = self.date_time_cl_cap_input.strftime('T-%H:%M')
                elif i == 1 and j == 7:
                    list_out_dek[i][j] = self.date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
                elif i == 2 and j == 7:
                    list_out_dek[i][j] = self.date_time_seal_1_dek12_new.strftime('T-%H:%M')
                elif i == 3 and j == 7:
                    list_out_dek[i][j] = self.stamp_numer_one_r
                elif i == 5 and j == 7:
                    list_out_dek[i][j] = self.date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
                elif i == 6 and j == 7:
                    list_out_dek[i][j] = self.date_time_seal_1_dek12_new.strftime('D-%d.%m.%Y')
                elif i == 7 and j == 7:
                    list_out_dek[i][j] = self.stamp_numer_two_r
                elif i == 1 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_2_dek1_new
                elif i == 2 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_2_dek1_new
                elif i == 3 and j == 8:
                    list_out_dek[i][j] = self.stamp_numer_one_r
                elif i == 5 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_2_dek2_new
                elif i == 6 and j == 8:
                    list_out_dek[i][j] = self.date_time_op_2_dek2_new
                elif i == 7 and j == 8:
                    list_out_dek[i][j] = self.stamp_numer_two_r
                elif i == 2 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
                elif i == 3 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_1_dek12_new.strftime('T-%H:%M')
                elif i == 6 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_1_dek12_new.strftime('D-%d.%m.%Y')
                elif i == 7 and j == 9:
                    list_out_dek[i][j] = self.date_time_erase_1_dek12_new.strftime('T-%H:%M')

                elif i in [1, 2, 3, 4, 5, 6, 7, 8] and j in [1, 3, 5, 10, 11]:
                    list_out_dek[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_dek[i][j] = ''

        list_out_dek[0][0] = 'Запись о вводе №2 DEK в аппарат'

        return list_out_dek


class JornalCKT(DataJornal):

    def __init__(self, n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, ser_number_ckt_old, number_tape_ckt_old, del_date_time):

        """Конструктор класса JornalCKT"""

        super().__init__(n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, del_date_time)

        # CKT данные
        if self.type_work == 'ОН':
            # cmd
            # старый ЦКТ
            self.ser_number_ckt_old = ser_number_ckt_old
            self.number_tape_ckt_old = number_tape_ckt_old
            # новый ЦКТ
            # self.ser_number_ckt_new = '№' + input('Введите номер ckt новый: ') + ', э.ед.'
            # self.number_tape_ckt_new = input('Введите номер ленты ckt новый: ')
        else:
            # test
            self.ser_number_ckt_old = 'номер ckt старый'
            self.number_tape_ckt_old = 'номер ленты ckt старый'
            self.ser_number_ckt_new = 'номер ckt новый'
            self.number_tape_ckt_new = 'номер ленты ckt новый'

    '''Функции для формирования журнала CKT'''
    def create_write_ckt_old(self):
        """Цикл для формирования записи проверке старым CKT"""

        list_out_ckt = self.read_file_jornal('ckt') # считывание данных из файла jornal_M567M(ckt).csv

        for i, row in enumerate(list_out_ckt):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_ckt[i][j] = f'№ {self.ser_number_ckt_old}, э.ед.'
                elif i == 1 and j == 1:
                    list_out_ckt[i][j] = self.date_time_ckt.strftime('%d.%m.%Y')
                elif i == 2 and j == 1:
                    list_out_ckt[i][j] = self.date_time_ckt.strftime('%H:%M')
                elif i == 1 and j == 2 or i == 2 and j == 3 or i == 2 and j == 6:
                    list_out_ckt[i][j] = self.number_tape_ckt_old
                elif i == 3 and j == 1:
                    list_out_ckt[i][j] = self.stamp_numer_one_r_ckt_old
                elif i == 2 and j == 2:
                    list_out_ckt[i][j] = self.extract_date_time_ckt.strftime('%d.%m.%Y %H:%M')
                elif i == 1 and j == 3:
                    list_out_ckt[i][j] = self.number_device
                elif i == 3 and j == 3:
                    list_out_ckt[i][j] = self.input_date_time_ckt.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 4:
                    list_out_ckt[i][j] = self.input_date_time_ckt.strftime('%d.%m.%Y')
                elif i == 1 and j == 5:
                    list_out_ckt[i][j] = self.stamp_numer_one_r
                elif i == 2 and j == 5:
                    list_out_ckt[i][j] = self.seal_date_time_ckt.strftime('%d.%m.%Y %H:%M')
                elif i == 1 and j == 6:
                    list_out_ckt[i][j] = self.del_date_time.strftime('%d.%m.%Y %H:%M')

                elif i in [1, 2, 3, 4] and j in [7]:
                    list_out_ckt[i][j] = ''  # str(i) + ',' + str(j)

        return list_out_ckt

    def create_write_ckt_new(self):
        """Цикл для формирования записи проверки новым CKT"""

        list_out_ckt = self.read_file_jornal('ckt')

        for i, row in enumerate(list_out_ckt):
            # print(row)
            for j, cell in enumerate(row):
                # print(cell)
                if i == 2 and j == 0:
                    list_out_ckt[i][j] = f'№ {self.ser_number_ckt_new}, э.ед.'
                elif i == 1 and j == 1:
                    list_out_ckt[i][j] = self.date_time_ckt_new.strftime('%d.%m.%Y')
                elif i == 2 and j == 1:
                    list_out_ckt[i][j] = self.date_time_ckt_new.strftime('%H:%M')
                elif i == 1 and j == 2 or i == 2 and j == 3 or i == 2 and j == 6:
                    list_out_ckt[i][j] = self.number_tape_ckt_new
                elif i == 3 and j == 1:
                    list_out_ckt[i][j] = 'подпись'
                elif i == 4 and j == 1:
                    list_out_ckt[i][j] = ''
                elif i == 2 and j == 2:
                    list_out_ckt[i][j] = self.extract_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
                elif i == 1 and j == 3:
                    list_out_ckt[i][j] = self.number_device
                elif i == 3 and j == 3:
                    list_out_ckt[i][j] = self.input_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
                elif i == 2 and j == 4:
                    list_out_ckt[i][j] = self.input_date_time_ckt_new.strftime('%d.%m.%Y')
                elif i == 1 and j == 5:
                    list_out_ckt[i][j] = self.stamp_numer_one_r
                elif i == 2 and j == 5:
                    list_out_ckt[i][j] = self.seal_date_time_ckt_new.strftime('%d.%m.%Y %H:%M')
                elif i == 1 and j == 6:
                    list_out_ckt[i][j] = self.del_date_time.strftime('%d.%m.%Y %H:%M')

                elif i in [1, 2, 3, 4] and j in [7]:
                    list_out_ckt[i][j] = '' # str(i) + ',' + str(j)
                elif i == 0:
                    list_out_ckt[i][j] = ''

        list_out_ckt[0][0] = 'Запись о проверке новым CKT'

        return list_out_ckt


class TechnicalJornal(DataJornal):

    def __init__(self, n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, ser_number_CUV_1_2, fac_number_CUV_1, del_date_time):

        """ Конструктор класса TechnicalJornal"""
        super().__init__(n, quantity_device, type_dt, type_work, date_time_begin, number_device, str_number_device, number_MUVK, FIO_1part,
                 FIO_2part, FIO_chief, FIO_carry_KD, stamp_numer_one_old, stamp_numer_two_old, stamp_numer_one,
                 stamp_numer_two, stamp_numer_one_old_MUVK, stamp_numer_two_old_MUVK, stamp_numer_one_r_ckt_old,
                 stamp_numer_one_r, stamp_numer_two_r, del_date_time)

        # номера и серии ключей
        # CUV
        if self.type_work == 'ОН':
            # cmd
            self.ser_number_CUV_1_2 = ser_number_CUV_1_2
            self.fac_number_CUV_1 = fac_number_CUV_1
        else:
            # test
            self.ser_number_CUV_1_2 = 'номер серии ЦУВ-1,2'
            self.fac_number_CUV_1 = 'заводской номер ЦУВ-1'

    def create_dict_technical(self):
        """Функция для формирования словаря технического журнала"""

        list_in_technical = self.read_file_jornal('technical')  # входной список технического журнала

        dict_out_technical = {
            # заголовки технического журнала
            'title': list_in_technical[0],
            # записи о вскрытии контейнера с МУВК
            'date_time_op_MUVK': self.date_time_op_MUVK,
            'write_open_kontainer': list_in_technical[1][1],
            'catatan_ON_begin': list_in_technical[1][8],
            'FIO_1part': list_in_technical[2][6],  # ФИО 1 часть
            'FIO_lukisan_1part': list_in_technical[2][7],  # подпись 1 часть
            # записи о вскрытии 1 аппарата
            'date_time_op_cap_input_1_device': self.date_time_begin,
            'date_time_op_cap_input_2_device': self.date_time_begin,
            'date_time_op_cap_input_n_device': self.date_time_begin,
            'write_open_cap_input_1_device': list_in_technical[3][1],
            'write_open_cap_input_devices': list_in_technical[5][1],
            # записи о проверке ЦПО МУВК
            'date_time_op_CUV_1': self.date_time_op_CUV_1,
            'write_open_CUV_1': list_in_technical[7][1],
            'date_time_op_CUV_2': self.date_time_op_CUV_2,
            'write_open_CUV_2': list_in_technical[9][1],
            'FIO_2part': list_in_technical[10][6],  # ФИО 2 часть
            'FIO_lukisan_2part': list_in_technical[10][7],  # подпись 2 часть
            'date_time_check_open': self.date_time_op_CUV_2,  # дата проверки вскрытия
            'write_check_open': list_in_technical[11][1],  # проверка вскрытия
            'FIO_chief': list_in_technical[2][6],  # ФИО начальник
            'FIO_lukisan_chief': list_in_technical[2][7],  # подпись начальник
            'date_time_check_CPO_MUVK_b': self.date_time_check_CPO_MUVK_b,  # проверка ЦПО МУВК начало
            'date_time_check_CPO_MUVK_e': self.date_time_check_CPO_MUVK_e,  # проверка ЦПО МУВК конец
            'write_check_CPO_MUVK': list_in_technical[13][1],  # проверка ЦПО МУВК
            'date_time_erase_CUV_1_b': self.date_time_erase_CUV_1_b,  # стирание ЦУВ-1 начало
            'date_time_erase_CUV_1_e': self.date_time_erase_CUV_1_e,  # стирание ЦУВ-1 конец
            'write_erase_CUV_1': list_in_technical[16][1],  # стирание ЦУВ-1
            'date_time_cl_CUV_1': self.date_time_cl_CUV_1,  # опечатывание ЦУВ-1
            'write_cl_CUV_1': list_in_technical[18][1],  # опечатывание ЦУВ-1
            'date_time_cl_CUV_2': self.date_time_cl_CUV_2,  # опечатывание ЦУВ-2
            'write_cl_CUV_2': list_in_technical[20][1],  # опечатывание ЦУВ-2
            'date_time_CPO_INPUT_b': self.date_time_CPO_INPUT_b,  # проверка ЦПО аппаратов, ввод ключей
            'date_time_CPO_INPUT_e': self.date_time_CPO_INPUT_e,  # проверка ЦПО аппаратов, ввод ключей
            'write_CPO_INPUT': list_in_technical[22][1],  # проверка ЦПО аппаратов, ввод ключей
            'date_time_erase_RDT_b': self.date_time_erase_RDT_b,  # стирание RDT
            'date_time_erase_RDT_e': self.date_time_erase_RDT_e,  # стирание RDT
            'write_erase_RDT': list_in_technical[25][1],  # стирание RDT
            'date_time_cl_cap_input_b': self.date_time_cl_cap_input_b,  # опечатывание крышки ввод аппарата №1
            'date_time_cl_cap_input_e': self.date_time_cl_cap_input_e,  # опечатывание крышки ввод последнего аппарата
            'write_cl_cap_input': list_in_technical[28][1],  # опечатывание крышек ввод  аппаратов
            'date_time_cl_MUVK': self.date_time_cl_MUVK,  # опечатывание МУВК
            'write_cl_MUVK': list_in_technical[31][1],  # опечатывание МУВК
            'date_time_op_box_CUV_2': self.date_time_op_box_CUV_2,  # вскрытие пенала ЦУВ-2
            'write_op_box_CUV_2': list_in_technical[34][1],  # вскрытие пенала ЦУВ-2
            'date_time_del_CUV_2': self.date_time_del_CUV_2,  # уничтожение ЦУВ-2
            'write_del_CUV_2': list_in_technical[36][1],  # уничтожение ЦУВ-2
            'date_time_use_KD': self.date_time_del_CUV_2,  # дата проверки правильности обращения с КД
            'write_use_KD': list_in_technical[39][1],  # проверка правильности обращения с КД
            'FIO_carry_KD': list_in_technical[39][6],  # ФИО ответственный за КД
            'lukisan_carry_KD': list_in_technical[39][7],  # подпись ответственный за КД
            'date_time_erase_RDT_old_b': self.date_time_erase_RDT_old_b,  # начало стирания выведенных из обращения RDT
            'date_time_erase_RDT_old_e': self.date_time_erase_RDT_old_e,  # конец стирания выведенных из обращения RDT
            'write_erase_RDT_old': list_in_technical[44][1],  # стирание выведенных из обращения RDT
            'date_time_cl_cap_input_dev1': self.date_time_cl_cap_input_dev1, # опечатывания разъёма ввод аппарата после стирания RDT
            'write_cl_cap_input_dev1': list_in_technical[47][1], # опечатывания разъёма ввод аппарата после стирания RDT
            'del_date_time' : self.del_date_time # уничтожение ключей и таблиц блокнотов
        }

        return dict_out_technical

    def create_write_technical(self):
        """Функция для формирования записи в техническом журнале"""

        dict_out_technical = self.create_dict_technical() # словарь технического журнала
        list_in_technical = self.read_file_jornal('technical')  # входной список технического журнала
        list_out_technical = []  # выходной список технического журналя
        # переопределение значений словаря technical_jornal
        if self.n == 1:
            dict_out_technical['date_time_op_cap_input_1_device'] = self.date_time_begin # вскрытие 1-го аппарата
        if self.n == 2:
            dict_out_technical['date_time_op_cap_input_2_device'] = self.date_time_begin # вскрытие 2-го аппарата
        if self.n == self.quantity_device:
            dict_out_technical['date_time_op_cap_input_n_device'] = self.date_time_begin # вкрытие n-го аппарата
        if self.n == 1:
            dict_out_technical['date_time_CPO_INPUT_b'] = self.date_time_CPO_INPUT_b # проверка ЦПО аппаратов, ввод ключей
        if self.n == self.quantity_device:
            dict_out_technical['date_time_CPO_INPUT_e'] = self.date_time_CPO_INPUT_e
        if self.n == 1:
            dict_out_technical['date_time_cl_cap_input_b'] = self.date_time_cl_cap_input_b # опечатывание крышки ввод аппарата №1
        if self.n == self.quantity_device:
            dict_out_technical['date_time_cl_cap_input_e'] = self.date_time_cl_cap_input_e # опечатывание крышки ввод n-го аппарата

        # Условие для формирования технического журнала при очередном наборе
        if self.type_work == 'ОН':
            list_out_technical.append(list_in_technical[0])
            # запись о вскрытии МУВК
            list_out_technical.append(list_in_technical[1])
            list_out_technical.append(list_in_technical[2])
            list_out_technical[1][0] = dict_out_technical['date_time_op_MUVK'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_kontainer'] = f'Вскрыт контейнер с МУВК ПА655М {self.number_MUVK}, опечатанный печатями {self.stamp_numer_common_old_MUVK}'
            list_out_technical[1][1] = dict_out_technical['write_open_kontainer']
            del list_out_technical[1][8]  # удаляем примечание
            # print(list_out_technical[1][1])
            list_out_technical[2][0] = dict_out_technical['date_time_op_MUVK'].strftime('%H:%M')
            dict_out_technical['FIO_1part'] = self.FIO_1part
            list_out_technical[2][6] = dict_out_technical['FIO_1part']
            # запись о вскрытии крышки "Ввод" первого аппарата
            list_out_technical.append(list_in_technical[3])
            list_out_technical.append(list_in_technical[4])
            list_out_technical[3][0] = dict_out_technical['date_time_op_cap_input_1_device'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_cap_input_1_device'] = f'Вскрыта крышка разъёма "Ввод" аппаратуры М-567М №{self.number_device},' \
                f'опечатанный печатями {self.stamp_numer_common_old}'
            list_out_technical[3][1] = dict_out_technical['write_open_cap_input_1_device']
            list_out_technical[4][0] = dict_out_technical['date_time_op_cap_input_1_device'].strftime('%H:%M')
            list_out_technical[4][6] = dict_out_technical['FIO_1part']
            # запись о вскрытии крышек "Ввод" остальных аппаратов
            list_out_technical.append(list_in_technical[5])
            list_out_technical.append(list_in_technical[6])
            list_out_technical[5][0] = dict_out_technical['date_time_op_cap_input_2_device'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_cap_input_devices'] = f'Вскрыты крышки разъёма "Ввод" аппаратуры М-567М №{self.str_number_device}, опечатанные печатями {self.stamp_numer_common_old}'
            list_out_technical[5][1] = dict_out_technical['write_open_cap_input_devices']
            list_out_technical[6][0] = dict_out_technical['date_time_op_cap_input_2_device'].strftime('%H:%M') + '-' + \
                                       dict_out_technical['date_time_op_cap_input_n_device'].strftime('%H:%M')
            list_out_technical[6][6] = dict_out_technical['FIO_1part']
            # запись о вскрытии ЦУВ-1
            list_out_technical.append(list_in_technical[7])
            list_out_technical.append(list_in_technical[8])
            list_out_technical[7][0] = dict_out_technical['date_time_op_CUV_1'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_CUV_1'] = f'Вкрыта упаковка шифрблокнота ЦУВ-1-1012 серия №{self.ser_number_CUV_1_2}, э.ед., {self.fac_number_CUV_1}'
            list_out_technical[7][1] = dict_out_technical['write_open_CUV_1']
            list_out_technical[8][0] = dict_out_technical['date_time_op_CUV_1'].strftime('%H:%M')
            list_out_technical[8][6] = dict_out_technical['FIO_1part']
            # запись о вскрытии ЦУВ-2
            list_out_technical.append(list_in_technical[9])
            list_out_technical.append(list_in_technical[10])
            list_out_technical[9][0] = dict_out_technical['date_time_op_CUV_2'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_CUV_2'] = f'Вкрыта упаковка шифрблокнота ЦУВ-2-1012 серия №{self.ser_number_CUV_1_2}, э.ед.'
            list_out_technical[9][1] = dict_out_technical['write_open_CUV_2']
            list_out_technical[10][0] = dict_out_technical['date_time_op_CUV_2'].strftime('%H:%M')
            dict_out_technical['FIO_2part'] = self.FIO_2part
            list_out_technical[10][6] = dict_out_technical['FIO_2part']
            # запись о проверки правильности вскрытия
            list_out_technical.append(list_in_technical[11])
            list_out_technical.append(list_in_technical[12])
            list_out_technical[11][0] = dict_out_technical['date_time_check_open'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_open_CUV_1'] = f'Вкрыта упаковка шифрблокнота ЦУВ-1-1012 серия №{self.ser_number_CUV_1_2}, э.ед., {self.fac_number_CUV_1}'
            list_out_technical[11][1] = dict_out_technical['write_check_open']
            dict_out_technical['FIO_chief'] = self.FIO_chief
            list_out_technical[12][6] = dict_out_technical['FIO_chief']
            # проверка ЦПО МУВК
            list_out_technical.append(list_in_technical[13])
            list_out_technical.append(list_in_technical[14])
            list_out_technical.append(list_in_technical[15])
            list_out_technical[13][0] = dict_out_technical['date_time_check_CPO_MUVK_b'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_check_CPO_MUVK'] = f'Проведена проверка ЦПО МУВК ПА655М(V1012) {self.number_MUVK}, подключенного к аппаратуре ' \
                f'М-567М(V1054)№{self.number_device} с использованием КД ЦУВ-1,2-1012 серия №{self.ser_number_CUV_1_2}, э.ед. Результат проверки - "норма"'
            list_out_technical[13][1] = dict_out_technical['write_check_CPO_MUVK']
            list_out_technical[14][0] = dict_out_technical['date_time_check_CPO_MUVK_b'].strftime('%H:%M') + '-' + \
                                        dict_out_technical['date_time_check_CPO_MUVK_e'].strftime('%H:%M')
            list_out_technical[14][6] = dict_out_technical['FIO_1part']
            list_out_technical[15][6] = dict_out_technical['FIO_2part']
            # стирание ЦУВ-1
            list_out_technical.append(list_in_technical[16])
            list_out_technical.append(list_in_technical[17])
            list_out_technical[16][0] = dict_out_technical['date_time_erase_CUV_1_b'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_erase_CUV_1'] = f'Произведено стирание КИ с КД ЦУВ-1-1012 серия №{self.ser_number_CUV_1_2}, э.ед.,' \
                f'зав. №{self.fac_number_CUV_1} с использованием МУВК ПА655М {self.number_MUVK}, подключенного к аппаратуре М-567М №{self.number_device}'
            list_out_technical[16][1] = dict_out_technical['write_erase_CUV_1']
            list_out_technical[17][0] = dict_out_technical['date_time_erase_CUV_1_b'].strftime('%H:%M') + '-' + \
                                        dict_out_technical['date_time_erase_CUV_1_e'].strftime('%H:%M')
            list_out_technical[17][6] = dict_out_technical['FIO_1part']
            # опечатывание стёртого ЦУВ-1
            list_out_technical.append(list_in_technical[18])
            list_out_technical.append(list_in_technical[19])
            list_out_technical[18][0] = dict_out_technical['date_time_cl_CUV_1'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_cl_CUV_1'] = f'Конверт с ключевым носителем К1634ДК6 {self.fac_number_CUV_1} закрыт и опечатан печатью {self.stamp_numer_one_r}'
            list_out_technical[18][1] = dict_out_technical['write_cl_CUV_1']
            list_out_technical[19][0] = dict_out_technical['date_time_cl_CUV_1'].strftime('%H:%M')
            list_out_technical[19][6] = dict_out_technical['FIO_1part']
            # опечатывание ЦУВ-2
            list_out_technical.append(list_in_technical[20])
            list_out_technical.append(list_in_technical[21])
            list_out_technical[20][0] = dict_out_technical['date_time_cl_CUV_2'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_cl_CUV_2'] = f'Пенал с КД ЦУВ-2-1012 серия {self.ser_number_CUV_1_2}, э.ед. закрыт и опечатан печатью {self.stamp_numer_two_r}'
            list_out_technical[20][1] = dict_out_technical['write_cl_CUV_2']
            list_out_technical[21][0] = dict_out_technical['date_time_cl_CUV_2'].strftime('%H:%M')
            list_out_technical[21][6] = dict_out_technical['FIO_2part']
            # проверка ЦПО аппаратов, ввод КИ, переход на очередную КИ в аппратах
            list_out_technical.append(list_in_technical[22])
            list_out_technical.append(list_in_technical[23])
            list_out_technical.append(list_in_technical[24])
            list_out_technical[22][0] = dict_out_technical['date_time_CPO_INPUT_b'].strftime('%d.%m.%Y')
            dict_out_technical['write_CPO_INPUT'] = f'В аппаратуре М-567М №{self.str_number_device} проведена проверка ЦПО,' \
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
            dict_out_technical[
                'write_erase_RDT'] = f'Стирание КИ с введённых КД с использованием МУВК ПА655М {self.number_MUVK}'
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
            dict_out_technical[
                'write_cl_cap_input'] = f'Крышки рзаъёмов "Ввод" аппаратуры М567М №{self.str_number_device} закрыты' \
                f' и опечатаны печатями {self.stamp_numer_common}'
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
            dict_out_technical[
                'write_cl_MUVK'] = f'Контейнер с МУВК ПА655М {self.number_MUVK} закрыт и опечатан печатями {self.stamp_numer_common}'
            list_out_technical[31][1] = dict_out_technical['write_cl_MUVK']
            list_out_technical[32][0] = dict_out_technical['date_time_cl_MUVK'].strftime('%H:%M')
            list_out_technical[32][6] = dict_out_technical['FIO_1part']
            list_out_technical[33][6] = dict_out_technical['FIO_2part']
            # запись о вскрытии ЦУВ-1 для стирания
            list_out_technical.append(list_in_technical[34])
            list_out_technical.append(list_in_technical[35])
            list_out_technical[34][0] = dict_out_technical['date_time_op_box_CUV_2'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_op_box_CUV_2'] = f'Вскрыт пенал с КД ЦУВ-2-1012 серия №{self.ser_number_CUV_1_2}, э.ед., ' \
                f'опечатанный печатью {self.stamp_numer_two_r}'
            list_out_technical[34][1] = dict_out_technical['write_op_box_CUV_2']
            list_out_technical[35][0] = dict_out_technical['date_time_op_box_CUV_2'].strftime('%H:%M')
            list_out_technical[35][6] = dict_out_technical['FIO_2part']
            # запись об уничтожении ЦУВ-2
            list_out_technical.append(list_in_technical[36])
            list_out_technical.append(list_in_technical[37])
            list_out_technical.append(list_in_technical[38])
            list_out_technical[36][0] = dict_out_technical['date_time_del_CUV_2'].strftime('%d.%m.%Y')
            dict_out_technical[
                'write_del_CUV_2'] = f'Произведено уничтожение ЦУВ-2-1012 серия №{self.ser_number_CUV_1_2}, э.ед.'
            list_out_technical[36][1] = dict_out_technical['write_del_CUV_2']
            list_out_technical[37][0] = dict_out_technical['date_time_del_CUV_2'].strftime('%H:%M')
            list_out_technical[37][6] = dict_out_technical['FIO_1part']
            list_out_technical[38][6] = dict_out_technical['FIO_2part']
            # запись о проверки правильности обращения с КД
            list_out_technical.append(list_in_technical[39])
            list_out_technical[39][0] = dict_out_technical['date_time_use_KD'].strftime('%d.%m.%Y')
            dict_out_technical['write_use_KD'] = f'Правильность обращения с КД проверил'
            list_out_technical[39][1] = dict_out_technical['write_use_KD']
            dict_out_technical['FIO_carry_KD'] = self.FIO_carry_KD
            list_out_technical[39][6] = dict_out_technical['FIO_carry_KD']

        return list_out_technical



if __name__ == '__main__':

    # data_1 = DataJornal('да')
    # data_2 = DataJornal()
    # print(data_2.duration_1_h_02_m)
    # print(type(data_2.duration_1_h_02_m))
    # data_3 = JornalDEK(DataJornal('да').date_time_begin)
    data_3 = DataJornal(type_work='тест') # создание объекта данных для журналов М567М
    # print(data_4.type_work)
    # print(data_3.date_time_begin.strftime('%H:%M'))
    # print(data_3.date_time_op_dek1_old)
    # print(data_3.date_time_op_dek2_old)
    # print(data_4.date_time_erase_dek1_new)
    # журнал DEK
    data_4 = JornalDEK()
    print(data_4.read_file_jornal('dek'))
    list_out_dek = data_4.create_write_dek_1()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Вскрытие DEK')
    list_out_dek = data_4.create_write_dek_2()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Стирание DEK')
    list_out_dek = data_4.create_write_dek_3()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Ввод №1 DEK_NEW')
    list_out_dek = data_4.create_write_dek_4()
    pprint.pprint(list_out_dek, depth=12, width=144)
    data_4.write_file_dek(list_out_dek, 'dek', 'Ввод №2 DEK_NEW')
    # журнал CKT
    data_5 = JornalCKT()
    print(data_5.read_file_jornal('ckt'))
    list_out_ckt = data_5.create_write_ckt_old()
    pprint.pprint(list_out_ckt, depth=12, width=144)
    data_5.write_file_dek(list_out_ckt, 'ckt', 'Запись о проверке старым CKT')
    list_out_ckt = data_5.create_write_ckt_new()
    pprint.pprint(list_out_ckt, depth=12, width=144)
    data_5.write_file_dek(list_out_ckt, 'ckt', 'Запись о проверке новым CKT')
    # Журнал NSD_SPO
    data_6 = JornalNSD_SPO()
    print(data_6.read_file_jornal('nsd_spo'))
    list_out_nsd_spo = data_6.create_write_spo_1()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о вскрытии SPO')
    list_out_nsd_spo = data_6.create_write_spo_2()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о сбросе SPO в  аппарате')
    list_out_nsd_spo = data_6.create_write_spo_3()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о вводе №1 СПО в аппарат')
    list_out_nsd_spo = data_6.create_write_spo_4()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о вводе №2 СПО в аппарат')
    list_out_nsd_spo = data_6.create_write_nsd_1()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о сбросе НСД в аппарате')
    list_out_nsd_spo = data_6.create_write_nsd_2()
    pprint.pprint(list_out_nsd_spo, depth=12, width=144)
    data_6.write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Запись о вводе НСД в аппарат')
    # Журнал RDT
    data_7 = JornalRDT('тест')
    print(data_7.read_file_jornal('rdt'))
    list_out_rdt = data_7.create_write_rdt_1()
    pprint.pprint(list_out_rdt, depth=12, width=144)
    data_7.write_file_dek(list_out_rdt, 'rdt', 'Запись о сбросе ранее введённого RDT')
    list_out_rdt = data_7.create_write_rdt_2()
    pprint.pprint(list_out_rdt, depth=12, width=144)
    data_7.write_file_dek(list_out_rdt, 'rdt', 'Запись о вводе RDT в аппарат')
    # Технический журнал
    data_8 = TechnicalJornal(type_work='ОН')
    print(data_8.read_file_jornal('technical'))
    # data_8.create_write_technical()
    list_out_technical = data_8.create_write_technical()
    pprint.pprint(list_out_technical, depth=12, width=144)
    data_8.write_file_dek(list_out_technical, 'technical', 'Запись техническом журнале')
