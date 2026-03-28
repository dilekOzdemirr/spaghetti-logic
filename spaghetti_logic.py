from pathlib import Path
from typing import List, Callable, Optional
from decimal import Decimal, ROUND_HALF_UP
import json

# Configuration Constants
PRICE_MULTIPLIER = Decimal("1.15")
LOG_FILE = Path("log.txt")
DECIMAL_PLACES = 2


def calculate_total_price(
    price: float, multiplier: Decimal = PRICE_MULTIPLIER
) -> Decimal:
    """
    Calculate total price with multiplier (e.g., tax or markup).
    Uses Decimal for precise financial calculations.
    """
    decimal_price = Decimal(str(price))
    result = decimal_price * multiplier
    return result.quantize(
        Decimal(10) ** -DECIMAL_PLACES, rounding=ROUND_HALF_UP
    )


def format_price_output(price, label: str = "Total") -> str:
    """Format price as human-readable string."""
    if isinstance(price, Decimal):
        price_str = str(price)
    else:
        price_str = f"{float(price):.{DECIMAL_PLACES}f}"
    return f"{label}: {price_str}"


def process_prices(
    prices: List[float], multiplier: Decimal = PRICE_MULTIPLIER
) -> List[Decimal]:
    """
    Apply price multiplier to list of prices.
    Pure function - no side effects.

    Args:
        prices: List of price values
        multiplier: Multiplication factor (default: 1.15 for 15% markup)

    Returns:
        List of calculated prices with proper rounding
    """
    if not prices:
        return []
    return [calculate_total_price(price, multiplier) for price in prices]


def format_log_entry(data: List) -> str:
    """
    Format data for logging using JSON for efficiency and clarity.
    Converts Decimal to float for JSON serialization.
    """
    json_data = [float(item) if isinstance(item, Decimal) else item for item in data]
    return json.dumps(json_data)


def display_results(results: List) -> None:
    """
    Display results to console.
    Handles both Decimal and float types.
    """
    if not results:
        print("No results to display.")
        return
    for result in results:
        print(format_price_output(result))


def save_to_log(data: List, filename: Path = LOG_FILE) -> None:
    """
    Persist data to log file.

    Args:
        data: List of prices to save
        filename: Path to log file

    Raises:
        IOError: If file cannot be written
    """
    if not data:
        return

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(format_log_entry(data) + "\n")
    except IOError as e:
        raise IOError(f"Failed to write to log file {filename}: {e}")


def process_data(
    data: List[float],
    display_handler: Optional[Callable] = None,
    log_handler: Optional[Callable] = None,
) -> List[Decimal]:
    """
    Orchestrate data processing pipeline.

    Args:
        data: List of prices to process
        display_handler: Optional callable for displaying results (default: print)
        log_handler: Optional callable for logging results (default: save to file)

    Returns:
        List of processed prices with precise decimal values

    Raises:
        ValueError: If data is not a list of numbers
    """
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of numbers")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All items in data must be numeric values")

    processed_prices = process_prices(data)

    if display_handler is not None:
        display_handler(processed_prices)
    else:
        display_results(processed_prices)

    if log_handler is not None:
        log_handler(processed_prices)
    else:
        save_to_log(processed_prices)

    return processed_prices