from cryptography.fernet import Fernet

def main():
#Add login/authentication??
    """
    Print statements greet the user. 
    The user is asked to select an option from the list.
    Input is used to select the option, which is stored in the option_selected variable.
    """
    print("Welcome to Password Manager\n")
    print("Please select one of the options below to continue...\n")
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
        print("Invalid option selected. Please enter a valid option...")

main()