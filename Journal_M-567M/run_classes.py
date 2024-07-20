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
        # data_1 = DataJornal(type_dt=type_dt, type_work=type_work)  # создание объекта данных для журналов М567М
        # print(data_1.type_work)
        # print(data_1.type_dt)
        # print(data_1.date_time_begin)
        ''' Формирование журнала RDT '''
        # Журнал RDT сброс
        data_2 = JornalRDT(type_dt, type_work) # создание объекта данных для журнала RDT М567М
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
        data_3 = JornalCKT(type_dt, type_work)
        print(data_3.read_file_jornal('ckt'))
        list_out_ckt = data_3.create_write_ckt_old()
        pprint.pprint(list_out_ckt, depth=12, width=144)
        data_3.write_file_dek(list_out_ckt, 'ckt', 'Запись о проверке старым CKT')
        # ''' Формирование технического журнала '''
        # # Технический журнал для очередного набора ключей
        # data_4 = TechnicalJornal(type_work='ОН')
        # print(data_4.read_file_jornal('technical'))
        # # data_8.create_write_technical()
        # list_out_technical = data_4.create_write_technical()
        # pprint.pprint(list_out_technical, depth=12, width=144)
        # data_4.write_file_dek(list_out_technical, 'technical', 'Запись техническом журнале')

    print(f'Вы набрали {n} аппарат.')
    n += 1
    if n <= quantity_device:
        point_exit = input('Продолжить набор аппаратов (да/нет): ')

