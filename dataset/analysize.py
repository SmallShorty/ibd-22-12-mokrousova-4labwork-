import pandas as pd
import numpy as np

# Read the csv file
df = pd.read_csv('movie_profit.csv')

# Filter the data for R-rated and PG-13-rated horror movies
r_movies = df[df['mpaa_rating'] == 'R']['production_budget']
pg13_movies = df[df['mpaa_rating'] == 'PG-13']['production_budget']

# Calculate the means of the two groups
r_mean = r_movies.mean()
pg13_mean = pg13_movies.mean()

# Calculate the standard deviations of the two groups
r_std = r_movies.std()
pg13_std = pg13_movies.std()

# Calculate the standard error of the mean for the two groups
r_sem = r_std / (r_movies.count() ** 0.5)
pg13_sem = pg13_std / (pg13_movies.count() ** 0.5)

# Calculate the t-statistic
t_stat = (r_mean - pg13_mean) / ((r_sem ** 2 + pg13_sem ** 2) ** 0.5)

# Calculate the degrees of freedom
df = r_movies.count() + pg13_movies.count() - 2

# Calculate the p-value
p_value = 2 * (1 - (1 - np.abs(t_stat)) ** df)

# Print the results
print('t-статистика [мера разлиичия меж выборками]:', t_stat)
print('p-значение [ероятность получения таких же или более экстремальных результатов]:', p_value)

print('Гипотеза: Бюджет производства фильмов ужасов с рейтингом R значимо отличается от бюджета производства фильмов ужасов с рейтингом PG-13.')
print('Т.к. p-значение<0.05, то нет значимых различий между бюджетом производства фильмов ужасов с рейтингом R и PG-13. \nСледовательно, мы можем заключить, что есть значимые различия между бюджетом производства фильмов ужасов с рейтингом R и PG-13.')
#