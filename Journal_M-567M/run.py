from read_write_file import read_file_jornal, write_file_dek, create_write_dek_1, create_write_dek_2, create_write_dek_3_new,\
    create_write_rdt_1, create_write_ckt_old, create_write_ckt_new, create_write_spo_1, create_write_spo_2, create_write_nsd_1,\
    create_write_nsd_2
import pprint



''' Формирование журнала DEK '''
# Запись о вкрытие старого DEK
# list_out_dek = create_write_dek_1(read_file_jornal('dek'))
# write_file_dek(list_out_dek, 'dek')

# Запись о стирание старого DEK
# list_out_dek = create_write_dek_2(read_file_jornal('dek'))
# write_file_dek(list_out_dek, 'dek')

# Запись о первом вводе нового DEK
# list_out_dek = create_write_dek_3_new(read_file_jornal('dek'))
# write_file_dek(list_out_dek, 'dek')

''' Формирование журнала RDT '''
# Запись о сбросе старого RDT
# list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
# pprint.pprint(list_out_rdt, depth=12, width=144)
# write_file_dek(list_out_rdt, 'rdt')

''' Формирование журнала CKT '''
# Запись о проверке старым CKT
list_out_ckt = create_write_ckt_old(read_file_jornal('ckt'))
write_file_dek(list_out_ckt, 'ckt', 'Проверка старым CKT')
# Запись о проверке новым CKT
list_out_ckt = create_write_ckt_new(read_file_jornal('ckt'))
write_file_dek(list_out_ckt, 'ckt', 'Проверка новым CKT')

'''Форимрование журнала SPO'''
# # Запись о вскрытие старого SPO
# list_out_nsd_spo = create_write_spo_1(read_file_jornal('nsd_spo'))
# pprint.pprint(list_out_nsd_spo, depth=12, width=144)
# write_file_dek(list_out_nsd_spo, 'nsd_spo')
# # Запись о сбросе введённого ранее SPO
# list_out_nsd_spo = create_write_spo_2(read_file_jornal('nsd_spo'))
# pprint.pprint(list_out_nsd_spo, depth=12, width=144)
# write_file_dek(list_out_nsd_spo, 'nsd_spo')
# # Запись о сбросе введённого ранее NSD
# list_out_nsd_spo = create_write_nsd_1(read_file_jornal('nsd_spo'))
# pprint.pprint(list_out_nsd_spo, depth=12, width=144)
# write_file_dek(list_out_nsd_spo, 'nsd_spo')
# # Запись о вводе нового NSD
# list_out_nsd_spo = create_write_nsd_2(read_file_jornal('nsd_spo'))
# pprint.pprint(list_out_nsd_spo, depth=12, width=144)
# write_file_dek(list_out_nsd_spo, 'nsd_spo')
