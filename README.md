# Python finance exercise

A short Python exercise using synthetic private-market investment transactions. Allow approximately 15–20 minutes. No real client or investment data is included.

## Dataset

Download [dataset.json](https://raw.githubusercontent.com/kvptkr/finance-python-exercise/main/dataset.json) programmatically. This public URL requires no authentication.

The dataset contains 500 distinct transactions across three funds. The JSON contains `reporting_date`, `currency`, `portfolio_nav` (an `amount` and `date`), and a `transactions` array. All amounts are positive, in USD, and all dates use `YYYY-MM-DD`.

Each transaction contains `fund`, `date`, `type`, `amount`, and `status`:

- `capital_call`: money paid into a fund.
- `distribution`: money received from a fund.
- `status`: `completed`, `pending`, or `cancelled`.

Portfolio NAV (net asset value) is the estimated value of all investments still held at the reporting date. It is separate from distributions already received.

## Your task

Write a Python script that:

1. Downloads and parses the JSON from the URL above.
2. Includes only `completed` transactions dated on or before the supplied `reporting_date` (30 September 2026).
3. Prints one row per fund, sorted alphabetically, showing total capital calls, total distributions, and net cash invested (capital calls minus distributions). Include a portfolio total row. Display monetary amounts to two decimal places; exact table formatting is up to you.
4. Calculates one annualised IRR for the whole portfolio using the actual dates (XIRR). Use only the transactions selected in step 2. Treat capital calls as negative cash flows and distributions as positive cash flows, and add `portfolio_nav.amount` as a final positive cash flow on `portfolio_nav.date`. Use a 365-day year and display the result as a percentage to two decimal places.

You may use any Python libraries, including an existing XIRR implementation. You do not need to implement a numerical solver. The dataset is valid; there are no missing fields or malformed records.

Submit your script and the command needed to run it, including any dependencies. A frontend, database, or formal test suite is not required.

## Optional download helper

The included [download.py](download.py) only fetches the data and saves it as `portfolio.json`; it does not perform the exercise calculations. It requires Python 3 with no extra packages.

```sh
git clone https://github.com/kvptkr/finance-python-exercise.git
cd finance-python-exercise
python3 download.py
```
