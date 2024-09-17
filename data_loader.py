import pandas as pd
def load_data(file_path):
    """
    Загрузка данных из CSV файла.
    """
    return pd.read_csv(file_path)
