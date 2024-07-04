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
        data_1 = DataJornal(type_dt=type_dt, type_work=type_work)  # создание объекта данных для журналов М567М
        print(data_1.type_work)
        print(data_1.type_dt)
        print(data_1.date_time_begin)

    print(f'Вы набрали {n} аппарат.')
    n += 1
    if n <= quantity_device:
        point_exit = input('Продолжить набор аппаратов (да/нет): ')

