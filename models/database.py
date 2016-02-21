__author__ = 'Tomas'
import sqlite3 as lite
import sqlite3
import json
import os
import inspect



class Schema (object):
    #Name
    NAME = os.getcwd()+"\SysDis.db"
    #Table student
    TABLE_STUDENT = "student"
    #Table Maestro
    TABLE_TEACHER = "techaer"
    #Create Table
    CREATE_TABLE_STUDENT = "CREATE TABLE " + TABLE_STUDENT + " ( id integer primary key, name text, last_name text, school text, level text, phone text, race text, email text)"
    CREATE_TABLE_TEACHER = "CREATE TABLE " + TABLE_TEACHER + " ( id integer primary key, name text, last_name text, race text, phone text, email text)"
    #Drop table
    DROP_TABLE_STUDENT = "DROP TABLE IF EXISTS student"
    DROP_TABLE_TEACHER = "DROP TABLE IF EXISTS techaer"

    #Count
    COUNT_ELEMENTS_TABLE_TEACHER = "SELECT COUNT(*) AS NUMBER FROM " + TABLE_TEACHER
    COUNT_ELEMENTS_TABLE_STUDENT = "SELECT COUNT(*) AS NUMBER FROM " + TABLE_STUDENT

    #Selelct *
    SELECT_ALL_OF_ELEMENTS_OF_THE_TABLE_STUDENT = "SELECT * FROM " + TABLE_STUDENT
    SELECT_ALL_OF_ELEMENTS_OF_THE_TABLE_TEACHER = "SELECT * FROM " + TABLE_TEACHER

    #Inser

    INSERT_INTO_TO_TABLE_STUDENT = "INSERT INTO " + TABLE_STUDENT +  "  VALUES ("
    INSERT_INTO_TO_TABLE_TEACHER = "INSERT INTO " + TABLE_TEACHER +  "  VALUES ("
    def __init__(self):
        pass


class SQLiteManager (Schema):
    def __init__(self, x):
        Schema.__init__(self)
        if x == True and os.path.exists(Schema.NAME):
            os.remove(Schema.NAME)
        __conn = lite.connect(Schema.NAME)
        __cursor = __conn.cursor()
        if x == True:
            __cursor.execute(Schema.CREATE_TABLE_TEACHER)
            __cursor.execute(Schema.CREATE_TABLE_STUDENT)
        __conn.commit()
        __conn.close()

    def insertIntoToTableStudent(self, idN, name, last_name, school, level, phone, race, email):
        try:
            __conn = lite.connect(Schema.NAME)
            __cursor = __conn.cursor()
            __cursor.execute(Schema.INSERT_INTO_TO_TABLE_STUDENT + str(idN) +", '"+ name +"', '"+ last_name +"', '"+ school +"', '"+ level +"', '"+ phone +"', '"+ race +"', '"+ email +"')")
            __conn.commit()
            __conn.close()
        except Exception as e:
            print("error id ya existe")

    def insertIntoToTableTeacher(self, idN, name, last_name, phone, race, email):
        try:
            __conn = lite.connect(Schema.NAME)
            __cursor = __conn.cursor()
            __cursor.execute(Schema.INSERT_INTO_TO_TABLE_TEACHER + str(idN) +", '"+ name +"', '"+ last_name +"', '"+ race +"', '"+ phone +"', '"+ email +"')")
            __conn.commit()
            __conn.close()
        except Exception as e:
            print("error el id ya exite")


    def readTheCursorOfStudentTable(self):
        __conn = lite.connect(Schema.NAME)
        __cursor = __conn.cursor()
        __cursor.execute(Schema.SELECT_ALL_OF_ELEMENTS_OF_THE_TABLE_STUDENT)
        string = '{"Student":['
        elements = self.countTheElementsOfTheTableStudent()
        count =0
        for row in __cursor:
            string += '{"_id":"'+str(row[0])+'",'
            string += '"name":"'+row[1]+'",'
            string += '"surname":"'+row[2]+'",'
            string += '"school":"'+row[3]+'",'
            string += '"career":"'+row[4]+'",'
            string += '"level":"'+row[5]+'",'
            string += '"phone":"'+row[6]+'",'
            string += '"email":"'+row[7]+'"'
            if count < (elements-1):
                string += '},'
                count+=1
            else:
                string += '}'
        string +=']}\n'
        __conn.commit()
        __conn.close()
        return string



    def readTheCursorOfTeacherTable(self):
        __conn = lite.connect(Schema.NAME)
        __cursor = __conn.cursor()
        __cursor.execute(Schema.SELECT_ALL_OF_ELEMENTS_OF_THE_TABLE_TEACHER)
        string = '{"Teacher":['
        elements = self.countTheElementsOfTheTableStudent()
        count =0
        for row in __cursor:
            string += '{"_id":"'+str(row[0])+'",'
            string += '"name":"'+row[1]+'",'
            string += '"surname":"'+row[2]+'",'
            string += '"career":"'+row[3]+'",'
            string += '"phone":"'+row[4]+'",'
            string += '"email":"'+row[5]+'"'
            if count < (elements-1):
                string += '},'
                count+=1
            else:
                string += '}'
        string +=']}\n'
        __conn.commit()
        __conn.close()
        return string

    def countTheElementsOfTheTableTeacher(self):
        __conn = lite.connect(Schema.NAME)
        __cursor = __conn.cursor()
        __cursor.execute(Schema.COUNT_ELEMENTS_TABLE_TEACHER)
        count = 0
        for row in __cursor:
            count = row[0]
        __conn.commit()
        __conn.close()
        return count

    def countTheElementsOfTheTableStudent(self):
        __conn = lite.connect(Schema.NAME)
        __cursor = __conn.cursor()
        __cursor.execute(Schema.COUNT_ELEMENTS_TABLE_STUDENT)
        count = 0
        for row in __cursor:
            count = row[0]
        __conn.commit()
        __conn.close()
        return count

SQLiteManager(True)