import re
import log
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


