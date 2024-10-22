import pandas as pd

def load_csv(file_path):
        data = pd.read_csv(file_path)
        return data

def load_excel(file_path):
        data = pd.read_excel(file_path)
        return data
