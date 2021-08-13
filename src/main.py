from controller.Controller import Controller


controller = Controller()
controller.clean_up_data()
print(controller.flightsList.head())
controller.visualise_timeline()
controller.visualise_top_5_pie_chart()
controller.visualize_top_10_countries()
controller.visualize_top_10_py()
controller.visualise_rank_of_uk_airports()
