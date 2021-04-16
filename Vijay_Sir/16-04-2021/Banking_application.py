class Bank:  #Class
    bank_total_amount = 0 # Class Variable

    def __init__(self, account_number, account_balance, pan_number):  # Constructor with local variables
        self.ac_number = account_number  # ac_number is instance Variable
        self.ac_balance = account_balance
        self.pan_number = pan_number
        Bank.bank_total_amount = Bank.bank_total_amount + self.ac_balance

    def credit(self, debited_money): # Method credit
        self.ac_balance = self.ac_balance + debited_money
        Bank.bank_total_amount = Bank.bank_total_amount + debited_money
        print("Account Balances is :", self.ac_balance)

    def debited(self, withdraws_money):
        if self.ac_balance >= 500 :
            self.ac_balance = self.ac_balance - withdraws_money
            Bank.bank_total_amount = Bank.bank_total_amount - withdraws_money
            print("Account Balances is :", self.ac_balance)

        elif self.ac_balance <= 500:
            print("Low Balances")

    # def __int__(self):
    #     print("Account Balances is:", self.ac_balance)


uday = Bank(1025423, 5000, 'TU10324D')
jock = Bank(10254213, 123000, 'UA25324C')

print("Uday Bank Balance:", uday.ac_number, uday.ac_balance)
print("Uday Bank Balance:", jock.ac_number, jock.ac_balance)
print()

uday.credit(15000)
uday.debited(10000)


