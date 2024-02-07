"""
Образцы записей в журналы.
Данные используемые в журналах.
"""
import datetime

last_device_input_dek = 'Номер аппарата куда в последний раз был введён ДЕК'

# Переменные даты и времени
date_time_now = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
date_time_begin = datetime.datetime.now()
date_now = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_now = datetime.datetime.now().strftime('Time - %H:%M')
date_time_ckt = datetime.datetime.now().strftime('Date - %d.%m.%Y Time - %H:%M')
date_ckt = datetime.datetime.now().strftime('Date - %d.%m.%Y')
time_ckt = datetime.datetime.now().strftime('Time - %H:%M')
duration_1_minutes = datetime.timedelta(minutes=1)
duration_2_minutes = datetime.timedelta(minutes=2)
duration_4_minutes = datetime.timedelta(minutes=4)
duration_10_hours = datetime.timedelta(hours=10)
duration_58_minutes = datetime.timedelta(minutes=58)
duration_10_h_19_m = datetime.timedelta(hours=2, minutes=19)
duration_1_h_25_m = datetime.timedelta(hours=1, minutes=25)
extract_date_time_ckt = (datetime.datetime.now() + duration_1_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
input_date_time_ckt = (datetime.datetime.now() + duration_2_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
seal_date_time_ckt = (datetime.datetime.now() + duration_4_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
del_date_time = (datetime.datetime.now() + duration_10_hours).strftime('Date - %d.%m.%Y Time - %H:%M')
date_time_cl_cap_input = date_time_begin + duration_10_h_19_m

# даты и время для DEK
date_time_op_dek1_new = date_time_begin + duration_58_minutes
date_time_op_dek2_new = date_time_op_dek1_new + duration_1_minutes
date_time_in_dek2_new = date_time_op_dek2_new + duration_1_minutes
date_time_erase_dek1_new = date_time_in_dek2_new + duration_2_minutes
# даты и время для SPO
date_time_op_spo1 = date_time_begin + duration_1_h_25_m
date_time_op_spo2 = date_time_op_spo1 + duration_1_minutes

number_device = '№апп.М567М'
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

# номера и серии ключей
ser_number_ckt_old = 'номер ckt старый'
number_tape_ckt_old = 'номер ленты ckt старый'
ser_number_dek_new_1 = '1-номер dek новый'
number_com_dek_new_1 = '1-номер компл dek новый'
fac_number_dek_new_1 = '1-зав. № dek новый'
ser_number_dek_new_2 = '2-номер dek новый'
number_com_dek_new_2 = '2-номер компл dek новый'
fac_number_dek_new_2 = '2-зав. № dek новый'
ser_number_comp_spo1 = '1-номер и комп spo1'
fac_number_spo1 = '1-зав. № spo1'
ser_number_comp_spo2 = '2-номер и комп spo2'
fac_number_spo2 = '2-зав. № spo2'



stamp_numer_common_old = stamp_numer_one_old + ', ' + stamp_numer_two_old
stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two
#print(stamp_numer_common)