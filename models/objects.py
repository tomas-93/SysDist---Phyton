__author__ = 'Tomas'

class Student():
    __numero = ""
    __name = ""
    __surname = ""
    __career = ""
    __school = ""
    __level = ""
    __phone = ""
    __email = ""

    def __init__(self):
        pass
#_id
    def setID(self, id):
        self.__numero = id

    def getID(self):
        return self.__numero
#Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
#Surname
    def setSurname(self, name):
        self.__surname = name

    def getSurname(self):
        return self.__surname
#School
    def setSchool(self, name):
        self.__school = name

    def getSchool(self):
        return self.__school
#Race
    def setCareer(self, name):
        self.__career = name

    def getCareer(self):
        return self.__career
#level
    def setLevel(self, name):
        self.__level = name

    def getLevel(self):
        return self.__level
#Phone
    def setPhone(self, name):
        self.__phone = name

    def getPhone(self):
        return self.__phone
#Email
    def setEmail(self, name):
        self.__email = name

    def getEmail(self):
        return self.__email


class Teacher():
    __number = ""
    __name = ""
    __surname = ""
    __career = ""
    __phone = ""
    __email = ""

    def __init__(self):
        pass
#_id
    def setID(self, id):
        self.__number = id

    def getID(self):
        return self.__number
#Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
#Surname
    def setSurname(self, name):
        self.__surname = name

    def getSurname(self):
        return self.__surname
#Career
    def setCareer(self, name):
        self.__career = name

    def getCareer(self):
        return self.__career
#Phone
    def setPhone(self, name):
        self.__phone = name

    def getPhone(self):
        return self.__phone
#Email
    def setEmail(self, name):
        self.__email = name

    def getEmail(self):
        return self.__email