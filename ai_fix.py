```python
# Define the users dictionary
users = {
    1: "Alice",
    2: "Bob"
}

def get_user(id):
    """
    Retrieves a username from the users dictionary based on the provided id.
    
    Args:
        id (int): The ID of the user to retrieve.
    
    Returns:
        str: The username associated with the provided ID, or None if the ID is not found.
    """
    return users.get(id)  # Using the dictionary's get() method to avoid KeyError

def main():
    # Test the modified get_user(id) function
    print(get_user(1))  # Should print: Alice
    print(get_user(2))  # Should print: Bob
    print(get_user(3))  # Should print: None

if __name__ == "__main__":
    main()
```