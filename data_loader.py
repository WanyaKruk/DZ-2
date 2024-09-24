import pandas as pd
class DataLoader:
  def load_datacsv(file_path):
    return pd.read_csv(file_path)
  
  def load_dataxcl(file_path):
    return pd.read_excel(file_path)