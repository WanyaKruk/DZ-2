import pandas as pd
class FindEmptyCell: 
    def __init__(self, df):
        self.df = df
    
    def count_empty_cell(self):
        count_cell = self.df.isnull().sum()
        return count_cell
    
    def generate_report(self):
        count_cell = self.count_empty_cell()
        report = pd.DataFrame()
        return report