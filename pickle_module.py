import pickle

def load_table(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def save_table(filename, table):
    with open(filename, 'wb') as file:
        pickle.dump(table, file)