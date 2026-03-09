```python
def get_user(id, users):
    """
    Retrieves a user from the users dictionary by their ID.
    
    Args:
        id (int): The ID of the user to retrieve.
        users (dict): A dictionary of users where the key is the user's ID and the value is the user's name.
    
    Returns:
        str: The name of the user if found, otherwise None.
    
    Raises:
        ValueError: If the user is not found and custom error handling is enabled.
    """
    user = users.get(id)
    if user is None:
        raise ValueError(f"User with ID {id} not found")
    return user

# Example usage:
users = {1: "Alice", 2: "Bob"}
print(get_user(1, users))  # Output: Alice
try:
    print(get_user(3, users))
except ValueError as e:
    print(e)  # Output: User with ID 3 not found
```