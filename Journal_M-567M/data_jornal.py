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

# Приращения времени
duration_1_minutes = datetime.timedelta(minutes=1)
duration_2_minutes = datetime.timedelta(minutes=2)
duration_4_minutes = datetime.timedelta(minutes=4)
duration_6_minutes = datetime.timedelta(minutes=6)
duration_14_minutes = datetime.timedelta(minutes=14)
duration_23_minutes = datetime.timedelta(minutes=23)
duration_27_minutes = datetime.timedelta(minutes=27)
duration_52_minutes = datetime.timedelta(minutes=52)
duration_58_minutes = datetime.timedelta(minutes=58)
duration_1_h_25_m = datetime.timedelta(hours=1, minutes=25)
duration_1_h_14_m = datetime.timedelta(hours=1, minutes=14)
duration_1_h_02_m = datetime.timedelta(hours=1, minutes=2)
duration_10_hours = datetime.timedelta(hours=10)
duration_10_h_19_m = datetime.timedelta(hours=10, minutes=19)
duration_14_hours = datetime.timedelta(hours=14)
duration_14_h_30_m = datetime.timedelta(hours=14, minutes=30)

# Время уничтожения ключей, блокнотов и упаковок
del_date_time = date_time_begin + duration_14_h_30_m
# Опечатывание крышки ввод аппарата
date_time_cl_cap_input = date_time_begin + duration_10_h_19_m

# даты и время для DEK
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
# даты и время для DEK продолжение
date_time_in_1_dek1_new = date_time_in_1_spo1 + duration_2_minutes
date_time_in_1_dek2_new = date_time_in_1_dek1_new + duration_1_minutes
date_time_seal_1_dek12_new = date_time_in_1_dek2_new + duration_23_minutes
date_time_op_2_dek1_new = 'вр вск dek для апп №2'
date_time_op_2_dek2_new = 'вр вск dek для апп №1'
date_time_erase_1_dek12_new = date_time_seal_1_dek12_new + duration_1_minutes
# даты и время для NSD
date_time_op_nsd_new = date_time_del_spo12 + duration_6_minutes
date_time_in_nsd_new = date_time_op_nsd_new + duration_1_minutes
date_time_erase_nsd_new = date_time_in_nsd_new + duration_14_minutes
date_time_cl_nsd_new = date_time_erase_nsd_new + duration_1_minutes
# даты и время для CKT
date_time_ckt = date_time_begin + duration_52_minutes
extract_date_time_ckt = date_time_ckt + duration_1_minutes
input_date_time_ckt = date_time_ckt + duration_2_minutes
seal_date_time_ckt = date_time_ckt + duration_4_minutes
date_time_ckt_new = date_time_begin + duration_1_h_14_m
extract_date_time_ckt_new = date_time_ckt_new + duration_1_minutes
input_date_time_ckt_new = date_time_ckt_new + duration_2_minutes
seal_date_time_ckt_new = date_time_ckt_new + duration_4_minutes

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
# CKT
ser_number_ckt_old = 'номер ckt старый'
number_tape_ckt_old = 'номер ленты ckt старый'
ser_number_ckt_new = 'номер ckt новый'
number_tape_ckt_new = 'номер ленты ckt новый'
# DEK
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



stamp_numer_common_old = stamp_numer_one_old + ', ' + stamp_numer_two_old
stamp_numer_common = stamp_numer_one + ', ' + stamp_numer_two
#print(stamp_numer_common)