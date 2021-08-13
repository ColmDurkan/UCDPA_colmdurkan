import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def visualise_timeline(flights):
    data = flights.groupby(['this_period'])['total_pax_this_period'].sum()
    data = pd.DataFrame(data).reset_index()
    data.columns = ['this_period', 'total_passengers']
    data = data.sort_values(['this_period'])
    plt.size = 20
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.this_period, data.total_passengers, color='blue', label='Passengers')
    ax.set_xlabel('Time')
    ax.set_ylabel('Passengers')
    ax.set_title('2021 Passengers over time')
    ax.grid(True)
    ax.legend(loc='upper right');
    plt.show()


def visualise_top_5_pie_chart(flights):
    top_5_regions = flights.groupby(['foreign_region']).sum()
    top_5_regions = top_5_regions.sort_values(by='total_pax_this_period', ascending=False)[:5]
    top_5_regions.plot(kind='pie', y='total_pax_this_period', title='Top 5 Regions', ylabel='Regions', shadow=True, figsize=(15, 10),
                       autopct='%1.1f%%')


def visualise_top_10(flights):
    top_10_countries = flights.groupby(['foreign_country'])['total_pax_this_period'].sum()
    top_10_countries = pd.DataFrame(top_10_countries).reset_index()
    top_10_countries.columns = ['foreign_country', 'total_passengers']
    top_10_countries = top_10_countries.sort_values(by='total_passengers', ascending=False)[:10]
    fig, ax = plt.subplots()
    x = top_10_countries['foreign_country']
    y = top_10_countries['total_passengers']
    width = 0.75  # the width of the bars
    ind = np.arange(len(y))  # the x locations for the groups
    ax.barh(ind, y, width, color="lightgreen")
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)
    plt.title('Total Passengers by country 2021')
    plt.xlabel('Total Passengers')
    plt.ylabel('Countries')
    for i, v in enumerate(y):
        ax.text(v + 3, i + .25, str(v), color='black', fontweight='bold')
    plt.show()


def visualise_top_10_py(flights):
    top_10_countries = flights.groupby(['foreign_country'])['total_pax_last_period'].sum()
    top_10_countries = pd.DataFrame(top_10_countries).reset_index()
    top_10_countries.columns = ['foreign_country', 'total_passengers_prior_year']
    top_10_countries = top_10_countries.sort_values(by='total_passengers_prior_year', ascending=False)[:10]
    fig, ax = plt.subplots()
    x = top_10_countries['foreign_country']
    y = top_10_countries['total_passengers_prior_year']
    width = 0.75
    ind = np.arange(len(y))
    ax.barh(ind, y, width, color="pink")
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)
    plt.title('Total Passengers by country 2020')
    plt.xlabel('Total Passengers')
    plt.ylabel('Countries')
    for i, v in enumerate(y):
        ax.text(v + 3, i + .25, str(v), color='black', fontweight='bold')
    plt.show()


def visualise_rank_of_uk_airports(flights):
    rank_uk_airports = flights.groupby(['UK_airport'])['total_pax_this_period'].sum()
    rank_uk_airports = pd.DataFrame(rank_uk_airports).reset_index()
    rank_uk_airports.columns = ['UK_airport', 'total_passengers']
    rank_uk_airports = rank_uk_airports.sort_values(by='total_passengers', ascending=False)[:20]
    fig, ax = plt.subplots()
    x = rank_uk_airports['UK_airport']
    y = rank_uk_airports['total_passengers']
    width = 0.65
    ind = np.arange(len(y))
    ax.barh(ind, y, width, color="lightblue")
    ax.set_yticks(ind + width / 1)
    ax.set_yticklabels(x, minor=False)
    plt.title('Total Passengers by UK airport')
    plt.xlabel('Total Passengers')
    plt.ylabel('Airports')
    for i, v in enumerate(y):
        ax.text(v + 3, i + .25, str(v), color='black', fontweight='bold')
    plt.show()