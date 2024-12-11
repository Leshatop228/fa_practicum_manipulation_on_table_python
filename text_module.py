def save_table(filename, table):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(" | ".join(table['headers']) + "\n")
        for row in table['data']:
            file.write(" | ".join(row) + "\n")