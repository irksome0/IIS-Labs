import matplotlib.pyplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data():
    new_data = pd.read_csv("police_project.csv", low_memory=False)
    new_data = pd.DataFrame(new_data)
    return new_data


def filter_data(data_frame):
    filtered_data = data_frame[['date', 'subject_sex', 'search_conducted', 'search_basis', 'raw_search_vehicle_description', 'reason_for_stop']]
    return filtered_data


def moving_violation(data_frame):
    current_data = data_frame[lambda x: x['reason_for_stop'] == 'Moving Violation']

    males = len(data_frame[lambda x: x['subject_sex'] == 'male'])
    females = len(data_frame[lambda x: x['subject_sex'] == 'female'])

    current_data["subject_sex"].value_counts().plot(kind="bar", fontsize=10)
    plt.title("Moving violation statistics by gender")
    plt.show()
    if males > females:
        return males
    else:
        return females


def search_quantity(data_frame):
    current_data = data_frame[lambda x: x['search_conducted'] == True]

    current_data['subject_sex'].value_counts().plot(kind="bar", fontsize=10)
    plt.title("Search conduction statistics by gender")
    plt.show()


def search_type(data_frame):
    current_data = data_frame[lambda x: x['search_conducted'] == True]
    current_data['raw_search_vehicle_description'].value_counts().plot(kind="bar", fontsize=10, color="darkgreen")
    plt.title("Search types")
    plt.show()


def add_field(data_frame):
    data_frame['frisk'] = data_frame['search_conducted']
    data_frame['search_conducted'] = 0
    data_frame.drop('search_conducted', axis='columns', inplace=True)
    return data_frame


def getYear(x):
    return x[:4]


def graph(data_frame):
    data_frame['date'].value_counts().plot()
    plt.show()


data = get_data()
print(filter_data(data))
print(moving_violation(data))
search_quantity(data)
search_type(data)
data = add_field(data)
print(data[lambda x: x['frisk'] == True])
graph(data)
