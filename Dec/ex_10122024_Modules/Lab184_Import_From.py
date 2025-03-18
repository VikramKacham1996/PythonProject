from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import close_browser

class Testcase:
    def test_case(self):
        start_browser()
        print("Hello, running test case")
        close_browser()

# Create an object and run the test case
obj_tc = Testcase()
obj_tc.test_case()



   