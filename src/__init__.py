"""Import data to be used in plots
"""

import pandas as pd

print("Welcome to malaria-visualiser!")


def make_deaths_df():
    """Read in dataframe (to be replaced by call to Heroku postgresql)
    """
    deaths: pd.DataFrame = pd.read_csv("data/malaria-deaths-by-region.csv").rename(
        {
            "Deaths - Malaria - Sex: Both - Age: All Ages (Number) (deaths)": "Deaths by malaria"
        },
        axis=1,
    )
    codes_and_continents: pd.DataFrame = pd.read_csv(
        "data/country-and-continent-codes-list.csv"
    ).rename({"Three_Letter_Country_Code": "Code"}, axis=1)
    deaths: pd.DataFrame = codes_and_continents[["Code", "Continent_Code"]].merge(
        deaths, on="Code"
    )
    return deaths


DEATHS = make_deaths_df()
