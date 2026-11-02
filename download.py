"""Download the exercise dataset. Requires Python 3 and no extra packages."""

import json
from pathlib import Path
from urllib.request import urlopen


DATA_URL = "https://raw.githubusercontent.com/kvptkr/finance-python-exercise/main/dataset.json"


def main():
    with urlopen(DATA_URL, timeout=30) as response:
        data = json.load(response)

    destination = Path("portfolio.json")
    destination.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Downloaded {len(data['transactions'])} transactions to {destination.resolve()}")


if __name__ == "__main__":
    main()
