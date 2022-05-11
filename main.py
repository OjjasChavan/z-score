import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random
import pandas as pd

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

population_mean = stats.mean(data)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        data_set.append(value)
    mean = stats.mean(data_set)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ['temp'], show_hist=False)
    fig.show()

mean = stats.mean(data)
std_deviation = stats.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * std_deviation), mean + (3 * std_deviation)

print ("stdl",first_std_deviation_start, first_std_deviation_end)
print ("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

z_score = (mean - population_mean) / std_deviation
print("z_score is: ", z_score)