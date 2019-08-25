import seaborn as sns

from src import DATA

sns.set()


def plot_country_deaths_over_time(country):
    return (
        DATA.query("Entity == '{}'".format(country))
        .set_index("Year")[["Deaths by malaria"]]
        .plot(figsize=(12, 8))
    )
