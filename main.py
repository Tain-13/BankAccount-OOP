# How to Run 

dab = BankAccount('dab', 1000)
dab.deposit(500)
dab.withdraw(200)
print(dab)
repr(dab)
dab.show_history()

bob = BankAccount('bob', 800)
print(dab + bob)