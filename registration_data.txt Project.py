# Exam Registration Form Management Program in Python

# Define the filename for storing the registration data
filename = 'registration_data.txt'

# Function to display the menu and get user input
def display_menu():
    print("\nWelcome to the Exam Registration Form Management Program!\n")
    print("1. Register a new candidate")
    print("2. View all registered candidates")
    print("3. Search for a candidate by name")
    print("4. Delete a candidate's registration")
    print("5. Exit the program")
    choice = input("\nEnter your choice: ")
    return choice

# Function to register a new candidate
def register_candidate():
    # Get the candidate's details from the user
    name = input("\nEnter candidate's name: ")
    age = input("Enter candidate's age: ")
    email = input("Enter candidate's email: ")
    phone = input("Enter candidate's phone number: ")

    # Open the file in append mode and write the candidate's details to it
    with open(filename, 'a') as file:
        file.write(name + ',' + age + ',' + email + ',' + phone + '\n')

    print("Candidate registration successful!")

# Function to view all registered candidates
def view_candidates():
    # Open the file in read mode and display the contents
    with open(filename, 'r') as file:
        print("\nRegistered Candidates:\n")
        for line in file:
            print(line.strip())

# Function to search for a candidate by name
def search_candidate():
    # Get the name of the candidate to search for
    name = input("\nEnter the name of the candidate to search for: ")

    # Open the file in read mode and search for the candidate's details
    with open(filename, 'r') as file:
        found = False
        for line in file:
            if name in line:
                print("\nCandidate details:\n")
                print(line.strip())
                found = True
                break

        if not found:
            print("\nCandidate not found!")

# Function to delete a candidate's registration
def delete_candidate():
    # Get the name of the candidate to delete
    name = input("\nEnter the name of the candidate to delete: ")

    # Open the file in read mode and a temporary file in write mode
    with open(filename, 'r') as file, open('temp.txt', 'w') as temp:
        deleted = False
        for line in file:
            if name not in line:
                temp.write(line)
            else:
                deleted = True

        if not deleted:
            print("\nCandidate not found!")
        else:
            # Rename the temporary file to overwrite the original file
            import os
            os.replace('temp.txt', filename)
            print("\nCandidate registration deleted successfully!")

# Main program
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            register_candidate()
        elif choice == '2':
            view_candidates()
        elif choice == '3':
            search_candidate()
        elif choice == '4':
            delete_candidate()
        elif choice == '5':
            print("\nThank you for using the Exam Registration Form Management Program!")
            break
        else:
            print("\nInvalid choice! Please try again.")

# Call the main function
main()
