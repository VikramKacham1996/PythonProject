try:
    num1 = int(input("enter a number 1\n"))
    num2 = int(input("enter a number 2\n"))
    result = num1/num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("output is", result)
finally:
    print(" this code will be always executed.!")


# lab169 and 168 same


# try:
#     num1 = int(input("enter a number 1\n"))
#     num2 = int(input("enter a number 2\n"))
#     result = num1/num2
# except Exception as e:
#     print(e)
