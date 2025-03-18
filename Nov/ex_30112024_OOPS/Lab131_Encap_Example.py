class Bank:
    def __init__(self,account_number,balance):
        self.balance = balance # public
        self.__account_number = account_number # private
    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance  = self.balance +amount
    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed!")
    def __internal_private_method(self):
        print("Private Method, can be access by only Class")

icici = Bank (7780281673,  100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
#print(icici.__account_number)
icici.show_me_account_number(False)


