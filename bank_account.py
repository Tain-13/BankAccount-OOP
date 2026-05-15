# parent class
class BankAccount():
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
    self._history = []       # _ = private convention

  # dunder : print(obj1)
  def __str__(self):
    return f"[{self.__class__.__name__}]{self.owner} | {self.balance:,.0f}"
  
  # dunder: repr(obj2)
  def __repr__(self):
    return f"BankAccount(owner ='{self.owner}', balance = '{self.balance}')"
  
  # dunder: obj1 + obj2
  def __add__(self, other):
    return self.balance + other.balance
  
  def deposit(self, amount):
      if amount <= 0:
          raise ValueError('Amount must be positive')
      self.balance += amount
      self._history.append(f"+ {amount:,.0f}")

  def withdraw(self, amount):
      if amount > self.balance:
          raise ValueError('Insufficient balance')
      self.balance -= amount
      self._history.append(f'-{amount:,.0f}')

  def show_history(self):
      print('\n Transaction history:')
      for t in self._history:
          print(f'{t}')  
