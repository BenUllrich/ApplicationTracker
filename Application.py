from datetime import date

class Application:
    def __init__(self,companyName, jobTitle, method,status = 'Submitted', connections=None,lastUpdate=None ):
        self.__title = jobTitle                 # The title of the position being applied to (string)    
        self.__company = companyName            # The name of the company being applied to (string)
        self.__status = status                  # Current status of the application (string)
        self.__platform = method                # Where the application was submitted
        self.__conn = connections               # Any connections established at the company
        if not lastUpdate:
            self.__date = date.today()       # The last time this particular application was updated

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
    def setConn(self,contact):
         self.__conn = contact
    def setLastUpdate(self,lastUpdate):
        self.__lastUpdated = lastUpdate
