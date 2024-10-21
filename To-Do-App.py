
import os

# set color class to select from for text colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# Write functions to handle the options to be selected by the user.

# Define function to add the item to do to the list and then mark it incomplete
def add_task(to_dos):
    os.system('cls')
    user_input = input("What do you need to add? \n").lower()
    to_dos.update({user_input:': incomplete'})
    print(f"'{user_input}' has been added to the list.")

# Define a function to print the dictionary to the screen when selected by the user.
def view_tasks(to_dos):
    os.system('cls')
    print("Here are the current items on your list.\n")
    for key, value in to_dos.items():
        print(bcolors.HEADER+key+bcolors.ENDC, bcolors.OKGREEN+value+bcolors.ENDC)

# Define a function to update the value of the item selected by the user as 'Complete!'
def mark_complete(to_dos):
    os.system('cls')
    user_input = input("Which of the prior tasks have you completed?\n").lower()
    to_dos[user_input]= ': Complete!'
    print(f"Task '{user_input}' has been marked complete. Well done!")

# Define a function to remove an item and its value from the dictionary based on user input.
def delete_task(to_dos):
    os.system('cls')
    user_input = input("Which task do you need to delete? \n").lower()
    del to_dos[user_input]
    print(f"'{user_input}' has been removed from the list.")

# Start with a couple of print statements to encompass the start menu.


# Set an empty list to store the tasks
to_dos = {}

# Set a while loop to contnue until the user enters 5 to quit the program
while True:
    print("Welcome to the To-Do List App!\n")
    print("Menu\n1. Add a task\n2. View Tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
    
    # Input a try, except, finally to catch errors from user inputs 
    try:
        user_input = int(input("Please type the number of the action you would like to take. \n"))

# Set conditionals to dictate action based on user input.
        if user_input == 1:
            add_task(to_dos)
        
        elif user_input == 2:
            view_tasks(to_dos)

        elif user_input == 3:
            mark_complete(to_dos)

        elif user_input == 4:
            delete_task(to_dos)

        elif user_input == 5:
            break


    except Exception:
        print("Invalid entry. Please be sure to type the number of the action you would like to take.")

    finally:
        print("Thank you for using the To-Do App, we hope it helped.")