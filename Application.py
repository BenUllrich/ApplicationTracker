from datetime import date
from webbrowser import open_new

class Application:
    def __init__(self, companyName, jobTitle, resumeFile, method, submissionDate, coverLetterFile = None, status = 'Submitted'):
        self.__company = companyName            # The name of the company being applied to (string)
        self.__title = jobTitle                 # The title of the position being applied to (string)
        self.__resume = resumeFile              # The absolute path to the file used to store the resume used to apply for this job (string)
        self.__coverLetter = coverLetterFile    # The absolute path to the file used to store the cover letter used to apply for this job (string or None)
        self.__status = status                  # Current status of the application (string)
        self.__platform = method                # Where the application was submitted
        self.__date = submissionDate            # When the application was submitted
        self.__lastUpdated = date.today()       # The last time this particular application was updated

    def openResume(self):
        open_new(self.__resume)
    def openCoverLetter(self):
        open_new(self.__coverLetter)

    def getCompany(self):
        return self.__company
    def getTitle(self):
        return self.__title
    def getResume(self):
        return self.__resume
    def getCoverLetter(self):
        return self.__coverLetter
    def getStatus(self):
        return self.__status
    def getPlatform(self):
        return self.__platform
    def getDate(self):
        return self.__date
    def getLastUpdate(self):
        return self.__lastUpdated

    def setCompany(self,company):
        self.__company=company
    def setTitle(self,title):
        self.__title=title
    def setResume(self,resume):
        self.__resume=resume
    def setCoverLetter(self,coverLetter):
        self.__coverLetter=coverLetter
    def setStatus(self,status):
        self.__status=status
    def setPlatform(self,platform):
        self.__platform=platform
    def setDate(self,date):
        self.__date=date
    def setLastUpdate(self,lastUpdate):
        self.__lastUpdated = lastUpdate
