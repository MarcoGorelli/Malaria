"""Line plot of malaria deaths over time
"""

from src import DEATHS


def plot_country_deaths_over_time(country):
    """Select data (from all years) for given country.
    """
    return DEATHS.query("Entity == '{}'".format(country))[["Year", "Deaths by malaria"]]
