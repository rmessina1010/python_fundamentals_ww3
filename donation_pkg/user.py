def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("\nWelcome,", username, "\n")
            return username
        else:
            print("\nIncorrect login!\n")
    else:
        print("\nPlease register to donate!\n")
    return ""


def register(database, username):
    if (username in database):
        print("\nUsername already registered.\n")
        return ""
    return username
