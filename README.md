# Coffeeshop Weekly Earnings

A Python module that calculates total weekly earnings for a coffeeshop by fetching and processing sales data from a remote JSON source.

## Description

This program fetches coffeeshop sales data (drinks sold, desserts sold, and tips) for each day of the week from a remote JSON file, then calculates and displays a formatted earnings report.

### Functions

| Function | Description |
|---|---|
| `fetch_data(url)` | Fetches raw JSON data from a given URL |
| `deserialize_data(json_string)` | Parses a JSON string into a Python dictionary |
| `get_data_from_key(data, key)` | Extracts a single day's data from the weekly dataset |
| `get_price(prices, item)` | Looks up the price of a menu item |
| `calculate_day(day_data, prices)` | Computes total earnings for one day (drinks + desserts + tips) |
| `calculate_week(data, prices)` | Computes total earnings for the entire week |

## Requirements

- Python 3
- `requests` module

## Usage

```bash
python3 coffeeshop.py
```

### Sample Output

```
==================================================
   COFFEESHOP WEEKLY EARNINGS REPORT
==================================================
      Monday: $  122.25
     Tuesday: $  173.00
   Wednesday: $  201.75
    Thursday: $  185.75
      Friday: $  374.25
    Saturday: $  488.50
      Sunday: $  351.75
--------------------------------------------------
  WEEK TOTAL: $ 1897.25
==================================================
```

## Author

Shaeeg
