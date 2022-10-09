# creating a class --->

from typing_extensions import Self


class Atm:

    def__init__(self):
        self.pin = " "
        self.balance = 0

    self.menu()

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
            print()
        elif user_input == '3':

        elif user_input == '4':

        elif user_input == '5':

    def create_pin(self):
        self.pin = input("Enter Your Pin :")
        print("Pin Set Successfully")      
