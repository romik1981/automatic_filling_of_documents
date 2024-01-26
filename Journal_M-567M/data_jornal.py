"""
Образцы записей в журналы.
Данные используемые в журналах.
"""
import datetime

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'
date_time_now = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
date_now = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_now = datetime.datetime.now().strftime('Time - %H:%M')
number_device = '428М-001676'
stamp_numer_one = 'печать №1 столбик'
stamp_numer_two = 'печать №2 столбик'
stamp_numer_one_r = 'печать №1 круглая'
stamp_numer_two_r = 'печать №2 круглая'


stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two
#print(stamp_numer_common)