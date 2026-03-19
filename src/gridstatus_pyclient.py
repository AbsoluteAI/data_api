# gridstatus_pyclient.py

# description

# import statements
import gridstatusio as gs
import pandas as pd

# Recommended: set GRIDSTATUS_API_KEY as an
# environment variable instead of hardcoding
client = gs.GridStatusClient("5464eea1cd7e4b3bbfd335968764be4d")

QUERY_LIMIT = 10_000

# Fetch data as pandas DataFrame
df = client.get_dataset(
    dataset="aeso_supply_and_demand",
    start="2026-03-16",
    end="2026-03-19",
    timezone="market",
    limit = QUERY_LIMIT,
)

with pd.option_context("display.max_columns", None):
    print(df)