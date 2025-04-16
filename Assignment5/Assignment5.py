# Program Name: Assignment5.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 5
# Due Date: 04/ 15/ 2025
# Purpose: This program creates a database containing days of the week and their corresponding temperatures.
#          It then uses SQL commands to compute the average temperature for the days 'SATURDAY' and 'THURSDAY'
#          and prints the results to the console.
# List Specific resources used to complete the assignment.
#   I used the reading provided in the class as well as the SQLite documentation.

import sqlite3

# this method creates and executes a SELECT statement that calculates the average temperature for a given day of week
# printing the result to the console
def average_temp(day):
    day_statement = "SELECT avg(Temperature_Value) FROM days WHERE Day_Of_Week='" + day + "'"
    cursor.execute(day_statement)

    average = cursor.fetchall()
    for x in average:
        # clean up the averaged value by removing the misc characters and rounding to 2 decimal places
        stripped = str(x).replace("(", "").replace(")", "").replace(",", "")
        stripped_rounded = round(float(stripped), 2)
        print("" + day + "'s average temperature is " + str(stripped_rounded))

# the main method CREATES a table called 'days' if it doesn't already exist,
# it then reads in the file containing the values and inserts them as rows into the 'days' table
def main():
    cursor.execute("DROP TABLE IF EXISTS days")
    cursor.execute("CREATE TABLE days (id INTEGER PRIMARY KEY, Day_Of_Week TEXT NOT NULL, Temperature_Value REAL)")

    # Read file and create array
    file = open("Assignment5input.txt", "r")

    # read file line by line until end of file
    line = file.readline()
    while line:
        split_line = line.split(' ')

        day_of_week = split_line[0]
        temperature = split_line[1]

        # insert each day of week along with its corresponding temperature into the 'days' table
        insert_statement = "INSERT INTO days (Day_Of_Week, Temperature_Value) VALUES ('" + day_of_week + "', " + temperature + ")"
        cursor.execute(insert_statement)
        # print(ins_statement)

        line = file.readline()

    conn.commit()
    file.close()


conn = sqlite3.connect('five_database.db')
cursor = conn.cursor()

main()

average_temp('Saturday')
average_temp('Thursday')

input("Press enter to exit...")


