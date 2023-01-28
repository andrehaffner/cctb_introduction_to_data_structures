import itertools


class BankAccount:
    id_itter = itertools.count()

    def __init__(self, first_name, last_name, balance):
        self.account_number = int(next(self.id_itter))
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
