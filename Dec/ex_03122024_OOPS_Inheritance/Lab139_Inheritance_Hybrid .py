# hybrid inheritance


#multiple types of inheritance,
# sach as sinle
#multiple, and
#multilevel inheritance.



class A:
    def methodA(self):
        return "method A"
class B(A):  # single
    def methodB(self):
        return "method B"

class C(A): # hierachica
    def methodC(self):
        return "method C"


class D(B,C):   #sister# multiple, Multilevel
    def methodD(self):
        return "Method D"
#creating an object of class D
d =D()
print(d.methodA())
print(d.methodB())
print(d.methodD())
print(d.methodC())
