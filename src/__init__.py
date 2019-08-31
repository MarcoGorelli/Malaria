import pandas as pd

DEATHS = pd.read_csv("data/malaria-deaths-by-region.csv").rename(
    {
        "Deaths - Malaria - Sex: Both - Age: All Ages (Number) (deaths)": "Deaths by malaria"
    },
    axis=1,
)
COORDS = pd.read_csv("data/coordinates.csv", sep="\t")
