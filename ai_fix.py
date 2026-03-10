```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers in the list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric values or is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("List must contain only numbers")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)

# Test with empty list
numbers = []
try:
    print(calculate_average(numbers))
except ValueError as e:
    print(f"Error: {e}")

# Test with non-empty list
numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))

# Test with non-list input
numbers = "not a list"
try:
    print(calculate_average(numbers))
except TypeError as e:
    print(f"Error: {e}")

# Test with list containing non-numeric values
numbers = [1, 2, 'a', 4, 5]
try:
    print(calculate_average(numbers))
except ValueError as e:
    print(f"Error: {e}")
```