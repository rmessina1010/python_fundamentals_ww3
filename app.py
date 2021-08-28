from donation_pkg.homepage import show_homepage, donate, show_donations
from donation_pkg.user import login, register

database = {
    "admin": "password123"
}
donations = []
authorized_user = ""
total_donations = 0

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
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[authorized_user] = password
    if option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            if type(donation) is tuple:
                donations.append(donation[0])
                total_donations += donation[1]
    if option == "4":
        show_donations(donations, total_donations)
    if option == "5":
        print("\nLeaving DonateMe...\n")
        exit()
