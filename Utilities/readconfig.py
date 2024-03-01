import configparser

config = configparser.RawConfigParser()
config.read("C:\\python fixture\\credKart\\configuration\\config.ini")


class Readconfig:
    @staticmethod
    def getUsername():
        useremail = config.get('common data', 'Username from config')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common data', 'Password from config')
        return password
