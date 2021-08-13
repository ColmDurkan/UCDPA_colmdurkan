import pandas as pd
from src.helpers.ReadDataHelper import get_data_frame
from src.helpers.VisualizationHelper import visualise_timeline
from src.helpers.VisualizationHelper import visualise_top_5_pie_chart
from src.helpers.VisualizationHelper import visualise_top_10
from src.helpers.VisualizationHelper import visualise_top_10_py
from src.helpers.VisualizationHelper import visualise_rank_of_uk_airports


def merge_lists(list_a, list_b):
    frames = [list_a, list_b]
    return pd.concat(frames)


class Controller:
    flights2021List = get_data_frame('../resources/Flights2021.csv')
    flightsJune2021List = get_data_frame('../resources/FlightsJune2021.csv')
    flightsList = None

    def __init__(self):
        self.flightsList = merge_lists(self.flightsJune2021List, self.flights2021List)

    def clean_up_data(self):
        self.flightsList = self.flightsList[self.flightsList.foreign_region != 'Unknown']
        del self.flightsList['rundate']
        del self.flightsList['total_pax_scheduled_this_period']
        del self.flightsList['total_pax_charter_this_period']
        del self.flightsList['total_pax_scheduled_last_period']
        del self.flightsList['total_pax_charter_last_period']
        del self.flightsList['total_pax_percent']
        self.flightsList = self.flightsList.sort_values(['foreign_country', 'this_period'])

    def visualise_timeline(self):
        visualise_timeline(self.flightsList)

    def visualise_top_5_pie_chart(self):
        visualise_top_5_pie_chart(self.flightsList)

    def visualize_top_10_countries(self):
        visualise_top_10(self.flightsList)

    def visualize_top_10_py(self):
        visualise_top_10_py(self.flightsList)

    def visualise_rank_of_uk_airports(self):
        visualise_rank_of_uk_airports(self.flightsList)
