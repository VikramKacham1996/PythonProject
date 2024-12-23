#user defined
#they can't return -> non return
#they can return something
#they have parameters
# they don't have parameters/ arguments





#1.they can't return -> non return
#No return type  and no parameter/arguments NRNP
def greet():
    print("Hello")
greet()


#2 no return type and with argument /parameters

def greet_by_name(name):
    print("Hello, " + name)
greet_by_name("vick")

#3. no Return type and with default argument (# positional argument)
def say_hello_default_arg(name="vick"):
    print("Hello", name.upper())
say_hello_default_arg("kacham")
say_hello_default_arg()



def multiple_args(name1= "A", name2 ="B"):
    print("Mul", name1, name2)
multiple_args(name1="vick",name2 ="kacham")
multiple_args("vick")
multiple_args()
multiple_args(name1 ="vick" , )
multiple_args(name2 ="kacham" )
multiple_args("vick", "kacham")





#4 ARGUMENT + RETURN TYPE
def sum_two_numbers(a, b):
    return a + b
result = sum_two_numbers(4, 56)
print(result)


#import math
#print(math.pow(2, 3))  # Example usage

#math.pow()


def sum_two_numbers_with_default(num1=100, num2=200):
    print("sum_two_numbers_with_default")
    return num1 + num2

result = sum_two_numbers_with_default(10, 20)
print(result)
result = sum_two_numbers_with_default(10)
print(result)






