from accounts_management import *
from time import sleep


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Raw data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

options = "\n\n\t1. Add account\n\t2. Update account\n\t3. Delete account\n\t4. Deposit\n\t5. Withdraw" \
          "\n\t6. Transfer\n\t7. Find by name\n\t8. Sort by last name" \
          "\n\t9. Filter by balance\n\t10. Print bank accounts\n\t0. Exit"
line = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
bank_accounts = [BankAccount("Andre", "Haffner", 10000), BankAccount("Long", "Nguyen", 2000)]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Program ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

while True:
    try:
        # ~~~~~ Getting user input ~~~~~ #
        sleep(1)
        print(line)
        print("\nRunning program...")
        sleep(1)
        chosen_option = int(input("\nOptions:" + options + "\n\nChoose one: "))

        # ~~~~~ Executing task related to input ~~~~~ #
        if chosen_option == 1:
            add_bank_account(bank_accounts)
        elif chosen_option == 2:
            update_bank_account(bank_accounts)
        elif chosen_option == 3:
            delete_account(bank_accounts)
        elif chosen_option == 4:
            deposit(bank_accounts)
        elif chosen_option == 5:
            withdraw(bank_accounts)
        elif chosen_option == 6:
            transfer(bank_accounts)
        elif chosen_option == 7:
            find_by_name(bank_accounts)
        elif chosen_option == 8:
            sort_by_last_name(bank_accounts)
        elif chosen_option == 9:
            filter_by_balance(bank_accounts)
        elif chosen_option == 10:
            print_bank_accounts(bank_accounts)
        elif chosen_option == 0:
            print("Shutting down!")
            break
        else:
            print("Wrong command!")

    # ~~~~~ If user inputs string ~~~~~ #
    except ValueError:
        print("\n\t- Input error: only numbers accepted!\n")
