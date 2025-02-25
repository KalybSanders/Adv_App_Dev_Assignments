# Program Name: Assignment2.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 2
# Due Date: 02/ 07/ 2025
# Purpose: Receives a txt file of input containing student names along with
#           six grades per student. This program calculates the averages for
#           all of these students and prints a summary ordering the students
#           in descending order by average grade.
# List Specific resources used to complete the assignment.
#   I used the reading provide in the class.


def main():
    # open the file containing the students to read from
    file = open("Assignment2input.txt", "r")
    students = []

    # read each line and exit the loop when end of file reached
    line = file.readline()
    while line:
        # split the line read into values separated by a space ' '
        split_line = line.split(' ')

        # the first value is the name, the following six values are the student's grades
        name = split_line[0]
        average = avg(split_line[1:7])

        # append the student from the current line along with their grade average to the students list
        students.append({"name": name, "grade": average})

        line = file.readline()

    # sort the student list by grades in descending order, then print
    students_sorted = sorted(students, key=lambda g: g['grade'], reverse=True)
    students_to_string(students_sorted)

    # close the file
    file.close()

    input('ENTER to exit')

# totals together and averages the six grades of a student
# then returns that average grade up to two decimal points
def avg(grades):
    total = 0
    for g in grades:
        total += int(g)
    return round(total/len(grades), 2)

# prints every student's name with their average grade
def students_to_string(students):
    for s in students:
        print(s['name'], ": ", s['grade'])
    print('\n')

main()