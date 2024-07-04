import configparser

config = configparser.RawConfigParser()

config.read(".\\configData.ini")


class readConfigData:
    @staticmethod
    def getURL():
        url = config.get("common value", "url")
        return url
