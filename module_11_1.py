import pandas as pd


#   Pandas — это программная библиотека на языке Python для обработки и анализа данных.
# Она предоставляет специальные структуры данных и операции для манипулирования
# числовыми таблицами и временными рядами.
# С помощью pandas можно:
# фильтровать, сортировать, агрегировать и преобразовывать данные;
# интегрироваться с различными источниками для чтения и записи;
# визуализировать наборы данных.

data = {'Имя': ['Анна', 'Петр', 'Мария', 'Иван'],
        'Возраст': [25, 30, 35, 40],
        'Город': ['Москва', 'Санкт-Петербург', 'Киев', 'Минск']}

df = pd.DataFrame(data)
print(df.head())

#  Matplotlib - это популярная библиотека для создания графиков и визуализации
#  данных в языке программирования Python. Она позволяет создавать различные типы
#  графиков, включая линейные графики, столбчатые графики, круговые диаграммы,
#  гистограммы и многие другие.

import matplotlib.pyplot as plt

# Данные
x = [i for i in range(-100, 101, 5)]
y = [j**3 for j in x]

# Создание графика
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика
plt.scatter(x, y, color='blue', marker='o', label='y = x^3')  # Параметры точек

# Настройки графика
plt.title('Визуализация функции y = x^3', fontsize=16)  # Заголовок графика
plt.xlabel('x', fontsize=14)  # Метка оси X
plt.ylabel('y', fontsize=14)  # Метка оси Y
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Горизонтальная линия y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Вертикальная линия x=0
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  # Сетка
plt.legend()  # Легенда

# Показать график
plt.show()

