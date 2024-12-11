def get_rows_by_number(table, start, stop=None, copy_table=False):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if start < 0 or (stop is not None and stop < start):
        raise ValueError("Некорректные значения 'start' и 'stop'.")

    if stop is None:
        stop = start + 1

    result_data = table["data"][start:stop]

    if copy_table:
        return {
            "headers": table["headers"],
            "data": [row[:] for row in result_data]
        }
    else:
        return {
            "headers": table["headers"],
            "data": result_data
        }


def get_rows_by_index(table, *values, copy_table=False):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if not values:
        raise ValueError("Необходимо указать хотя бы одно значение для фильтрации строк.")

    result_data = [row for row in table["data"] if row[0] in values]

    if copy_table:
        return {
            "headers": table["headers"],
            "data": [row[:] for row in result_data]
        }
    else:
        return {
            "headers": table["headers"],
            "data": result_data
        }


def get_column_type(table, by_number=False):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")

    data = table["data"]
    headers = table["headers"]
    if not data:
        raise ValueError("Таблица не содержит данных для определения типа столбцов.")

    dct = {}
    for i in range(len(headers)):
        check_val = data[0][i]
        if isinstance(check_val, int):
            column_type = "int"
        elif isinstance(check_val, float):
            column_type = "float"
        elif isinstance(check_val, bool):
            column_type = "bool"
        else:
            column_type = "str"

        key = i if by_number else headers[i]
        dct[key] = column_type

    return dct




def set_column_type(table, type_dict=None, by_number=False):

    data = table["data"]
    headers = table["headers"]
    dct = {}

    for i in range(len(headers)):
        check_val = data[0][i]

        if check_val.isdigit():
            column_type = "int"
        elif check_val.replace('.', '', 1).isdigit() and '.' in check_val:
            column_type = "float"
        elif check_val.lower() in ["true", "false"]:
            column_type = "bool"
        else:
            column_type = "str"

        key = (i if by_number==True else headers[i])
        dct[key] = column_type


    if type_dict:
        for key, new_type in type_dict.items():
            if key in dct:
                dct[key] = new_type

    return dct
def set_values(table, value, column=0):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if not value or not isinstance(value, list):
        raise ValueError("Параметр 'value' должен быть списком.")
    if isinstance(column, str) and column not in table["headers"]:
        raise ValueError(f"Столбец '{column}' отсутствует в заголовках таблицы.")
    if isinstance(column, str):
        column = table["headers"].index(column)



    for i, val in enumerate(value):
        table["data"][i][column] = val

    return table


def set_value(table, value, column=0):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if column not in table["headers"] and not isinstance(column, int):
        raise ValueError(f"Столбец '{column}' отсутствует в таблице.")
    if isinstance(column, str):
        column = table["headers"].index(column)

    for row in table["data"]:
        row[column] = type(row[column])(value)

    return table


def get_values(table, column=0):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if isinstance(column, str) and column not in table["headers"]:
        raise ValueError(f"Столбец '{column}' отсутствует в заголовках таблицы.")
    if isinstance(column, str):
        column = table["headers"].index(column)

    return [row[column] for row in table["data"]]


def get_value(table, column=0, row=0):
    if table is None or "data" not in table or "headers" not in table:
        raise ValueError("Параметр 'table' должен быть корректной таблицей с 'headers' и 'data'.")
    if not (0 <= row < len(table["data"])):
        raise ValueError(f"Индекс строки '{row}' выходит за пределы данных таблицы.")
    if isinstance(column, str) and column not in table["headers"]:
        raise ValueError(f"Столбец '{column}' отсутствует в заголовках таблицы.")
    if isinstance(column, str):
        column = table["headers"].index(column)

    return table["data"][row][column]
def print_table(table):
    return table