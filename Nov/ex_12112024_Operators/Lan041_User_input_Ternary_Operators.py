# program -if age>18 -all0wed to vote
#else -> not allowed to vote

user_age = int (input("enter your age\n"))
if user_age>18:
     print("yes you can go to vote")
else:
    print("No you can't allowed" )
#print("Yes, you can vote" if user_age > 18 else "No, you are not allowed")

#--- 3rd type: don't use this type
#print("yes you can go to vote" if int(input("Enter your age\n")) > 18 else "No, you are not allowed")


