# multiple inheritance isnot supported in java it will support in python.


class Father:
    def home(self):
        return"This is from the father"
    def father_money(self):
        return 5
class Mother:
    def home(self):
        return"This is from the mother"
    def Mother_money(self):
        return 2

#class Son(Mother, Father):
class Son(Father, Mother): # Multiple in -FCFS
    def print_info(self):
        print("Son")



s= Son()
print(s.father_money())
print(s.Mother_money())
print(s.print_info())
print(s.home())
