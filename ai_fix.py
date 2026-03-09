```python
def get_user(user_id, users):
    """
    Retrieves a user from the users dictionary.

    Args:
        user_id (int): The ID of the user to retrieve.
        users (dict): A dictionary of users where the key is the user ID and the value is the user name.

    Returns:
        str: The name of the user if found, otherwise None.
    """
    # Using the get() method to safely retrieve the user
    return users.get(user_id)

def get_user_explicit(user_id, users):
    """
    Retrieves a user from the users dictionary.

    Args:
        user_id (int): The ID of the user to retrieve.
        users (dict): A dictionary of users where the key is the user ID and the value is the user name.

    Returns:
        str: The name of the user if found, otherwise None.
    """
    # Using a try-except block to catch and handle the KeyError explicitly
    try:
        return users[user_id]
    except KeyError:
        return None

# Example usage
users = {1: "Alice", 2: "Bob"}

print(get_user(1, users))  # Expected output: Alice
print(get_user(3, users))  # Expected output: None

print(get_user_explicit(1, users))  # Expected output: Alice
print(get_user_explicit(3, users))  # Expected output: None
```