import requests
import json


def fetch_data(url):
    response = requests.get(url)
    data = response.text
    return data


def deserialize_data(json_string):
    """
    Turn a JSON string into a Python dictionary.

    Steps:
    - Parse the JSON string
    - Return the resulting dictionary
    """
    return json.loads(json_string)


def get_data_from_key(data, key):
    """
    Get one day's data out of the weekly data dictionary.

    Parameters:
    - data: the full coffeeshop dictionary
    - key: the day name (e.g. "monday")

    Returns:
    - Dictionary with 'drinks', 'desserts', and 'tips' for that day
    """
    return data[key]


def get_price(prices, item):
    """
    Get the price of one coffee or dessert.

    Parameters:
    - prices: the prices dictionary
    - item: the item name (e.g. "latte")

    Returns:
    - The price as a float
    """
    return prices[item]


def calculate_day(day_data, prices):
    total = 0.0

    for drink, quantity in day_data["drinks"].items():
        total += get_price(prices, drink) * quantity

    for dessert, quantity in day_data["desserts"].items():
        total += get_price(prices, dessert) * quantity

    total += day_data["tips"]

    return total


def calculate_week(data, prices):
    days = ["monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday"]
    weekly_total = 0.0

    for day in days:
        day_data = get_data_from_key(data, day)
        weekly_total += calculate_day(day_data, prices)

    return weekly_total


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ruslanhamidov/coffee_data/main/coffeeshop.json"

    raw_json = fetch_data(url)
    data = deserialize_data(raw_json)

    prices = data["prices"]
    days = ["monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday"]

    print("=" * 50)
    print("   COFFEESHOP WEEKLY EARNINGS REPORT")
    print("=" * 50)

    for day in days:
        day_data = get_data_from_key(data, day)
        day_total = calculate_day(day_data, prices)
        print(f"{day.capitalize():>12}: ${day_total:>8.2f}")

    print("-" * 50)
    week_total = calculate_week(data, prices)
    print(f"{'WEEK TOTAL':>12}: ${week_total:>8.2f}")
    print("=" * 50)
