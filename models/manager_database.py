__author__ = 'Tomas'

from models.objects import Student
from models.objects import Teacher
from models.database import SQLiteManager
import json


class ReadJSON():
    __objectStudent = ""
    __objectTeacher = ""
    def __init__(self):
        self.__objectStudent = Student()
        self.__objectTeacher = Teacher()
        self.__sqlite = SQLiteManager(False)

    def indetifyAndInsertDataJSON(self, string):
        try:
            python_json = json.loads(string)
            identify = ""
            for row in python_json:
                identify = row
                if identify == "students":
                    return self.__readJSONStudent(python_json[row])
                elif identify == "teacher":
                    return self.__readJSONTeacher(python_json[row])
        except Exception as err:
            print(err)
    def __readJSONTeacher(self, json_teacher):
        for array in json_teacher:
            for elementArray in array:
                if elementArray == "_id":
                    self.__objectTeacher.setID(array[elementArray])
                elif elementArray == "name":
                    self.__objectTeacher.setName(array[elementArray])
                elif elementArray == "surname":
                    self.__objectTeacher.setSurname(array[elementArray])
                elif elementArray == "career":
                    self.__objectTeacher.setCareer(array[elementArray])
                elif elementArray == "phone":
                    self.__objectTeacher.setPhone(array[elementArray])
                elif elementArray == "email":
                    self.__objectTeacher.setEmail(array[elementArray])
        return self.__insertDataInTeacher(self.__objectTeacher)

    def __readJSONStudent(self, json_student):
        for array in json_student:
            for elementArray in array:
                if elementArray == "_id":
                    self.__objectStudent.setID(array[elementArray])
                elif elementArray == "name":
                    self.__objectStudent.setName(array[elementArray])
                elif elementArray == "surname":
                    self.__objectStudent.setSurname(array[elementArray])
                elif elementArray == "school":
                    self.__objectStudent.setSchool(array[elementArray])
                elif elementArray == "career":
                    self.__objectStudent.setCareer(array[elementArray])
                elif elementArray == "level":
                    #print(self.__objectStudent.getLevel())
                    self.__objectStudent.setLevel(array[elementArray])
                    print(self.__objectStudent.getLevel())
                elif elementArray == "phone":
                    self.__objectStudent.setPhone(array[elementArray])
                elif elementArray == "email":
                    self.__objectStudent.setEmail(array[elementArray])
        return self.__insertDataInStudent(self.__objectStudent)

    def __insertDataInStudent(self, object):
        return self.__sqlite.insertIntoToTableStudent(
                                    object.getID(),
                                    object.getName(),
                                    object.getSurname(),
                                    object.getSchool(),
                                    object.getLevel(),
                                    object.getPhone(),
                                    object.getCareer(),
                                    object.getEmail())
    def __insertDataInTeacher(self, object):
        return self.__sqlite.insertIntoToTableTeacher(object.getID(),
                                                 object.getName(),
                                                 object.getSurname(),
                                                 object.getPhone(),
                                                 object.getCareer(),
                                                 object.getEmail())

class SendJSON():
    def __init__(self):
        self.__sqlite = SQLiteManager(False)


    def sendJSONStudent(self):
        return self.__sqlite.readTheCursorOfStudentTable()

    def sendJSONTeacher(self):
        return self.__sqlite.readTheCursorOfTeacherTable()



