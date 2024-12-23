  #triangle  classifier:

  #write a program that classifies a triangle based on it's side lengths
  #given three i/p values respresenting the lengths of the sides,
  #determine if the triangle is equilateral (all sides are equal), isosce
  #use an if -else statement to  classify the triangle.


# Triangle classifier program
# Classifies a triangle based on the lengths of its sides

def classify_triangle(side1, side2, side3):
    # Ensure all sides are positive
    if side1 > 0 and side2 > 0 and side3 > 0:
        # Check if the sides form a valid triangle
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            # Classify the triangle
            if side1 == side2 == side3:
                return "The triangle is equilateral."
            elif side1 == side2 or side1 == side3 or side2 == side3:
                return "The triangle is isosceles."
            else:
                return "The triangle is scalene."
        else:
            return "The given lengths do not form a valid triangle."
    else:
        return "Side lengths must be positive."

# Input lengths of the sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Classify and print the result
result = classify_triangle(side1, side2, side3)
print(result)




# Enter the length of side 1: 5
# Enter the length of side 2: 5
# Enter the length of side 3: 5
# The triangle is equilateral.
# Valid Input (Isosceles Triangle)
#
#
# Enter the length of side 1: 5
# Enter the length of side 2: 5
# Enter the length of side 3: 3
# The triangle is isosceles.
# Valid Input (Scalene Triangle)
#
# Enter the length of side 1: 5
# Enter the length of side 2: 6
# Enter the length of side 3: 7
# The triangle is scalene.
# Invalid Input (Not a Triangle)
#
#
# Enter the length of side 1: 1
# Enter the length of side 2: 2
# Enter the length of side 3: 10
# The given lengths do not form a valid triangle.
# Invalid Input (Negative or Zero Sides)
#
# Enter the length of side 1: -5
# Enter the length of side 2: 5
# Enter the length of side 3: 5
# Side lengths must be positive.

