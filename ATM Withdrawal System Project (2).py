# Sample ATM Machine program in Python (without initial variables)

# Function to display balance
def display_balance(balance):
    print("Your current balance is Rs.", balance)

# Function to reset PIN
def reset_pin():
    new_pin = int(input("Enter new PIN: "))
    confirm_pin = int(input("Confirm new PIN: "))
    if new_pin == confirm_pin:
        pin = new_pin
        print("PIN successfully reset")
    else:
        print("PIN reset failed. Try again.")

# Function to transfer money
def transfer_money(balance):
    amount = int(input("Enter amount to transfer: "))
    if amount <= balance:
        account_number = input("Enter account number: ")
        print("Amount of Rs.", amount, "successfully transferred to account number", account_number)
        balance -= amount
        return balance
    else:
        print("Insufficient funds. Transfer failed.")
        return balance

# Main program
def main():
    # Get user input for PIN
    pin = int(input("Enter your PIN: "))

    # Check if PIN is correct
    if pin == 1234: # Hardcoded initial value for demonstration purposes
        # Display options
        print("1. Display balance")
        print("2. Reset PIN")
        print("3. Transfer money")
        option = int(input("Enter option: "))
        
        # Execute option
        if option == 1:
            display_balance(10000) # Hardcoded initial value for demonstration purposes
        elif option == 2:
            reset_pin()
        elif option == 3:
            balance = transfer_money(10000) # Hardcoded initial value for demonstration purposes
            display_balance(balance)
        else:
            print("Invalid option. Try again.")
    else:
        print("Incorrect PIN. Try again.")

# Call the main function
main()
