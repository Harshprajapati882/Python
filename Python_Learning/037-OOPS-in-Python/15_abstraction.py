# Abstraction using Abstract Base Classes (ABCs) in Python

from abc import ABC, abstractmethod

# --- The Abstract Base Class ---
# This class defines a 'contract' or a 'template' for what a payment processor should be able to do.
# It hides the complexity of how each specific payment method works.
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        """
        An abstract method. Any subclass MUST implement this method.
        """
        pass # No implementation here, just the definition.

    @abstractmethod
    def get_transaction_id(self):
        """
        Another abstract method that all subclasses must have.
        """
        pass

    def get_status(self):
        """
        A regular method can also exist in an ABC.
        Subclasses will inherit this method as is.
        """
        print("Checking status from the central system...")
        return "OK"

# --- Concrete Subclass 1 ---
# Implements the 'PaymentProcessor' contract for Credit Cards.
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number
        self.transaction_id = None

    def process_payment(self, amount):
        print(f"Processing ${amount} payment with credit card {self.card_number[-4:]}...")
        # Complex logic for communicating with the bank network would be here.
        self.transaction_id = f"CC_TXN_{random.randint(1000, 9999)}"
        print("Payment successful.")

    def get_transaction_id(self):
        return self.transaction_id

# --- Concrete Subclass 2 ---
# Implements the 'PaymentProcessor' contract for PayPal.
class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
        self.transaction_id = None

    def process_payment(self, amount):
        print(f"Processing ${amount} payment with PayPal account {self.email}...")
        # Complex logic for PayPal's API would be here.
        self.transaction_id = f"PP_TXN_{random.randint(1000, 9999)}"
        print("Payment successful.")

    def get_transaction_id(self):
        return self.transaction_id

# --- Trying to instantiate the ABC will fail ---
try:
    # This line will raise a TypeError because you can't create an object from an abstract class.
    generic_payment = PaymentProcessor()
except TypeError as e:
    print(f"Error as expected: {e}\n")


# --- The Abstraction in Action ---
import random

# Our high-level function doesn't care about the details of credit cards or PayPal.
# It only knows that it has a 'PaymentProcessor' object which is guaranteed to have
# a 'process_payment' method.
def execute_purchase(payment_processor: PaymentProcessor, amount):
    print(f"--- Starting a new purchase of ${amount} ---")
    payment_processor.process_payment(amount)
    txn_id = payment_processor.get_transaction_id()
    print(f"Purchase complete. Transaction ID: {txn_id}")
    # We can also call regular inherited methods
    status = payment_processor.get_status() 
    print(f"Transaction status: {status}\n")

# Create instances of the concrete classes
credit_card = CreditCardProcessor("1234-5678-9876-5432")
paypal = PayPalProcessor("user@example.com")

# Pass them to our high-level function. Abstraction lets us treat them the same.
execute_purchase(credit_card, 150.75)
execute_purchase(paypal, 49.99)
