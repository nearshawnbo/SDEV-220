
account_balance = 1000
current_balance = account_balance



def deposit(amount):
    """Demonstrates state change via the 'global' keyword."""
    global current_balance
    if amount > 0:
        current_balance += amount  # State Change
        print(f"Deposited: ${amount}, Balance = ${current_balance}")

def withdraw(amount):
    """Demonstrates conditional state change."""
    global current_balance
    if 0 < amount <= current_balance:
        current_balance -= amount  # State Change
        print(f"Withdrew: ${amount}, Balance = ${current_balance}")
    else:
        current_balance -= amount  # State Change
        print(f"Withdrew: ${amount}, Balance = ${current_balance}")

        print("WARNING!! Insufficient funds or invalid amount.")

def update_status():
    current_balance = account_balance

def check_account():
     print(f"Current Account Balance: ${account_balance}")


def check_status():
    """Accesses the shared data without modifying it."""
    print(f"Current Balance: ${current_balance}")

deposit(500)
withdraw(200)
withdraw(500)
withdraw(1000)
check_account()
check_status()

