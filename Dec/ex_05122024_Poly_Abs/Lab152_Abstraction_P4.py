from abc import  ABC,abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readFromEXcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
         pass
    def stopBrowser(self):
         pass
class  TC1(Browser):
    def startBrowser(self):
        print("starting")
    def stopBrowser(self):
        print("stop")

    def readFromEXcel(self):
        print ("readFromExcel is ready")


    def runTC(self):
        self.stopBrowser()
        self.readFromEXcel()
        self.stopBrowser()

tc1 =TC1()
tc1.runTC()

