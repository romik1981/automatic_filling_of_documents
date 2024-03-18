from read_write_file import read_file_jornal, write_file_dek, create_write_dek_1, create_write_dek_2, create_write_dek_3_new,\
    create_write_rdt_1, create_write_ckt_old, create_write_ckt_new, create_write_spo_1, create_write_spo_2, create_write_nsd_1,\
    create_write_nsd_2, create_write_spo_3, create_write_dek_4_new, create_write_spo_4, create_write_rdt_2, create_dict_tech,\
    create_write_technical
import pprint

point_exit = 'y'

while True:
    if point_exit == 'n':
        break
    else:
        n = 1
        ''' Формирование журнала DEK '''
        # # Запись о вкрытие старого DEK
        # list_out_dek = create_write_dek_1(read_file_jornal('dek'))1676
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Вскрытие старого DEK')
        # # Запись о стирание старого DEK
        # list_out_dek = create_write_dek_2(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Стирание старого DEK')
        # # Запись о первом вводе нового DEK
        # list_out_dek = create_write_dek_3_new(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Ввод №1 нового DEK')
        # # Запись о втором вводе нового DEK
        # list_out_dek = create_write_dek_4_new(read_file_jornal('dek'))
        # pprint.pprint(list_out_dek, depth=12, width=144)
        # write_file_dek(list_out_dek, 'dek', 'Ввод №2 нового DEK')

        ''' Формирование журнала RDT '''
        # Запись о сбросе старого RDT
        list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_rdt, 'rdt', 'Сброс старого RDT')
        # Запись о вводе RDT
        list_out_rdt = create_write_rdt_2(read_file_jornal('rdt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_rdt, 'rdt', 'Ввод нового RDT')

        ''' Формирование журнала CKT '''
        # Запись о проверке старым CKT
        list_out_ckt = create_write_ckt_old(read_file_jornal('ckt'))
        pprint.pprint(list_out_rdt, depth=12, width=144)
        write_file_dek(list_out_ckt, 'ckt', 'Проверка старым CKT')
        # Запись о проверке новым CKT
        # list_out_ckt = create_write_ckt_new(read_file_jornal('ckt'))
        # pprint.pprint(list_out_rdt, depth=12, width=144)
        # write_file_dek(list_out_ckt, 'ckt', 'Проверка новым CKT')

        '''Форимрование журнала SPO'''
        # # Запись о вскрытие старого SPO
        # list_out_nsd_spo = create_write_spo_1(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Вскрытие старого СПО')
        # # Запись о сбросе введённого ранее SPO
        # list_out_nsd_spo = create_write_spo_2(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс введённого ранее СПО')
        # # Запись о сбросе введённого ранее NSD
        # list_out_nsd_spo = create_write_nsd_1(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Сброс введённого ранее НСД')
        # # Запись о вводе нового NSD
        # list_out_nsd_spo = create_write_nsd_2(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод нового НСД')
        # # Запись о вводе №1 SPO
        # list_out_nsd_spo = create_write_spo_3(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №1 СПО')
        # # Запись о вводе №1 SPO
        # list_out_nsd_spo = create_write_spo_4(read_file_jornal('nsd_spo'))
        # pprint.pprint(list_out_nsd_spo, depth=12, width=144)
        # write_file_dek(list_out_nsd_spo, 'nsd_spo', 'Ввод №2 СПО')
        '''Форимрование  технического журнала'''
        # Записи в технический журнал
        list_in_technical = read_file_jornal('technical')
        dict_out_technical = create_dict_tech(list_in_technical)
        list_out_technical = create_write_technical(list_in_technical, dict_out_technical, 'ОН')
        pprint.pprint(list_out_technical, depth=12, width=144)
        write_file_dek(list_out_technical, 'technical', 'Технический журнал')

        print(f'Вы набрали {n} аппарат.')
        n += 1

        point_exit = input('Продолжить ввод (y/n): ')
