class Student:

    def __init__(self, name, surname, email, grade, county):
        if name.isalpha():
            self._name = name
        else:
            raise ValueError("Invalid name!")
        if surname.isalpha():
            self._surname = surname
        else:
            raise ValueError("Invalid surname!")
        if '@' in email:
            self._email = email
        else:
            raise ValueError("Invalid e-mail!")
        try:
            self._grade = float(grade)
        except:
            raise ValueError("Invalid grade!")
        self._county = county

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getEmail(self):
        return self._email

    def getGrade(self):
        return self._grade

    def getCounty(self):
        return self._county

    def __str__(self):
        return (self._name + ' ' + self._surname + ' ' + self._email + ' ' + str(self._grade) + ' ' + self._county)
