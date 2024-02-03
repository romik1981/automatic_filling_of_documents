"""
Образцы записей в журналы.
Данные используемые в журналах.
"""
import datetime

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'

# Переменные даты и времени
date_time_now = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
date_now = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_now = datetime.datetime.now().strftime('Time - %H:%M')
date_time_ckt = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
date_ckt = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_ckt = datetime.datetime.now().strftime('Time - %H:%M')
duration_1_minutes = datetime.timedelta(minutes=1)
duration_2_minutes = datetime.timedelta(minutes=2)
duration_4_minutes = datetime.timedelta(minutes=4)
duration_10_hours = datetime.timedelta(hours=10)
extract_date_time_ckt = (datetime.datetime.now() + duration_1_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
input_date_time_ckt = (datetime.datetime.now() + duration_2_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
seal_date_time_ckt = (datetime.datetime.now() + duration_4_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
del_date_time = (datetime.datetime.now() + duration_10_hours).strftime('Date - %d.%m.%Y Time - %H:%M')


number_device = '428М-001676'
stamp_numer_one = 'п.ст.№1'
stamp_numer_two = 'п.ст.№2'
stamp_numer_one_r = 'п.кр.№1'
stamp_numer_two_r = 'п.кр.№2'
stamp_numer_one_r_ckt_old = 'п.кр.№1 ckt_old'

ser_number_ckt_old = 'номер ckt старый'
number_tape_ckt_old = 'номер ленты ckt старый'


stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two
#print(stamp_numer_common)