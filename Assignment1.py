# Program Name: Assignment1.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 1
# Due Date: 01/27/ 2025
# Purpose: This program allows the user to add text to a string buffer,
#          clear the buffer text, display the buffer text, or exit the program.
# List Specific resources used to complete the assignment.
#   I used the reading provided by the class.

def main():
    option = 0
    inBuffer = ""
    
    # Main program loop. Exiting ends the program.
    while option != "4":
        option = input("Please input an Option no. :\n"
                       "1: Append data to input buffer \n"
                       "2: Clear the input buffer\n"
                       "3: Display the input buffer\n"
                       "4: Exit the program\n")

        if option == "1":
            append = input("Input text to append: ")
            inBuffer = inBuffer + append
        elif option == "2":
            inBuffer = ""
        elif option == "3":
            print(inBuffer)
        elif option == "4":
            print("Exiting program... ")
        else:
            print("Please enter a valid option.")

main()