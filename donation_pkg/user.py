import re


def login(database, username, password):
    db_key = username.lower()
    if db_key in database:
        if database[db_key]["pass"] == password:
            print("\nWelcome,", database[db_key]["reg_name"], "\n")
            return (db_key, database[db_key]["reg_name"])
        else:
            print("\nIncorrect login!\n")
    else:
        print("\nPlease register to donate!\n")
    return ""


def register(database, username, password):
    malformed = False
    if len(username) > 10:
        print("Username cannot exceed 10 characters!")
    if len(username) == 0:
        print("Provide a Username")
    if len(password) < 5:
        print("Password must be at least 5 characters long!")
    if re.search(r"^[a-z]\w*$", username, re.I) == None:
        print("Username must begin with a letter and only use alpha numeric chacters!")
        malformed = True
    if (len(username) > 10 or len(username) == 0 or len(password) < 5 or malformed):
        return ""

    db_key = username.lower()
    if (db_key in database):
        print("\nUsername already registered.\n")
        return ""
    return db_key
