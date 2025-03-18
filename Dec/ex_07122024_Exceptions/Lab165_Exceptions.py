print("--start of the program--")
try:

    a = int(input("Ent the num1")) #Enter alphabets instead of numbers # ValueError: invalid literal for int() with base 10: ' vikram'

    b = int(input("Ent the num2")) # enter 10 and 0 #  ZeroDivisionError: division by zero

    c= a/b
    print("Result Div is ",c)

except Exception as e:
    print(e)  # e = division by zero
print ("---End of the program")

#try and except