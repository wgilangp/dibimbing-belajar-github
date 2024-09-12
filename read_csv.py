import pandas as pd

def read_csv_to_dataframe(filename):
    # Membaca file CSV dengan delimiter ';'
    data = pd.read_csv(filename, delimiter=';')
    return data