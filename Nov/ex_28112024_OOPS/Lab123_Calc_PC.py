class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"


# Create an object of the Calc class
object_ref = Calc(3, 4)

# Call methods on the object and assign output
output_sum = object_ref.sum()
output_sub = object_ref.sub()
output_mul = object_ref.mul()
output_div = object_ref.div()

# Print the outputs
print(output_sum)
print(output_sub)
print(output_mul)
print(output_div)


# retry this program it's taken from chatgpt
