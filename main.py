#!/usr/bin/python3

import re
import log
import sys
from student import Student

def getStudent(line):
    log.info("Got line:\n" + line)
    # Clear whitespace
    line = re.sub(r"\s", "", line)
    # Generate fields list
    fields = line.split(';')
    if len(fields) != 5:
        raise ValueError("Invalid row found!")
        return
    # Put in each student field the value from corresponding field element
    name = fields[0]
    surname = fields[1]
    email = fields[2]
    grade = fields[3]
    county = fields[4]
    return Student(name, surname, email, grade, county)

def checkStudent(student):
    # Return True if student is from Cluj and has a grade higher than 8,
    # False otherwise
    return (student.getCounty() == "Cluj" and student.getGrade() >= 8.0)

def printStudent(student):
    print(student.getSurname() + ' ' + student.getName())

def run():
    """
    Script entry point.
    """
    log.info("Trying to open csv file...")
    filename = "" 
    try:
        filename = sys.argv[1]
    except:
        print("Please provide csv file!")
        return
    try:
        with open(filename, 'r') as csvfile:
            log.info("Succesfully opened csv file!")
            # Iterate through each line in the csvfile
            row_count = 0
            for line in csvfile:
                # Get the student object from the current line string
                log.info("Trying to create student...")
                row_count += 1
                try:
                    student = getStudent(line)
                    log.info("Student succesfully created! Result: " + str(student))
                    # If the student meets the requirements, print it
                    if checkStudent(student):
                        log.info("Student " + student.getName() + " checks.")
                        printStudent(student)
                    else:
                        log.info("Student " + student.getName() + " does not check.")
                except ValueError as e:
                    print(str(e) + " at row " + str(row_count))
                    return
                except:
                    print("Error at row " + str(row_count) + "!")
                    return
    except:
        print("Error openening file!")

# Only call run() the program if it is run as a script
if __name__ == "__main__":
    run()
