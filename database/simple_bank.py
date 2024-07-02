from datetime import datetime
from pydantic import BaseModel

# Define entity and relationship
class Account(BaseModel):
    Id: int
    Onwer: str
    Currency: str
    CreatedAt: datetime
    Balance: int

# record about balance changes in a Account
class Entry(BaseModel):
    Id: int
    AccountId: int # FK to Account.Id
    # Negative or Positive
    Amount: int
    CreatedAt: datetime

# Record transtraction transfer between two accounts
class Transfer(BaseModel):
    Id: int
    FromAccountId: int  # FK to Account.Id
    ToAccountId: int  # FK to Account.Id
    # alway positive
    Amount: int
    CreateAt: datetime

# To make transfer money from a bank account to other account, we need there step
#   1. create entities balance change in two accounts (insert)
#   2. create a record transactions (insert)
#   3. update account's balances 


"""
Update Account Balance Sent with -amount
SQL:
    update 
        Account
    set
        balance = balance -$amount
    where
        id = $FromAccountId

Update Account Balance Receive with +amount
SQL:
    update
        Account
    set
        balance = balance + $amount
    where
        id = $ToAccountId

--> Atomic operation ensure consistency: balance = balance +- $amount 
"""