def average_ratios(numbers):
    """
    Calculate average of ratios (100 / number) for non-zero values.

    Args:
        numbers: List of numeric values

    Returns:
        Average of ratios, skipping zero values

    Raises:
        ValueError: If all numbers are zero or list is empty
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    valid_ratios = []
    for num in numbers:
        if num == 0:
            # Skip zero values to avoid division by zero
            continue
        valid_ratios.append(100 / num)

    if not valid_ratios:
        raise ValueError("All numbers are zero - cannot calculate average ratio")

    return sum(valid_ratios) / len(valid_ratios)


# Test cases
if __name__ == "__main__":
    print("Test 1: [10, 5, 0]")
    try:
        result = average_ratios([10, 5, 0])
        print(f"Result: {result}")  # (10 + 20) / 2 = 15.0
    except Exception as e:
        print(f"Error: {e}")

    print("\nTest 2: [10, 5]")
    try:
        result = average_ratios([10, 5])
        print(f"Result: {result}")  # (10 + 20) / 2 = 15.0
    except Exception as e:
        print(f"Error: {e}")

    print("\nTest 3: [0, 0, 0]")
    try:
        result = average_ratios([0, 0, 0])
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Caught error: {e}")
