def login(database, username, password):
    username = username.lower()
    if username in database:
        if database[username] == password:
            print("\nWelcome,", username, "\n")
            return username
        else:
            print("\nIncorrect login!\n")
    else:
        print("\nPlease register to donate!\n")
    return ""


def register(database, username, password):
    if len(username) > 10:
        print("Username cannot exceed 10 characters!")
    if len(username) == 0:
        print("Provide a Username")
    if len(password) < 5:
        print("Password must be at least 5 characters long!")
    if (len(username) > 10 or len(username) == 0 or len(password) < 5):
        return ""

    username = username.lower()
    if (username in database):
        print("\nUsername already registered.\n")
        return ""
    return username
