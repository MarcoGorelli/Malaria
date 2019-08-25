import pandas as pd

DATA = pd.read_csv("../data/malaria-deaths-by-region.csv").rename(
    {
        "Deaths - Malaria - Sex: Both - Age: All Ages (Number) (deaths)": "Deaths by malaria"
    },
    axis=1,
)
