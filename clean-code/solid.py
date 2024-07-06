from abc import ABC, abstractclassmethod

#https://arjancodes.com/blog/solid-principles-in-python-programming/

class Order:
    def __init__(self):
        pass


#3. Liskov Substitution Principle (LSP)
# Violet case
class PaymentProcessor(ABC):
    @abstractclassmethod
    def pay(self, order: Order, security_code: str):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, email: str):
        pass

# PaypalPaymentProcessor use email to verity, not use security_code like 
# PaymentProcessor

# Modification: move security_code, email to __init__
class PaymentProcessor(ABC):
    def __init__(self, security_code: str):
        pass
    @abstractclassmethod
    def pay(self, order: Order):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        pass

    def pay(self, order: Order):
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str):
        pass

    def pay(self, order: Order):
        pass



