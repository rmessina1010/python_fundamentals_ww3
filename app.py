from donation_pkg.homepage import show_homepage, donate, show_donations
from donation_pkg.user import login, register

database = {
    "admin": {"pass": "password123", "reg_name": "admin"}
}
donations = []
authorized_user = ""
total_donations = 0
display_name = ""

while True:

    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", display_name)

    option = input("Choose an Option: ")
    if option == "1" or option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
    if option == "1":
        login_attemp = login(database, username, password)
        if type(login_attemp) is tuple:
            authorized_user = login_attemp[0]
            display_name = login_attemp[1]

    if option == "2":
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[authorized_user] = {
                "pass": password, "reg_name": username}
            display_name = username
    if option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(display_name)
            if type(donation) is tuple:
                donations.append(donation[0])
                total_donations += donation[1]
    if option == "4":
        show_donations(donations, total_donations)
    if option == "5":
        print("\nLeaving DonateMe...\n")
        exit()
