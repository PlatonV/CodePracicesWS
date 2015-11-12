#!/usr/bin/python3

import re
import log
from student import Student

def get_student(line):
    log.info("Got line:\n" + line)
    # Clear whitespace
    line = re.sub(r"\s", "", line)
    # Generate fields list
    fields = line.split(';')
    # Put in each student field the value from corresponding field element
    name = fields[0]
    surname = fields[1]
    email = fields[2]
    grade = fields[3]
    county = fields[4]
    return Student(name, surname, email, grade, county)

def check_student(student):
    # Return True if student is from Cluj and has a grade higher than 8,
    # False otherwise
    return (student.getCounty() == "Cluj" and student.getGrade() >= 8.0)

def print_student(student):
    print(student.getSurname() + ' ' + student.getName())

def run():
    """
    Script entry point.
    """
    log.info("Trying to open csv file...")
    with open("students.csv", 'r') as csvfile:
        log.info("Succesfully opened csv file!")
        # Iterate through each line in the csvfile
        for line in csvfile:
            # Get the student object from the current line string
            log.info("Trying to create student...")
            student = get_student(line)
            log.info("Student succesfully created! Result: " + str(student))
            # If the student meets the requirements, print it
            if check_student(student):
                log.info("Student " + student.getName() + " checks.")
                print_student(student)
            else:
                log.info("Student " + student.getName() + " does not check.")

# Only call run() the program if it is run as a script
if __name__ == "__main__":
    run()
