class BankAccount:
  def withdraw():
    pass
  def deposit():
    pass
    
class chooseAccount:
  def choose():
    return '\tchoose your account type'

import chooseAccount
class SavingsAccount(BankAccount):
  def __init__(self):
     self.balance = 500
  def deposit(self, amount):
    if amount<0:
      return 'Invalid deposit amount'
    else:
      self.balance = self.balance + amount
      return self.balance
  def withdraw(self, cash):
    if cash < 0:
      return 'Invalid withdraw amount'
    elif (self.balance - cash) < 500:
      return 'Cannot withdraw beyond the minimum account balance'
    elif (self.balance - amount) < 0:
      return 'Cannot withdraw beyond the current account balance'
    else:
     self.balance = self.balance - cash
     return self.balance
     
class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance = 0
  def deposit(self, amount):
    if amount<0:
      return 'Invalid deposit amount'
    else:
      self.balance = self.balance + amount
      return self.balance
  def withdraw(self, cash):
    if cash < 0:
      return 'Invalid withdraw amount'
    elif (self.balance-cash) < 0:
      return 'Cannot withdraw beyond the current account balance'
    else:
      self.balance = self.balance - cash
      return self.balance