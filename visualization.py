import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
  def __init__(self, data):
    self.data = data

  def add_histogram(self, column):
    plt.hist(self.data[column].dropna())
    plt.title(f'Гистограмма для {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

  def add_line_plot(self, x_column, y_column):
    plt.bar(self.data[x_column], self.data[y_column])
    plt.title(f'Столбчатая диаграмма  {y_column} vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

  def add_scatter_plot(self, x_column, y_column):
    plt.scatter(self.data[x_column], self.data[y_column])
    plt.title(f'Диаграмма рассеивания  {y_column} vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()