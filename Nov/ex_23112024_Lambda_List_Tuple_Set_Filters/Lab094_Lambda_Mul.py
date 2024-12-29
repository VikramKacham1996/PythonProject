
# Write a program to calculate even and odd




# def find_even_odd(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print( "odd")
#
# find_even_odd(9)
# find_even_odd(8)

n = int(input("Enter a number\n "))
check_even_odd = lambda num: "even" if num % 2 == 0 else "odd"
#print(check_even_odd(9))
#print(check_even_odd(8))
print(check_even_odd(n))


