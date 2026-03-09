```python
def divide(a, b):
    """
    Divide two numbers and handle division by zero.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division, or None if the divisor is zero.

    Raises:
        ValueError: If the divisor is zero.
    """
    # Check if the divisor is zero
    if b == 0:
        # Raise a custom error message
        raise ValueError("Cannot divide by zero")
    # Perform the division operation
    return a / b

# Test the division function
print(divide(10, 2))  # Output: 5.0
try:
    print(divide(10, 0))  # Output: ValueError: Cannot divide by zero
except ValueError as e:
    print(e)
```
Alternatively, you can return a specific value:
```python
def divide(a, b):
    """
    Divide two numbers and handle division by zero.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division, or None if the divisor is zero.
    """
    # Check if the divisor is zero
    if b == 0:
        # Return a specific value to indicate an invalid operation
        return None
    # Perform the division operation
    return a / b

# Test the division function
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: None
```