class BankAccountSaving:
    def __init__(self,int_rate = 0.2, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit_saving(self, amount):
        self.balance += amount
        return self

    def withdraw_saving(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient saving funds: Charging a $5 fee")
        
        else: 
            self.balance -= amount
        return self

    def display_saving_account(self):
        print(f"Saving Account Balance: ${self.balance}")
        return self

    def yield_interest_saving(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self

class BankAccountChecking:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient checking funds: Charging a $5 fee")
        
        else: 
            self.balance -= amount
        return self
        
    def display_checking_account(self):
        print(f"Checking Account Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self

class User:       
    def __init__(self, name, email, int_rate = 0.01, balance = 0):
        self.name = name
        self.email = email
        self.account1 = BankAccountChecking(int_rate, balance)
        self.account2 = BankAccountSaving(int_rate, balance)
    
    def make_deposit(self, amount):    
        self.account1.deposit(amount)
        return self 
        
    def make_withdrowal(self, amount):
        self.account1.withdraw(amount)
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Email: {self.email}")
        self.account1.display_checking_account()
        return self

    def make_deposit_saving(self, amount):
        self.account2.deposit_saving(amount)
        return self

    def make_withdrowal_saving(self, amount):
        self.account2.withdraw_saving(amount)
        return self

    def display_saving_balance(self):
        self.account2.display_saving_account()
        return self   
    
michael = User("Michael", "michael@michael.com")
michael.make_deposit(100). make_withdrowal(100). make_deposit(200).make_deposit(50). make_withdrowal(100). display_user_balance()
michael.make_deposit_saving(1500). display_saving_balance()

peter = User("Peter", "peter@peter.com")
peter.make_deposit(200). make_deposit(50). make_withdrowal(100). make_withdrowal(10). display_user_balance()
peter.make_deposit_saving(1400). make_withdrowal_saving(100). display_saving_balance()

mary = User("Mary", "mary@mary.com")
mary.make_deposit(500). make_withdrowal(100). make_withdrowal(10). make_withdrowal(20). display_user_balance()
mary.make_deposit_saving(100). make_withdrowal_saving(400). display_saving_balance()
