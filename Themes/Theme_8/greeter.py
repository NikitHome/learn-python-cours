def greet_user():
    """Выводит простое приветствие."""
    print("Hello!")
    
greet_user()


def greet_user(username):
    """Выводит простое приветствие."""
    print(f"Hello, {username.title()}!")
    
greet_user('jesse')