```python
class UserNotFoundError(Exception):
    pass

def get_user(user_id):
    if user_id not in users:
        raise UserNotFoundError(f"User with ID {user_id} not found")
    return users[user_id]
```