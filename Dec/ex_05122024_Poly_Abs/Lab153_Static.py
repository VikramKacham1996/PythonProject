#static methods
#a static method isa  method that belongs to a
#class rather than an instance of the class.


class O:

    @staticmethod
    def sum(a, b):   # Static method
        return a + b

    def sub(self, a, b):  # nonstatic method
        return a - b

obj_O = O()
result = obj_O.sub(3, 4)
print(result)  # Output: -1

print("--")

print(O.sum(3, 4))  # Output: 7
