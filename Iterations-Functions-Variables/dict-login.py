users = [
    (0, "Bob", "password"),
    (1, "Jane", "plain_jane"),
    (2, "Anna", "1234"),
    (3, "Abdul", "qwerty"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter username: ")
password_input = input("Enter password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print(f"Welcome {username}!")

else:
    print("Your details are incorrect!")
