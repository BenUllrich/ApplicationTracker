from datetime import date
from webbrowser import open_new

class Application:
    def __init__(companyName, self, jobTitle, method, submissionDate, connections, status = 'Submitted'):
        self.__title = jobTitle                 # The title of the position being applied to (string)    
        self.__company = companyName            # The name of the company being applied to (string)
        self.__status = status                  # Current status of the application (string)
        self.__platform = method                # Where the application was submitted
        self.__date = submissionDate            # When the application was submitted
        self.__conn = connections               # Any connections established at the company
        self.__lastUpdated = date.today()       # The last time this particular application was updated

    """
    def openResume(self):
        open_new(self.__resume)
    def openCoverLetter(self):
        open_new(self.__coverLetter)
    """

    def getTitle(self):
        return self.__title
    def getCompany(self):
        return self.__company
    def getStatus(self):
        return self.__status
    def getPlatform(self):
        return self.__platform
    def getDate(self):
        return self.__date
    def getConn(self):
        return self.__conn
    def getLastUpdate(self):
        return self.__lastUpdated


    def setTitle(self,title):
        self.__title=title
    def setCompany(self,company):
        self.__company=company
    def setStatus(self,status):
        self.__status=status
    def setPlatform(self,platform):
        self.__platform=platform
    def setDate(self,date):
        self.__date=date
    def setConn(self):
        return self.__conn
    def setLastUpdate(self,lastUpdate):
        self.__lastUpdated = lastUpdate
