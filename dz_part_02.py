import pandas as pd

# Чтение CSV файла
df = pd.read_csv('dz.csv')

# Группировка по городу и вычисление среднего значения зарплаты
group = df.groupby('City')['Salary'].mean()

print(group)
