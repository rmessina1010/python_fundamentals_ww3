from donation_pkg.homepage import show_homepage

database = {
    "admin": "pasword123"
}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)

while True:
    option = input("Choose an Option: ")
    if option == "1":
        print("TODO: Write Login Functionality")
    if option == "2":
        print("TODO: Write Register Functionality")
    if option == "3":
        print("TODO: Write Donate Functionality")
    if option == "4":
        print("TODO: Write Show Donations Functionality")
    if option == "5":
        print("Leaving DonateMe...")
        exit()
