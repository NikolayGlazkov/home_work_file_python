"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import re

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    files = ['info_1.txt', 'info_2.txt', 'info_3.txt'] 
    for file in files:
        with open(file, 'r', encoding='cp1251') as f:
            for line in f:
                if re.match(r'^Изготовитель системы:', line):
                    os_prod_list.append(line.split(':')[1].strip())
                elif re.match(r'^Название ОС:', line):
                    os_name_list.append(line.split(':')[1].strip())
                elif re.match(r'^Код продукта:', line):
                    os_code_list.append(line.split(':')[1].strip())
                elif re.match(r'^Тип системы:', line):
                    os_type_list.append(line.split(':')[1].strip())
        main_data.append([os_prod_list[-1], os_name_list[-1], os_code_list[-1], os_type_list[-1]])

    return main_data

def write_to_csv(file_path):
    main_data = get_data()

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(main_data[0])
        for data in main_data[1:]:
            writer.writerow(data)

write_to_csv('data_report.csv')
