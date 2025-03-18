class Father:
    def home(self):
        print("1bhk")


class Vikram(Father):
    def home(self):
        print("2bhk")


v= Vikram()
v.home()  # why because local have highest priority


f = Father()
f.home()


