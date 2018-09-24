
class BankAccount:

    def __init__(self,first,last,middle,account,balance,status):

        if not [isinstance(name,str) for name in (first,last,middle)]:
            raise ValueError('First, last, and middle name should be strings.')
        
        if not isinstance(balance,int) and not isinstance(balance,float):
            raise ValueError("Balance must be a number.")
        
        if balance < 100:
            raise Exception("Minimum balance: $100")
        
        if account not in ("checking","savings"):
            raise ValueError("Invalid account type.")
        
        if status not in ("open","closed","freeze"):
            raise ValueError("Invalid status.")

        if balance < 100:
            raise ValueError("Mininum balance to open account: $100")

        self._first = first
        self._last = last
        self._middle = middle
        self._account = account
        self._balance = balance
        self._status = status

    @property
    def first(self):
        return self._first
    
    @property
    def last(self):
        return self._last
    
    @property
    def middle(self):
        return self._middle
    
    @property
    def balance(self):
        if balance < 0:
            balance -= 35
        return self._balance
    
    @property
    def account(self):
        return self._account
    
    @property
    def status(self):
        return self._status

    def transfer(self,funds,account_to):
        if funds < self.balance:
            raise ValueError("Inadequate balance.")
        if not isinstance(account_to,BankAccount):
            raise ValueError("Invalid transfering account.")
        if self.status == "freeze" or account_to.status == "freeze":
            raise Exception("Cannot transfer from or to a frozen account.")
        self._balance -= funds
        account_to.balance += funds
    
    def __repr__(self):
        return f"<{self.first} {self.middle} {self.last}>"
