#!/usr/bin/python3

from student import Student
from main import *

RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'

def custom_assert(assertionString, condition):
    print("Testing: " + assertionString)
    if condition:
        print(GREEN + "SUCCES!" + END)
    else:
        print(RED + "FAILURE!" + END)

def testStudentClass():
    print(BOLD + "Testing student class." + END)
    s = Student("name", "surname", "email@", 9.50, "county")
    custom_assert("Student contains correct given name.", s.getName() == "name")
    custom_assert("Student contains correct given surname.", s.getSurname() == "surname")
    custom_assert("Student contains correct given e-mail.", s.getEmail() == "email@")
    custom_assert("Student contains correct given grade.", s.getGrade() == 9.5)
    custom_assert("Student contains correct given county.", s.getCounty() == "county")
    try:
        s = Student("name123", "surname", "email@", 9.50, "county")
        custom_assert("Testing for raising exception for invalid name.", False)
    except ValueError:
        custom_assert("Testing for raising exception for invalid name.", True)
    try:
        s = Student("name", "surname123", "email@", 9.50, "county")
        custom_assert("Testing for raising exception for invalid surname.", False)
    except ValueError:
        custom_assert("Testing for raising exception for invalid surname.", True)
    try:
        s = Student("name", "surname", "email", 9.50, "county")
        custom_assert("Testing for raising exception for invalid email.", False)
    except ValueError:
        custom_assert("Testing for raising exception for invalid email.", True)
    try:
        s = Student("name", "surname", "email@", "9asd.50", "county")
        custom_assert("Testing for raising exception for invalid grade.", False)
    except ValueError:
        custom_assert("Testing for raising exception for invalid grade.", True)

def testGetStudent():
    print(BOLD + "Testing getStudent()" + END)
    line = "   asd   ; asdf ;   p laton@gmail; 6.432;  Cluj "
    s = getStudent(line)
    custom_assert("Student contains correct name.", s.getName() == "asd")
    custom_assert("Student contains correct surname.", s.getSurname() == "asdf")
    custom_assert("Student contains correct e-mail.", s.getEmail() == "platon@gmail")
    custom_assert("Student contains correct grade.", s.getGrade() == 6.432)
    custom_assert("Student contains correct county.", s.getCounty() == "Cluj")

def testAll():
    testStudentClass()
    testGetStudent()

# Only call testAll if run as script
if __name__ == "__main__":
    testAll()
