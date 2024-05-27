import pandas as pd

# Чтение CSV файла
df = pd.read_csv('animal.csv')

# Вывод содержимого DataFrame
print(df)

df.to_csv('output.csv', index=False)

