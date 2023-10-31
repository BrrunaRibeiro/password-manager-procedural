from cryptography.fernet import Fernet

#Generate a key for encryption
key = Fernet.generate_key()
f = Fernet(key)

#Save  everything in json file or database?

passwords = {}

#def authentication(): Master password?? update save funtion after deciding and uncomment calling it


#def save():

def list_accounts():
    """
    Lists(prints) all saved accounts
    """
    if passwords:
        print("Saved Accounts:\n")
        for account in passwords:
            print(account)
    else:
        print("No accounts saved yet.\n")
        start()

def add_account():
    """
    Adds a new account with input funtions and stores in their corresponding variables.
    Stores it in a dictionary.
    """
    account_name = input("Enter the Account Name(Ex:'Netflix'): ")
    username = input("Enter the Username/Email: ")
    password = input("Enter the Password: ")
    passwords[account_name] = {'username': username, 'password': password}
    #save()
    print(f"{account_name} account details have been saved successfully.")

def view_specific_account():
    """
    Uses input function to get the specific account details.
    """
    account_name = input("Enter Account Name you would like to view: ")
    if account_name in passwords:
        account = passwords[account_name]
        print(f"Account:{account_name}")
        print(f"Username: {account['username']}")
        print(f"Password: {account['password']}")
    else:
        print(f"'{account_name}' account not found.\n")
        start()

#def update_account():
#def delete_account():

def start():
#Add login/authentication?? (use while true and else(false)=exit)
    """
    The user is asked to select an option from the list.
    Input is used to select the option, which is stored in the option_selected variable.
    """   
    print("Please select one of the options below...\n")
    print("1. View all stored accounts")
    print("2. Add new account")
    print("3. View a specific account")
    print("4. Update an account")
    print("5. Delete an account")
    print("6. Leave Password Manager\n")

    option_selected = input("Enter your option: ")

    if option_selected == '1':
        list_accounts()
    elif option_selected == '2':
        add_account()
    elif option_selected == '3':
        view_specific_account()
    elif option_selected == '4':
        update_account()
    elif option_selected == '5':
        delete_account()
    elif option_selected == '6':
        print("Thank you for using Password Manager! Goodbye!\n")
    else:
        print("Invalid option selected. Please enter a valid option...\n")
        start()

#def main():
    """
    Calls all functions in the program.
    """

print("Welcome to Password Manager\n")
start()