import pandas as pd

DEATHS = pd.read_csv("data/malaria-deaths-by-region.csv").rename(
    {
        "Deaths - Malaria - Sex: Both - Age: All Ages (Number) (deaths)": "Deaths by malaria"
    },
    axis=1,
)
CODES_AND_CONTINENTS = pd.read_csv("data/country-and-continent-codes-list.csv").rename(
    {"Three_Letter_Country_Code": "Code"}, axis=1
)
DEATHS = CODES_AND_CONTINENTS[["Code", "Continent_Code"]].merge(DEATHS, on="Code")
