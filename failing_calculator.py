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


print(average_ratios([10, 5, 0]))
