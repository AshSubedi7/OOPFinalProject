#Parent Class User
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print('Personal Details')
        print('')
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)

Jackson = User('Jackson', 21, 'Male')
Hailey = User('Hailey', 18, 'Female')
Daniel = User('Daniel', 35, 'Male')
Taylor = User('Taylor', 25, 'Female')
#Child Class Bank
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    #Allows for a deposit into your account
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('Account balance has been updated: $', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient Funds | Balance Available: $', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Account Balance has been updated: $', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account Balance is: $', self.balance)


Jackson.show_details()
Harry = Bank('Harry', 29, 'Male')
Harry.deposit(50000000)
Harry.withdraw(250000)
Harry.view_balance()