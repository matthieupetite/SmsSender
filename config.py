import configparser
import os


class ScheduleConfig():
    def __init__(self, timeBetweenRunInSecond=0):
        self.timeBetweenRunInSecond = timeBetweenRunInSecond


class DatabaseConfig():
    def __init__(self, host="", database="", user="", password="", port=""):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = int(port)


class ModemConfig():
    def __init__(self, login="", password="", host=""):
        self.login = login
        self.password = password
        self.host = host


class SenderConfig():

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.schedule = ScheduleConfig()
        self.database = DatabaseConfig()
        self.modem = ModemConfig()

    def loadConfiguration(self):
        # self.__config.read((os.path.abspath(os.getcwd().join('/config.ini'))))
        self.__config.read('/workspaces/SmsSender/config.ini')
        self.schedule.timeBetweenRunInSecond = self.__config.get(
            'schedule', 'timeBetweenRunInSecond')
        self.database.database = self.__config.get('database', 'host')
        self.database.host = self.__config.get('database', 'host')
        self.database.user = self.__config.get('database', 'user')
        self.database.password = self.__config.get(
            'database', 'password')
        self.database.port = self.__config.get('database', 'port')
        self.modem.host = self.__config.get('modem', 'host')
        self.modem.login = self.__config.get('modem', 'login')
        self.modem.password = self.__config.get('modem', 'password')
