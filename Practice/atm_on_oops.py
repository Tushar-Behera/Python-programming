from typing_extensions import Self


class Atm:

    def __init__(self):
        self.pin = " "
        self.balance = 0

        self.menu()     # Calling of menu method comes to function when we create obj of Atm

    # Menu method Created 

    def menu(self):
        user_input = input('''
                        Enter Your Choice To Proceed 
                        1. Create Pin
                        2. Diposit
                        3. Withdraw
                        4. Check balance
                        5. Exit
        
        ''')

        if user_input == '1':
            self.create_pin()

        elif user_input =='2':
            self.deposit()

        elif user_input == '3':
            self.withdraw()

        elif user_input == '4':
            self.check_bal()

        else:
            print("Thank You For Banking")


    
    # Defining the methods for the Menu ---> 

    def create_pin(self):
        self.pin = input("Enter Your Pin :")
        print("Pin Set Successfully")      
        self.menu()

    def deposit(self):
        temp = input("Enter Your pin : ")
        if temp == self.pin:
            amount = int(input("Enter The Amount : "))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")
        self.menu()

    def withdraw(self):
        temp = input("Enter Your pin : ")
        if temp == self.pin:
            amount = int(input("Enter The Amount : "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("withdraw Successful")
            else:
                print("Insufficient Fund")    
        else:
            print("Invalid Pin")
        self.menu()

    def check_bal(self):
        temp = input("Enter Your pin : ")
        if temp == self.pin:
            print("Available Balance : ",self.balance)
        else:
            print("Invalid Pin")
        self.menu()


# object of Atm Created
sbi = Atm()