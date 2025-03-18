#Hierrchical inheritance
#one parent  multiple child


class Father:
    def BHk1(self):
        print("BHK1")

class Vikram(Father):
    def BHk12(self):
        print("BHk12")


class Vinod(Father):
    def BHk2(self):
        print("2BHK")


class Vani(Father):
    def BHk3(self):
        print("3BHK")
class Vikky(Father):
    pass # inherits methods from father but doesn't add anything new

vikram = Vikram()
vikram.BHk1()
vikram.BHk12()


vani= Vani()
vani.BHk1()
vani.BHk3()

vinod = Vinod()
vinod.BHk1()
vinod.BHk2()
#vinod.BHk12() # this belongs to vikram

v  = Vikky()
v.BHk1() # only father house

