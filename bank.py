from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance

    # ----------------------------
    # Getter
    # ----------------------------
    def get_balance(self):
        return self.__balance

    # ----------------------------
    # Deposit
    # ----------------------------
    def deposit(self, amount):

        if amount <= 0:
            return False, "Deposit amount should be greater than zero."

        self.__balance += amount

        return True, f"₹{amount} deposited successfully."

    # ----------------------------
    # Withdraw
    # ----------------------------
    def withdraw(self, amount):

        if amount <= 0:
            return False, "Withdrawal amount should be greater than zero."

        if amount > self.__balance:
            return False, "Insufficient Balance."

        self.__balance -= amount

        return True, f"₹{amount} withdrawn successfully."

    # ----------------------------
    # Display Details
    # ----------------------------
    def display_details(self):

        return {
            "Account Number": self.account_number,
            "Customer Name": self.customer_name,
            "Balance": self.get_balance()
        }

    # ----------------------------
    # Abstract Method
    # ----------------------------
    @abstractmethod
    def calculate_interest(self):
        pass


# ==================================================
# Savings Account
# ==================================================

class SavingsAccount(Account):

    def __init__(
            self,
            account_number,
            customer_name,
            balance,
            interest_rate):

        super().__init__(
            account_number,
            customer_name,
            balance
        )

        self.interest_rate = interest_rate

    def calculate_interest(self):

        interest = (
            self.get_balance() *
            self.interest_rate
        ) / 100

        return interest

    def display_details(self):

        details = super().display_details()

        details["Account Type"] = "Savings"
        details["Interest Rate"] = f"{self.interest_rate}%"

        return details


# ==================================================
# Current Account
# ==================================================

class CurrentAccount(Account):

    def __init__(
            self,
            account_number,
            customer_name,
            balance,
            overdraft_limit):

        super().__init__(
            account_number,
            customer_name,
            balance
        )

        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):

        return "Interest is not applicable for Current Accounts."

    def display_details(self):

        details = super().display_details()

        details["Account Type"] = "Current"
        details["Overdraft Limit"] = self.overdraft_limit

        return details


# ==================================================
# Search Function
# ==================================================

def search_account(accounts, account_number):

    for account in accounts:

        if account.account_number == account_number:
            return account

    return None


# ==================================================
# Create Savings Account
# ==================================================

def create_savings_account(
        accounts,
        account_number,
        customer_name,
        balance,
        interest_rate):

    account = SavingsAccount(
        account_number,
        customer_name,
        balance,
        interest_rate
    )

    accounts.append(account)

    return "Savings Account Created Successfully."


# ==================================================
# Create Current Account
# ==================================================

def create_current_account(
        accounts,
        account_number,
        customer_name,
        balance,
        overdraft_limit):

    account = CurrentAccount(
        account_number,
        customer_name,
        balance,
        overdraft_limit
    )

    accounts.append(account)

    return "Current Account Created Successfully."


# ==================================================
# Display All Accounts
# ==================================================

def get_all_accounts(accounts):

    all_accounts = []

    for account in accounts:
        all_accounts.append(
            account.display_details()
        )

    return all_accounts