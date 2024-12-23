# create a program to sum of the three number from the user input,
# if user doesn't enter any number, use default as 100,200,300



# logic building

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def sum_of_three(num1=1, num2=12, num3=34):
    return num1 + num2 + num3
result = sum_of_three(num1, num2, num3)
print(result)


result2 = sum_of_three()
result2 = sum_of_three(10)
result2 = sum_of_three(num1=10, num2=20)
result2 = sum_of_three(num1=10, num2=20, num3=30)
print(result2)



