class Bank_Account:

    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    # Cradit balance
    def credit(self, credit_balance):
        if credit_balance <= 0:
            print("Invalid amount to credit.")
        else:
            self.account_balance += credit_balance
            print(f"{credit_balance} debited successfully.\nCurrent balance: {self.account_balance}")

    # Debit blance
    def debit(self, debit_blance):
        if debit_blance <=0:
            print("Invalid amount to debit.")
        elif self.account_balance < debit_blance:
            print("You don't have enouth money to debit!")
        else:
            self.account_balance -= debit_blance
            print(f"{debit_blance} debited successfully.\nCurrent balance: {self.account_balance}")
    
    # Check balance
    def check_balance(self):
        print(f"💰 Your current balance: {self.account_balance}")

def bank_account():

    account = Bank_Account(account_number=11270050, account_balance=0)

    user_account_number = int(input("Enter your account number: "))

    if user_account_number == account.account_number:
        print("Account matched successfully!")

        while True:

            option = input("Credit or Debit what do you want (C)redit or (D)ebit?\n: ").title()

            if option == "C":

                credit_amount = int(input("How many BDT do you want to credit in your bank account?\n: "))
                account.credit(credit_amount)
            elif option == "D":

                debit_amount = int(input("How many BDT do you want to debit from your bank account?\n: "))
                account.debit(debit_amount)
            else:
                print("Try again...")

            again = input("Do you want to credit or debit again (Y)es or (N)o?\n: ").title()
            if again != "Y":
                print("Thank you sir!")
                break

            account.check_balance()

        return account
    else:
        print("Account dosen't match try again...")
        return None
    
person = bank_account()
