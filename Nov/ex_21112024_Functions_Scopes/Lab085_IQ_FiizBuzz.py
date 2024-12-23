#write a program that prints numbers from 1 to 100.
#however ,  for multiples of 3 , print "Fizz" instead of the number,
#and for multiples of 5, print "Bizz." for the numbers that are
# multiples of both 3 and5, print "FizzBuzz." ( for ,if)


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)