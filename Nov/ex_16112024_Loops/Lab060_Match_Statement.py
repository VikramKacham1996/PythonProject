# Match Statement -> #Swich in Java
# Match the op and execute
#python >3.10
#from unittest import case

#match variable:
  #  case pattern1:
        # code block
 #   case pattern2:
        # code block


# write a program to ask the user which browser he want to run automation


browser_name = input("Which browser do you want to run automation|\n")
match browser_name:
    case "Chrome":
        print("Chrome automation is running")
    case "Firefox":
        print("Firefox automation is running")
    case "Safari":
        print("Safari automation is running")
    case _:  #default (when nothing match)
        print("Browser Not Found")


food_name = input("Which food do you want to eat \n")
match food_name:
    case "Pizza":
        print("Pizza is delicious")


    case "Burger":
        print("Burger is delicious")

    case _:
        print("Sorry, we don't have that food")

sport_name = input("What's your favorite sport?\n")
match sport_name:
    case "Football":
        print("Football is thrilling! A perfect mix of strategy and athleticism.")
    case "Basketball":
        print("Basketball is exciting! It's all about speed and skill.")
    case "Cricket":
        print("Cricket is fascinating! A game of patience and precision.")

    case "Swimming":
        print("Swimming is fantastic! It's a full-body workout and so refreshing.")
    case _:
        print("That's an interesting choice! Sports are always fun to play or watch.")



