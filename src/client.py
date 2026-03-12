# client.py

# description

# import statements
from gridstatusio import GridStatusClient
from websockets.sync.client import connect
import pandas as pd

def hello(uri):
    with connect(uri) as ws:
        name = input("Enter your name: ")

        ws.send(name)
        print(f">>> {name}")

        greeting = websocket.recv()
        print(f"<<< {greeting}")

def main():
    uri = "ws://localhost:8765"
    hello(uri)

    # Recommended: set GRIDSTATUS_API_KEY as an
    # environment variable instead of hardcoding
    client = GridStatusClient("5464eea1cd7e4b3bbfd335968764be4d")

    # Fetch data as pandas DataFrame
    df = client.get_dataset(
      dataset="aeso_supply_and_demand",
      start="2026-03-10",
      end="2026-03-13",
      timezone="market",
    )

if __name__ == "__main__":
    main()