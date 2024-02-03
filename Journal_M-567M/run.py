from read_write_file import read_file_jornal, read_file_rdt, write_file_dek,create_write_dek_1, create_write_dek_2,\
    create_write_rdt_1
import pprint



''' Формирование журнала DEK '''
list_out_dek = create_write_dek_1(read_file_jornal('dek'))
write_file_dek(list_out_dek, 'dek')
list_out_dek = create_write_dek_2(read_file_jornal('dek'))

pprint.pprint(list_out_dek, depth=12, width=144)

# print(list_out_dek)
write_file_dek(list_out_dek, 'dek')

''' Формирование журнала RDT '''
list_out_rdt = create_write_rdt_1(read_file_jornal('rdt'))
pprint.pprint(list_out_rdt, depth=12, width=144)
write_file_dek(list_out_rdt, 'rdt')


''' Формирование журнала CKT '''
# read_file_jornal()