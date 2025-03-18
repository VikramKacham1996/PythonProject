
class Calc:

    def sum(self, *args):
        for a in args:
            print(a)
# *args - multiple values
calc_ref = Calc()
result = calc_ref.sum(3, 4)
print("___")
result = calc_ref.sum(1)
print("___")
result = calc_ref.sum(3, 4,7)
print("___")

# print(result)
