# checking for a leap year , 2024 -> Yes
#
# leap day occurs in each year that is multiple of 4,
# except for years evenly divisible by 100 but  not by 400



# the year is multiple of 400
# the year is a multiple of 4 and not a multiple of 100

def check_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Define the year to check
year = 2024

# Check and print whether it's a leap year
if check_leap(year):
    print(" 2024 is Leap year")
else:
    print("2024 is Not a leap year")