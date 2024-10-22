import pandas as pd

class DataFrameAnalyzer:
  def __init__(self, data):
   self.data = data

  def missing_values_report(self):
   missing_values = self.df.isnull().sum()
   missing_percentage = (missing_values / len(self.df)) * 100
   report = pd.DataFrame({
'Missing Values': missing_values,
'Percentage': missing_percentage
})
   return report

  def fill_missing_values(self, method='mean'):
   if method == 'mean':
    self.df.fillna(self.df.mean(), inplace=True)
   elif method == 'median':
    self.df.fillna(self.df.median(), inplace=True)
   elif method == 'mode':
    self.df.fillna(self.df.mode().iloc[0], inplace=True)
   else:
    raise ValueError("Метод должен быть 'mean', 'median', or 'mode'")


    