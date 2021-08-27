from donation_pkg.homepage import show_homepage
from donation_pkg.user import login, register

database = {
    "admin": "password123"
}
donations = []
authorized_user = ""

while True:

    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    option = input("Choose an Option: ")
    if option == "1" or option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
    if option == "1":
        authorized_user = login(database, username, password)
    if option == "2":
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password
    if option == "3":
        print("TODO: Write Donate Functionality")
    if option == "4":
        print("TODO: Write Show Donations Functionality")
    if option == "5":
        print("\nLeaving DonateMe...\n")
        exit()
