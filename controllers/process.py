from threading import Thread
from models.manager_database import ReadJSON
from models.manager_database import SendJSON
import time, re, json

class ProcessCliente (Thread):

    def __init__(self, connectClient):
        Thread.__init__(self)
        self.client = connectClient
        self.sqlite = ReadJSON()

    def run(self):
        self.sqlite = ReadJSON()
        string = ""
        while True:
            try:
                while True:
                    data =  self.client.recv(1024)
                    if not data: break
                    string += data.decode()
                    boolean = re.search("HandleServicesSockets", string)
                    if boolean:
                        self.sqlite.indetifyAndInsertDataJSON(string.replace("\nHandleServicesSockets\n",""))
                        break
                print(string)
                string = ""
                time.sleep(5)
            except ConnectionResetError as e:
                print("Se cerro la conexion", self.client)
                break
            except Exception as e:
                print(e)
                break

    def startRun(self):
        try:
            self.start()
        except Exception as e:
            print (e)



class ProcessServer (Thread):

    def __init__(self, connectClient):
        Thread.__init__(self)
        self.client = connectClient
        self.processRun = True

    def run(self):
        try:
            while self.processRun:
                sqlite = SendJSON()
                self.client.send(str.encode(sqlite.sendJSONTeacher()))
                self.client.send(str.encode(sqlite.sendJSONStudent()))
                print(sqlite.sendJSONTeacher())
                print(str.encode(sqlite.sendJSONStudent()))
                time.sleep(5)
        except Exception as e:
            print(e)

    def startRun(self):
        try:
            self.start()
        except Exception as e:
            print (e)

