class Parent:
    def home(self):
        print("2BHK")
class Son(Parent):
    def home(self):
        print("3BHK")
    def town(self):
        print("31BHK")



ob_ref =Son()
ob_ref.home()
ob_ref.town()




