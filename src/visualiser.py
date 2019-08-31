from src import DEATHS


def plot_country_deaths_over_time(country):
    return DEATHS.query("Entity == '{}'".format(country))[["Year", "Deaths by malaria"]]
