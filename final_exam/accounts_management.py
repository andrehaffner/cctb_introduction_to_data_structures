from bank_account import BankAccount
from time import sleep


def add_bank_account(bank_accounts):
    print("\n\tCreating new bank account:")
    name = input("\tFirst name: ")
    last_name = input("\tLast name: ")
    while True:
        try:
            balance = float(input("\tBalance: "))
            if balance < 0:
                print("\tBalance must be positive float!")
            else:
                break
        except ValueError:
            print("\tBalance must be positive float!")
    bank_accounts.append(BankAccount(name, last_name, balance))


def update_bank_account(bank_accounts):
    print("\n\tUpdating bank account:")
    while True:
        try:
            account_id = int(input("\tAccount number: "))
            break
        except ValueError:
            print("\tInvalid account number!")
    found = False
    for ba in bank_accounts:
        if ba.account_number == account_id:
            print(f"\n\tOld values:\n\t\tName: {ba.first_name}"
                  f"\n\t\tLast name: {ba.last_name}\n\t\tBalance: {ba.balance}")
            print("\n\tNew values:")
            name = input("\t\tName: ")
            last_name = input("\t\tName: ")
            while True:
                try:
                    balance = float(input("\t\tBalance: "))
                    if balance < 0:
                        print("\t\tBalance must be positive float!")
                    else:
                        break
                except ValueError:
                    print("\t\tBalance must be positive float!")
            ba.first_name = name
            ba.last_name = last_name
            ba.balance = balance
            found = True
            print(f"\n\tUpdated {name} {last_name}'s account!")
    if not found:
        print("Account not found!")


def delete_account(bank_accounts):
    print("\n\tDeleting bank account:")
    while True:
        try:
            account_id = int(input("\tAccount number: "))
            break
        except ValueError:
            print("\tInvalid account number!")
    found = False
    for ba in bank_accounts:
        if ba.account_number == account_id:
            bank_accounts.remove(ba)
            found = True
            print(f"\tAccount {account_id} deleted!")
    if not found:
        print("Account not found!")


def deposit(bank_accounts):
    print("\n\tDepositing:")
    while True:
        try:
            account_id = int(input("\tAccount number: "))
            found = False
            for ba in bank_accounts:
                if ba.account_number == account_id:
                    found = True
                    while True:
                        try:
                            value = float(input("\tDeposit value: "))
                            break
                        except ValueError:
                            print("\tInvalid deposit value!")
                    ba.balance += value
                    print(f"\tDeposited {value} on account {account_id}!")
            if not found:
                print("\tAccount doesn't exists!")
            break
        except ValueError:
            print("\tInvalid account number!")


def withdraw(bank_accounts):
    print("\n\tWithdrawing:")
    while True:
        try:
            account_id = int(input("\tAccount number: "))
            found = False
            for ba in bank_accounts:
                if ba.account_number == account_id:
                    found = True
                    while True:
                        try:
                            value = float(input("\tWithdraw value: "))
                            if value > ba.balance:
                                print("\tYou don't have that money on account!")
                            else:
                                break
                        except ValueError:
                            print("\tInvalid withdraw value!")
                    ba.balance -= value
                    print(f"\tWithdrawed {value} from account {account_id}!")
            if not found:
                print("\tAccount doesn't exists!")
            break
        except ValueError:
            print("\tInvalid account number!")


def transfer(bank_accounts):
    print("\n\tTransfering:")
    while True:
        try:
            origin = int(input("\tOrigin account number: "))
            found = False
            for ba in bank_accounts:
                if ba.account_number == origin:
                    found = True
                    while True:
                        try:
                            value = float(input("\tTransfer value: "))
                            if value > ba.balance:
                                print("\tYou don't have that money on account!")
                            else:
                                break
                        except ValueError:
                            print("\tInvalid tranfer value!")
                    origin = ba
                    while True:
                        try:
                            account_id = int(input("\tDestiny account number: "))
                            found = False
                            for ba in bank_accounts:
                                if ba.account_number == account_id:
                                    found = True
                                    ba.balance += value
                                    origin.balance -= value
                                    print(f"\tDeposited {value} on account {account_id}!")
                            if not found:
                                print("\tAccount doesn't exists!")
                                break
                            break
                        except ValueError:
                            print("\tInvalid account number!")
                if not found:
                    print("\tAccount doesn't exists!")
            break
        except ValueError:
            print("\tInvalid account number!")


def find_by_name(bank_accounts):
    print("\n\tFinding by name:")
    name = input("\tEnter name: ")
    found = False
    for ba in bank_accounts:
        if ba.first_name == name:
            print("\n\tAccount found!")
            print("\t\tAccount number:", ba.account_number)
            print("\t\tOwner:", ba.first_name, ba.last_name)
            print("\t\tBalance:", ba.account_number)
            found = True
    if not found:
        print("\tAccount not found!")


def sort_by_last_name(bank_accounts):
    print("\n\tSorting by last name:")
    order = dict()
    for ba in bank_accounts:
        order[ba.last_name] = {"owner": ba.first_name + " " + ba.last_name,
                               "balance": ba.balance,
                               "id": ba.account_number}
    order = dict(sorted(order.items()))
    print("\n\tPrinting students by gpa:")
    for key, value in order.items():
        sleep(1)
        print("\n\t\tOwner:", value["owner"])
        print("\t\tAccount number:", value["id"])
        print("\t\tBalance:", value["balance"])


def filter_by_balance(bank_accounts):
    print("\n\tFiltering by balance:")
    while True:
        try:
            minn = float(input("\tMinimum balance: "))
            break
        except ValueError:
            print("\tInvalid value!")
    results = dict()
    found = False
    for ba in bank_accounts:
        if ba.balance >= minn:
            found = True
            results[ba.last_name] = {"owner": ba.first_name + " " + ba.last_name,
                                     "balance": ba.balance,
                                     "id": ba.account_number}
    for key, value in results.items():
        sleep(1)
        print("\n\t\tOwner:", value["owner"])
        print("\t\tAccount number:", value["id"])
        print("\t\tBalance:", value["balance"])
    if not found:
        print("\tNo account with that balance!")


def print_bank_accounts(bank_accounts):
    print("\n\tPrinting bank accounts:")
    for ba in bank_accounts:
        sleep(1)
        print("\n\t\tOwner:", ba.first_name, ba.last_name)
        print("\t\tAccount number:", ba.account_number)
        print("\t\tBalance:", ba.balance)
