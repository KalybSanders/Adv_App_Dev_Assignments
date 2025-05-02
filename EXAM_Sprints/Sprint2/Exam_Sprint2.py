# Program Name: Exam_Sprint2.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: Final Exam
# Due Date: 05/03/ 2025


# method that converts user input string to an array,
# passes the array as a parameter to the array_to_dollars method
def process_input(some_input):
    # exit
    if some_input == "exit":
        return

    input_array = some_input.split(' ')
    array_to_dollars(input_array)

# method that calculates the total amount in dollars from the parameterised array
def array_to_dollars(some_array):
    # exit function early, if array format incorrect
    if len(some_array)%3 != 2:
        print("Input Error: Invalid Format\n")
        return

    total = 0
    # calculate total amount in dollars while checking that the correct format is maintained
    for i in range(0, len(some_array)):

        # validate 'quantity' formatting
        if i % 3 == 0:
            # try to convert number to integer, throw exception if not an integer
            try:
                int(some_array[i])
                if int(some_array[i]) < 0:
                    print("Input Error: Invalid Quantity (Negative Number)\n")
                    return
            except ValueError:
                print("Input Error: Invalid Quantity\n")
                return

        # validate 'coin type' formatting then recalculate total
        elif i % 3 == 1:
            coin_value = coin_to_value(some_array[i], (int(some_array[i - 1]) > 1))
            if coin_value < 0.01:
                print("Input Error: Misspelled Word\n")
                return

            total = total + (coin_value * int(some_array[i - 1]))

        # validate 'and' separator formatting
        else:
            if some_array[i] != "and":
                print("Input Error: Invalid Format\n")
                return

    print("-> " + "{:.2f}".format(total) + "\n")

# method for identifying coins and returning their value
def coin_to_value(coin_type, is_multiple):
    if not is_multiple:
        if coin_type == "penny":
            return 0.01
        if coin_type == "nickel":
            return 0.05
        if coin_type == "dime":
            return 0.10
        if coin_type == "quarter":
            return 0.25
    else:
        if coin_type == "pennies":
            return 0.01
        if coin_type == "nickels":
            return 0.05
        if coin_type == "dimes":
            return 0.10
        if coin_type == "quarters":
            return 0.25
    return 0

# main method
def main():
    user_input = ""
    print("\nFormat: \"[quantity] [type of coin] *[and]\"\n"
          "*[and] separates different coins\n"
          "(ex. 1 penny and 2 quarters)\n")

    # main program loop gets user input from keyboard then outputs the result
    while user_input != "exit":
        user_input = input("Enter an amount of coins: ")
        user_input = user_input.strip().lower() # clean up user input
        process_input(user_input)

main()


