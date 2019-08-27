from src import DATA


def plot_country_deaths_over_time(country):
    return DATA.query("Entity == '{}'".format(country))[["Year", "Deaths by malaria"]]
