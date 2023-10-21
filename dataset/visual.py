import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_profit.csv')

plt.scatter(df['production_budget'], df['worldwide_gross'],s=10)

plt.xlabel('Бюджет фильмов ужасов')
plt.ylabel('Мировая касса')
plt.title('Бюджет фильмов ужасов и мировая касса')

plt.show()