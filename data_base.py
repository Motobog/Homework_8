import pandas as pd


def readCSV(file_name):
    return pd.read_csv(file_name, sep=';', encoding='utf-8')
