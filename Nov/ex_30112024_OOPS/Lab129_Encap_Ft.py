from dotenv import load_dotenv
import os
class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "vikram@gmail.com" and self.password == "Pass123":
            print("Allowed, Login success")
        else:
            print("Login Failed")
load_dotenv()

eamil = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
print(email, password)

#Take user input for email and password

#Create an object of VWOLoginPage and call login_confirm
# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()
#
# vikram = VWOLoginPage("vikram@gmail.com" , "Pass123")
# vikram.login_confirm()
