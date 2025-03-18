class ExcelReader:
    @staticmethod
    def read_from_excel():
        print("Reading from excel")
class MYSQLDBConnection:
    @staticmethod
    def readMYSQLFile():
        print("Reading from MySQL Database")



class TC1:
    static_var = 10
    def testcase(self):
        MYSQLDBConnection.readMYSQLFile()
        ExcelReader.read_from_excel()
        print(TC1.static_var) # shared among all instances of the class

tc1_obj = TC1()
tc1_obj.testcase()