import csv

def load_table(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)
        return {'headers': headers, 'data': data}

def save_table(filename, table):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(table['headers'])
        writer.writerows(table['data'])