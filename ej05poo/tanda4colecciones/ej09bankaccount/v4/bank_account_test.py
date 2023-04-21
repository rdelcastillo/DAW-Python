from bank_account import BankAccount

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
cuenta1.deposit(2000)
cuenta1.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta1, 100)
cuenta1.transfer(cuenta3, 250)
cuenta3.transfer(cuenta1, 22)
print(cuenta1.movements)
