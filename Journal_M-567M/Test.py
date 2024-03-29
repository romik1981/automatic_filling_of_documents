'''
Программа для тестирования приложения для генерации документов
'''
import random
#from datetime import datetime
#from datetime import date
import time
import datetime
import pprint
# from read_write_file import read_file_jornal, create_dict_tech, list_out_technical, dict_out_technical



cap_let = [chr(let) for let in range(ord('A'), ord('Z') + 1)]  # Заглавные буквы латиницы
low_let = [chr(let) for let in range(ord('a'), ord('z') + 1)]  # Строчные буквы латиницы
cap_let_ru = [chr(let) for let in range(ord('А'), ord('Я') + 1)]  # Заглавные буквы кирилицы
low_let_ru = [chr(let) for let in range(ord('а'), ord('я') + 1)]  # Строчные буквы кирилицы
num = [str(num) for num in range(0, 10)]
symbol = ['-', '+', '=', '_', '*', '$', '/', '#', '&', '%', '!', '@']
low_let.remove('l'), cap_let.remove('I'), cap_let.remove('O')
cap_let_ru.remove('О'), cap_let_ru.remove('З')


def get_password(n_cap, n_low, n_num, n_sym, k_sym_pass, pass_lang) -> str:
    """
    Функция генерации парлей уникальных значений или с повторами
    :param n_cap: число заглавных букв
    :param n_low: число строчных букв
    :param n_num: число цифр
    :param n_sym: число символов
    :param can_repeat: флаг возможности повтора символов
    :return: возвращает строку пароля
    """
    cap_let_work = cap_let
    low_let_work = low_let
    if 'ru' in pass_lang:
        cap_let_work = cap_let_ru
        low_let_work = low_let_ru
    if 'y' in pass_lang:
        can_repeat = True
    else:
        can_repeat = False

    if not can_repeat:
        cap_let_list = list(random.sample(cap_let_work, n_cap))  # делаем выборку уникальных элементов из списка
        low_let_list = list(random.sample(low_let_work, n_low))
        num_list = list(random.sample(num, n_num))
        symbol_list = list(random.sample(symbol, n_sym))
        password_list = cap_let_list + low_let_list + num_list + symbol_list
        random.shuffle(password_list)
        password_str = ''.join(password_list)
        return password_str

    if can_repeat:
        password_list = []
        while len(password_list) < int(k_sym_pass):
            if n_cap != 0:
                password_list.append(random.choice(cap_let_work))
            if n_low != 0:
                password_list.append(random.choice(low_let_work))
            if n_num != 0:
                password_list.append(random.choice(num))
            if n_sym != 0:
                password_list.append(random.choice(symbol))
            if len(password_list) == int(k_sym_pass):
                break
        random.shuffle(password_list)
        password_str = ''.join(password_list)
        return password_str

def write_file_password(password, type_f=None):
    ''' Функция записи паролей в файл'''

    # if type_f == None:
    #     with open('password.xml', 'a+', encoding='utf-8') as fa:
    #         fa.writelines(f'{password}\n')  # Записывает в файл сгенерированный пароль.
    #     return print(f'Пароли сгенерированны в файл password.xml')

    # if type_f == 'sed':
    list_out = []
    with open('password_test.csv', 'r', encoding='cp1252') as fr:
        for str_ in fr:
            a = str_.strip().split(";")
            #print(a)
            for i, _ in enumerate(a):
                if _ == 'p':
                    a[i] = password #get_password(2, 2, 3, 1, 8, 'lat n')
            a.append('\n')
            list_out.append(';'.join(a))
    with open(f'jornal_out_{type_f}.csv', 'w+', encoding='cp1252') as fw:
        for _ in list_out:
            fw.writelines(_)
    return print(f'Пароли сгенерированны в файл password_out_{type_f}.csv')



# current_time = datetime.now().strftime('Date - %d/%m/%Y Time - %H:%M')
# write_file_password(current_time, 'test')



# a = date(2002, 12, 4).isoformat()
# b = date(2002, 12, 4).ctime()
# c = date.today()
# d = datetime(2023, 12, 16, 20, 59, 31)
# e = datetime.now()
# e1 = datetime.now().time()
# e2 = datetime.now().isoformat(sep=' ', timespec='minutes')
# e3 = datetime.now().time().isoformat(timespec='minutes')
# f = date.fromordinal(730920)
# d.strftime("%A %d. %B %Y")
# print(a)
# print(b)
# print(c)
# print(d)
# date_now = datetime.datetime.now()
# duration_10_minutes = datetime.timedelta(minutes=10)
# result_10_min = (date_now + duration_10_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')


