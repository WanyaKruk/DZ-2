import pandas as pd
class DataLoader:
  def load_datacsv(file_path):
    data = pd.read_csv(file_path)
    return data
  
  def load_dataxcl(file_path):
    data = pd.read_excel(file_path)
    return data