from operator import index

from module.text_module import save_table as text_save_table
from module.csv_module import load_table as csv_load_table, save_table as csv_save_table
from module.pickle_module import load_table as pickle_load_table, save_table as pickle_save_table
from module.base_operation_on_table import get_rows_by_number, get_rows_by_index, get_column_type, set_column_type, \
    get_values, get_value, set_values,set_value,print_table


def print_table(table):
    print(" | ".join(table['headers']))
    for row in table['data']:
        print(" | ".join(row))

# Пример использования
filename = input("Введите имя файла с расширением (csv, pickle, txt): ")

if filename.endswith('.csv'):
    table = csv_load_table(filename)
    #print_table(table)
    csv_save_table('output.csv', table)
elif filename.endswith('.pickle'):
    table = pickle_load_table(filename)
    #print_table(table)
    pickle_save_table('output.pickle', table)
elif filename.endswith('.txt'):
    table = pickle_load_table(filename)
    #print_table(table)
    text_save_table('output.txt', table)
else:
    print("Неизвестный формат файла")

def user_menu(table):
    while True:
        print("\nВыберите операцию:")
        print("1. Вывод таблицы по номеру строк")
        print("2. Получение строк по значениям в первом столбце")
        print("3. Определить типы столбцов")
        print("4. Установить типы столбцов")
        print("5. Получить значения столбца")
        print("6. Получить конкретное значение")
        print("7. Установить значения столбца")
        print("8. Установить значение в столбец для всех строк")
        print("9. Вывести таблицу")
        print("0. Выход")
        choice = input("Введите номер операции: ").strip()
        if choice == "0":
            print("Выход")
            break
        elif choice == '1':
            sub_table = get_rows_by_number(table, 1, 4, copy_table=True)
            print_table(sub_table)
        elif choice == "2":
            values = input("Введите значения через запятую: ").split(",")
            sub_table = get_rows_by_index(table, *values, copy_table=True)
            print(sub_table)
        elif choice == "3":
            get_column = get_column_type(table, by_number=True)
            print(get_column)
        elif choice == "4":
            type_dict_index = {4: "int", 7: "str"}
            type_dict_number = {"Phone": "str", "Sex": "str"}
            set_column = set_column_type(table, type_dict_index, by_number=True)
            print(set_column)
        elif choice == "5":
            # Используем переменную только в области её выполнения
            column_values = get_values(table, column="First Name")
            print(column_values)
        elif choice == "6":
            cell_value = get_value(table, column="First Name", row=0)
            print(cell_value)
        elif choice == "7":
            updated_values = set_values(table, ["ALEXEY", "John", "Alexander"], column=0)
            print(updated_values)
        elif choice == "8":
            updated_list = set_value(table, "MASK", column="Last Name")
            print(updated_list)
        elif choice == "9":
            print_table(table)


# print("Вывод таблицы по номеру")
# sub_table = get_rows_by_number(table, 1, 4, copy_table=True)
#
# print_table(sub_table)
#
# print("\nКакие строки хотите получить по значениям в первом столбце?")
# values = input("Введите значения через запятую: ").split(",")
# sub_table = get_rows_by_index(table, *values, copy_table=True)
# print(sub_table)
#
# print("\nИсходная таблица после изменений:")
# print_table(table)
#
# get_column = get_column_type(table,by_number=True)
# print(get_column)
# type_dict_index={4:"int",7:"str"}
# type_dict_number ={"Phone": "str", "Sex": "str"}
# set_column = set_column_type(table,type_dict_index,by_number=True)
# print(set_column)
# get_values = get_values(table,column="First Name")
# print(get_values)
# get_value = get_value(table,column="First Name",row=0)
# print(get_value)
# set_values = set_values(table,["ALEXEY","John","Alexander"],column=0)
#
# print(set_values)
# set_value = set_value(table,"MASK",column="Last Name")
# print(set_value)
# print_table1 = print_table(table)
# print(print_table1)
user_menu(table)