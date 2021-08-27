def show_homepage():
    print("\n      === DonateMe Homepage ===")
    print("------------------------------------------")
    print("| 1.   Login      | 2.   Register        |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|            5.    Exit                  |")
    print("------------------------------------------")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    try:
        donation_amt = float(donation_amt)
        donation = username+" donated $" + "{:.2f}".format(donation_amt) + "\n"
        print("Thank you for your donation,", username)
        return donation
    except:
        print("Invalid amount.\n")
        return None


def show_donations(donations):
    print("\n--- All Donations ---")
    if (len(donations) == 0):
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
