import pandas as pd

df = pd.read_csv("california_housing_train.csv")

filtered_data = df[(df['population'] >= 0) & (df['population'] <= 500)]

# Вычисление средней стоимости дома
average_house_value = filtered_data['median_house_value'].mean()

min_population = df['population'].min()

# Фильтрация данных по минимальному значению population
min_population_data = df[df['population'] == min_population]

# Находим максимальное значение households в этой выборке
max_households = min_population_data['households'].max()

print(f"Средняя стоимость дома с количеством людей от 0 до 500: ${average_house_value:.2f}\n"
      f"Максимальное количество households в зоне с минимальным значением population: {max_households}")


