# Enhanced Bank Account Management System
import re

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account():
    """Create a new account."""
    username = input("Enter a username: ")
    if username not in account_holders:
        account_holders.append(username)
        balances.append(0)
        loans.append(0)
        transaction_histories.append([])
        print("Account created successfully!")
    else:
        print("This username already exists. Please enter another username.")


def deposit():
    """Deposit money into an account."""
    username = input("Please enter your username: ")
    if username in account_holders:
        deposit_amount = float(input("Please enter your deposit amount: "))

        if deposit_amount > 0:
            account_index = account_holders.index(username)
            balances[account_index] += deposit_amount
            print(f"Deposit was successful! Current balance: {balances[account_index]:.2f} lv.")
            transaction_histories[account_index].append(f"Deposited {deposit_amount:.2f} lv. to balance.")
        else:
            print("Invalid deposit amount! Please try again.")

    else:
        print(f"The username {username} does not exist. Please try again.")


def withdraw():
    """Withdraw money from an account."""
    username = input("Please enter your username: ")
    if username in account_holders:
        withdrawal_money = float(input("Please enter a withdrawal amount: "))
        account_index = account_holders.index(username)

        if 0 < withdrawal_money <= balances[account_index]:
            balances[account_index] -= withdrawal_money
            print(f"Withdrawal was successful! Current balance: {balances[account_index]:.2f} lv.")
            transaction_histories[account_index].append(f"Withdrew {withdrawal_money:.2f} lv.")
        elif withdrawal_money <= 0:
            print("Invalid withdrawal amount! Please try again.")
        else:
            print("Withdrawal amount is more than the balance! Please try again.")

    else:
        print(f"The username {username} does not exist. Please try again.")


def check_balance():
    """Check balance of an account."""
    username = input("Please enter your username: ")
    if username in account_holders:
        account_index = account_holders.index(username)
        balance = balances[account_index]
        print(f"Your current balance is: {balance:.2f} lv.")
    else:
        print(f"The username {username} does not exist. Please try again.")


def list_accounts():
    """List all account holders and details."""
    if account_holders:
        print("Listing all accounts...")
        for index in range(len(account_holders)):
            user, balance, loan = account_holders[index], balances[index], loans[index]
            print(f"User: {user} -> Balance: {balance:.2f} lv., Loan amount: {loan:.2f} lv.")
    else:
        print("There are no accounts at the moment.")


def transfer_funds():
    """Transfer funds between two accounts."""
    username_sender = input("Please enter your username: ")
    if username_sender in account_holders:
        username_receiver = input("Please enter the username you want to transfer funds to: ")

        if username_sender == username_receiver:
            print("You cannot transfer funds to yourself. Please try again.")

        elif username_receiver in account_holders:
            account_index_sender = account_holders.index(username_sender)
            transfer_money = float(input(f"Please enter the amount of money you want to transfer "
                                         f"to {username_receiver}: "))

            if 0 < transfer_money <= balances[account_index_sender]:
                account_index_receiver = account_holders.index(username_receiver)
                balances[account_index_receiver] += transfer_money
                balances[account_index_sender] -= transfer_money
                print(f"Transaction was successful! Current balance: {balances[account_index_sender]:.2f} lv.")
                transaction_histories[account_index_sender].append(f"Transferred {transfer_money:.2f} lv. "
                                                                   f"to {username_receiver}")
                transaction_histories[account_index_receiver].append(f"{username_sender} transferred "
                                                                     f"{transfer_money:.2f} lv. to your account.")
            elif transfer_money <= 0:
                print("Invalid money amount! Please try again.")
            else:
                print("Transfer money is more than balance! Please try again.")

        else:
            print(f"The username {username_receiver} does not exist. Please try again.")

    else:
        print(f"The username {username_sender} does not exist. Please try again.")


def view_transaction_history():
    """View transactions for an account."""
    username = input("Please enter your username: ")
    if username in account_holders:
        account_index = account_holders.index(username)
        account_transactions = transaction_histories[account_index]
        for transaction in account_transactions:
            print(transaction)
    else:
        print(f"The username {username} does not exist. Please try again.")


def apply_for_loan():
    """Allow user to apply for a loan."""
    username = input("Please enter your username: ")
    if username in account_holders:
        loan_amount = float(input("Please enter your loan amount: "))

        if loan_amount > 0:
            account_index = account_holders.index(username)
            loans[account_index] += loan_amount + loan_amount * INTEREST_RATE

            if loans[account_index] > MAX_LOAN_AMOUNT:
                loans[account_index] = MAX_LOAN_AMOUNT + MAX_LOAN_AMOUNT * INTEREST_RATE
                print("Loan has been set to 10 000 lv. with 3% interest, because that is the maximum loan amount.")
            else:
                print(f"Successfully applied for a loan with a loan amount of {loan_amount:.2f} lv with 3% interest!")
            transaction_histories[account_index].append(f"Applied for a loan of {loan_amount:.2f} lv. "
                                                        f"with 3% interest.")

        else:
            print("Invalid loan amount! Please try again.")
    else:
        print(f"The username {username} does not exist. Please try again.")


def repay_loan():
    """Allow user to repay a loan."""
    username = input("Please type in your username: ")
    if username in account_holders:
        account_index = account_holders.index(username)
        if not loans[account_index]:
            print("You haven't applied for any loans yet!")

        else:
            repay_amount = float(input("Please enter the amount of money you want to repay your loan: "))

            if 0 < repay_amount <= balances[account_index]:
                balances[account_index] -= repay_amount
                loans[account_index] -= repay_amount
                if loans[account_index] < 0:
                    balances[account_index] += abs(loans[account_index])
                    loans[account_index] = 0
                print(f"Transaction was successful! Current balance: {balances[account_index]:.2f} lv. "
                      f"Remaining loan amount: {loans[account_index]:.2f} lv.")
                transaction_histories[account_index].append(f"Repaid {repay_amount:.2f} lv. for loan")
            elif repay_amount > balances[account_index]:
                print("Repay amount more than balance! Please try again.")
            else:
                print("Repay amount less than 0! Please try again.")

    else:
        print(f"The username {username} does not exist. Please try again.")


def identify_card_type():
    """Identify type of credit card."""
    card_number = input("Please enter your card number: ")
    visa_card_pattern = r"(([4]\d{3})\s(\d{4})\s(\d{4})\s(\d{4}))"
    mastercard_card_pattern = r"(([5][1-5]\d{2})\s(\d{4})\s(\d{4})\s(\d{4}))"
    amex_card_pattern = r"((34\d{2}|37\d{2})\s(\d{4})\s(\d{4})\s(\d{3}))"

    visa_match = re.findall(visa_card_pattern, card_number)
    mastercard_match = re.findall(mastercard_card_pattern, card_number)
    amex_match = re.findall(amex_card_pattern, card_number)

    if visa_match:
        print("Your credit card is a Visa credit card.")
    elif mastercard_match:
        print("Your credit card is a Mastercard credit card.")
    elif amex_match:
        print("Your credit card is an American Express credit card.")
    else:
        print("Your credit card number is not valid.")


def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