if __name__ == '__main__':

    # Операции с датой и временем
    print()
    print('Работаю с этим:')
    # получение и форматирование даты и времени
    # print(e)
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e.strftime('Дата - %d/%m/%Y Время - %H:%M'))
    # print(e.strftime('%d-%m-%Y'))
    # print(e.strftime('%H:%M'))

    # date_now = datetime.datetime.now()
    # duration_10_minutes = datetime.timedelta(minutes=10)
    # duration_minutes = datetime.timedelta(days=1, minutes=10)
    # duration_minutes_1 = datetime.timedelta(days=1, minutes=10, seconds=10)
    # duration_minutes_2 = datetime.timedelta(days=1, minutes=10, seconds=10, milliseconds=10)
    # duration_minutes_3 = datetime.timedelta(days=1, minutes=10, seconds=10, milliseconds=10, microseconds=10)
    # # print(duration_minutes)
    # result_10_min = (date_now + duration_10_minutes).strftime('Date - %d.%m.%Y Time - %H:%M')
    # result = date_now + duration_minutes
    # result_1 = date_now + duration_minutes_1
    # result_2 = date_now + duration_minutes_2
    # result_3 = date_now + duration_minutes_3
    # print(result_10_min, type(result_10_min))
    # print(result, type(result))
    # print(result_1, type(result))
    # print(result_2, type(result))
    # print(result_3, type(result))
    # print(date_now.timestamp())
    # print(e - d)
    # print(time.time())
    # print(f.strftime("%A %d. %B %Y Time %h %m"))
    # write_file_password(result_10_min, 'test')

    # list_out_dek = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']]
    # print(list_out_dek[1][2])
    # list_out_dek[1][2] = '2a'
    # list_out_dek[1][1] = '1a'
    # list_out_dek[1][3] = '3a'
    # print(list_out_dek)
    #
    # # Кодирование декодирование данных
    #
    # data_dek = read_file_jornal()
    # print('Изменение кодировки:')
    # print(data_dek[1][2])
    # print(data_dek[0][0])
    # # d[0][0] = d[0][0].decode('cp1251').encode('utf8')
    # print(data_dek[0][0])
    #
    # text = "pitón"
    #
    # data_dek[0][0] = data_dek[0][0].encode()
    # print(type(data_dek[0][0]))
    # data_dek[0][0] = data_dek[0][0].decode()
    # print(data_dek[0][0], type(data_dek[0][0]), '1')
    #
    # text = "pitón"
    # text = text.encode()
    # print(text)
    # text = text.decode('utf-8')
    # print(text, type(text), '2')
    #
    # text = "pitón"
    # text = text.encode()
    # print(text)
    # text = text.decode('utf-16')
    # print(text, type(text), '3')
    #
    # data_dek = read_file_jornal()
    # data_dek[0][0] = data_dek[0][0].encode('cp1251')
    # print(data_dek[0][0])
    # data_dek[0][0] = data_dek[0][0].decode('cp1251')
    # print(data_dek[0][0], type(data_dek[0][0]), '4')
    #
    # data_dek = read_file_jornal()
    # data_dek[0][0] = data_dek[0][0].encode('utf-8')
    # print(data_dek[0][0])
    # data_dek[0][0] = data_dek[0][0].decode('utf-8')
    # print(data_dek[0][0], type(data_dek[0][0]), '5')

    # Создание собственной даты и времени
    # date_now = datetime.datetime.now()
    # print(date_now)
    # print(date_now.strftime('%d.%m.%Y - %H:%M'))
    # date = datetime.date(2024, 2, 23)
    # print(date, type(date))
    # date_time = datetime.datetime(year=2024, month=2, day=23, hour=10, minute=00, second=00)
    # print(date_time.strftime('%d.%m.%Y - %H:%M:'), type(date_time))
    # time = date_time.strftime('%X')
    # print(time, type(time))
    # h = 12
    # date_time = datetime.datetime(year=2024, month=2, day=23, hour=h, minute=00, second=00)
    # print(date_time.strftime('%d.%m.%Y - %H:%M:'), type(date_time))
    # m = 15
    # time = datetime.time(12, m, second=33, microsecond=122)
    # print(time, type(time))
    # print(time.hour)

    # Работа со словарём
    # list_out_technical = read_file_jornal('technical')
    # print(type(create_dict_tech(list_out_technical)))
    # pprint.pprint(create_dict_tech(list_out_technical), depth=12, width=144)
    # dict_out_technical = create_dict_tech(list_out_technical)
    # print(dict_out_technical['date_time_cl_MUVK'].strftime('Дата и время начала работ %d.%m.%Y - %H:%M:'))
    # print(len(dict_out_technical))
    # x = dict_out_technical.copy()
    # print(x)
    # print(dict_out_technical.get('title')[0])
    # for k, v in dict_out_technical.items():
    #     print(f'Ключ: {k}; значение: {v}')
    # print('Вставляю значения в словарь')
    # print(dict_out_technical.setdefault('date_time_use_KD'))
    # print(dict_out_technical.setdefault('Мой ключ', 'Добавил данныев словарь'))
    # pprint.pprint(dict_out_technical, depth=12, width=144)
    # Работа со списками
    list_number_device = ['428М-001676', '428М-001677', '428М-001678']
    s = str(list_number_device)
    print(s)
    print(s[1:len(s)-1])