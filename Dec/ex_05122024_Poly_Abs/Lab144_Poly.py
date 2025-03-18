
# method overloading id not supported -python
class Calc:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c


clac_ref = Calc()
result = calc_ref.sum(3,4)
print(result)



    #same name of function/method  but diff arg.
