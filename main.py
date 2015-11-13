#!/usr/bin/python3

import log
import sys
from funcs import *
from student import Student

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
